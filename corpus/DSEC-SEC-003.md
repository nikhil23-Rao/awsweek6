doc_id: DSEC-SEC-003
title: AppSec Critical Vulnerability Remediation Runbook
doc_type: runbook
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Security Engineer
status: approved
last_updated: 2025-02-11
supersedes:
fact_ids: F-DSEC-008

# AppSec Critical Vulnerability Remediation Runbook

**Owner:** AppSec (SEC) | **Covers:** services owned by SEC, which are Sentinel and Vaultline

## Why we hold ourselves to a tighter clock

Sentinel and Vaultline sit in the path of every pull request and every secret in the company. A Critical vulnerability in either is more urgent than the same finding elsewhere. So for SEC-owned services, **Critical findings must be fixed within 3 days** of confirmation.

## The 3-day clock

| Day | What must happen |
|---|---|
| Day 0 | Finding confirmed. Page the SEC on-call, open a Critical ticket, name an incident lead. |
| Day 1 | Fix approach agreed. Patch or mitigation in progress. Engineering manager informed. |
| Day 2 | Fix built and tested in staging. Peer review done. |
| Day 3 | Fix deployed to production and verified. Ticket closed with evidence. |

## Roles

- **Incident lead:** a Security Engineer who owns the ticket until it is closed.
- **Reviewer:** a second engineer who is not the author of the fix.
- **SEC Engineering Manager:** receives a daily summary and unblocks resources.

## If the fix is not ready

If a fix cannot ship by Day 3, the incident lead must apply a mitigation (disable a feature, add a deny rule, rotate affected credentials) and notify the SEC Engineering Manager. A mitigation does not close the ticket; the permanent fix keeps its own tight deadline set by the SEC Tech Lead.

## Checklist for the incident lead

- [ ] Ticket opened with severity evidence
- [ ] Scope assessed: which versions and environments
- [ ] Mitigation considered on Day 0
- [ ] Customer or internal communications drafted if data is at risk
- [ ] Verification steps recorded
- [ ] Retro note added to the SEC weekly sync agenda

## Tooling

Use Sentinel to confirm that the vulnerable version no longer appears in any build, and use Vaultline audit logs to check for abuse during the exposure window.
