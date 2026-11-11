doc_id: PROD-SRCH-010
title: SRCH Insight Roadmap Review, August 2026
doc_type: meeting notes
scope_level: team
owner_team: SRCH
owner_org: PROD
author_role: Engineering Manager
status: unmarked
last_updated: 2026-08-19
supersedes:
fact_ids: 

---

# SRCH Insight Roadmap Review, August 2026

*Team discussion notes. Present: Engineering Manager, Tech Lead, Staff Engineers, SRE, a Product partner.*

## Items reviewed

1. **Saved search improvements.** Users want folders and sharing. Large effort; need design input.
2. **Faster time-range queries.** Staff Engineer proposed pre-aggregated rollups. Promising for dashboards.
3. **Better query errors.** Several teams noted that error messages are hard to read. Quick wins likely.
4. **Alerting on search results.** Mobile team is interested. Needs a conversation about volume.

## Discussion

- Rollups could reduce load but add storage and complexity.
- The SRE suggested measuring query patterns first.
- The Product partner asked for a ranking of items by customer demand.

## Ideas, not decisions

- Rollups as a pilot on one account.
- Reuse the planner's statistics for query hints.
- Share an early demo with Console designers.

## Actions

- Tech Lead to collect demand data.
- Staff Engineer to sketch the rollup design.
- Engineering Manager to ask Design for a time slot.

## Next review

October.
