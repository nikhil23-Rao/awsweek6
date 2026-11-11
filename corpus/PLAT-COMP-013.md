---
doc_id: PLAT-COMP-013
title: "Kestrel GPU Node Pools: Architecture Notes"
doc_type: design doc
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-06-30
supersedes: ""
fact_ids: ""
---

# Kestrel GPU Node Pools: Architecture Notes

Author: Staff Engineer, Compute. Status: approved.

## Context

ML Infrastructure runs training and online inference for Foundry on Kestrel. Until early 2025 these workloads shared generic node pools with a handful of manually managed GPU nodes. As Foundry usage grew, we needed dedicated, autoscaled GPU capacity with clear isolation from general workloads.

## Design

### Separate pools by workload shape

| Pool | Instances | Used for |
|---|---|---|
| `gpu-train` | p5 | Distributed training jobs |
| `gpu-infer` | g6 | Online inference behind FeatureHub-backed services |
| `gpu-batch` | g6, spot | Batch scoring, evaluation jobs |

### Isolation

- GPU nodes carry a `nvidia.com/gpu` taint. Only pods that tolerate it and request GPUs land there.
- Each pool is restricted by node affinity to Foundry namespaces (`mli-*`).

### Autoscaling

Karpenter provisions GPU nodes on demand. `gpu-train` scales to zero when idle because p5 capacity is expensive; `gpu-infer` keeps a minimum of two nodes per AZ so inference doesn't cold-start.

### Drivers and runtime

The NVIDIA driver and container toolkit are baked into a dedicated GPU node image, rebuilt alongside the standard Kestrel node images.

## Capacity reservations

For `gpu-train`, MLI and Compute jointly maintain AWS capacity reservations in us-east-1. Reservations are reviewed quarterly against Foundry's training calendar.

## Open questions

- Should `gpu-batch` move to eu-west-1 for models trained on EU data? Pending a decision from MLI.
- Multi-instance GPU partitioning for small inference models is being evaluated.

## Owners

Compute owns the pools and images. ML Infrastructure owns Foundry and decides how capacity is split among its workloads.
