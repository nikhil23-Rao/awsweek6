---
doc_id: PLAT-OBS-006
title: Lookout and PagerDuty Integration Runbook
doc_type: runbook
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2026-07-21
supersedes: ""
fact_ids: ""
---

# Lookout and PagerDuty Integration Runbook

Observability, SRE rotation

Lookout evaluates alert rules and sends firing alerts to PagerDuty, which pages humans. This runbook covers how the integration works and what to do when it breaks.

## How it works

1. A rule in Lookout fires.
2. Lookout looks up the routing key from the alert's `team` label and the namespace's `techsync.io/oncall` label.
3. Lookout sends an event to the PagerDuty Events API with a dedup key.
4. PagerDuty creates or updates an incident on the team's service and pages according to the team's escalation policy.
5. When the rule resolves, Lookout sends a resolve event with the same dedup key.

## Checking health

- `lookout_pagerduty_events_sent_total` should be non-zero and steady.
- `lookout_pagerduty_errors_total` should be near zero.
- The PagerDuty status page for Events API incidents.

## Failure modes

**Alerts fire in Lookout but no pages arrive.**
1. Check the error metric. `401` errors mean an expired or revoked integration key; rotate it in Vaultline and restart the notifier.
2. `429` errors mean PagerDuty is rate-limiting us, usually during an alert storm. The notifier batches and retries.
3. Missing routing key: the namespace is missing its on-call label. Page the owning team manually.

**Duplicate pages for the same problem.**
Usually a rule with a high-cardinality label (like pod name) in the dedup key. Fix the rule.

**Pages for a deleted service.**
Remove the rule from the service's repo, or ask OBS to archive orphaned rules.

## Manual paging fallback

If the integration is down, the OBS on-call pages affected teams directly from the PagerDuty UI and posts in #eng-announce.

## Key rotation

Integration keys are stored in Vaultline under `obs/lookout/pagerduty`.
