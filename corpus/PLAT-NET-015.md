---
doc_id: PLAT-NET-015
title: Cross-Region Traffic Shift Runbook (us-east-1 to us-west-2)
doc_type: runbook
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2025-10-21
supersedes: ""
fact_ids: ""
---

# Cross-Region Traffic Shift Runbook (us-east-1 to us-west-2)

Networking, SRE rotation

Use this runbook to move customer traffic from us-east-1 to us-west-2, either during a regional disaster recovery event or a planned exercise. The SRE guild decides when to shift. NET executes the network steps.

## Preconditions

- The SRE guild incident commander has called for the shift.
- Kestrel clusters in us-west-2 are up and the target services report healthy.
- EdgeGate cells in us-west-2 are scaled up (they run at reduced capacity normally).

## Steps

1. **Scale EdgeGate in us-west-2.** Set the cell autoscaler minimums to production levels and wait for pods to be ready.
2. **Lower DNS TTLs** if they aren't already at 60 seconds (they should be).
3. **Shift public traffic.** Update the Route 53 weighted records for `api.techsync.io` and `console.techsync.io` in steps: 10%, 50%, 100% to us-west-2. Watch error rates for at least five minutes at each step.
4. **Shift internal names.** Update `internal.techsync.io` records for failed-over internal tools.
5. **Mesh failover.** Confirm Meridian Mesh in us-west-2 has the full set of service endpoints.
6. **Verify.** Run the synthetic checks in Lookout for Ship, Ledger, Insight, and Console.
7. **Announce** in #incident-room and on the status page.

EU traffic through eu-west-1 is not affected by this runbook.

## Shifting back

Reverse the steps once us-east-1 is healthy and the CTO approves failback. Shift back gradually, the same way.

## Notes from past exercises

- Step 1 is the slowest; start it as soon as a shift looks likely.
- Some Enterprise customers allowlist our IPs. The us-west-2 EdgeGate IPs are published in the customer docs, but warn the support team anyway.
