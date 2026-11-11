doc_id: CO-PROD-004
title: Product Overview: TechSync Insight
doc_type: product overview
scope_level: company
owner_team: Technical Writing
owner_org: PROD
author_role: Technical Writer
status: approved
last_updated: 2026-05-18
supersedes: PROD-SRCH-003
fact_ids: F-PROD-007

---

# Product Overview: TechSync Insight

**Category:** Logs, metrics, traces and search
**General availability:** June 2024

## Summary

TechSync Insight brings the signals you need to run software into one place: logs, metrics and traces, with a search experience that lets you move between them without changing tools. Insight was introduced in 2023 as a beta program and reached general availability in June 2024.

## Availability by tier

Insight is generally available to **all customer tiers: Free, Team and Enterprise**. Usage limits differ by tier and are set out in each customer's order form. During the beta in 2023, access was limited to Enterprise customers; that restriction ended when the product reached general availability in June 2024.

## What you can do

- **Search.** Query logs and events with a purpose-built query language and save the searches you use often.
- **Metrics.** Build dashboards from metrics emitted by your services and compare them against deploys.
- **Traces.** Follow a request across services to find where time is spent.
- **Alerting.** Define alert conditions and route notifications to your on-call tools.

## How it is built

Under the hood, Insight uses a query engine (Quarry) and an indexer (Sieve) maintained by the Search team, with OpenSearch as one of the storage back ends. Customers do not need to know these names to use the product, but they help when you read internal documentation.

## Related products

- **Ship** can send release markers to Insight.
- **Console** hosts the Insight user interface alongside our other products.
- **Mobile** can surface Insight alerts as push notifications.

## Questions

Customers should contact support. Internal readers can find the owning team in the Product Engineering directory.
