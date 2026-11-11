---
doc_id: PLAT-NET-005
title: EdgeGate Production Change Windows
doc_type: guide
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: Engineering Manager
status: unmarked
last_updated: 2024-05-16
supersedes: ""
fact_ids: F-POL-01
---

# EdgeGate Production Change Windows

Networking team. Last reviewed May 2024.

EdgeGate is the front door for every customer request to TechSync Ship, Ledger, Insight, and Console. A bad change here is visible to every customer immediately, so we're deliberate about when production changes go out.

## When we ship to prod

**Preferred window:** Tuesday through Thursday, 9 AM to 3 PM PT. This is when the most NET engineers are online and the product teams are around to help verify.

**Allowed:** Monday and Friday during business hours, as long as you follow the company freeze rule below.

**Not allowed:**

- No production deploys after **4 PM PT on Friday**, through the weekend. This follows the company production deploy freeze.
- No production deploys on company holidays.
- No deploys during an active Sev1 or Sev2 incident unless the change is the fix.

## Emergency changes

If an EdgeGate change is needed to fix or mitigate an active incident, it can go out at any time. The incident commander approves it in the incident channel, and the NET on-call ships it. Document it in the incident timeline.

## Large customer events

For planned high-traffic events (for example a large Enterprise customer's launch or end-of-quarter billing runs in Ledger), the NET engineering manager may declare an extra no-change window. These are posted in #net-announcements at least a week in advance.

## Before any prod change

- Confirm the release passed staging.
- Make sure a second NET engineer is available to watch the rollout.
- Check #incident-room for anything ongoing.

## Questions

Ask in #net-edgegate or ping the NET engineering manager.
