---
doc_id: PLAT-NET-006
title: Meridian Mesh Configuration Reference
doc_type: reference
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: Tech Lead
status: approved
last_updated: 2026-07-14
supersedes: ""
fact_ids: F-PLAT-003
---

# Meridian Mesh Configuration Reference

Maintained by Networking (NET). Applies to every service that runs with a Meridian Mesh sidecar on Kestrel, in dev, staging, and prod.

This page lists the defaults the mesh applies when a service doesn't override them. NET owns these values. If you need something different for a route, override it in your service's `mesh.yaml` (see "Overrides" below) rather than asking us to change the global default.

## Traffic defaults

| Setting | Default | Notes |
|---|---|---|
| Per-route request timeout | **15 s** | Applies to each HTTP and gRPC route. The timer starts when the sidecar sends the request upstream. |
| Retries | 2 | Only on connect failures, `503`, and gRPC `UNAVAILABLE`. Never on `POST` unless the route opts in. |
| Retry per-try timeout | 5 s | |
| Retry budget | 20% of active requests | Prevents retry storms during partial outages. |
| Connection idle timeout | 60 min | |
| Max concurrent requests per upstream host | 1,024 | |

## Security defaults

| Setting | Default |
|---|---|
| mTLS mode | STRICT in staging and prod, PERMISSIVE in dev |
| Peer authentication | Workload identity from Kestrel service accounts |
| Authorization policy | Deny by default between namespaces; allow within a namespace |

## Load balancing

- Algorithm: least-request.
- Locality-aware routing is on by default; traffic stays in the caller's availability zone while that zone is healthy.
- Outlier detection ejects a host after 5 consecutive `5xx` responses, for 30 s initially.

## Overrides

Add a `mesh.yaml` next to your service manifest:

```yaml
routes:
  - match: /v1/reports/export
    timeout: 45s
    retries: 0
```

Overrides are reviewed by Gatekeeper CI policy checks. Timeouts above 120 s need a NET reviewer on the PR.

## Observability

Every sidecar exports request metrics to Lookout and spans to Tracewell. Look for the `meridian_route_timeouts_total` metric when debugging slow upstreams.

## Change log

- 2026-07-14: Clarified retry per-try timeout and outlier ejection settings.
- 2026-01-20: Raised max concurrent requests per host from 512 to 1,024.

Questions: #net-mesh.
