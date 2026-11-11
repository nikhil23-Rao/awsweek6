doc_id: PROD-MOB-009
title: Postmortem: Android Alert Delay under Doze
doc_type: postmortem
scope_level: team
owner_team: MOB
owner_org: PROD
author_role: SRE
status: approved
last_updated: 2026-04-28
supersedes:
fact_ids: 

---

# Postmortem: Android Alert Delay under Doze

**Severity:** Sev2  **Incident date:** 2026-04-21  **Published:** 2026-04-28  **Author:** SRE (MOB)

## Summary

Some Android users received alerts up to 40 minutes late when their phones were idle. No alerts were lost. The delay affected roughly 6% of Android users that day.

## Timeline (Pacific)

- **08:15** Support noted a few reports of late alerts.
- **09:30** The on-call engineer compared send and receive times and saw delays only on Android.
- **10:50** The pattern pointed to devices in battery-saving Doze mode.
- **13:10** A change to message priority was prepared.
- **15:30** The change reached all users.

## Root cause

A release the previous week changed how the app requested high-priority delivery. Messages were sent with normal priority, which Android may batch while a device is in Doze mode.

## What went well

Support spotted the trend early; engineers compared timestamps rather than guessing.

## What went badly

We had no test that measured delivery delay on an idle device. The release notes did not mention the priority change.

## Action items

1. Add a test that sends alerts to an idle device and checks delay (owner: Tech Lead).
2. Add a delivery delay graph by platform (owner: SRE).
3. Add a line about delivery priority to the release checklist template.
