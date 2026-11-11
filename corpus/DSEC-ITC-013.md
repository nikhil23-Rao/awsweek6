doc_id: DSEC-ITC-013
title: "ADR: Keystone SCIM Provisioning"
doc_type: ADR
scope_level: team
owner_team: ITC
owner_org: DSEC
author_role: Tech Lead
status: approved
last_updated: 2025-09-16
supersedes:
fact_ids:

# ADR: Keystone SCIM Provisioning

**Status:** Accepted | **Date:** September 2025

## Context

Applications that integrate with Keystone need user and group records. Today each app either reads claims at sign-in only, or relies on a custom sync written by its owning team. The custom syncs differ in quality, and some leave accounts behind when people leave the company.

## Decision

Keystone will offer **SCIM 2.0 provisioning** as the standard way for applications to receive user and group changes. New integrations should use SCIM where the application supports it. Existing custom syncs will be migrated over time.

## Consequences

**Positive**
- Joiners, movers, and leavers propagate to applications through a single, tested mechanism.
- Less custom code for application teams to maintain.
- Easier to show an auditor how deprovisioning works.

**Negative**
- Applications without SCIM support still need a connector or a custom sync.
- ITC must operate a SCIM endpoint and monitor delivery failures.
- Migration of existing integrations takes effort from other teams.

## Alternatives considered

1. **Keep custom syncs.** Flexible but inconsistent.
2. **Event-based provisioning through Streamline.** Fits our stack, but is non-standard for third-party applications.
3. **Buy a provisioning product.** Adds cost and another vendor.

## Follow-up

- Publish the SCIM endpoint details and an onboarding checklist.
- Migrate Console and the largest internal applications first.
- Report adoption in the ITC weekly sync.
