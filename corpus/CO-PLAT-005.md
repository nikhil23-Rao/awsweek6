---
doc_id: CO-PLAT-005
title: Incident Communication Standard
doc_type: standard
scope_level: company
owner_team: SRE guild
owner_org: PLAT
author_role: TPM
status: approved
last_updated: 2026-04-02
supersedes: ""
fact_ids: ""
---

# Incident Communication Standard

**Owner:** SRE guild, with Customer Support and Technical Program Management
**Applies to:** all Sev1 and Sev2 incidents, and any incident with customer impact

## Internal updates

Post updates in #incident-room:

| Severity | Update interval |
|---|---|
| Sev1 | Every 30 minutes, or sooner when something changes |
| Sev2 | Every 60 minutes |
| Sev3 / Sev4 | At start and resolution |

Each update follows the format:

> **Status:** investigating / identified / mitigating / monitoring / resolved
> **Impact:** who is affected and how
> **Next update:** time

## Customer-facing updates

For incidents affecting customers, the communications lead posts to the status page:

1. **First post** within 15 minutes of declaring a customer-impacting Sev1 or Sev2. It's fine to say "we're investigating."
2. **Updates** at the same interval as internal updates.
3. **Resolution post** when impact ends.

Name the affected products (Ship, Ledger, Insight, Console, Mobile) and regions. Don't speculate about causes in public posts.

## Enterprise customers

Customer Support notifies Enterprise account contacts directly for incidents affecting them, using the template in the Support handbook.

## Leadership

For Sev1 incidents, the IC or communications lead sends a brief summary to the CTO within 30 minutes of declaration, then at each major change.

## After the incident

A customer-facing incident summary is published for Sev1 incidents within one week, reviewed by the CTO office and Support.

## Templates

Status page and Enterprise email templates live in Confluence under *Incident Communication*.
