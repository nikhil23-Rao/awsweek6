---
doc_id: PLAT-NET-010
title: Networking Weekly Sync Notes (Aug 2026)
doc_type: meeting notes
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: TPM
status: unmarked
last_updated: 2026-08-12
supersedes: ""
fact_ids: ""
---

# Networking Weekly Sync Notes, August 2026

**Date:** August 12, 2026
**Attendees:** NET engineering manager, NET tech lead, five NET engineers, TPM (notes)

## 1. IPv6

- Tech lead shared a draft plan for dual-stack EdgeGate listeners.
- Biggest unknown is whether all customer-facing load balancers in eu-west-1 support it in our current setup.
- **Decision:** start with the staging EdgeGate in us-east-1. Revisit in October.

## 2. WAF backlog

- 14 open WAF rule requests, 6 from AppSec.
- Two are false-positive reports from Enterprise customers on Ledger API calls. Prioritize those.
- Proposal to rotate a "WAF duty" engineer weekly. Generally supported.

## 3. Mesh control-plane upgrade

- Staging upgrade done last week, no issues.
- Prod upgrade to be coordinated with Compute's next cluster maintenance.

## 4. Hiring

- One senior engineer offer accepted, starts in September.
- Still interviewing for the second opening.

## 5. AOB

- Reminder: Q4 planning inputs due August 29.
- Someone left a test route on the staging EdgeGate pointing to a deleted service; cleaned up.

## Action items

| Owner | Item |
|---|---|
| NET tech lead | IPv6 staging plan with milestones |
| NET engineer | Fix the two Enterprise WAF false positives |
| NET engineering manager | Set up WAF duty rotation |
| TPM | Collect Q4 planning inputs |
