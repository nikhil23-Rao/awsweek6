doc_id: PROD-SRCH-007
title: OpenSearch Cluster Capacity Planning
doc_type: guide
scope_level: team
owner_team: SRCH
owner_org: PROD
author_role: SRE
status: approved
last_updated: 2026-03-26
supersedes:
fact_ids: 

---

# OpenSearch Cluster Capacity Planning

**Author:** SRE (SRCH)  **Status:** Approved

## Why plan

Search clusters run out of capacity slowly and then suddenly. Planning ahead avoids emergency expansions.

## Key quantities

| Quantity | Guidance |
|---|---|
| Shard size | Target 30 to 50 GB |
| Shards per node | Fewer than 20 per GB of heap |
| Disk headroom | Keep at least 25% free |
| Heap | Half of memory, up to 31 GB |

## Estimating growth

1. Take the daily ingest volume from the Sieve dashboard.
2. Multiply by the replication factor.
3. Multiply by retention days to get the storage needed.
4. Add 25% headroom.
5. Divide by usable disk per node.

## Review cadence

Review each cluster monthly. Raise a ticket when projected usage will pass 70% within 90 days.

## Expansion

Add nodes in pairs across availability zones. Rebalancing takes hours; schedule expansions off-peak and watch search latency.

## Warning signs

Rising rejected-bulk counts, long garbage collection pauses, or shards stuck relocating.

## Cost

The finance partner reviews cluster costs each quarter. Savings usually come from shard sizing and index lifecycle choices.
