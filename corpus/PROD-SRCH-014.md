doc_id: PROD-SRCH-014
title: Search Relevance Evaluation Harness
doc_type: how-to
scope_level: team
owner_team: SRCH
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-02-02
supersedes:
fact_ids: 

---

# Search Relevance Evaluation Harness

## What it is

A set of tools that measure how good our search ranking is. You give it queries and the results people consider correct; it reports how well Quarry ranks them.

## Inputs

- **Query set:** a CSV of sample queries (about 500).
- **Judgments:** for each query, a list of documents with a relevance grade from 0 to 3.
- **Configuration:** the ranking settings to test.

## Metrics

| Metric | Meaning |
|---|---|
| nDCG@10 | Quality of the top ten, weighted by position |
| Recall@50 | Share of relevant documents in the top fifty |
| MRR | How high the first relevant result appears |

## Running it

```
relevance-eval run --queries queries.csv --judgments judgments.csv --config candidate.yaml
```

The tool prints a table and writes a detailed report. Use `--baseline baseline.yaml` to compare two configurations side by side.

## Interpreting results

Small changes can be noise. Look at the whole query set and at the worst-hit queries, not only the average.

## Adding judgments

Judges grade results in the review tool. Aim for at least two graders per query.

## Limits

Judgments reflect today's content and may need refreshing.
