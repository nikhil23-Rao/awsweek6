doc_id: DSEC-DATA-009
title: Data Platform Team Operating Cadence
doc_type: guide
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: Engineering Manager
status: approved
last_updated: 2026-01-14
supersedes:
fact_ids:

# Data Platform Team Operating Cadence

How the Data Platform team spends its week. If something here is not working for you, tell me; we change it.

## Weekly rhythm

| Day | Meeting | Purpose |
|---|---|---|
| Monday | Planning (30 min) | Pick up the week's priorities from the board |
| Tuesday to Thursday | Standup (10 min, async in Slack) | Blockers only |
| Wednesday | Design review (45 min) | Look at one design or ADR |
| Thursday | Demo (30 min) | Show what shipped |
| Friday | No meetings | Focus time |

## Tracking work

All work lives on the DATA board in Jira. Each ticket has an owner, a size (S, M, L), and a link to the OKR it supports. Unplanned work gets a ticket too, so we can see how much interruption the team absorbs.

## Intake

Requests from other teams come in through the DSEC intake queue and are triaged on Mondays. Anything urgent can be raised in the DATA channel and I will make a call the same day.

## Decisions

Small decisions are made by the owner. Cross-team decisions go through a design review and are written up as ADRs. The tech lead breaks ties.

## Quality bars

- Every production job and consumer has a runbook with an owner.
- Dashboards exist for each service before launch.
- Changes to shared interfaces are announced in the DSEC channel.

## Retrospectives

We hold a retrospective each month and keep the actions in the retro doc. We try to finish at least two actions before the next retro.

## One-on-ones

I meet each engineer every other week for 30 minutes. The agenda belongs to you.
