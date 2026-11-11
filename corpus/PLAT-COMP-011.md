---
doc_id: PLAT-COMP-011
title: Forge Build Runner Fleet Overview
doc_type: reference
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: Tech Lead
status: approved
last_updated: 2025-11-12
supersedes: ""
fact_ids: ""
---

# Forge Build Runner Fleet Overview

Compute (COMP), Forge tech lead

Forge is the pool of machines that runs build and test jobs for Gatekeeper CI. Developer Tooling owns the pipeline logic; Compute owns the runners: their images, capacity, and health.

## Runner pools

| Pool | Instance family | Architecture | Typical jobs |
|---|---|---|---|
| `forge-standard` | c7i | x86 | Most Go, Python, and TypeScript builds |
| `forge-large` | c7i.8xlarge | x86 | Monorepo builds, large integration suites |
| `forge-large-arm` | c8g | ARM (Graviton) | Multi-arch images |
| `forge-macos` | mac2 | ARM | TechSync Mobile iOS builds |
| `forge-gpu` | g6 | x86 + GPU | Foundry model tests |

All pools run in us-east-1. A smaller standby fleet in us-west-2 can be scaled up if needed.

## Scheduling

Gatekeeper CI submits each job with a pool label. Forge places it on an idle runner or queues it. Runners are ephemeral: one job per runner, then the runner is destroyed. This prevents state from leaking between jobs.

## Scaling

Pools autoscale on queue depth. During business hours in the US we keep a warm buffer of idle runners in `forge-standard` to keep queue times low. Overnight, pools shrink to a small floor.

## Caching

- **Dependency cache:** shared S3-backed cache for Go modules, pip, npm, and Gradle.
- **Docker layer cache:** per-pool, on local NVMe of each runner, prewarmed from the latest base layers.

See the *Forge Build Cache Troubleshooting FAQ* for cache problems.

## Health metrics we watch

- Median and p95 queue time per pool
- Runner boot time
- Job failure rate attributable to infrastructure (not test failures)

## Contacting us

#comp-forge for questions; page COMP on-call if all builds are failing.
