---
doc_id: ORG-PLAT-020
title: Platform SLO Policy
doc_type: policy
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2025-07-08
supersedes: ""
fact_ids: ""
---

# Platform SLO Policy

**Owner:** SRE, Platform Engineering
**Scope:** internal service level objectives for Platform systems

## Which systems need SLOs

Every system in the Platform Service Catalog must publish at least one SLO:

| System | Example SLIs |
|---|---|
| Kestrel | API server availability, pod scheduling latency |
| Forge | Job queue time |
| Meridian Mesh | Sidecar-added latency |
| EdgeGate | Availability, added latency |
| Lookout | Alert evaluation delay, notification delivery |
| Tracewell | Ingestion delay |
| Gatekeeper CI | Pipeline dispatch time, deploy success rate |

## Requirements

1. SLOs are defined in Lookout using the SLO Definition Guide.
2. Each SLO has a burn-rate alert.
3. SLO targets are reviewed every six months by the owning team and the Platform staff engineers.
4. SLO dashboards are linked from the Platform Service Catalog.

## Error budget policy

- When a Platform system exhausts its error budget for the 28-day window, the owning team prioritizes reliability work over new features until the budget recovers.
- The team's engineering manager decides which work pauses.
- Repeated budget exhaustion is raised at the Platform quarterly review.

## Customer-facing commitments

Customer contracts are managed by the CTO office and are out of scope here. Internal SLOs should be tighter than anything customers depend on.

## Reporting

A monthly SLO report covering every Platform system is posted in #platform.
