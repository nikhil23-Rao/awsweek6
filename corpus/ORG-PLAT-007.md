---
doc_id: ORG-PLAT-007
title: Platform Game Day Playbook
doc_type: runbook
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2026-06-09
supersedes: ""
fact_ids: ""
---

# Platform Game Day Playbook

**Owner:** SRE, Platform Engineering

A game day is a planned exercise where we deliberately break something in a controlled way to check that our systems, alerts, runbooks, and people respond the way we expect.

## Picking a scenario

Good scenarios are realistic and teach something:

- Kill all CoreDNS pods in a staging Kestrel cluster.
- Make Lookout unable to reach PagerDuty.
- Fail one EdgeGate cell in staging.
- Block Forge runners from reaching the dependency cache.

Pick one scenario per game day.

## Roles

| Role | Responsibility |
|---|---|
| Facilitator | Runs the exercise, controls the injected failure, calls stop |
| Responders | The on-call for the affected team, working as they would for real |
| Observers | Take notes on timing, confusion, missing docs |

## Before

1. Write the hypothesis: "If X happens, we expect alert Y within Z minutes and runbook R to resolve it."
2. Agree on a stop condition and a rollback.
3. Run it in staging first. Prod game days need VP approval.
4. Announce the time in #platform-releases and #incident-room.

## During

- The facilitator injects the failure and starts a timer.
- Responders work the problem using real tools and runbooks.
- Observers note every time someone gets stuck.

## After

- 30-minute debrief immediately after.
- Write up results: what matched the hypothesis, what didn't.
- File tickets for gaps in alerts, runbooks, or tooling.

## Cadence

Each Platform team runs at least one game day per quarter.
