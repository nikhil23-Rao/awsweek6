doc_id: DSEC-MLI-005
title: Foundry Model Serving Rollout Guide
doc_type: runbook
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: SRE
status: approved
last_updated: 2026-05-12
supersedes:
fact_ids:

# Foundry Model Serving Rollout Guide

This runbook covers rolling out a new model version to a Foundry serving endpoint with a canary.

## Before you start

- The model is registered in the model registry with a version tag.
- Offline evaluation results are attached to the release ticket.
- You are in the `foundry-operators` group.
- A second engineer is available as a reviewer.

## Rollout stages

| Stage | Traffic | Minimum soak |
|---|---|---|
| Shadow | 0% (mirrored) | 30 minutes |
| Canary | 5% | 1 hour |
| Partial | 25% | 1 hour |
| Full | 100% | n/a |

## Steps

1. Create the rollout: `foundry serve rollout create --model <name>:<version> --stage shadow`.
2. Compare shadow results with the current version in the comparison dashboard. Latency and error rate must be within the thresholds in the release ticket.
3. Advance to canary. Watch p95 latency, error rate, and the business metric named in the ticket.
4. Advance to partial, and then to full, only after each soak period has passed with metrics inside their thresholds.
5. Record each stage change in the release ticket.

## Automatic rollback

Foundry rolls back automatically if the error rate exceeds the threshold for 5 consecutive minutes during canary or partial. A Lookout alert is sent to the owning team.

## Manual rollback

`foundry serve rollout rollback --to <previous-version>` returns all traffic to the previous version within about a minute. Use it without hesitation if anything looks wrong. A rollback can be repeated safely.

## After rollout

- Keep the previous version deployed and warm for 24 hours.
- Update the model card with the new version and evaluation results.
- Close the release ticket.
