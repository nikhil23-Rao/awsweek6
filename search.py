#!/usr/bin/env python3
"""Search the local vector index for top-k chunks matching a question.

Usage:
    python search.py "question" --k 5 [--org ORG] [--team TEAM] [--scope SCOPE] [--index-dir INDEX_DIR]
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

import numpy as np
from sentence_transformers import SentenceTransformer

DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"
BGE_QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
FORBIDDEN_FIELDS = {"role_in_plan", "conflict_plan_id"}


def load_model(model_name: str) -> SentenceTransformer:
    """Load SentenceTransformer from local cache first, falling back to download."""
    offline_env = os.environ.get("HF_HUB_OFFLINE", "0") == "1"
    if offline_env:
        return SentenceTransformer(model_name, local_files_only=True)
    try:
        return SentenceTransformer(model_name, local_files_only=True)
    except Exception:
        return SentenceTransformer(model_name)


def load_index(index_dir: str | Path = "index") -> tuple[list[dict[str, Any]], np.ndarray, dict[str, Any]]:
    """Load chunks.jsonl, embeddings.npy, and config.json from index_dir."""
    idx_path = Path(index_dir)
    chunks_path = idx_path / "chunks.jsonl"
    embeddings_path = idx_path / "embeddings.npy"
    config_path = idx_path / "config.json"

    if not chunks_path.exists() or not embeddings_path.exists():
        raise FileNotFoundError(
            f"Index files not found in '{idx_path}'. Run 'python ingest.py' first."
        )

    chunks: list[dict[str, Any]] = []
    with chunks_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))

    embeddings = np.load(embeddings_path)
    config: dict[str, Any] = {}
    if config_path.exists():
        with config_path.open("r", encoding="utf-8") as f:
            config = json.load(f)

    return chunks, embeddings, config


def embed_queries(
    questions: list[str],
    model: SentenceTransformer,
    query_prefix: str = BGE_QUERY_PREFIX,
) -> np.ndarray:
    """Embed one or more questions with the BGE query prefix and L2-normalize."""
    prefixed = [f"{query_prefix}{q}" for q in questions]
    q_embs = model.encode(
        prefixed,
        batch_size=64,
        show_progress_bar=False,
        normalize_embeddings=True,
        convert_to_numpy=True,
    ).astype(np.float32)
    norms = np.linalg.norm(q_embs, axis=1, keepdims=True)
    norms = np.where(norms == 0, 1.0, norms)
    return (q_embs / norms).astype(np.float32)


def search_chunks(
    query_emb: np.ndarray,
    chunks: list[dict[str, Any]],
    embeddings: np.ndarray,
    k: int = 5,
    org: str | None = None,
    team: str | None = None,
    scope: str | None = None,
) -> list[dict[str, Any]]:
    """Return top-k chunks by cosine similarity.

    Optional filters on owner_org (--org), owner_team (--team), and scope_level (--scope)
    are off by default. Never ranks or filters by status, last_updated, or supersedes.
    """
    valid_indices: list[int] = []
    for i, c in enumerate(chunks):
        if org is not None and c.get("owner_org", "").lower() != org.strip().lower():
            continue
        if team is not None and c.get("owner_team", "").lower() != team.strip().lower():
            continue
        if scope is not None and c.get("scope_level", "").lower() != scope.strip().lower():
            continue
        valid_indices.append(i)

    if not valid_indices:
        return []

    cand_idx = np.array(valid_indices, dtype=np.int64)
    cand_embs = embeddings[cand_idx]

    # Compute cosine similarity via dot product on normalized vectors
    with np.errstate(divide="ignore", over="ignore", invalid="ignore"):
        scores = cand_embs.astype(np.float64) @ query_emb.astype(np.float64)

    top_order = np.argsort(-scores)[:k]
    results: list[dict[str, Any]] = []
    for rank, pos in enumerate(top_order, start=1):
        chunk_idx = int(cand_idx[pos])
        chunk = chunks[chunk_idx]
        # Strip forbidden plan fields so they can never be exposed
        safe_chunk = {key: val for key, val in chunk.items() if key not in FORBIDDEN_FIELDS}
        safe_chunk["rank"] = rank
        safe_chunk["score"] = float(scores[pos])
        results.append(safe_chunk)

    return results


def make_preview(text: str, max_chars: int = 300) -> str:
    """Create a clean 300-character preview of chunk text."""
    collapsed = " ".join(text.split())
    if len(collapsed) <= max_chars:
        return collapsed
    return collapsed[:max_chars]


def format_result(item: dict[str, Any]) -> str:
    """Format a single search result for terminal output."""
    rank = item["rank"]
    score = item["score"]
    chunk_id = item["chunk_id"]
    title = item["title"]
    heading = item["heading"]
    scope = item["scope_level"]
    owner_org = item["owner_org"]
    owner_team = item["owner_team"]
    status = item["status"]
    updated = item["last_updated"]
    preview = make_preview(item["text"], max_chars=300)

    lines = [
        f"[{rank}] score={score:.4f} | {chunk_id} | {title} > {heading}",
        f"    scope={scope} | owner={owner_org}/{owner_team} | status={status} | updated={updated}",
        f"    preview: {preview}",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Search the local vector index.")
    parser.add_argument("question", type=str, help="Question to search for.")
    parser.add_argument("--k", type=int, default=5, help="Number of top chunks to return (default: 5).")
    parser.add_argument("--org", type=str, default=None, help="Optional filter by owner_org (e.g., PLAT, PROD, DSEC).")
    parser.add_argument("--team", type=str, default=None, help="Optional filter by owner_team (e.g., COMP, WEB, org-wide).")
    parser.add_argument("--scope", type=str, default=None, help="Optional filter by scope_level (team, org, company).")
    parser.add_argument("--index-dir", type=str, default="index", help="Path to index directory (default: index).")
    args = parser.parse_args()

    chunks, embeddings, config = load_index(args.index_dir)
    model_name = config.get("model_name", DEFAULT_MODEL)
    query_prefix = config.get("query_prefix", BGE_QUERY_PREFIX)

    model = load_model(model_name)
    query_emb = embed_queries([args.question], model, query_prefix=query_prefix)[0]

    results = search_chunks(
        query_emb=query_emb,
        chunks=chunks,
        embeddings=embeddings,
        k=args.k,
        org=args.org,
        team=args.team,
        scope=args.scope,
    )

    print(f'Query: "{args.question}" (top {args.k})')
    if args.org or args.team or args.scope:
        print(f"Filters: org={args.org}, team={args.team}, scope={args.scope}")
    print("-" * 80)
    if not results:
        print("No matching chunks found.")
        return

    for item in results:
        print(format_result(item))
        print()


if __name__ == "__main__":
    main()
