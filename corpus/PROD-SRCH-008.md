doc_id: PROD-SRCH-008
title: Postmortem: Quarry Slow Queries after Shard Rebalance
doc_type: postmortem
scope_level: team
owner_team: SRCH
owner_org: PROD
author_role: SRE
status: approved
last_updated: 2026-06-22
supersedes:
fact_ids: 

---

# Postmortem: Quarry Slow Queries after Shard Rebalance

**Severity:** Sev2  **Incident date:** 2026-06-15  **Published:** 2026-06-22  **Author:** SRE (SRCH)

## Summary

After an automatic shard rebalance, query latency for a group of accounts rose sharply for about 90 minutes. Searches completed, but many were several times slower than normal.

## Impact

Around 12% of queries were affected. Dashboards that refresh frequently were slow to update.

## Timeline (UTC)

- **13:00** OpenSearch began moving shards after a node was added.
- **13:25** Latency alerts fired for the affected accounts.
- **13:40** The on-call engineer found heavy relocation traffic on two nodes.
- **14:10** Relocation was throttled.
- **14:35** Latency returned to normal.

## Root cause

Rebalancing ran at its default concurrency while the cluster was under normal query load. Several large shards moved at once and competed with search for disk and network.

## What went well

Alerts fired early. The mitigation was simple and quick once the cause was identified.

## What went badly

We expanded the cluster during busy hours and had no limit on rebalance concurrency.

## Action items

1. Set a lower default relocation concurrency (owner: SRE).
2. Update the capacity planning guide to recommend off-peak expansions (owner: Tech Lead).
3. Add a dashboard panel for shard relocations.
