doc_id: DSEC-MLI-011
title: "ADR: Foundry Serving Autoscaling"
doc_type: ADR
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: Tech Lead
status: approved
last_updated: 2026-01-08
supersedes:
fact_ids:

# ADR: Foundry Serving Autoscaling

**Status:** Accepted | **Date:** January 2026

## Context

Foundry serving endpoints previously scaled on CPU utilization. For GPU-backed models, CPU is a poor signal: an endpoint can be saturated on the GPU while CPU looks calm. Several endpoints were slow during traffic peaks and wasteful overnight.

## Decision

Serving endpoints will autoscale on **request concurrency per replica**, with GPU utilization as a secondary signal. The autoscaler runs on Kestrel.

Initial settings:

| Setting | Value |
|---|---|
| Minimum replicas | 2 |
| Target concurrency | per-model, set in the serving spec |
| Scale-up reaction | 1 minute |
| Scale-down delay | 10 minutes |

## Consequences

- Better latency during spikes because replicas are added based on actual queueing.
- Lower idle cost because the scale-down delay is short.
- Model owners must set a realistic target concurrency from load tests; a wrong value causes flapping.
- Cold starts for large models remain slow, so a minimum of 2 replicas is kept for all production endpoints.

## Alternatives considered

1. **Keep CPU-based scaling.** Rejected for the reason above.
2. **Fixed replica counts.** Predictable but expensive.
3. **Scheduled scaling.** Good for known daily peaks but fails on unexpected traffic.

## Follow-up

- Add target concurrency to the serving spec template.
- Add a dashboard panel for queue depth per replica.
- Review the settings after one quarter of data.
