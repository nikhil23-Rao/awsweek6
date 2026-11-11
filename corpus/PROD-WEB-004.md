doc_id: PROD-WEB-004
title: Console Service Profile and Support Model
doc_type: service profile
scope_level: team
owner_team: WEB
owner_org: PROD
author_role: Engineering Manager
status: approved
last_updated: 2025-12-09
supersedes:
fact_ids: F-POL-13; F-PROD-012

---

# Console Service Profile and Support Model

*Maintained by the Web Engineering Manager. Reviewed each quarter.*

## Summary

| Item | Value |
|---|---|
| Service | Console |
| Owner | Web (WEB) |
| Service tier | Tier 2 |
| Support hours | Business hours, Monday to Friday |
| Primary channel | #prod-web |

## How we operate Console

Console is operated as a Tier 2 service. The Web team's on-call engineer responds during business hours; outside those hours, customer-visible problems are picked up the next working morning unless Support escalates manually.

## Escalation

1. Support posts in #prod-web with the customer impact and any ticket links.
2. The on-call engineer acknowledges and decides whether the matter needs a wider response.
3. If the cause is in the platform, the engineer asks for help from the platform team.

## Monitoring

Alerts for Console go to the Web on-call channel. Dashboards for latency, error rate and sign-in success are linked from the team wiki.

## Dependencies

Console depends on the TechSync identity service for sign-in, on the product APIs it displays, and on the platform that runs it.

## Review

This profile is reviewed every quarter or when the support model changes.
