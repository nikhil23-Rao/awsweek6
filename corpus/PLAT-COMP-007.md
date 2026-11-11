---
doc_id: PLAT-COMP-007
title: "Postmortem: Kestrel CoreDNS Saturation (Sev2, Apr 2025)"
doc_type: postmortem
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2025-04-22
supersedes: ""
fact_ids: ""
---

# Postmortem: Kestrel CoreDNS Saturation (Sev2, Apr 2025)

**Severity:** Sev2
**Duration:** 47 minutes
**Owning team:** Compute
**Author:** SRE, Compute rotation

## Summary

On April 15, 2025, CoreDNS pods in the us-east-1 prod Kestrel cluster became saturated. Services saw intermittent DNS lookup failures, which surfaced as elevated `5xx` rates on several customer-facing APIs, including Ledger usage ingestion and parts of Console.

## Customer impact

About 3% of API requests to affected services failed over 47 minutes. Some Ledger usage events were retried and delivered late but none were lost, because Meterflow buffers on Streamline.

## Timeline (PT)

- 10:12: Search deploys a new Sieve indexer version that opens a fresh connection per document.
- 10:19: CoreDNS CPU climbs; first Lookout alert on DNS latency.
- 10:24: Compute on-call joins #incident-room; Sev2 declared.
- 10:38: Sieve identified as the source of the query spike.
- 10:44: Search rolls Sieve back through Gatekeeper CI.
- 10:59: DNS latency back to normal; incident resolved.

## Contributing factors

1. CoreDNS replicas were fixed at 6 and didn't scale with query volume.
2. No per-namespace DNS query metrics existed, so finding the source took 14 minutes.
3. Sieve's HTTP client wasn't reusing connections.

## What went well

- Search responded fast once identified.
- Meterflow's buffering prevented data loss.

## Action items

| Item | Owner | Ticket |
|---|---|---|
| Autoscale CoreDNS by query rate | COMP | COMP-4412 |
| Add NodeLocal DNSCache to all clusters | COMP | COMP-4413 |
| Per-namespace DNS query dashboard | OBS | OBS-2290 |
| Fix connection reuse in Sieve | SRCH | SRCH-1187 |
