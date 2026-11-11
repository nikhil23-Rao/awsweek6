# Local Retrieval Pipeline — TechSync Synthetic Corpus

A local dense retrieval and evaluation pipeline over the TechSync synthetic company corpus (`279` Markdown documents across Platform, Product, and Data & Security). Built for Python 3.10+ using `sentence-transformers` (`BAAI/bge-small-en-v1.5`) and `numpy` — no hosted APIs, LangChain, or LlamaIndex.

---

## Setup

```bash
python3 -m pip install -r requirements.txt
```

### Offline Mode (`HF_HUB_OFFLINE=1`)

The first run of `ingest.py` or `search.py` downloads `BAAI/bge-small-en-v1.5` into the local Hugging Face cache (`~/.cache/huggingface/hub`). All subsequent runs work completely offline:

```bash
export HF_HUB_OFFLINE=1
```

All three scripts automatically load cached model files (`local_files_only=True`) before attempting any network access.

---

## 1. Ingest Corpus (`ingest.py`)

Strips plain `key: value` headers from `corpus/*.md`, loads authoritative document metadata from `tables/documents.csv`, splits document bodies at Markdown headings (and at paragraph breaks with a 50-token overlap if a section exceeds ~400 tokens, scaled proportionally to `--chunk-tokens`), merges sections under ~50 tokens while keeping tables and fenced code blocks intact, embeds `"Title > Heading\n" + text` with L2 normalization, and writes:
- `index/chunks.jsonl`
- `index/embeddings.npy`
- `index/config.json`

```bash
# Default target size (300 tokens) -> writes to index/
python3 ingest.py

# Offline execution
HF_HUB_OFFLINE=1 python3 ingest.py --chunk-tokens 300 --index-dir index

# Build an alternative index to compare chunk sizes
HF_HUB_OFFLINE=1 python3 ingest.py --chunk-tokens 150 --index-dir index_150
```

---

## 2. Search (`search.py`)

Embeds the query using the BGE query prefix (`"Represent this sentence for searching relevant passages: "`), computes cosine similarity against normalized chunk embeddings, and prints the top `k` results (`rank`, `score`, `chunk_id`, `title > heading`, `scope/owner/status/updated`, and a `300`-character preview).

- Never prints `role_in_plan` or `conflict_plan_id`.
- Never ranks or filters by `status`, `last_updated`, or `supersedes`.
- Supports optional `--org`, `--team`, and `--scope` filters (off by default).

```bash
# Basic top-5 search
HF_HUB_OFFLINE=1 python3 search.py "We're spinning up a new Web team namespace on Kestrel. How many CPU cores do we get by default, and how do we get more?" --k 5

# Search with optional metadata filters
HF_HUB_OFFLINE=1 python3 search.py "How often do we review who has access to production systems?" --k 5 --org DSEC --scope company

# Search against a specific index directory
HF_HUB_OFFLINE=1 python3 search.py "How do I deploy Console to prod?" --k 5 --index-dir index_150
```

---

## 3. Evaluate (`eval.py`)

Runs top-5 search across all 90 questions in `tables/questions.csv` and compares retrieved `doc_id`s against `authoritative_doc_ids` and `distractor_doc_ids` (split on `"; "`). Computes:
- **Authoritative Hit@5**
- **Distractor-in-Top-5**
- **Authoritative-Ranked-First**

broken down overall, by `conflict_type`, and by `scope_level`. Writes:
- `results/eval_per_question.csv`
- `results/eval_summary.md`
- `results/failures.md` (questions with no authoritative document in the top 5)

```bash
# Evaluate default index
HF_HUB_OFFLINE=1 python3 eval.py

# Compare a different chunk size index
HF_HUB_OFFLINE=1 python3 eval.py --index-dir index_150 --output-dir results_150
```
