---
doc_id: ORG-PLAT-002
title: Platform Documentation Standards
doc_type: standard
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: Technical Writer
status: approved
last_updated: 2024-10-29
supersedes: ""
fact_ids: ""
---

# Platform Documentation Standards

**Scope:** documentation written by Platform Engineering teams
**Maintained by:** Technical Writing, with the Platform staff engineers

## Why

Platform docs are read by every engineer in the company, often during an incident. They should be easy to find, easy to scan, and clearly owned.

## Document types

| Type | Use it for | Example |
|---|---|---|
| Runbook | Step-by-step operational procedures | Cluster upgrade |
| Reference | Facts that people look up: settings, flags, schemas | Mesh configuration reference |
| How-to guide | Accomplishing one task | Instrumenting a service |
| Standard / policy | Rules teams must follow | Release standard |
| ADR | A decision and why it was made | Adopt Karpenter |
| Postmortem | What happened in an incident and what we're changing | |
| Meeting notes | Record of a discussion | Weekly sync |

Pick one type per doc. A runbook that also tries to be a reference is hard to use in a hurry.

## Required header

Every doc in Confluence starts with: owning team, document type, status (draft, approved, deprecated), and last-updated date.

## Writing style

- Lead with what the reader needs to do or know.
- Use tables for settings and comparisons.
- Put commands in code blocks that can be copied as-is.
- Use roles ("the COMP on-call"), not individual names, for responsibilities that rotate.

## Status

- **Draft**: not yet reviewed. Readers shouldn't rely on it.
- **Approved**: reviewed by the owning team's tech lead or manager.
- **Deprecated**: kept for history; the banner at the top points to the replacement.

## Review cadence

Owning teams review runbooks and references every 12 months. Technical Writing sends reminders.

## Where docs live

Confluence, under the Platform space, one section per team. Service-specific docs can live in the service's repo `docs/` folder, linked from Confluence.
