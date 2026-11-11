---
doc_id: PLAT-COMP-003
title: Kestrel Cluster Upgrade Runbook
doc_type: runbook
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2026-05-04
supersedes: ""
fact_ids: ""
---

# Kestrel Cluster Upgrade Runbook

**Owner:** Compute (COMP)
**Who runs this:** the COMP engineer assigned to the upgrade, with a second COMP engineer on watch

## Overview

We upgrade Kestrel clusters one EKS minor version at a time, always in the order dev, staging, prod. Each prod region is done separately. A full cycle usually takes three weeks.

## Before you start

- [ ] Read the EKS release notes for the target version and list deprecated Kubernetes APIs.
- [ ] Run `kestrel-apicheck` against every cluster to find workloads still using removed APIs. Open tickets for owning teams at least two weeks ahead.
- [ ] Confirm add-on versions (CoreDNS, VPC CNI, Karpenter, Meridian Mesh control plane) are compatible. Coordinate with NET for the mesh.
- [ ] Schedule the upgrade Tuesday to Thursday, during business hours.
- [ ] Post the plan in #platform-releases.

## Procedure (per cluster)

1. **Snapshot.** Take an etcd backup through the EKS console and record the cluster's current version.
2. **Control plane.** Run the Terraform change that bumps `cluster_version`. Wait for the EKS control-plane upgrade to finish (typically 20 to 40 minutes).
3. **Add-ons.** Apply the add-on version bumps.
4. **Node pools.** Update the Karpenter node class to the new node image. Karpenter replaces nodes gradually, respecting PodDisruptionBudgets.
5. **Watch.** Monitor the Kestrel control-plane dashboard and the cluster-wide error rate for one hour.
6. **Record.** Update the cluster version table on Confluence.

## Rollback

EKS control planes can't be downgraded. If something goes wrong after step 2, roll back add-ons and node images, and work the problem forward. This is why dev and staging go first.

## Common problems

- **Pods stuck terminating** during node replacement: usually a PDB that allows zero disruptions. Contact the owning team.
- **Webhook timeouts** after the control-plane upgrade: restart the admission controller pods.
