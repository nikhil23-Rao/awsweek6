doc_id: DSEC-DATA-008
title: Streamline Capacity Planning Notes
doc_type: design doc
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: SRE
status: draft
last_updated: 2026-08-12
supersedes:
fact_ids:

# Streamline Capacity Planning Notes (DRAFT)

**Status: draft, open for comments.** Numbers are estimates and need validation against production metrics before use.

## Goal

Decide how many Streamline brokers and how much disk we need for the next twelve months, and when to add capacity, so that we do not scramble when a large product team launches a new feed.

## Current state

- Three Kafka clusters: dev, staging, and prod. This document concerns prod, in us-east-1.
- Throughput has grown steadily over the last year, with peaks at the start of each business day in North America.
- Brokers run on Kestrel with local SSD-backed volumes.
- Producers are mostly product services, with Ledger Core's Meterflow feed as the largest.

## Sizing approach

We size on three constraints, and the tightest one wins:

1. **Network throughput:** peak inbound plus replication traffic per broker must stay under about 60 percent of the instance limit.
2. **Disk:** projected storage after replication must stay under about 70 percent of volume capacity.
3. **Request handling:** broker CPU should stay under about 50 percent at peak to leave room for failures and rebalances.

## Method

1. Take peak hourly inbound volume from the last quarter.
2. Multiply by a growth factor. We propose 1.6 for the next twelve months, based on last year's trend plus known launches.
3. Multiply by the replication factor of three to estimate total broker traffic and storage.
4. Divide by per-broker limits and add one broker of headroom so that a single failure does not exceed limits.

## Early estimate

With the proposed growth factor, we expect the current broker count to meet network and CPU limits until about the second quarter of next year, with disk the first constraint to tighten. Disk expansion is cheaper than adding brokers, so the first step is larger volumes.

## Triggers for action

| Signal | Action |
|---|---|
| Disk above 65 percent on any broker for a week | Plan a volume expansion |
| Network above 55 percent at peak for two weeks | Plan an additional broker |
| Any under-replicated topic during peak | Investigate immediately |

## Risks

- Large launches that were not planned in advance.
- A noisy producer that sends far more than its estimate.
- Rebalancing storms when adding brokers.

## Open questions

1. Is a growth factor of 1.6 reasonable?
2. Should we ask product teams for forecasts each quarter?
3. Is it worth moving the largest feed to a dedicated cluster?

Please comment in the draft or in the DATA channel.
