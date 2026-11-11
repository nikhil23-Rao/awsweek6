doc_id: DSEC-MLI-013
title: Foundry Cost Allocation Guide
doc_type: guide
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2026-03-30
supersedes:
fact_ids:

# Foundry Cost Allocation Guide

Foundry costs are charged back to the teams that cause them. This guide explains how allocation works, so that your team's bill is accurate and predictable.

## How charges are calculated

Costs fall into three buckets:

| Bucket | Driver | Allocated by |
|---|---|---|
| Training | GPU-hours consumed by jobs | `cost_center` tag on the job |
| Serving | Replica-hours of each endpoint | `cost_center` tag on the endpoint |
| Shared | Registry, tracking, dashboards | Split in proportion to the other two |

## Tagging

Every job spec and serving spec must contain a `cost_center` tag, using the codes published by Finance. Jobs without a tag are blocked at submission, so you will find out immediately rather than at the end of the month.

```yaml
tags:
  cost_center: search
  project: ranker-v7
```

## Reports

Weekly and monthly reports are available in the Foundry cost dashboard. Each report lists spend by `cost_center`, by project, and by user.

## Common questions

- **Why is the shared bucket not zero?** It covers platform components that nobody can use alone.
- **Can I move spend to another cost center?** Only with the approval of both cost center owners, through a ticket.
- **What about idle GPUs?** They are charged to the reserving team. Cancel jobs you no longer need.
- **Do spot GPUs cost less?** Yes, and the report shows them separately.

## Disputes

If a charge looks wrong, open a ticket in the MLI queue with the job ID or endpoint name. The MLI engineering manager decides within a week.
