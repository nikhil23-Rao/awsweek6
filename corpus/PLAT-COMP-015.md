---
doc_id: PLAT-COMP-015
title: "ADR: Adopt Karpenter for Kestrel Node Autoscaling"
doc_type: ADR
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2024-11-19
supersedes: ""
fact_ids: ""
---

# ADR: Adopt Karpenter for Kestrel Node Autoscaling

**Status:** Accepted
**Date:** November 2024
**Deciders:** Compute engineering manager, Compute tech lead, two Compute staff engineers
**Consulted:** ML Infrastructure, Networking

## Context

Kestrel uses the Kubernetes Cluster Autoscaler with fixed managed node groups: one per instance type per AZ, about 60 node groups across our clusters. Problems we've hit:

- Scale-up is slow (often 4 to 6 minutes) because node groups scale independently.
- Bin-packing is poor. We pay for a lot of idle capacity.
- Adding a new instance type means new node groups and Terraform changes.
- GPU and spot capacity are awkward to manage.

## Decision

Replace Cluster Autoscaler with **Karpenter** on all Kestrel clusters. Define capacity with a small number of NodePools (general, memory-heavy, GPU, spot) instead of per-instance node groups.

## Consequences

**Positive**
- Faster scale-up, usually under 90 seconds.
- Karpenter chooses from many instance types, improving bin-packing and spot availability.
- Consolidation removes underused nodes automatically.

**Negative**
- Consolidation means more frequent voluntary pod evictions. Teams need correct PodDisruptionBudgets.
- A new component to operate and upgrade.

## Rollout

1. dev clusters, December 2024
2. staging, January 2025
3. prod, one region at a time, Q1 2025

## Alternatives considered

- **Tuning Cluster Autoscaler.** Helps scale-up speed a little, doesn't fix bin-packing.
- **Fargate.** Doesn't support our sidecar and GPU needs.
