doc_id: PROD-SRCH-004
title: Sieve Indexing Pipeline Overview
doc_type: design doc
scope_level: team
owner_team: SRCH
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2025-09-10
supersedes:
fact_ids: 

---

# Sieve Indexing Pipeline Overview

**Author:** Staff Engineer (SRCH)  **Status:** Approved

## Purpose

Sieve turns incoming data into searchable indexes. This document describes the path from ingest to a query-ready index.

## Stages

1. **Collect.** Data arrives from customers' agents and integrations through the ingestion gateway.
2. **Parse.** Records are parsed into fields using the account's schema mapping. Unparseable records go to a quarantine stream.
3. **Enrich.** Optional enrichment adds fields (for example, geographic data for IP addresses).
4. **Batch.** Records are grouped into batches by account and time window.
5. **Index.** Batches are written to OpenSearch shards.
6. **Publish.** When a batch is searchable, Sieve updates the metadata that Quarry reads.

## Latency

Typical time from arrival to searchable is under a minute. Under heavy load it can be a few minutes.

## Failure handling

Each stage commits progress, so a failed worker restarts from the last committed point. Quarantined records are visible in Console so customers can fix their data.

## Scaling

Parse and index stages scale independently. The index stage is limited by OpenSearch write capacity, which is monitored.

## Open topics

Smarter batching for very small accounts is an idea we plan to explore.
