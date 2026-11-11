doc_id: DSEC-ITC-012
title: Keystone Directory Sync Troubleshooting
doc_type: runbook
scope_level: team
owner_team: ITC
owner_org: DSEC
author_role: SRE
status: approved
last_updated: 2026-03-31
supersedes:
fact_ids:

# Keystone Directory Sync Troubleshooting

Keystone synchronizes users and groups from the HR directory. Use this runbook when group changes or new accounts are not appearing.

## 1. Symptoms

- A new hire's account is missing.
- Group membership changes do not apply.
- The sync dashboard shows a growing "pending changes" count.

## 2. First checks

1. Open the directory sync dashboard and note the time of the last successful run.
2. Check for a failed run and read its error summary.
3. Check whether the HR directory itself is reachable.

## 3. Error patterns

| Error | Meaning | Action |
|---|---|---|
| `auth_failed` | Service credential rejected | Rotate the connector credential through Vaultline, then re-run |
| `schema_mismatch` | HR directory changed a field | Update the mapping file and re-run |
| `rate_limited` | Too many requests | Wait and re-run with a smaller batch |
| `partial_apply` | Some records failed | Download the failure report and fix records individually |

## 4. Re-running a sync

`keystone sync run --full` re-reads the whole directory. Prefer `--incremental` first. Full runs take about 20 minutes and cause a brief increase in load.

## 5. Checking a single user

Use `keystone user show <email>` and compare groups against the HR directory record. If the HR record is wrong, ask the people team to fix it at the source; do not edit Keystone by hand.

## 6. Escalation

If the sync is down and new hires cannot start, escalate to the ITC on-call through Lookout. Post updates in the ITC incidents channel.
