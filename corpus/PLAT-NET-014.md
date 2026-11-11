---
doc_id: PLAT-NET-014
title: "Postmortem: EdgeGate TLS Certificate Expiry (Sev1, Jul 2025)"
doc_type: postmortem
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2025-07-17
supersedes: ""
fact_ids: ""
---

# Postmortem: EdgeGate TLS Certificate Expiry (Sev1, Jul 2025)

**Severity:** Sev1
**Duration:** 26 minutes
**Owning team:** Networking
**Author:** SRE, NET rotation

## Summary

On July 10, 2025, the TLS certificate for the EdgeGate listener serving `api.eu.techsync.io` expired. Customers calling TechSync APIs through the EU endpoint got TLS errors until a renewed certificate was deployed.

## Customer impact

All API traffic through the EU endpoint failed for 26 minutes. Ship deploys for EU customers stalled, and Ledger usage events from EU customers were rejected. Clients retried, and Meterflow accepted the backlog once service was restored.

## Timeline (UTC)

- 08:00: Certificate for `api.eu.techsync.io` expires.
- 08:03: Lookout alert on EU EdgeGate `5xx` and TLS handshake failures.
- 08:06: Sev1 declared; NET on-call is incident commander.
- 08:14: Expired certificate identified.
- 08:21: Renewed certificate issued manually and deployed.
- 08:26: Error rates back to normal.

## Root cause

The EU listener's certificate had been issued manually in 2023, when eu-west-1 EdgeGate was first set up, and was never moved to the automated renewal system used everywhere else. No alert existed for certificate expiry on that listener.

## Contributing factors

- No inventory of which certificates were managed by automation.
- The expiry alert only covered certificates the automation knew about.

## What went well

- Detection in three minutes.
- Clear ownership; the right engineer was paged first.

## Action items

| Item | Owner | Ticket |
|---|---|---|
| Move all EdgeGate certificates to automated issuance | NET | NET-3021 |
| Alert on any certificate under 21 days to expiry, from live scans | OBS | OBS-2411 |
| Certificate inventory dashboard | NET | NET-3022 |
| Status page update template for regional API outages | SRE guild | SRE-588 |
