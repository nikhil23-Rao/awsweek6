---
doc_id: PLAT-DEVT-009
title: Gatekeeper CI Working Group Notes (Sep 2026)
doc_type: meeting notes
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: TPM
status: unmarked
last_updated: 2026-09-16
supersedes: ""
fact_ids: F-PLAT-005
---

# Gatekeeper CI Working Group Notes, September 2026

**Date:** September 16, 2026
**Attendees:** Gatekeeper CI tech lead, two DEVT staff engineers, an SRE from the SRE guild, TPM (notes)
**Absent:** DEVT engineering manager

## Agenda

1. Deploy duration complaints from Product teams
2. Canary configuration
3. Forge runner queue times
4. AOB

## 1. Deploy duration

- Product Engineering teams say end-to-end prod deploys take too long, especially for small config-only changes. Median deploy is about 38 minutes from merge.
- Biggest single block of time is the canary stage.

## 2. Canary configuration

- Discussed moving the canary to **10% of traffic for 5 minutes**. Larger slice gets statistically meaningful signal faster, so we could shorten the window.
- SRE rep's concern: 5 minutes may miss slow-burn problems like memory growth. Suggested keeping the longer window for Tier 0 services.
- Consensus in the room was that 10% / 5 min is the direction we want for most services.
- Nobody opposed; open question on whether Tier 0 gets an opt-out.

**Action item:** Gatekeeper CI tech lead to write an RFC for the canary change, including data from the last two quarters of canary failures.

## 3. Forge runner queue times

- Queue times spiked on Monday mornings. Compute is raising the warm buffer on the large-build pools for Monday mornings.
- No action for DEVT.

## 4. AOB

- Reminder that the Q4 planning doc is due next week.

## Action items

| Owner | Item |
|---|---|
| Gatekeeper CI tech lead | Canary RFC |
| DEVT staff engineer | Pull canary failure data for the RFC |
| TPM | Schedule follow-up in two weeks |
