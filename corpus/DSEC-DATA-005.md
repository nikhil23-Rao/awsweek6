doc_id: DSEC-DATA-005
title: Reservoir Batch Ingestion Job Runbook
doc_type: runbook
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: Tech Lead
status: approved
last_updated: 2026-04-02
supersedes:
fact_ids:

# Reservoir Batch Ingestion Job Runbook

How batch ingestion jobs are scheduled, how they retry, and what to do when they fail. Event streams are covered in the Streamline guides; this runbook is only for scheduled batch jobs that load data into Reservoir.

## Job anatomy

Each job is a container image run on Kestrel by the scheduler. A job has a source, a transformation, a target table, and a schedule. Jobs are defined in the `reservoir-jobs` repo and deployed through Gatekeeper CI.

```yaml
job: payments-ledger-sync
schedule: "0 * * * *"
source: postgres://ledger-replica/transactions
target: payments.transactions
timeout: 45m
retries: 3
```

## Scheduling

- Most jobs run hourly; heavy jobs run overnight.
- Do not schedule more than five heavy jobs at the same time. The scheduler dashboard shows current load.
- Jobs must be idempotent: running twice must produce the same result.

## Retries

The scheduler retries a failed job with exponential backoff: 2, 4, and then 8 minutes. After the final retry, the job is marked Failed and a Lookout alert goes to the owning team's channel.

## When a job fails

1. Open the job's page in the scheduler and read the last log lines.
2. Classify the failure:
   - **Source unavailable:** wait for the source to recover, then run the job manually.
   - **Schema mismatch:** coordinate with the source owner; do not change the target table without the DATA team's review.
   - **Timeout:** check source volume; raise the timeout only if the increase is justified in the ticket.
   - **Out of memory:** raise the memory request in the job file and redeploy.
3. Re-run with `reservoir job run <name> --once` after the fix.
4. Confirm the target table has the expected row count with a Quarry query.

## Ownership

Every job has an owner team in its definition. Orphaned jobs are reported monthly and disabled if no owner claims them.

## Change process

Changes go through a pull request reviewed by someone on DATA. Schedule changes for heavy jobs need the Tech Lead's approval.
