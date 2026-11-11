doc_id: PROD-MOB-008
title: Mobile Crash Triage Runbook
doc_type: runbook
scope_level: team
owner_team: MOB
owner_org: PROD
author_role: SRE
status: approved
last_updated: 2026-04-21
supersedes:
fact_ids: 

---

# Mobile Crash Triage Runbook

**Owner:** Mobile SRE  **Audience:** on-call and release engineers

## Where crashes come from

Crash reports flow into the crash reporting dashboard from both apps. Each report has the app version, OS version, device model and a stack trace.

## Daily triage

1. Open the dashboard and sort by affected users.
2. Look at new crash groups first, then those growing quickly.
3. Assign each significant group to an engineer in Jira.

## Severity mapping

| Crash profile | Severity |
|---|---|
| App cannot start for many users | Sev1 |
| Crash in a core flow (alerts, approvals) affecting many users | Sev2 |
| Crash in a secondary screen | Sev3 |
| Rare crash on an unusual device | Sev4 |

## Investigating

- Reproduce on a device or simulator matching the report.
- Check whether the crash began in a specific release.
- Look for correlations with OS version or device model.

## Fixing

Fix in the next release unless it is Sev1 or Sev2, in which case discuss an expedited release with the Tech Lead.

## Closing

Mark the crash group resolved with the release number. Confirm it does not recur after rollout.
