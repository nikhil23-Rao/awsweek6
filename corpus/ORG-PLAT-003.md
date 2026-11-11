---
doc_id: ORG-PLAT-003
title: Platform Service Catalog
doc_type: reference
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: Technical Writer
status: approved
last_updated: 2026-09-10
supersedes: ""
fact_ids: ""
---

# Platform Service Catalog

**Maintained by:** Technical Writing, Platform Engineering
**Last full review:** September 2026

The list of every system Platform Engineering runs, who owns it, and where to ask questions.

| System | What it does | Owning team | Help channel | Pager |
|---|---|---|---|---|
| Kestrel | Internal Kubernetes platform (EKS) | Compute | #comp-help | COMP on-call |
| Forge | Build runners for Gatekeeper CI | Compute | #comp-forge | COMP on-call |
| Meridian Mesh | Service mesh: mTLS, routing, retries | Networking | #net-mesh | NET on-call |
| EdgeGate | API gateway, ingress, WAF, rate limits | Networking | #net-edgegate | NET on-call |
| Lookout | Alerting and paging | Observability | #obs-lookout | OBS on-call |
| Tracewell | Tracing and log pipeline | Observability | #obs-tracewell | OBS on-call |
| Scaffold | Service templates and CLI | Developer Tooling | #devt-scaffold | DEVT on-call |
| Gatekeeper CI | Build, test, and deploy pipeline | Developer Tooling | #devt-gatekeeper | DEVT on-call |

## Supporting infrastructure

| Component | Owning team |
|---|---|
| Kestrel node images | Compute |
| VPCs, Transit Gateways, internal DNS | Networking |
| Standard dashboards | Observability |
| GitHub Enterprise administration | Developer Tooling |
| Dependency update bot | Developer Tooling |

## Systems people often assume are Platform's (but aren't)

- **Vaultline** (secrets) and **Sentinel** (scanning): AppSec.
- **Keystone** (SSO and IAM): IT & Compliance.
- **Streamline** (Kafka event bus): Data Platform.
- **TechSync Ship**: Product Engineering. Platform uses it heavily but doesn't own it.

## Updating this page

Owning teams update their rows. Technical Writing reviews the whole page each quarter.
