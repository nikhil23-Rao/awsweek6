doc_id: DSEC-DATA-011
title: Reservoir Cost Reports Guide
doc_type: guide
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2026-03-18
supersedes:
fact_ids:

# Reservoir Cost Reports Guide

Reservoir costs money, and every team that uses it should be able to see its share. This guide explains how to read the cost dashboards and what to do when a number surprises you.

## Where the numbers come from

Costs are pulled daily from the AWS bill and from the Kestrel usage meter, then attributed to teams using the `owner_team` tag on buckets, jobs, and query workloads. Untagged resources land in an "unattributed" line, which we chase every month.

## Dashboards

| Dashboard | What it shows |
|---|---|
| Overview | Total Reservoir spend by month |
| By team | Spend per owning team, split into storage, compute, and transfer |
| Top tables | The 20 most expensive tables |
| Queries | Quarry query cost by team and user |

## Reading the "By team" view

- **Storage** grows with data volume. A steady upward slope is normal.
- **Compute** follows jobs and queries. Spikes usually line up with a backfill or a heavy report.
- **Transfer** should be small. A large value often means cross-region reads.

## When a number surprises you

1. Open the Top tables view and sort by change over the last month.
2. Check whether a new job or backfill started recently.
3. Look at the Queries view for expensive query patterns, such as full scans of large tables.
4. If nothing explains it, ask in the DATA channel with a link to the dashboard.

## Reducing cost

- Filter on the table's date column in queries to avoid reading everything.
- Remove tables nobody reads; the Top tables view lists last access.
- Schedule heavy jobs overnight.
- Right-size job memory and timeouts.

## Monthly review

Each month DATA posts a summary with the biggest movers and any unattributed cost. Team leads are expected to reply to items that concern them.
