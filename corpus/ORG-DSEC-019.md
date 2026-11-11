doc_id: ORG-DSEC-019
title: DSEC Internal Request Intake
doc_type: process
scope_level: org
owner_team: none (DSEC org-wide)
owner_org: DSEC
author_role: Engineering Manager
status: approved
last_updated: 2026-06-09
supersedes:
fact_ids:

# DSEC Internal Request Intake

How to ask a DSEC team for something, and what happens next.

## One front door

All requests from outside DSEC, and most from inside, go through the DSEC intake queue in Jira. Do not send requests by direct message; they are easy to lose, and a ticket gives you a place to track progress.

## What to put in a request

1. A one-line summary.
2. What you need, and why.
3. Who is affected and by when it matters.
4. Links to related tickets, documents, or incidents.
5. Which system it concerns, if you know.

## Request types

| Type | Examples |
|---|---|
| Access | Group membership, vault paths, GPU quota |
| Advice | Design consultation, security questions |
| Change | A feature in a DSEC system |
| Docs | A missing or incorrect document |
| Incident follow-up | A fix coming out of a postmortem |

Urgent operational problems are not requests. Page the owning team through Lookout or use the team's on-call channel.

## Triage

An intake rota of engineering managers reviews the queue each business day. They:

- Confirm the request is clear, or ask for detail.
- Route it to the owning team.
- Set a priority from P1 to P4.

The owning team then schedules the work in its own planning process.

## Priorities

| Priority | Meaning |
|---|---|
| P1 | Blocks a launch or many people |
| P2 | Blocks one team |
| P3 | Useful, can wait |
| P4 | Nice to have |

## Tracking and closing

The assignee comments when work starts and when it finishes. Requesters should confirm that the result works before the ticket is closed.

## If a request is stuck

Comment on the ticket first. If there is no response, raise it in the DSEC channel and mention the owning team's engineering manager.
