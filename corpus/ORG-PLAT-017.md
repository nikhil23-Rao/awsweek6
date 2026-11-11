---
doc_id: ORG-PLAT-017
title: EKS Version Support Policy
doc_type: policy
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-12-16
supersedes: ""
fact_ids: ""
---

# EKS Version Support Policy

**Owner:** Compute, for all Kestrel clusters
**Scope:** dev, staging, and prod clusters in every region

## Policy

1. Kestrel prod clusters run an EKS version that is within **one minor version** of the newest version AWS offers in standard support.
2. Kestrel never runs a version that has left AWS standard support. Extended support costs extra and delays upgrades.
3. All prod regions run the same minor version, except during an upgrade cycle.
4. dev runs the target version at least two weeks before prod.

## Upgrade cadence

AWS releases a new minor version roughly three times a year. Compute plans one upgrade cycle per release.

## Team responsibilities

Teams running on Kestrel must:

- Fix use of deprecated Kubernetes APIs before the announced upgrade date. Compute opens tickets at least two weeks ahead.
- Keep PodDisruptionBudgets correct so node replacement works.

## If a team can't migrate in time

Raise it with the Compute engineering manager. We may hold a single cluster back briefly, but never past the end of AWS standard support.

## Version table

The current version for each cluster is listed in Confluence under *Kestrel cluster versions* and updated at the end of each upgrade.
