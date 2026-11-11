---
doc_id: CO-PLAT-003
title: Disaster Recovery Plan (2023)
doc_type: policy
scope_level: company
owner_team: SRE guild
owner_org: PLAT
author_role: SRE
status: deprecated
last_updated: 2025-01-14
supersedes: ""
fact_ids: F-POL-09
---

# Disaster Recovery Plan (2023)

> **Deprecated.** This plan was deprecated on January 14, 2025, and is superseded by the current *Disaster Recovery Policy*, which tightens the Tier 0 and Tier 1 RTO. Kept for historical reference.

**Owner:** SRE guild
**Originally approved:** 2023

## Scope

Covers recovery of TechSync production services in the event that the primary region (us-east-1) is unavailable for an extended period.

## Recovery targets

| Service tier | RPO | RTO |
|---|---|---|
| Tier 0 and Tier 1 | 15 minutes | 8 hours |
| Tier 2 | 24 hours | 72 hours |
| Tier 3 | Best effort | Best effort |

## Failover region

Production fails over to us-west-2. EU customer data remains in eu-west-1, which has its own regional recovery plan.

## Responsibilities

- SRE guild: coordinates the failover and owns this plan.
- Each service-owning team: maintains its own failover runbook and data replication.

## Declaring a disaster

The SRE guild on-call lead declares a regional disaster after confirming with AWS that us-east-1 recovery isn't expected within the RTO window. The CTO is informed at declaration.

## Recovery order

1. Core platform (Kestrel, Meridian Mesh, EdgeGate)
2. Identity and secrets (Keystone, Vaultline)
3. Customer-facing products (Ship, Ledger, Insight, Console)
4. Internal tools

## Testing

An annual company-wide failover test, plus team-level tabletop exercises.
