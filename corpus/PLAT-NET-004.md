---
doc_id: PLAT-NET-004
title: EdgeGate Rate Limiting Reference
doc_type: reference
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-12-01
supersedes: ""
fact_ids: ""
---

# EdgeGate Rate Limiting Reference

Networking, EdgeGate

EdgeGate enforces rate limits at the edge so a single noisy client can't degrade TechSync for everyone. This page explains the policy types and how to configure them for your routes.

## Policy types

| Type | Key | Typical use |
|---|---|---|
| `per_api_key` | API key or token | Public APIs for Ship and Ledger |
| `per_ip` | Client IP | Unauthenticated endpoints such as login and signup |
| `per_org` | Customer org ID | Fair-share limits across a customer's users |
| `global` | Route | Protecting a fragile backend |

Limits use a token bucket: a sustained rate plus a burst size.

## Configuring a route

Rate limits live in the route's EdgeGate config in the owning team's repo:

```yaml
route: /v2/ledger/usage
rate_limits:
  - type: per_api_key
    rate: 200/s
    burst: 400
  - type: per_org
    rate: 1000/s
    burst: 2000
```

Changes go through Gatekeeper CI like any other config.

## Tier-based defaults

Customer plans (Free, Team, Enterprise) map to default limit profiles maintained by the Product teams. EdgeGate reads the customer's plan from the auth token, so you usually only set route-specific overrides.

## What clients see

Requests over the limit get HTTP `429` with `Retry-After` and `X-RateLimit-*` headers. Make sure your public API docs describe them.

## Monitoring

The `edgegate_ratelimit_rejections_total` metric is labeled by route and policy type. Sudden spikes usually mean a customer integration is retrying in a tight loop. Contact the account team before raising limits.

## Getting help

#net-edgegate.
