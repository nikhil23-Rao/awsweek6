---
doc_id: CO-PLAT-009
title: Disaster Recovery Game Day Program
doc_type: standard
scope_level: company
owner_team: SRE guild
owner_org: PLAT
author_role: TPM
status: approved
last_updated: 2025-05-20
supersedes: ""
fact_ids: ""
---

# Disaster Recovery Game Day Program

**Owner:** SRE guild, coordinated by Technical Program Management
**Applies to:** all teams owning Tier 0 and Tier 1 services

## Purpose

A disaster recovery plan that hasn't been tested isn't a plan. This program sets how TechSync exercises its regional recovery.

## Exercise types

| Type | Frequency | Scope |
|---|---|---|
| Tabletop | Twice a year per team | Walk through the team's failover runbook as a discussion |
| Component failover | Once a year per team | Fail one service over to us-west-2 in a controlled window |
| Company failover | Once a year | Shift production traffic for all Tier 0 and Tier 1 services to us-west-2 |

## Company failover exercise

- Scheduled by the SRE guild at least six weeks in advance.
- Announced to customers through the status page one week ahead.
- Runs during a low-traffic window, never during a freeze or holiday period.
- Uses the real failover runbooks, including the cross-region traffic shift.
- Has a go/no-go check with the CTO before the shift begins.

## What we measure

- Time taken for each step of the recovery order.
- Data replication lag at the moment of the shift.
- Every runbook step that was unclear or wrong.

## After each exercise

1. Debrief within one week.
2. Every gap becomes a Jira ticket with an owner.
3. Results are stored as compliance evidence in Compass.

## Readiness checklist for teams

- Failover runbook reviewed in the last six months.
- Terraform for us-west-2 applied successfully in the last six months.
- Named primary and backup DR owners.
