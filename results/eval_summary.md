# Retrieval Evaluation Summary

## Index Configuration

- **Index directory:** `index`
- **Model:** `BAAI/bge-small-en-v1.5`
- **Target chunk tokens:** `300`
- **Total chunks indexed:** `1164` across `279` documents
- **Mean / Max chunk tokens:** `92.97` / `397`
- **Questions evaluated:** `90` (`k=5`)

## Overall Metrics

| Overall | Questions | Authoritative Hit@5 | Distractor-in-Top-5 | Authoritative-Ranked-First |
| :--- | ---: | ---: | ---: | ---: |
| All Questions | 90 | 88.9% (80/90) | 72.2% (65/90) | 51.1% (46/90) |

## Breakdown by Conflict Type

| Conflict Type | Questions | Authoritative Hit@5 | Distractor-in-Top-5 | Authoritative-Ranked-First |
| :--- | ---: | ---: | ---: | ---: |
| contradicting | 26 | 96.2% (25/26) | 80.8% (21/26) | 65.4% (17/26) |
| outdated | 24 | 83.3% (20/24) | 87.5% (21/24) | 20.8% (5/24) |
| team_vs_company | 25 | 80.0% (20/25) | 64.0% (16/25) | 40.0% (10/25) |
| control | 15 | 100.0% (15/15) | 46.7% (7/15) | 93.3% (14/15) |

## Breakdown by Scope Level

| Scope Level | Questions | Authoritative Hit@5 | Distractor-in-Top-5 | Authoritative-Ranked-First |
| :--- | ---: | ---: | ---: | ---: |
| team | 47 | 95.7% (45/47) | 66.0% (31/47) | 72.3% (34/47) |
| org | 10 | 90.0% (9/10) | 60.0% (6/10) | 60.0% (6/10) |
| company | 33 | 78.8% (26/33) | 84.8% (28/33) | 18.2% (6/33) |
