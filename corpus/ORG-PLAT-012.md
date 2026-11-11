---
doc_id: ORG-PLAT-012
title: Platform Disaster Recovery Readiness Guide
doc_type: guide
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: SRE
status: unmarked
last_updated: 2024-07-23
supersedes: ""
fact_ids: F-POL-09
---

# Platform Disaster Recovery Readiness Guide

**Audience:** all Platform Engineering teams
**Maintained by:** SRE, Platform Engineering

## Purpose

TechSync's disaster recovery plan assumes we can fail production over from us-east-1 to us-west-2 if us-east-1 becomes unusable. Platform systems have to come back first, because every product service depends on them. This guide tells each Platform team what "ready" means for its systems.

## Recovery targets

For Tier 0 and Tier 1 services:

| Target | Value |
|---|---|
| Recovery point objective (RPO) | **15 minutes** |
| Recovery time objective (RTO) | **8 hours** |

Platform's systems are almost all Tier 0, so these targets apply to nearly everything we own.

## Recovery order

1. Kestrel clusters in us-west-2 (COMP)
2. Meridian Mesh and EdgeGate (NET)
3. Lookout and Tracewell (OBS)
4. Gatekeeper CI and Forge (DEVT, COMP)

Product and Data services start recovery once steps 1 and 2 are complete.

## What each team must have

- **Infrastructure as code.** Everything needed to stand up your system in us-west-2 is in Terraform and has been applied there at least once in the last six months.
- **Data replication.** Any state your system needs is replicated to us-west-2 often enough to meet the RPO.
- **Runbook.** A step-by-step failover runbook that someone outside your team could follow.
- **Owner.** A named primary and backup for DR, listed in the team charter.

## Exercises

Each team runs a tabletop exercise every six months and participates in the annual company failover test. Record results and follow-up tickets in Confluence under *Platform DR*.

## Questions

#platform-sre
