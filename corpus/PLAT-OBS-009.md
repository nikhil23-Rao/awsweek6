---
doc_id: PLAT-OBS-009
title: SLO Definition Guide
doc_type: guide
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2024-12-03
supersedes: ""
fact_ids: ""
---

# SLO Definition Guide

Observability. Author: Staff Engineer.

Service level objectives (SLOs) are how we decide whether a service is reliable enough, and how we balance shipping features against reliability work. This guide explains how to define good ones for internal service SLOs. It doesn't cover customer contracts.

## Terms

- **SLI (indicator):** a measurement of good events divided by total events. Example: the share of HTTP requests that return a non-5xx response in under 300 ms.
- **SLO (objective):** a target for the SLI over a window. Example: 99.5% over 28 days.
- **Error budget:** what's left over. A 99.5% SLO gives a 0.5% budget.

## Choosing SLIs

Pick indicators your users would notice:

| Service type | Good SLIs |
|---|---|
| Request/response API | Availability, latency |
| Data pipeline | Freshness, completeness |
| Batch job | Success rate, completion time |

Avoid CPU, memory, and other resource metrics as SLIs. They're causes, not user experience.

## Choosing targets

- Start from what the service achieves today, then decide if that's good enough.
- Don't set a target higher than your dependencies can support.
- Two or three SLOs per service is plenty.

## Using error budgets

- **Budget healthy:** ship freely.
- **Budget burning fast:** alert on burn rate, not on single errors.
- **Budget exhausted:** pause risky changes and prioritize reliability work, by agreement with the team's manager.

## Implementing

Define SLOs in `lookout/slos.yaml` in your repo. Lookout generates burn-rate alerts and a standard SLO dashboard panel.

## Help

#obs-help
