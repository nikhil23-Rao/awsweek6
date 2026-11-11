#!/usr/bin/env python3
"""Evaluate retrieval performance on tables/questions.csv.

Runs top-5 search for each evaluation question, compares retrieved doc_ids
against authoritative_doc_ids and distractor_doc_ids (split on '; '), and
computes authoritative hit@5, distractor-in-top-5, and authoritative-ranked-first
overall and by conflict_type and scope_level.

Writes:
  - results/eval_per_question.csv
  - results/eval_summary.md
  - results/failures.md
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

from search import (
    BGE_QUERY_PREFIX,
    DEFAULT_MODEL,
    embed_queries,
    load_index,
    load_model,
    make_preview,
    search_chunks,
)


def parse_id_list(raw: str) -> list[str]:
    """Split semicolon-delimited document IDs on '; '."""
    if not raw or not raw.strip():
        return []
    return [item.strip() for item in raw.split("; ") if item.strip()]


def compute_group_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Compute count and rates for authoritative hit@5, distractor-in-top-5, and authoritative-ranked-first."""
    n = len(rows)
    if n == 0:
        return {
            "count": 0,
            "auth_hit_count": 0,
            "auth_hit_rate": 0.0,
            "dist_top5_count": 0,
            "dist_top5_rate": 0.0,
            "auth_first_count": 0,
            "auth_first_rate": 0.0,
        }
    auth_hit = sum(1 for r in rows if r["authoritative_hit_at_5"])
    dist_top5 = sum(1 for r in rows if r["distractor_in_top_5"])
    auth_first = sum(1 for r in rows if r["authoritative_ranked_first"])
    return {
        "count": n,
        "auth_hit_count": auth_hit,
        "auth_hit_rate": auth_hit / n,
        "dist_top5_count": dist_top5,
        "dist_top5_rate": dist_top5 / n,
        "auth_first_count": auth_first,
        "auth_first_rate": auth_first / n,
    }


def format_metric_cell(count: int, total: int, rate: float) -> str:
    """Format a metric as 'XX.X% (count/total)'."""
    return f"{rate * 100:.1f}% ({count}/{total})"


def build_markdown_table(
    group_label: str,
    groups: list[tuple[str, list[dict[str, Any]]]],
) -> str:
    """Render a Markdown summary table for a list of (group_name, rows) pairs."""
    lines = [
        f"| {group_label} | Questions | Authoritative Hit@5 | Distractor-in-Top-5 | Authoritative-Ranked-First |",
        "| :--- | ---: | ---: | ---: | ---: |",
    ]
    for name, grp_rows in groups:
        m = compute_group_metrics(grp_rows)
        n = m["count"]
        lines.append(
            f"| {name} | {n} | "
            f"{format_metric_cell(m['auth_hit_count'], n, m['auth_hit_rate'])} | "
            f"{format_metric_cell(m['dist_top5_count'], n, m['dist_top5_rate'])} | "
            f"{format_metric_cell(m['auth_first_count'], n, m['auth_first_rate'])} |"
        )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate local retrieval pipeline on tables/questions.csv.")
    parser.add_argument(
        "--index-dir",
        type=str,
        default="index",
        help="Path to index directory (default: index).",
    )
    parser.add_argument(
        "--questions-csv",
        type=str,
        default="tables/questions.csv",
        help="Path to questions.csv (default: tables/questions.csv).",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="results",
        help="Directory to write evaluation outputs (default: results).",
    )
    parser.add_argument(
        "--k",
        type=int,
        default=5,
        help="Top-k cutoff for evaluation (default: 5).",
    )
    args = parser.parse_args()

    questions_path = Path(args.questions_csv)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with questions_path.open("r", encoding="utf-8", newline="") as f:
        questions = list(csv.DictReader(f))

    chunks, embeddings, config = load_index(args.index_dir)
    model_name = config.get("model_name", DEFAULT_MODEL)
    query_prefix = config.get("query_prefix", BGE_QUERY_PREFIX)

    print(f"Loaded index from '{args.index_dir}' ({len(chunks)} chunks, chunk_tokens={config.get('chunk_tokens')}).")
    print(f"Embedding {len(questions)} questions from {questions_path}...")
    model = load_model(model_name)
    q_texts = [q["question"].strip() for q in questions]
    q_embs = embed_queries(q_texts, model, query_prefix=query_prefix)

    eval_rows: list[dict[str, Any]] = []
    failure_records: list[dict[str, Any]] = []

    for idx, q in enumerate(questions):
        qid = q["question_id"].strip()
        plan_id = q["plan_id"].strip()
        asker_team = q["asker_team"].strip()
        question_text = q["question"].strip()
        gold_answer = q["gold_answer"].strip()
        conflict_type = q["conflict_type"].strip()
        scope_level = q["scope_level"].strip()
        hops = q["hops"].strip()

        auth_docs = parse_id_list(q["authoritative_doc_ids"])
        dist_docs = parse_id_list(q["distractor_doc_ids"])
        auth_set = set(auth_docs)
        dist_set = set(dist_docs)

        top_chunks = search_chunks(
            query_emb=q_embs[idx],
            chunks=chunks,
            embeddings=embeddings,
            k=args.k,
        )

        top_doc_ids = [c["doc_id"] for c in top_chunks]
        top_chunk_ids = [c["chunk_id"] for c in top_chunks]
        top_1_score = round(top_chunks[0]["score"], 4) if top_chunks else 0.0

        auth_hit_at_5 = any(d in auth_set for d in top_doc_ids)
        dist_in_top_5 = any(d in dist_set for d in top_doc_ids)
        auth_ranked_first = bool(top_doc_ids and top_doc_ids[0] in auth_set)

        first_auth_rank = next((i + 1 for i, d in enumerate(top_doc_ids) if d in auth_set), "")
        first_dist_rank = next((i + 1 for i, d in enumerate(top_doc_ids) if d in dist_set), "")

        row_record = {
            "question_id": qid,
            "plan_id": plan_id,
            "asker_team": asker_team,
            "conflict_type": conflict_type,
            "scope_level": scope_level,
            "hops": hops,
            "question": question_text,
            "authoritative_doc_ids": "; ".join(auth_docs),
            "distractor_doc_ids": "; ".join(dist_docs),
            "top_5_doc_ids": "; ".join(top_doc_ids),
            "top_5_chunk_ids": "; ".join(top_chunk_ids),
            "top_1_score": f"{top_1_score:.4f}",
            "authoritative_hit_at_5": auth_hit_at_5,
            "distractor_in_top_5": dist_in_top_5,
            "authoritative_ranked_first": auth_ranked_first,
            "first_authoritative_rank": first_auth_rank,
            "first_distractor_rank": first_dist_rank,
        }
        eval_rows.append(row_record)

        if not auth_hit_at_5:
            failure_records.append(
                {
                    "question": row_record,
                    "gold_answer": gold_answer,
                    "top_chunks": top_chunks,
                }
            )

    # 1. Write results/eval_per_question.csv
    per_question_path = output_dir / "eval_per_question.csv"
    fieldnames = [
        "question_id",
        "plan_id",
        "asker_team",
        "conflict_type",
        "scope_level",
        "hops",
        "question",
        "authoritative_doc_ids",
        "distractor_doc_ids",
        "top_5_doc_ids",
        "top_5_chunk_ids",
        "top_1_score",
        "authoritative_hit_at_5",
        "distractor_in_top_5",
        "authoritative_ranked_first",
        "first_authoritative_rank",
        "first_distractor_rank",
    ]
    with per_question_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(eval_rows)

    # 2. Write results/eval_summary.md
    conflict_order = ["contradicting", "outdated", "team_vs_company", "control"]
    seen_conflicts = sorted({r["conflict_type"] for r in eval_rows}, key=lambda x: (conflict_order.index(x) if x in conflict_order else 99, x))
    conflict_groups = [(ct, [r for r in eval_rows if r["conflict_type"] == ct]) for ct in seen_conflicts]

    scope_order = ["team", "org", "company"]
    seen_scopes = sorted({r["scope_level"] for r in eval_rows}, key=lambda x: (scope_order.index(x) if x in scope_order else 99, x))
    scope_groups = [(sc, [r for r in eval_rows if r["scope_level"] == sc]) for sc in seen_scopes]

    overall_table = build_markdown_table("Overall", [("All Questions", eval_rows)])
    conflict_table = build_markdown_table("Conflict Type", conflict_groups)
    scope_table = build_markdown_table("Scope Level", scope_groups)

    summary_lines = [
        "# Retrieval Evaluation Summary",
        "",
        "## Index Configuration",
        "",
        f"- **Index directory:** `{args.index_dir}`",
        f"- **Model:** `{model_name}`",
        f"- **Target chunk tokens:** `{config.get('chunk_tokens', 'N/A')}`",
        f"- **Total chunks indexed:** `{len(chunks)}` across `{config.get('num_documents', 279)}` documents",
        f"- **Mean / Max chunk tokens:** `{config.get('mean_chunk_tokens', 'N/A')}` / `{config.get('max_chunk_tokens', 'N/A')}`",
        f"- **Questions evaluated:** `{len(eval_rows)}` (`k={args.k}`)",
        "",
        "## Overall Metrics",
        "",
        overall_table,
        "",
        "## Breakdown by Conflict Type",
        "",
        conflict_table,
        "",
        "## Breakdown by Scope Level",
        "",
        scope_table,
        "",
    ]

    summary_path = output_dir / "eval_summary.md"
    summary_path.write_text("\n".join(summary_lines), encoding="utf-8")

    # 3. Write results/failures.md
    failure_lines = [
        "# Retrieval Failures (No Authoritative Document in Top 5)",
        "",
        f"- **Index directory:** `{args.index_dir}` (`chunk_tokens={config.get('chunk_tokens', 'N/A')}`)",
        f"- **Total failures:** `{len(failure_records)}` out of `{len(eval_rows)}` questions",
        "",
    ]
    if not failure_records:
        failure_lines.append("All questions had at least one authoritative document in the top 5.")
    else:
        for item in failure_records:
            q_info = item["question"]
            failure_lines.extend(
                [
                    f"## {q_info['question_id']} ({q_info['conflict_type']} | scope: {q_info['scope_level']} | plan: {q_info['plan_id'] or 'control'})",
                    "",
                    f"- **Asker team:** `{q_info['asker_team']}` | **Hops:** `{q_info['hops']}`",
                    f"- **Question:** {q_info['question']}",
                    f"- **Expected authoritative doc(s):** `{q_info['authoritative_doc_ids']}`",
                    f"- **Distractor doc(s):** `{q_info['distractor_doc_ids'] or 'none'}`",
                    f"- **Distractor in top 5:** `{q_info['distractor_in_top_5']}` (first distractor rank: `{q_info['first_distractor_rank'] or 'N/A'}`)",
                    f"- **Gold answer:** {item['gold_answer']}",
                    "",
                    "### Retrieved Top 5 Chunks",
                    "",
                    "| Rank | Score | Chunk ID | Doc ID | Title > Heading | Scope / Owner / Status / Updated | Preview |",
                    "| ---: | ---: | :--- | :--- | :--- | :--- | :--- |",
                ]
            )
            for c in item["top_chunks"]:
                meta_str = f"{c['scope_level']} / {c['owner_org']}:{c['owner_team']} / {c['status']} / {c['last_updated']}"
                preview_str = make_preview(c["text"], max_chars=120).replace("|", "\\|")
                title_heading = f"{c['title']} > {c['heading']}".replace("|", "\\|")
                failure_lines.append(
                    f"| {c['rank']} | {c['score']:.4f} | `{c['chunk_id']}` | `{c['doc_id']}` | {title_heading} | `{meta_str}` | {preview_str} |"
                )
            failure_lines.append("")

    failures_path = output_dir / "failures.md"
    failures_path.write_text("\n".join(failure_lines), encoding="utf-8")

    # Print summary to stdout
    print("\n" + "\n".join(summary_lines))
    print(f"Wrote {per_question_path}")
    print(f"Wrote {summary_path}")
    print(f"Wrote {failures_path} ({len(failure_records)} failures)")


if __name__ == "__main__":
    main()
