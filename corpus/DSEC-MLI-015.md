doc_id: DSEC-MLI-015
title: "Postmortem: Foundry Serving Latency Regression"
doc_type: postmortem
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: SRE
status: approved
last_updated: 2026-05-27
supersedes:
fact_ids:

# Postmortem: Foundry Serving Latency Regression

**Severity:** Sev2 | **Incident date:** 19 May 2026 | **Duration:** about 2 hours 40 minutes | **Authors:** MLI SRE

## Summary

After a model rollout on a customer-facing recommendation endpoint, p95 latency roughly doubled for several hours. No requests failed, so the automatic rollback did not trigger. The latency regression was found by a customer-facing team's alert, not by Foundry's own alerts.

## Impact

- p95 latency rose from about 120 ms to about 260 ms on the affected endpoint.
- Downstream pages that call the endpoint loaded visibly slower.
- No data loss, and no errors above baseline.

## Timeline (UTC)

| Time | Event |
|---|---|
| 14:05 | Rollout reaches the partial stage (25 percent). Metrics inside thresholds. |
| 14:50 | Rollout advances to full. |
| 15:20 | Latency begins to climb as traffic increases through the afternoon. |
| 16:10 | A downstream team's latency alert fires; they message the MLI channel. |
| 16:25 | MLI SRE opens an incident and starts investigating. |
| 16:55 | Autoscaler dashboards show replicas at the minimum while queue depth is high. |
| 17:10 | Manual scale-up applied; latency starts to fall. |
| 18:45 | Latency back to baseline. Rollout of the previous version prepared as a fallback but not needed. |

## Root cause

The new model was larger and slower per request. The serving spec still carried the target concurrency of the old model, set far too high for the new one. The autoscaler therefore believed the replicas had capacity, and it did not add replicas as load rose.

## Contributing factors

1. The rollout gates measured error rate and median latency, but not queue depth.
2. The partial stage soaked during a quiet period; the traffic peak came after full rollout.
3. No check compared the serving spec's target concurrency with the model's load test results.

## What went well

- The manual scale-up worked immediately.
- The downstream team reported clearly and quickly.

## What went poorly

- Foundry's own alerts did not catch a slow-but-healthy endpoint.
- The rollout guide did not require updating the concurrency target for a new model.

## Action items

| Action | Owner | Due |
|---|---|---|
| Add p95 latency and queue-depth thresholds to the automatic rollback | MLI SRE | June 2026 |
| Require target concurrency to be re-validated in the release ticket | MLI Tech Lead | June 2026 |
| Add a soak requirement that spans peak traffic for customer-facing endpoints | MLI SRE | July 2026 |
| Alert on high queue depth with minimum replicas | MLI SRE | June 2026 |
