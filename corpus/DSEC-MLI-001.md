doc_id: DSEC-MLI-001
title: FeatureHub Ingestion and Offline Store Guide
doc_type: guide
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2026-03-09
supersedes:
fact_ids: F-DSEC-005

# FeatureHub Ingestion and Offline Store Guide

FeatureHub is the feature store used by teams that train and serve models on Foundry. This guide explains how the offline store is populated from Reservoir and how to configure a new feature view. It is written for ML engineers who are new to FeatureHub.

## How the offline store is built

The offline store is materialized from Reservoir tables by a scheduled FeatureHub job. The job does not copy raw data; it reads the Parquet files of the source table and computes the feature columns you define.

Reservoir tables are **partitioned daily by ingest date**, which means each `dt=` folder holds the rows that were loaded on that day. This matters for two reasons:

1. A daily materialization run reads one new partition, which is the one for the day just ingested.
2. Rows with an old event timestamp can appear in a recent partition, so point-in-time joins must always use the event timestamp column, never the partition value.

To catch stragglers the job re-reads a lookback window of the 3 most recent partitions on every run. You can raise the window per feature view if your source is known to deliver late.

## Configuring a feature view

A feature view is a YAML file in the FeatureHub repo:

```yaml
name: payments_txn_counts
source:
  reservoir_table: payments.transactions
  timestamp_column: event_ts
entities: [account_id]
lookback_partitions: 3
features:
  - name: txn_count_1h
    agg: count
    window: 1h
```

Steps:

1. Open a PR adding the YAML under `views/`.
2. CI validates the schema and checks that the source table exists in the Reservoir catalog.
3. After merge, the next scheduled run creates the offline table. First runs of large views can take several hours.

## Backfills

To backfill history for a new view, set `backfill_from` to the first date you need and submit the backfill job. Because partitions follow ingest date, a backfill for a given calendar day reads the partitions loaded on that day; if you need events that happened on that day but arrived later, widen the range forward by a few days.

## Common problems

- **Features look empty for yesterday:** the upstream load may not have finished. Check the ingestion job status before re-running.
- **Duplicate entity rows:** confirm the view declares every entity key.
- **Slow materialization:** reduce `lookback_partitions` or narrow the column list.

Questions go to the ML Infrastructure channel.
