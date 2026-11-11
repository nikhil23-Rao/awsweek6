---
doc_id: PLAT-NET-003
title: EdgeGate Release Guide
doc_type: runbook
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2026-02-24
supersedes: ""
fact_ids: F-PLAT-004
---

# EdgeGate Release Guide

Networking team runbook. Use this for every change to EdgeGate itself: gateway binaries, global configuration, plugins, and TLS settings. It doesn't cover individual route onboarding; see the *EdgeGate Route Onboarding Guide* for that.

## Release path

All EdgeGate changes go through Gatekeeper CI in this order:

1. **dev**: deploy automatically on merge to `main`.
2. **staging**: promote once dev checks pass.
3. **staging soak**: a **20-minute** soak in staging under replayed production traffic.
4. **prod canary**: one EdgeGate cell in us-east-1.
5. **prod**: remaining cells, then eu-west-1, then the us-west-2 standby cells.

## Staging soak

During the 20-minute soak we watch the EdgeGate staging dashboard in Lookout:

- `5xx` rate stays within 0.1 percentage points of the pre-deploy baseline.
- p99 latency stays within 10% of baseline.
- No new TLS handshake errors.
- Memory per gateway pod is flat (watch for slow leaks after plugin changes).

If any check fails, roll back staging and stop. Don't "push through" to prod to see whether it was noise.

## Who can release

Any NET engineer who has shadowed two releases. The release author shouldn't also be the only person watching the canary; grab a second NET engineer or the NET on-call.

## Rollback

```
gatekeeper rollback edgegate --env prod --to <previous-release>
```

Rollback takes about four minutes across all cells. Announce it in #net-releases and #incident-room if customers were affected.

## Checklist

- [ ] Change description and Jira ticket linked in the release
- [ ] Staging soak passed (20 min)
- [ ] Canary cell healthy for 10 minutes
- [ ] Release notes posted in #net-releases

## Contacts

NET on-call via PagerDuty, or #net-edgegate.
