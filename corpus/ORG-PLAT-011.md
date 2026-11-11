---
doc_id: ORG-PLAT-011
title: Platform Glossary
doc_type: reference
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: Technical Writer
status: approved
last_updated: 2026-05-12
supersedes: ""
fact_ids: ""
---

# Platform Glossary

*Technical Writing, Platform Engineering*

**ADR** — Architecture decision record. A short document recording a decision and its reasons.

**Canary** — A deploy stage where a new version receives part of production traffic before full rollout.

**Cell** — An independent group of EdgeGate pods serving a share of traffic.

**CODEOWNERS** — GitHub file listing which teams own which paths.

**EdgeGate** — TechSync's API gateway and ingress. Owned by Networking.

**Forge** — The fleet of build runners. Owned by Compute.

**Gatekeeper CI** — The build, test, and deploy pipeline. Owned by Developer Tooling.

**Golden signals** — Request rate, errors, latency, and saturation.

**Karpenter** — The node autoscaler used by Kestrel.

**Kestrel** — TechSync's internal Kubernetes platform on EKS. Owned by Compute.

**Lookout** — Alerting and paging. Owned by Observability.

**Meridian Mesh** — The service mesh on Kestrel. Owned by Networking.

**Namespace** — The unit of isolation for a team or system on Kestrel.

**PDB** — PodDisruptionBudget. Limits how many pods can be evicted at once.

**Runbook** — A step-by-step operational procedure.

**Scaffold** — Service templates and the `scaffold` CLI. Owned by Developer Tooling.

**Sidecar** — A helper container running next to your application container; the mesh proxy is one.

**Silence** — A temporary mute for matching Lookout alerts.

**SLI / SLO** — Service level indicator and objective.

**Soak** — Time a release spends in an environment before being promoted.

**Tracewell** — The tracing and log pipeline. Owned by Observability.

**Workload identity** — The identity Kestrel gives each service account, used to authenticate to other systems.
