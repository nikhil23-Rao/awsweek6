doc_id: DSEC-MLI-004
title: Foundry Training Job Submission Runbook
doc_type: runbook
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2026-04-28
supersedes:
fact_ids:

# Foundry Training Job Submission Runbook

Terse reference for submitting and monitoring training jobs.

## Prerequisites

- Member of `foundry-users`
- GPU quota pool assigned to your team
- Job spec in version control

## Job spec

```yaml
name: ranker-v7
image: registry.internal/ml/ranker:2026.04
resources:
  gpu: a100
  count: 4
  memory: 128Gi
checkpoint:
  interval: 20m
  path: s3://foundry-ckpt/ranker-v7/
retries: 2
tags:
  cost_center: search
```

## Submit

1. Validate: `foundry job validate -f job.yaml`
2. Submit: `foundry job submit -f job.yaml`
3. Record the job ID in your experiment notes.

## Monitor

- Logs: `foundry job logs <id> --follow`
- Metrics: the Foundry job dashboard, GPU utilization panel
- Alerts: Lookout pages the owning team only for jobs tagged `critical`

## Common failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Pending for more than 30 min | Quota exhausted | Check pool usage; wait or ask MLI for temporary quota |
| OOMKilled | Memory request too low | Raise `memory`, or reduce batch size |
| ImagePullBackOff | Wrong tag or registry permission | Check image tag and service account |
| Loss becomes NaN | Learning rate or data issue | Resume from the last checkpoint with a lower rate |

## Resuming from a checkpoint

Add `resume_from: <checkpoint path>` to the spec and resubmit. Foundry will pick up at the last saved step.

## Cancelling

`foundry job cancel <id>`. Cancel jobs you no longer need; idle GPUs still cost money.

## Escalation

ML Infrastructure channel during business hours; the MLI on-call through Lookout for cluster-wide failures.
