---
doc_id: PLAT-OBS-013
title: Dashboard Standards
doc_type: standard
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-05-14
supersedes: ""
fact_ids: ""
---

# Dashboard Standards

Observability, Staff Engineer

Standard dashboards mean anyone can open any service's dashboard during an incident and know where to look. Scaffold generates a dashboard that meets this standard; keep it that way as you customize.

## Required rows

Every service dashboard has these rows, in this order:

1. **Overview**: request rate, error rate, p50/p95/p99 latency (the "golden signals"), plus SLO status if defined.
2. **Dependencies**: error rate and latency for each downstream the service calls, from Meridian Mesh metrics.
3. **Saturation**: CPU, memory, and pod count against limits; queue depths for workers.
4. **Deploys**: deploy markers from Ship overlaid on the Overview row.

Teams can add rows below these.

## Naming

- Dashboard title: `<TEAM> / <service>`, for example `SRCH / quarry-api`.
- Panel titles in plain language, with units: "Error rate (%)" not "err_ratio".

## Visual rules

- Time range defaults to the last 6 hours.
- Use the same y-axis units across environments.
- Avoid pie charts. Avoid more than 6 series per panel.
- Red is reserved for thresholds and errors.

## Links

Every dashboard links to the service's runbook, its Tracewell service view, and its Lookout rules file.

## Review

OBS reviews dashboards on request and during the twice-yearly alert quality reviews.
