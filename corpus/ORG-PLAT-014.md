---
doc_id: ORG-PLAT-014
title: Platform RFC Process
doc_type: process
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: TPM
status: approved
last_updated: 2024-05-21
supersedes: ""
fact_ids: ""
---

# Platform RFC Process

**Owner:** Platform TPM

An RFC (request for comments) is how Platform proposes significant changes and gets feedback before building them.

## When to write an RFC

- A new Platform system or a major new feature in an existing one.
- A change that affects how many teams work (new pipeline stage, new required config).
- Anything that will take more than about a month of engineering time.

Small changes and bug fixes don't need an RFC.

## Template

1. **Summary**: one paragraph.
2. **Problem**: what's wrong today, with data.
3. **Proposal**: what you'll build.
4. **Alternatives**: what else you considered and why not.
5. **Rollout**: how it reaches dev, staging, and prod, and how teams migrate.
6. **Risks and open questions.**

## Process

1. **Draft** in the Platform Confluence space, status "draft."
2. **Share** in #platform-rfcs and with affected teams. Comment period of at least one week.
3. **Review meeting** with the owning team's tech lead and at least one tech lead from another Platform team.
4. **Decide.** The owning team's engineering manager approves, rejects, or asks for changes.
5. **Record.** Approved RFCs become ADRs, or link to one.

## Status values

Draft, In review, Approved, Rejected, Withdrawn.

## Tips

- Lead with data.
- Name the teams affected and talk to them before posting.
- Keep it short. Two to four pages is usually enough.
