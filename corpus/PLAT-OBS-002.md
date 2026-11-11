---
doc_id: PLAT-OBS-002
title: Lookout On-Call Standard
doc_type: standard
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: Engineering Manager
status: approved
last_updated: 2025-11-04
supersedes: ""
fact_ids: F-PLAT-007
---

# Lookout On-Call Standard

**Team:** Observability (OBS)
**Owner:** Ingrid Solheim, Engineering Manager, Observability
**Applies to:** the OBS on-call rotation

## Why OBS has its own standard

Lookout is the system that pages everyone else. If Lookout is degraded, other teams' alerts may be delayed or lost, and they won't know it. That makes a Lookout outage uniquely dangerous: an incident can be happening anywhere in the company with nobody being paged. We hold ourselves to a tighter response than a typical service.

This standard applies in addition to the company on-call policy. Everything in the company policy still applies to the OBS rotation; this page adds to it.

## Acknowledgment

- **Sev1 pages on Lookout must be acknowledged within 3 minutes.**
- If the primary hasn't acknowledged in 3 minutes, PagerDuty escalates to the secondary automatically.
- Tracewell pages follow the company on-call policy.

## Heartbeat monitoring

Lookout sends a heartbeat to an external monitor every 60 seconds. If heartbeats stop, the external monitor pages the OBS primary and secondary directly through PagerDuty (not through Lookout). Treat a missed-heartbeat page as Sev1 until proven otherwise.

## During a Lookout incident

1. Acknowledge and join #incident-room.
2. Post in #eng-announce that paging may be delayed, and ask other teams' on-calls to watch their dashboards manually.
3. Check the Lookout evaluation queue and PagerDuty integration health first; they are the most common failure points.
4. Once paging is restored, replay any alerts that fired during the gap.

## Handoffs

Handoff notes go in the #obs-oncall channel at the end of each shift, including any silenced alerts and open tickets.

## Readiness

New OBS engineers shadow one full rotation before joining as primary.
