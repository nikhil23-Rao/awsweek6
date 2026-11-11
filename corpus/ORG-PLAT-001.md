---
doc_id: ORG-PLAT-001
title: Platform Incident Review Standard
doc_type: standard
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: Engineering Manager
status: approved
last_updated: 2026-03-12
supersedes: ""
fact_ids: F-POL-04
---

# Platform Incident Review Standard

**Applies to:** all incidents owned by Platform Engineering teams (Compute, Networking, Observability, Developer Tooling)
**Maintained by:** Platform Engineering managers

## Purpose

Platform incidents tend to hit many teams at once, and the lessons are often shared across our four teams. This standard sets out how Platform runs incident reviews so they are consistent and the follow-ups actually get done.

## Postmortem deadlines

| Severity | Postmortem due |
|---|---|
| Sev1 | Within **5 business days** of resolution |
| Sev2 | Within **10 business days** of resolution |
| Sev3 | Optional; write one if there's a lesson worth sharing |
| Sev4 | Not required |

Sev2 incidents on Platform systems often involve several teams and longer root-cause investigations (cross-region networking, cluster behavior under load), so we allow more time to get the analysis right.

## Review meeting

- Held weekly, Thursdays, in the Platform incident review slot.
- The postmortem author presents; the owning team's engineering manager attends.
- Reviews focus on contributing factors and system changes, not on individual blame.

## Action items

- Every action item gets a Jira ticket, an owner, and a due date.
- P0 action items (those that would have prevented or significantly shortened the incident) are due within 30 days.
- The Platform TPM reviews open action items monthly and raises overdue ones with the owning manager.

## Template

Use the company postmortem template on Confluence.

## Sharing

Completed Platform postmortems are linked in #platform-incidents and summarized in the monthly Platform newsletter.
