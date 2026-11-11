---
doc_id: ORG-PLAT-010
title: Platform Team Interface Contracts
doc_type: design doc
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-11-18
supersedes: ""
fact_ids: ""
---

# Platform Team Interface Contracts

**Author:** Staff Engineer, Platform Engineering
**Status:** Approved

Platform's four teams own systems that sit right next to each other. This doc writes down where one team's responsibility ends and another's begins, so problems don't fall into gaps.

## Compute ↔ Networking

- **Compute owns** EKS clusters, node images, the VPC CNI plugin, and node-level networking.
- **Networking owns** Meridian Mesh (control plane and sidecars), EdgeGate, VPCs, and DNS outside clusters.
- **Shared:** CoreDNS inside clusters is run by Compute; Networking owns the upstream resolvers it forwards to.
- **Upgrade coordination:** Compute schedules cluster upgrades; Networking confirms mesh compatibility before each one.

## Compute ↔ Developer Tooling

- **Compute owns** Forge runners: images, pools, capacity, and runner health.
- **Developer Tooling owns** Gatekeeper CI scheduling and pipeline logic.
- If jobs queue because no runners are available, that's Compute. If jobs aren't dispatched to available runners, that's Developer Tooling.

## Observability ↔ everyone

- **Observability owns** Lookout and Tracewell, the SDKs, and dashboard standards.
- **Each team owns** its own alert rules, dashboards, and instrumentation.

## Networking ↔ Observability

- Mesh and EdgeGate metrics are exported by Networking's components; Observability owns their storage and alerting infrastructure.

## When ownership is unclear

Raise it with the Platform staff engineers. Update this doc once it's decided.
