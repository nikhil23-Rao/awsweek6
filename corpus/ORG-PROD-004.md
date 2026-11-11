doc_id: ORG-PROD-004
title: Product Design Review Process
doc_type: process doc
scope_level: org
owner_team: PROD
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2025-10-21
supersedes:
fact_ids: 

---

# Product Design Review Process

## Purpose

A design review is a short, structured conversation that lets other engineers find problems while they are cheap to fix. It is not an approval gate for every change.

## When to hold one

Hold a design review when a change introduces a new service, a new data store, a new external dependency, or a significant change to how a component behaves. If you are unsure, ask your Tech Lead.

## How it runs

1. The author writes a design document using the standard template (context, goals, proposal, alternatives, risks).
2. The author shares it at least two working days before the review.
3. A Staff Engineer acts as reviewer-of-record and invites two or three other engineers with relevant experience.
4. The review lasts 45 minutes. The author presents for ten minutes; the rest is discussion.
5. The reviewer-of-record posts a written summary of decisions and open questions within two working days.

## What reviewers look for

Clear goals, honest alternatives, operability (how will we know it is broken?), and the cost of changing course later.

## Records

Design documents and summaries are stored in the team's Confluence space. Link them from the pull request that implements the design.

## Questions

Contact a Staff Engineer in your team or ask in #prod-design-review.
