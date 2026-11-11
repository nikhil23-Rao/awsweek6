---
doc_id: ORG-PLAT-008
title: Platform Intake and Request Process
doc_type: process
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: TPM
status: approved
last_updated: 2026-02-02
supersedes: ""
fact_ids: ""
---

# Platform Intake and Request Process

**Owner:** Platform TPM

How teams outside Platform Engineering ask us for things.

## Self-service first

Many things don't need a request:

- New service: `scaffold new`
- Pipeline changes: edit `gatekeeper.yaml`
- Alert rules: edit `lookout/rules.yaml`
- New EdgeGate route: follow the route onboarding guide

Check the Platform Service Catalog and the team's docs before filing.

## Where to file

| You need | File in |
|---|---|
| Kestrel or Forge work | COMP Jira |
| Mesh, EdgeGate, network connectivity | NET Jira |
| Lookout or Tracewell work | OBS Jira |
| Scaffold, Gatekeeper CI, GitHub | DEVT Jira |
| Not sure, or spans teams | PLATFORM Jira (TPM triages) |

## What to include

- What you're trying to accomplish (not just the change you want)
- When you need it and why
- Who to contact

## Triage

Each team triages its queue at least twice a week. Requests get a response within 3 business days: accepted with a target date, redirected, or declined with a reason.

## Larger requests

Anything bigger than about two engineer-weeks goes into quarterly planning. Bring it to the Platform TPM before the planning deadline.

## Urgent issues

Production problems aren't requests. Page the on-call.

## Escalation

If a request is stuck, raise it with the owning team's engineering manager, then the Platform TPM.
