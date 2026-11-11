doc_id: CO-PROD-012
title: Service Tiering Policy
doc_type: policy
scope_level: company
owner_team: CTO office
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2025-11-04
supersedes:
fact_ids: F-POL-13; F-PROD-012

---

# Service Tiering Policy

**Owner:** CTO office

## 1. Purpose

Not every service matters equally when something goes wrong. Tiering gives us a shared vocabulary for how critical a service is, so that other policies can set expectations by tier instead of naming services one at a time.

## 2. The tiers

| Tier | Definition |
|---|---|
| Tier 0 | Core platform |
| Tier 1 | Customer-facing |
| Tier 2 | Internal |
| Tier 3 | Experimental |

- **Tier 0** covers the platform that other services depend on to run at all.
- **Tier 1** covers services that customers use directly.
- **Tier 2** covers services used only by TechSync employees and internal tooling.
- **Tier 3** covers prototypes and experiments that are not relied on by customers or by other services.

## 3. Reference assignments

Some assignments are fixed here so that every team uses the same answer:

- **Keystone** (SSO and IAM) is **Tier 0**.
- **Kestrel** (the internal Kubernetes platform) is **Tier 0**.
- **Console** (the shared web console) is **Tier 1**.

The full assignment for every system is kept in the service catalog, which teams update through the CTO office.

## 4. How a tier is assigned

1. The owning team proposes a tier using the definitions above.
2. The CTO office reviews the proposal against the definitions.
3. The agreed tier is recorded in the service catalog.

A tier is a property of the service, not of the team that owns it. If a service gains customers or other services come to depend on it, the owning team should ask for a review.

## 5. How other policies use tiers

Policies for code review, on-call, disaster recovery and similar topics refer to tiers. Read those documents for the details; this policy only defines what the tiers mean.

## 6. Changing a tier

Request a change through the CTO office with a short written rationale. Tier changes take effect once the service catalog is updated.

## 7. Review

The CTO office reviews this policy once a year.
