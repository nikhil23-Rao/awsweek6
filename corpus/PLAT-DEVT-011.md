---
doc_id: PLAT-DEVT-011
title: "Postmortem: Gatekeeper CI Queue Stall (Sev2, Jan 2026)"
doc_type: postmortem
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2026-01-15
supersedes: ""
fact_ids: ""
---

# Postmortem: Gatekeeper CI Queue Stall (Sev2, Jan 2026)

**Severity:** Sev2
**Duration:** 1 hour 35 minutes
**Owning team:** Developer Tooling
**Author:** SRE, DEVT rotation

## Summary

On January 8, 2026, Gatekeeper CI stopped dispatching jobs to Forge. Pipelines across the company queued without starting. No deploys reached any environment during the incident, including a fix Payments was trying to ship for an unrelated Ledger issue.

## Impact

Internal only. About 600 pipelines were delayed. Payments' Ledger fix was delayed by 70 minutes.

## Timeline (PT)

- 09:58: A Gatekeeper CI scheduler deploy rolls out.
- 10:05: Queue depth alert fires.
- 10:12: DEVT on-call confirms jobs aren't being dispatched; Sev2 declared.
- 10:40: The new scheduler version is found to deadlock when two jobs share a cache namespace and start in the same second.
- 10:52: Rollback attempted through Gatekeeper CI, which can't run because the scheduler is stalled.
- 11:20: Scheduler rolled back manually with the break-glass procedure.
- 11:33: Queue drained; incident resolved.

## Contributing factors

1. The deadlock path wasn't covered by tests.
2. Gatekeeper CI deploys itself, so a broken scheduler blocks its own rollback.
3. The break-glass procedure was documented but nobody on the rotation had practiced it.

## What went well

- Fast detection.
- Payments communicated their urgent need clearly in the incident channel.

## Action items

| Item | Owner | Ticket |
|---|---|---|
| Fix the cache-namespace lock ordering | DEVT | DEVT-1871 |
| Add concurrency tests for the scheduler | DEVT | DEVT-1872 |
| Independent deploy path for the scheduler | DEVT | DEVT-1873 |
| Quarterly break-glass drill for the DEVT rotation | DEVT | DEVT-1874 |
