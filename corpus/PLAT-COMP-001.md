---
doc_id: PLAT-COMP-001
title: Compute Team Charter
doc_type: team charter
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: Engineering Manager
status: approved
last_updated: 2025-02-03
supersedes: ""
fact_ids: ""
---

# Compute Team Charter

**Team:** Compute (COMP), Platform Engineering
**Engineering manager:** Marcus Oyelaran
**Tech lead:** Lin Zhao

## Mission

Give every engineering team at TechSync a reliable, boring place to run and build software. When Compute is doing its job well, product teams rarely think about servers, clusters, or build machines.

## What we own

| System | What it is |
|---|---|
| **Kestrel** | TechSync's internal Kubernetes platform, running on Amazon EKS in us-east-1, us-west-2, and eu-west-1 |
| **Forge** | The fleet of build runners that Gatekeeper CI uses to build and test code |

We also own the Kestrel node images, the cluster add-ons (autoscaling, DNS, admission controllers), and the Forge runner images.

## What we don't own

- **Service mesh and ingress.** Meridian Mesh and EdgeGate belong to Networking.
- **Alerting and tracing.** Lookout and Tracewell belong to Observability.
- **Pipelines.** Gatekeeper CI and Scaffold belong to Developer Tooling. We run the machines; they run the pipeline logic.
- **Application code** running on Kestrel. That belongs to the teams who wrote it.

## How to work with us

- **Requests:** the COMP project in Jira. We triage twice a week.
- **Questions:** #comp-help.
- **Urgent production problems:** page the COMP on-call through PagerDuty.

## Goals for 2025

1. Finish moving all Kestrel node autoscaling to Karpenter.
2. Cut median Forge queue time in half.
3. Keep Kestrel within one minor version of the newest EKS release.
4. Publish runbooks for every Kestrel and Forge alert.

## Team rituals

- Weekly planning on Mondays.
- Weekly patch sync on Wednesdays to review node-image updates.
- Monthly operational review covering incidents, alert noise, and capacity.

## Disaster recovery owners

Primary: Kestrel tech lead. Backup: senior SRE on the COMP rotation.
