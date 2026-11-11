doc_id: PROD-WEB-010
title: Postmortem: Console Dashboard Load Regression
doc_type: postmortem
scope_level: team
owner_team: WEB
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-05-20
supersedes:
fact_ids: 

---

# Postmortem: Console Dashboard Load Regression

**Severity:** Sev3  **Date of incident:** 2026-05-12  **Authors:** Staff Engineer (WEB), with input from the on-call engineer

## Summary

For about six hours, Console dashboards with many widgets took more than twenty seconds to load. No data was lost, and all views remained usable once loaded.

## Impact

Roughly 4% of dashboard views were affected. Support received nine tickets.

## Timeline (Pacific)

- **09:10** A release containing a change to widget loading went out.
- **11:40** Support reported slow dashboards.
- **12:05** The on-call engineer reproduced the problem with a dashboard of 40 widgets.
- **13:20** The cause was found: widget data was requested one at a time instead of in parallel.
- **15:05** A fix was released and load times returned to normal.

## Root cause

A refactor accidentally serialized widget requests. The existing test used a dashboard with three widgets, so it did not notice.

## What went well

Support's early report; a clear reproduction; a quick fix once the cause was known.

## What went badly

No alert existed for slow dashboard loads, and tests did not cover large dashboards.

## Action items

1. Add a performance test with a 40-widget dashboard (owner: Tech Lead).
2. Add an alert on the p75 dashboard load time (owner: SRE).
3. Review other places where requests are made in loops.
