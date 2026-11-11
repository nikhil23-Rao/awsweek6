doc_id: ORG-PROD-003
title: Product Release Readiness Checklist
doc_type: policy
scope_level: org
owner_team: PROD
owner_org: PROD
author_role: TPM
status: approved
last_updated: 2026-01-28
supersedes:
fact_ids: 

---

# Product Release Readiness Checklist

Use this checklist for any release that customers will notice. It is short on purpose; teams add their own steps on top.

## Before the release

- [ ] Changes have been exercised in staging and a named engineer has signed off.
- [ ] A rollback plan is written down and has been read by the person releasing.
- [ ] Release notes are drafted in plain language and reviewed by the Tech Lead.
- [ ] Feature flags are configured so that new behavior can be switched off without a new build.
- [ ] Dashboards and alerts for the affected service have been checked.
- [ ] Support has been told about customer-visible changes.

## During the release

- [ ] The releasing engineer announces start and finish in the team channel.
- [ ] Error rates and latency are watched for at least thirty minutes.

## After the release

- [ ] Release notes are published.
- [ ] Flags that are no longer needed are scheduled for cleanup.
- [ ] Anything surprising is written up in the team's notes for the next planning meeting.

## Ownership

The TPM function owns this checklist and reviews it each January. Suggestions are welcome in #prod-release.
