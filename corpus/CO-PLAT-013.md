---
doc_id: CO-PLAT-013
title: On-Call Policy (v3)
doc_type: policy
scope_level: company
owner_team: SRE guild
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2025-08-12
supersedes: ""
fact_ids: F-POL-03
---

# On-Call Policy (v3)

**Policy owner:** SRE guild
**Effective:** August 12, 2025
**Applies to:** every engineer on an on-call rotation at TechSync

## Rotations

- Rotations are **1 week** long, handing off Monday at 10 AM local time of the primary.
- No engineer is primary on-call more than **1 week in every 4 weeks**. Teams that can't staff this should pair with another team or raise it with their engineering manager.
- Each rotation has a primary and a secondary.

## Acknowledgment

- **Sev1 pages on Tier 0 and Tier 1 services must be acknowledged within 5 minutes.**
- If the primary doesn't acknowledge in time, PagerDuty escalates to the secondary, then to the team's engineering manager.
- Lower-severity pages and pages on Tier 2 and Tier 3 services should be acknowledged within business-appropriate time and handled during working hours where possible.

## Expectations while on call

- Keep your laptop and a working network connection within reach.
- Join #incident-room for any Sev1 or Sev2.
- Hand off clearly at the end of your week: open incidents, silenced alerts, anything unusual.

## Compensation and recovery

On-call engineers receive the on-call stipend set by People Operations. After a night with a Sev1 page, take the next morning off.

## What changed in version 3

Rotations are now one week instead of two, and Sev1 acknowledgment is faster than in version 2. Shorter rotations reduce fatigue; faster acknowledgment reflects our customer commitments.

## Questions

#sre-guild
