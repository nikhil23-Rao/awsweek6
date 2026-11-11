---
doc_id: PLAT-OBS-008
title: "Postmortem: Tracewell Ingestion Backlog (Sev2, Mar 2026)"
doc_type: postmortem
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2026-03-18
supersedes: ""
fact_ids: ""
---

# Postmortem: Tracewell Ingestion Backlog (Sev2, Mar 2026)

**Severity:** Sev2
**Duration:** 2 hours 10 minutes
**Owning team:** Observability
**Author:** SRE, OBS rotation

## Summary

On March 11, 2026, Tracewell collectors in us-east-1 couldn't keep up with incoming log volume after a large spike from one service. A backlog built up, and logs and traces for all services in the region were delayed by up to 85 minutes. Search and dashboards showed stale data during the incident.

## Impact

No customer impact. Internal impact was significant: three teams were debugging unrelated incidents during the window and couldn't see recent logs.

## Timeline (PT)

- 13:40: A Meterflow deploy enables debug logging in prod by mistake. Log volume from Meterflow rises about 20x.
- 13:52: Collector queue depth alert fires.
- 14:05: Sev2 declared after confirming delays across all services.
- 14:30: Meterflow identified as the source.
- 14:41: Payments rolls back the logging change.
- 15:50: Backlog fully drained; incident resolved.

## Contributing factors

1. Collectors ran at a fixed replica count and couldn't scale out.
2. No per-service ingestion limits, so one service could starve everyone else.
3. The debug flag was set through an environment variable that skipped code review.

## What went well

- Data wasn't lost; the queue held everything.
- Payments responded quickly once contacted.

## Action items

| Item | Owner | Ticket |
|---|---|---|
| Autoscale collectors on queue depth | OBS | OBS-2602 |
| Per-service ingestion rate limits | OBS | OBS-2603 |
| Block debug log level in prod via Gatekeeper CI policy | DEVT | DEVT-1944 |
| Ingestion volume panel per service | OBS | OBS-2604 |
