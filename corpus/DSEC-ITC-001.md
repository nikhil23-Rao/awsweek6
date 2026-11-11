doc_id: DSEC-ITC-001
title: Keystone Sev1 Paging and Escalation Procedure
doc_type: runbook
scope_level: team
owner_team: ITC
owner_org: DSEC
author_role: SRE
status: approved
last_updated: 2026-01-22
supersedes:
fact_ids: F-POL-03, F-DSEC-001

# Keystone Sev1 Paging and Escalation Procedure

## Service details

| Item | Value |
|---|---|
| Service | Keystone (SSO and IAM) |
| Owner | IT & Compliance (ITC) |
| Tier | 0 |
| Paging | Lookout, routed to PagerDuty |
| Primary channel | #itc-incidents |

## When this applies

Use this procedure when a Keystone alert is classified Sev1: SSO sign-in is failing for a large share of employees, token issuance is down, or directory sync has stopped and group changes are not applying.

## Acknowledgement target

**Keystone Sev1 pages are acknowledged within 15 minutes, because IT systems are internal.** Our users are employees, not customers, and a short delay in acknowledgement does not affect customer-facing availability. The 15-minute clock starts when Lookout fires the page.

## Escalation ladder

| Elapsed since page | Action |
|---|---|
| 0 min | Page goes to the primary on-call |
| 15 min, no ack | Page auto-escalates to the secondary on-call |
| 30 min, no ack | ITC Engineering Manager is paged |
| 45 min, no ack | SRE guild duty lead is notified |

## First actions after acknowledging

1. Post in #itc-incidents: "Sev1 acknowledged, investigating".
2. Open an incident ticket and note the start time.
3. Check the Keystone status dashboard for token error rates and directory sync lag.
4. If sign-in is down, announce a workaround for break-glass accounts through the IT helpdesk page.
5. Post a status update every 30 minutes until mitigated.

## Handoff and closure

When mitigated, move the incident to monitoring, record the resolution time, and schedule the postmortem. Hand off to the next on-call with a summary in the channel.

## Common pitfalls

- Muting the PagerDuty app on a phone while travelling. Use the swap calendar instead.
- Acknowledging the page but not posting in the channel.
- Forgetting to update the incident ticket after mitigation.
