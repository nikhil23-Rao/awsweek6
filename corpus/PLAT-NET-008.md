---
doc_id: PLAT-NET-008
title: "ADR: Locality-Aware Load Balancing in Meridian Mesh"
doc_type: ADR
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-03-26
supersedes: ""
fact_ids: ""
---

# ADR: Locality-Aware Load Balancing in Meridian Mesh

**Status:** Accepted
**Date:** March 2025
**Deciders:** Networking tech lead, Networking engineering manager, Networking staff engineers
**Consulted:** Compute, Observability, Payments

## Context

Meridian Mesh distributes requests evenly across all healthy upstream pods regardless of availability zone. In us-east-1, roughly two-thirds of service-to-service calls cross AZ boundaries. That adds about 1 to 2 ms per hop and is a significant part of our AWS data transfer bill.

## Decision

Enable locality-aware load balancing in the mesh by default:

- Requests go to upstream pods in the caller's AZ when that AZ has enough healthy endpoints.
- If healthy endpoints in the local AZ drop below 70% of normal, traffic spills over to other AZs proportionally.
- Services can opt out per route.

## Consequences

**Positive**
- Lower p50 latency for chatty call chains.
- Large reduction in cross-AZ data transfer cost.

**Negative**
- Uneven load if a service's pods are unevenly spread across AZs. Teams must use topology spread constraints (Scaffold templates now include them).
- Harder to reason about traffic during partial AZ failures.

## Rollout

Dev in April 2025, staging in May, prod clusters one at a time through June. Observability added per-AZ request panels to the standard dashboards.

## Alternatives considered

- **Do nothing.** Rejected because of cost.
- **Topology-aware routing in Kubernetes Services.** Doesn't apply to mesh-routed traffic.
