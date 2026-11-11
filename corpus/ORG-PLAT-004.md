---
doc_id: ORG-PLAT-004
title: Platform Q2 2026 Quarterly Review Notes
doc_type: meeting notes
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: TPM
status: unmarked
last_updated: 2026-07-15
supersedes: ""
fact_ids: ""
---

# Platform Q2 2026 Quarterly Review Notes

**Date:** July 15, 2026
**Attendees:** Dana Whitfield (VP Platform Engineering), Platform engineering managers and tech leads, Platform TPM (notes)

## Highlights

- **Compute:** Karpenter consolidation tuned; Kestrel compute spend down 11% quarter over quarter. Second large-build Forge pool live.
- **Networking:** eu-west-1 EdgeGate cells reached parity with us-east-1. Certificate automation covers every listener.
- **Observability:** Tracewell tail sampling in all prod clusters. Collector autoscaling shipped.
- **Developer Tooling:** median merge-to-prod time down to 34 minutes. `scaffold upgrade` used by 41% of services.

## Misses

- OpenSearch per-team cost reports slipped again (OBS). Now committed for Q3.
- IPv6 plan not started (NET). Moved to H2.
- Flaky test rate still at 1.8% of runs, above the 1% goal (DEVT).

## Incidents

- Two Sev2s on Platform systems this quarter, both with completed postmortems.
- No Sev1s on Platform systems.

## Staffing

- Three new hires joined; two open roles remain (NET, OBS).
- One OBS engineer on leave through September.

## Discussion

- The VP asked teams to reduce the number of alerts that page at night. Each team will report its night-page count monthly.
- Product Engineering asked for faster deploys. DEVT will bring options to the Gatekeeper CI working group.

## Action items

| Owner | Item |
|---|---|
| Each EM | Monthly night-page count |
| DEVT EM | Deploy speed options |
| TPM | H2 roadmap draft by July 31 |
