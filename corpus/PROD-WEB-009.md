doc_id: PROD-WEB-009
title: Console Frontend Performance Budget
doc_type: standard
scope_level: team
owner_team: WEB
owner_org: PROD
author_role: Tech Lead
status: approved
last_updated: 2025-11-18
supersedes:
fact_ids: 

---

# Console Frontend Performance Budget

## Purpose

A budget keeps Console fast as it grows. Each page has targets; a pull request that pushes a page over its budget needs a conversation before merging.

## Budgets

| Metric | Target |
|---|---|
| Initial JavaScript (gzipped) | 250 KB |
| Largest Contentful Paint (p75) | 2.5 s |
| Interaction to Next Paint (p75) | 200 ms |
| Cumulative Layout Shift (p75) | 0.1 |

Measured on a mid-range laptop on a typical broadband connection.

## How it is enforced

- The CI pipeline reports bundle sizes on every pull request.
- A bot comments when the initial bundle grows by more than 5 KB.
- Real-user measurements from production feed weekly dashboards.

## Common ways to stay within budget

1. Split code by route and load heavy components on demand.
2. Prefer lightweight libraries; check size before adding a dependency.
3. Avoid layout shifts by reserving space for images and tables.
4. Cache API responses where it is safe.

## Exceptions

If a feature genuinely needs more, the Tech Lead can approve a temporary increase. Record it in the pull request with a plan to recover the budget.

## Review

The budget is reviewed each November.
