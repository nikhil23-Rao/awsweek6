doc_id: DSEC-DATA-001
title: Reservoir Table Layout and Partitioning Runbook
doc_type: runbook
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2026-07-14
supersedes:
fact_ids: F-DSEC-005

# Reservoir Table Layout and Partitioning Runbook

**Owner:** Data Platform (DATA) | **Audience:** engineers who create, read, or repair Reservoir tables

## Purpose

This runbook describes how tables are laid out in Reservoir, our data lake, and how to create, inspect, and repair partitions. Reservoir stores tables as Parquet files on S3 in us-east-1, with table metadata kept in the Reservoir catalog.

## Partitioning standard

Every Reservoir table is partitioned **daily by event date**. The partition value is derived from the event timestamp carried in the record itself, converted to UTC, and written as `dt=YYYY-MM-DD` in the object path:

```
s3://reservoir-prod/<domain>/<table>/dt=2026-07-14/part-0000.parquet
```

Consequences you should plan for:

- A record that arrives late is written to the partition of the day it happened, not the day it arrived. Partitions for the most recent 7 days therefore remain open for rewrite.
- Queries that filter on `dt` are pruned to the matching partitions. Always include a `dt` range in ad hoc queries through Quarry.
- Each record also carries an `_ingested_at` column, populated by the ingestion job. It exists for audit and debugging.

## Creating a new table

1. Register the dataset (see the Dataset Onboarding FAQ) and pick a domain prefix.
2. Define the schema in the Reservoir catalog, naming the event timestamp column that drives `dt`.
3. Apply the Terraform module for the table so bucket policy and catalog entries are created together.
4. Run the smoke-load job against a one-day sample and confirm that one `dt=` folder appears for each distinct event date in the sample.

## Compaction

A nightly compaction job runs at 02:00 UTC and merges small files inside each open partition into files of roughly 256 MB. Do not run manual compaction on a partition while the nightly job is active; check the job status page first.

## Repairing a partition

If a partition is missing or contains duplicates:

1. Pause the downstream Streamline consumer group that feeds the table.
2. Move the damaged `dt=` folder to the `_quarantine/` prefix. Do not delete it until the repair is verified.
3. Re-run the batch job for that event date only.
4. Compare row counts against the Streamline topic offsets for the same date window.
5. Resume the consumer group and note the repair in the DATA on-call log.

## Escalation

Questions about layout go to the DATA channel in Slack. Anything affecting more than one domain should go to the Tech Lead before changes are made.
