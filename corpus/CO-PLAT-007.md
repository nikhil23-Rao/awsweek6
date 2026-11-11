---
doc_id: CO-PLAT-007
title: Disaster Recovery Policy
doc_type: policy
scope_level: company
owner_team: SRE guild
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2025-01-14
supersedes: CO-PLAT-003
fact_ids: F-POL-09
---

# Disaster Recovery Policy

**Policy owner:** SRE guild
**Effective:** January 14, 2025
**Applies to:** all production services at TechSync

## Recovery targets

| Service tier | Recovery point objective (RPO) | Recovery time objective (RTO) |
|---|---|---|
| Tier 0 (core platform) | **15 minutes** | **4 hours** |
| Tier 1 (customer-facing) | **15 minutes** | **4 hours** |
| Tier 2 (internal) | 24 hours | 72 hours |
| Tier 3 (experimental) | Best effort | Best effort |

## Regions

- **Primary:** us-east-1
- **Disaster recovery:** us-west-2
- **EU customer data:** eu-west-1, recovered within the EU only

## Requirements for Tier 0 and Tier 1 services

1. **Replication.** State is replicated to us-west-2 continuously or at least every 15 minutes.
2. **Infrastructure as code.** All infrastructure can be recreated in us-west-2 from Terraform.
3. **Runbook.** A tested failover runbook exists and was exercised in the last 12 months.
4. **Dependencies.** Each service documents which Tier 0 services it needs to recover first.

## Roles

- **SRE guild** declares a regional disaster, coordinates the failover, and owns this policy.
- **Service-owning teams** execute their runbooks and confirm recovery.
- **CTO** is informed at declaration and approves failback.

## Testing

- An annual company-wide failover exercise, coordinated by the SRE guild.
- Team tabletop exercises at least twice a year.

Results are recorded in Compass as compliance evidence.

## Questions

#sre-guild
