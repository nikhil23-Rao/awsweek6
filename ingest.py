#!/usr/bin/env python3
"""Ingest synthetic company corpus Markdown files into a local vector index.

Strips plain 'key: value' headers from corpus/*.md, uses tables/documents.csv
as the source of truth for document metadata, splits Markdown bodies at
headings and paragraph breaks while keeping tables and code blocks intact,
merges tiny sections (< ~50 tokens), embeds 'Title > Heading' + chunk text
using sentence-transformers (BAAI/bge-small-en-v1.5) with L2 normalization,
and writes index/chunks.jsonl, index/embeddings.npy, and index/config.json.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
from pathlib import Path
from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer

DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"
BGE_QUERY_PREFIX = "Represent this sentence for searching relevant passages: "

HEADER_KEY_RE = re.compile(r"^[a-zA-Z0-9_\\]+\s*:")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")


def load_model(model_name: str) -> SentenceTransformer:
    """Load SentenceTransformer from local cache first, falling back to download."""
    offline_env = os.environ.get("HF_HUB_OFFLINE", "0") == "1"
    if offline_env:
        return SentenceTransformer(model_name, local_files_only=True)
    try:
        return SentenceTransformer(model_name, local_files_only=True)
    except Exception:
        return SentenceTransformer(model_name)


def strip_header(raw_text: str) -> str:
    """Find the end of the plain 'key: value' header and strip it from the Markdown text.

    Handles:
    - Headers starting with '---' and ending with '---'
    - Plain 'key: value' headers ending with a blank line (and optional '---')
    - Quoted or blank header values
    - Malformed single-line headers or stray prefix lines present in the corpus
      (e.g., PLAT-DEVT-015.md starting with 'No' + '---' + '## doc\\_id: ...',
      and PROD-PAY-009.md starting with a single-line 'doc\\_id: ...' + '---').
    """
    lines = raw_text.splitlines()
    idx = 0
    n = len(lines)

    # Skip leading blank lines
    while idx < n and not lines[idx].strip():
        idx += 1

    # Handle stray 'No' line before '---' in PLAT-DEVT-015.md
    if idx < n and lines[idx].strip() == "No":
        lookahead = idx + 1
        while lookahead < n and not lines[lookahead].strip():
            lookahead += 1
        if lookahead < n and lines[lookahead].strip() == "---":
            idx = lookahead

    if idx < n and lines[idx].strip() == "---":
        idx += 1
        while idx < n:
            stripped = lines[idx].strip()
            if stripped == "---":
                idx += 1
                break
            if not stripped:
                # Could be a blank line before closing '---' or after '---'
                next_nonblank = idx + 1
                while next_nonblank < n and not lines[next_nonblank].strip():
                    next_nonblank += 1
                if next_nonblank < n and lines[next_nonblank].strip() == "---":
                    idx = next_nonblank + 1
                else:
                    idx = next_nonblank
                break
            if HEADER_KEY_RE.match(stripped) or "doc\\_id:" in stripped or "doc_id:" in stripped:
                idx += 1
            else:
                break
    else:
        while idx < n:
            stripped = lines[idx].strip()
            if not stripped:
                idx += 1
                while idx < n and not lines[idx].strip():
                    idx += 1
                if idx < n and lines[idx].strip() == "---":
                    idx += 1
                break
            if stripped == "---":
                idx += 1
                break
            if HEADER_KEY_RE.match(stripped) or "doc\\_id:" in stripped or "doc_id:" in stripped:
                idx += 1
            else:
                break

    # Skip blank lines following header
    while idx < n and not lines[idx].strip():
        idx += 1

    # Handle single-line escaped header placed after '---' (e.g., PLAT-DEVT-015.md)
    if idx < n and ("doc\\_id:" in lines[idx] or re.match(r"^#{0,6}\s*doc_id\s*:", lines[idx].strip())):
        idx += 1
        while idx < n and not lines[idx].strip():
            idx += 1

    return "\n".join(lines[idx:]).strip()


def clean_heading_text(raw_heading: str) -> str:
    """Clean escaped Markdown punctuation from heading strings."""
    cleaned = raw_heading.strip()
    cleaned = cleaned.replace("\\#", "#").replace("\\)", ")").replace("\\(", "(")
    cleaned = cleaned.replace("\\.", ".").replace("\\_", "_").replace("\\-", "-")
    return cleaned.strip()


def split_at_headings(body: str, default_heading: str) -> list[tuple[str, str]]:
    """Split Markdown body at headings (# to ######), keeping fenced code blocks intact."""
    lines = body.splitlines()
    sections: list[tuple[str, str]] = []
    cur_heading = default_heading
    cur_lines: list[str] = []
    in_code_block = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block

        heading_match = HEADING_RE.match(line) if not in_code_block else None
        if heading_match:
            if cur_lines:
                sec_text = "\n".join(cur_lines).strip()
                if sec_text:
                    sections.append((cur_heading, sec_text))
            cur_heading = clean_heading_text(heading_match.group(2))
            cur_lines = [line]
        else:
            cur_lines.append(line)

    if cur_lines:
        sec_text = "\n".join(cur_lines).strip()
        if sec_text:
            sections.append((cur_heading, sec_text))

    return sections


def split_into_atomic_blocks(section_text: str) -> list[str]:
    """Split a section into paragraph blocks while keeping tables and code blocks whole."""
    lines = section_text.splitlines()
    blocks: list[str] = []
    cur: list[str] = []
    in_code_block = False
    in_table = False

    for line in lines:
        stripped = line.strip()

        # Fenced code block handling
        if stripped.startswith("```"):
            if not in_code_block:
                if cur and not in_table:
                    blocks.append("\n".join(cur).strip())
                    cur = []
                elif in_table:
                    blocks.append("\n".join(cur).strip())
                    cur = []
                    in_table = False
                in_code_block = True
                cur.append(line)
            else:
                cur.append(line)
                blocks.append("\n".join(cur).strip())
                cur = []
                in_code_block = False
            continue

        if in_code_block:
            cur.append(line)
            continue

        # Markdown table handling (lines starting with |)
        is_table_line = stripped.startswith("|") and stripped.endswith("|")
        if is_table_line:
            if not in_table:
                if cur:
                    blocks.append("\n".join(cur).strip())
                    cur = []
                in_table = True
            cur.append(line)
            continue
        else:
            if in_table:
                blocks.append("\n".join(cur).strip())
                cur = []
                in_table = False

        # Paragraph break
        if not stripped:
            if cur:
                blocks.append("\n".join(cur).strip())
                cur = []
        else:
            cur.append(line)

    if cur:
        blocks.append("\n".join(cur).strip())

    return [b for b in blocks if b]


def chunk_document(
    body: str,
    doc_title: str,
    count_tokens_fn,
    chunk_tokens: int = 300,
    overlap_tokens: int = 50,
    min_tokens: int = 50,
) -> list[tuple[str, str, int]]:
    """Chunk a stripped Markdown body according to the specification.

    1. Split body at Markdown headings.
    2. Split any section exceeding ~400 tokens (scaled proportionally to
       --chunk-tokens: round(chunk_tokens * 400 / 300), which is 400 when
       --chunk-tokens=300) at paragraph breaks toward --chunk-tokens with a
       50-token overlap, keeping tables and code blocks whole.
    3. Merge sections under ~50 tokens with adjacent sections.
    """
    max_tokens = round(chunk_tokens * 400 / 300)
    effective_min = min(min_tokens, max(20, chunk_tokens // 2))
    effective_overlap = min(overlap_tokens, max(10, chunk_tokens // 3))

    raw_sections = split_at_headings(body, default_heading=doc_title)

    # Step 2: Split oversized sections at paragraph breaks (keeping tables/code whole)
    split_sections: list[tuple[str, str]] = []
    for heading, sec_text in raw_sections:
        sec_toks = count_tokens_fn(sec_text)
        if sec_toks <= max_tokens:
            split_sections.append((heading, sec_text))
            continue

        blocks = split_into_atomic_blocks(sec_text)
        # If first block is just the markdown heading line, attach it to the first content block
        if len(blocks) > 1 and HEADING_RE.match(blocks[0]) and "\n" not in blocks[0]:
            blocks[1] = blocks[0] + "\n\n" + blocks[1]
            blocks.pop(0)

        cur_blocks: list[str] = []
        for block in blocks:
            candidate = "\n\n".join(cur_blocks + [block]) if cur_blocks else block
            if cur_blocks and count_tokens_fn(candidate) > chunk_tokens:
                split_sections.append((heading, "\n\n".join(cur_blocks)))
                # Build ~50-token overlap from trailing blocks of cur_blocks
                overlap_list: list[str] = []
                overlap_toks = 0
                for prev_block in reversed(cur_blocks):
                    pb_toks = count_tokens_fn(prev_block)
                    if overlap_toks + pb_toks <= effective_overlap or not overlap_list:
                        # Avoid carrying over a giant table/code block if it exceeds chunk_tokens alone
                        if pb_toks < chunk_tokens:
                            overlap_list.insert(0, prev_block)
                            overlap_toks += pb_toks
                    if overlap_toks >= effective_overlap:
                        break
                cur_blocks = overlap_list + [block]
                # If overlap + block already exceeds max_tokens, drop overlap
                if len(cur_blocks) > 1 and count_tokens_fn("\n\n".join(cur_blocks)) > max_tokens:
                    cur_blocks = [block]
            else:
                cur_blocks.append(block)

        if cur_blocks:
            split_sections.append((heading, "\n\n".join(cur_blocks)))

    # Step 3: Merge sections under ~50 tokens
    merged: list[tuple[str, str]] = []
    i = 0
    while i < len(split_sections):
        heading, text = split_sections[i]
        # Merge forward while current section is under effective_min tokens
        while count_tokens_fn(text) < effective_min and i + 1 < len(split_sections):
            next_heading, next_text = split_sections[i + 1]
            # If current section is the top-level document title preamble, adopt the specific subheading
            if heading == doc_title:
                heading = next_heading
            text = text + "\n\n" + next_text
            i += 1

        # If this is the final section and still under effective_min tokens, merge into previous
        if count_tokens_fn(text) < effective_min and merged:
            prev_heading, prev_text = merged[-1]
            if prev_heading == doc_title:
                prev_heading = heading
            merged[-1] = (prev_heading, prev_text + "\n\n" + text)
        else:
            merged.append((heading, text))
        i += 1

    result: list[tuple[str, str, int]] = []
    for heading, text in merged:
        result.append((heading, text, count_tokens_fn(text)))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest corpus Markdown files into local vector index.")
    parser.add_argument(
        "--chunk-tokens",
        type=int,
        default=300,
        help="Target chunk size in tokens (default: 300).",
    )
    parser.add_argument(
        "--corpus-dir",
        type=str,
        default="corpus",
        help="Path to directory containing .md corpus files (default: corpus).",
    )
    parser.add_argument(
        "--documents-csv",
        type=str,
        default="tables/documents.csv",
        help="Path to documents.csv metadata table (default: tables/documents.csv).",
    )
    parser.add_argument(
        "--index-dir",
        type=str,
        default="index",
        help="Directory to write chunks.jsonl, embeddings.npy, and config.json (default: index).",
    )
    parser.add_argument(
        "--model-name",
        type=str,
        default=DEFAULT_MODEL,
        help=f"SentenceTransformer model name (default: {DEFAULT_MODEL}).",
    )
    args = parser.parse_args()

    corpus_dir = Path(args.corpus_dir)
    docs_csv_path = Path(args.documents_csv)
    index_dir = Path(args.index_dir)
    index_dir.mkdir(parents=True, exist_ok=True)

    # Load metadata from tables/documents.csv (source of truth)
    with docs_csv_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        doc_rows = list(reader)

    print(f"Loaded {len(doc_rows)} document metadata rows from {docs_csv_path}.")
    print(f"Loading embedding model '{args.model_name}'...")
    model = load_model(args.model_name)
    tokenizer = model.tokenizer

    def count_tokens(text: str) -> int:
        return len(tokenizer.encode(text, add_special_tokens=False, truncation=False))

    chunk_records: list[dict[str, Any]] = []
    texts_to_embed: list[str] = []

    for row in doc_rows:
        doc_id = row["doc_id"].strip()
        filename = row["filename"].strip()
        md_path = corpus_dir / filename
        if not md_path.exists():
            raise FileNotFoundError(f"Missing corpus file {md_path} referenced in {docs_csv_path}")

        raw_md = md_path.read_text(encoding="utf-8")
        body = strip_header(raw_md)
        title = row["title"].strip()

        doc_chunks = chunk_document(
            body=body,
            doc_title=title,
            count_tokens_fn=count_tokens,
            chunk_tokens=args.chunk_tokens,
            overlap_tokens=50,
            min_tokens=50,
        )

        for idx, (heading, chunk_text, tok_count) in enumerate(doc_chunks, start=1):
            chunk_id = f"{doc_id}#{idx:03d}"
            record = {
                "chunk_id": chunk_id,
                "doc_id": doc_id,
                "title": title,
                "heading": heading,
                "text": chunk_text,
                "token_count": tok_count,
                "doc_type": row["doc_type"].strip(),
                "scope_level": row["scope_level"].strip(),
                "owner_team": row["owner_team"].strip(),
                "owner_org": row["owner_org"].strip(),
                "status": row["status"].strip(),
                "last_updated": row["last_updated"].strip(),
                "conflict_plan_id": row["conflict_plan_id"].strip(),
                "role_in_plan": row["role_in_plan"].strip(),
                "supersedes": row["supersedes"].strip(),
            }
            chunk_records.append(record)
            embed_input = f"{title} > {heading}\n{chunk_text}"
            texts_to_embed.append(embed_input)

    print(f"Created {len(chunk_records)} chunks across {len(doc_rows)} documents. Embedding...")
    embeddings = model.encode(
        texts_to_embed,
        batch_size=64,
        show_progress_bar=True,
        normalize_embeddings=True,
        convert_to_numpy=True,
    ).astype(np.float32)

    # Ensure strict L2 normalization in float32
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    embeddings = (embeddings / norms).astype(np.float32)

    chunks_path = index_dir / "chunks.jsonl"
    embeddings_path = index_dir / "embeddings.npy"
    config_path = index_dir / "config.json"

    with chunks_path.open("w", encoding="utf-8") as f:
        for rec in chunk_records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    np.save(embeddings_path, embeddings)

    tok_counts = [r["token_count"] for r in chunk_records]
    config = {
        "model_name": args.model_name,
        "query_prefix": BGE_QUERY_PREFIX,
        "chunk_tokens": args.chunk_tokens,
        "max_section_tokens": round(args.chunk_tokens * 400 / 300),
        "overlap_tokens": min(50, max(10, args.chunk_tokens // 3)),
        "min_section_tokens": min(50, max(20, args.chunk_tokens // 2)),
        "normalize_embeddings": True,
        "embedding_dim": int(embeddings.shape[1]),
        "num_documents": len(doc_rows),
        "num_chunks": len(chunk_records),
        "min_chunk_tokens": int(min(tok_counts)) if tok_counts else 0,
        "mean_chunk_tokens": round(float(np.mean(tok_counts)), 2) if tok_counts else 0.0,
        "max_chunk_tokens": int(max(tok_counts)) if tok_counts else 0,
        "corpus_dir": str(corpus_dir),
        "documents_csv": str(docs_csv_path),
    }
    with config_path.open("w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    print(f"Wrote {chunks_path} ({len(chunk_records)} records)")
    print(f"Wrote {embeddings_path} (shape={embeddings.shape}, dtype={embeddings.dtype})")
    print(f"Wrote {config_path}")


if __name__ == "__main__":
    main()
