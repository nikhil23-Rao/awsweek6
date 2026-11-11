---
doc_id: PLAT-OBS-015
title: Tracewell Collector Scaling Runbook
doc_type: runbook
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2026-04-28
supersedes: ""
fact_ids: ""
---

# Tracewell Collector Scaling Runbook

Observability, SRE rotation

Collectors receive spans and logs from every service and write them to storage. If they fall behind, data is delayed and dashboards go stale. Collectors autoscale on queue depth since Q2 2026; this runbook covers what to do when autoscaling isn't enough.

## Signals

- `tracewell_collector_queue_depth` rising for more than 10 minutes.
- `tracewell_ingest_delay_seconds` above 300.
- Alert: `TracewellIngestionLagging`.

## Step 1: Find the source

Check the **Ingestion by service** panel. If one service's volume jumped, that's almost always the cause. Contact the owning team; a debug log level or a logging loop is the usual culprit.

## Step 2: Apply a per-service limit

Per-service ingestion limits can be tightened temporarily:

```
tracewell limits set --service meterflow --logs-per-sec 20000 --ttl 4h
```

Dropped data is counted in `tracewell_dropped_total` so the team knows what they lost.

## Step 3: Scale manually

If load is broad, raise the autoscaler maximum:

```
kubectl -n obs-tracewell patch hpa collectors --patch '{"spec":{"maxReplicas":120}}'
```

Check that OpenSearch can absorb the higher write rate before going further.

## Step 4: Protect OpenSearch

If OpenSearch write latency climbs, enable the collector's spill-to-S3 mode. Data is buffered in S3 and replayed later.

```
tracewell spill enable --region us-east-1
```

## After the incident

Reset any manual changes, remove temporary limits, and file a ticket for follow-ups.
