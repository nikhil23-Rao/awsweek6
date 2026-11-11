doc_id: PROD-SRCH-005
title: Quarry Query Planner Internals
doc_type: design doc
scope_level: team
owner_team: SRCH
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-02-19
supersedes:
fact_ids: 

---

# Quarry Query Planner Internals

**Audience:** Search engineers  **Status:** Approved design reference

## What the planner does

Given a parsed query, the planner chooses how to run it: which shards to read, in what order, which filters to push down, and how to combine partial results.

## Stages

1. **Parse and validate.** Produce a syntax tree and check field names against the schema.
2. **Normalize.** Rewrite equivalent expressions into a canonical form, so that planning rules apply consistently.
3. **Estimate.** Use shard statistics to estimate how many rows each filter will match.
4. **Choose a plan.** Compare candidate plans using a cost model.
5. **Execute.** Run sub-queries on shards and merge.

## Cost model

Costs combine estimated rows scanned, rows returned, and the number of shards touched. The model is deliberately simple. We prefer plans that read less data over those that look clever.

## Pushdown rules

- Time range filters are always pushed to shard selection.
- Equality filters on indexed fields are applied first.
- Aggregations are computed per shard and merged.

## Known limits

- The planner has no statistics for brand-new fields until a batch has been indexed.
- Very wide `OR` expressions can produce large plans.

## Testing

Planner changes are tested with a corpus of 2,000 saved queries; the plan and results must match the previous release unless intended.
