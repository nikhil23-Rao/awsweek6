# Retrieval Baseline — PM Summary

**Status:** Complete & verified offline (`ingest.py`, `search.py`, `eval.py` over `279` docs / `90` test questions).

---

## 1. Key Answers at a Glance

* **Chunking (`--chunk-tokens 300`):** Produced **`1,164` chunks** across `279` docs, averaging **`93` tokens** (`min 50`, `max 397`). Docs are short, so almost every Markdown subheading stayed intact as one chunk.
* **What works vs. what fails (`k=5`):**
  * **Overall:** **88.9% Recall (`80/90`)**, **72.2% Distractor-in-Top-5 (`65/90`)**, **51.1% Ranked-First (`46/90`)**.
  * **Works well:** `control` queries (**100%** Hit@5, **93.3%** Ranked-1st) and `team`-scope lookups (**95.7%** Hit@5).
  * **Fails on:** `outdated` docs (**20.8%** Ranked-1st) and `company` policy vs. `team` overrides (**18.2%** Ranked-1st on `company` scope; **75.0%** Hit@5 on 2-hop questions). Plain similarity ignores `status`/`supersedes` and lets multiple chunks from one specific team runbook crowd out general company policies.
* **Did changing chunk size help?** **No.** `150`, `300`, and `500` tokens gave the exact same **88.9%** Hit@5 and **51.1%** Ranked-1st on both conflicts and controls. Going smaller (`80` tokens) hurt *both* (`85.6%` overall Hit@5) by worsening single-doc crowding.

| Slice | Questions | Hit@5 (Recall) | Distractor in Top 5 | Authoritative Ranked #1 |
| :--- | ---: | ---: | ---: | ---: |
| **All Questions** | **90** | **88.9% (80/90)** | **72.2% (65/90)** | **51.1% (46/90)** |
| `control` | 15 | 100.0% | 46.7% | 93.3% |
| `contradicting` | 26 | 96.2% | 80.8% | 65.4% |
| `outdated` | 24 | 83.3% | 87.5% | **20.8%** |
| `team_vs_company` | 25 | 80.0% | 64.0% | **40.0%** |

---

## 2. Sample Search Spot-Checks (`HF_HUB_OFFLINE=1`)

1. **Kestrel default CPU cores (`Q-PLAT-001`):** Returns both docs, but `PROD-WEB-001` (wrong: 60 cores) ranks `#1` above `PLAT-COMP-009` (authoritative: 40 cores) because the query mentions *"Web team"*.
2. **Ledger API key rotation (`Q-PROD-006`):** Misses the active 90-day policy (`CO-DSEC-005`) completely—4 chunks of an old team runbook (`PROD-PAY-002`) + 1 deprecated policy (`CO-DSEC-006`) take all 5 slots.
3. **Access review frequency (`--scope company`):** Filter works, but deprecated `CO-DSEC-002` (twice/year) ranks `#1` over active `CO-DSEC-001` (quarterly).

---

## 3. Data Fixes Needed Before Phase 2

* **Broken `.md` headers (`corpus/`):**
  * `PLAT-DEVT-015.md` (lines 1–5): Starts with a stray `"No"` line and puts a collapsed `## doc\_id: ...` header *after* `---`.
  * `PROD-PAY-009.md` (line 1): All 12 header fields collapsed onto one line with `\_` escapes.
  * `DSEC-ITC-001.md`, `DSEC-ITC-004.md`, `CO-DSEC-001.md`, `CO-DSEC-011.md`: `fact_ids` uses `, ` instead of `; `.
  * All 60 `ORG-*.md` files: Header `owner_team` values (`PLAT (org-wide)`, `PROD`, `none (DSEC org-wide)`) don't match `org-wide` in `documents.csv`.
* **Table bugs (`tables/`):**
  * `documents.csv` (rows 268–269): Active `CO-DSEC-001` (`2024-02-12`) has an *older* `last_updated` date than the deprecated `CO-DSEC-002` (`2024-02-20`) it supersedes; 5 other deprecated `CO-*` pairs have identical dates on both docs.
  * `questions.csv` (rows 27–31, 57–61, 87–91): All 15 `control` rows list filler docs in `distractor_doc_ids`, inflating control distractor rates (`46.7%`).
  * `questions.csv` (row 33, `Q-PROD-002`): Plan is `X-01`, but `distractor_doc_ids` points to `CO-PLAT-011` (from `PLAT-OUT-1`).
  * `conflict_plans.csv` (row 27, `PROD-TVC-3`): Missing `CO-PLAT-013`, which `Q-PROD-024` requires as an authoritative doc.
  * `facts.csv`: Row 42 (`F-DSEC-006`) puts two IDs (`ORG-DSEC-001; DSEC-MLI-002`) in singular `authoritative_doc_id`; Rows 27 (`F-PROD-003`) & 37 (`F-DSEC-001`) aren't linked back in `documents.csv` `fact_ids`.

---

## 4. Recommended Next Step

Do not tune chunk sizes further. Move to **Phase 2 retrieval**: (1) cap chunks per document (deduplication) so one team runbook cannot take all 5 slots, and (2) rerank using `status`, `supersedes`, and `scope_level` so active company policies beat deprecated/unmarked team docs.
