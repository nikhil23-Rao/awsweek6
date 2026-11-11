doc_id: PROD-SRCH-015
title: Design Doc: Quarry Result Caching
doc_type: design doc
scope_level: team
owner_team: SRCH
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-07-28
supersedes:
fact_ids: 

---

# Design Doc: Quarry Result Caching

**Author:** Staff Engineer (SRCH)  **Status:** Approved

## Context

Dashboards run the same queries repeatedly. Quarry re-executes them each time, which uses shard capacity unnecessarily.

## Goals

- Reduce repeated work for identical queries over unchanged data.
- Never return results that are staler than the data's freshness allows.
- Keep memory use predictable.

## Proposal

Add two cache layers:

1. **Result cache** keyed by account, normalized query and time range. Entries are valid until new data arrives for that window.
2. **Shard-level cache** for partial aggregates over closed time windows. Closed windows never change, so entries can live longer.

## Invalidation

Sieve publishes an event when it indexes a batch. Quarry invalidates cache entries that overlap the batch's time range. Windows older than the indexing delay are treated as closed.

## Sizing

The result cache uses up to 2 GB per node, with a least-recently-used policy. The shard cache uses up to 4 GB.

## Risks

- Cache stampedes on popular queries; mitigated by request coalescing.
- Subtle staleness bugs; mitigated by tests comparing cached and uncached results.

## Alternatives

A cache outside Quarry was simpler but lacked visibility into data freshness.

## Rollout

Enable for a few internal accounts, then compare latency and hit rates.
