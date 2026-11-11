---
doc_id: PLAT-OBS-001
title: Observability Q3 2026 Planning Notes
doc_type: meeting notes
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: TPM
status: unmarked
last_updated: 2026-07-08
supersedes: ""
fact_ids: ""
---

# Observability Q3 2026 Planning Notes

**Date:** July 8, 2026
**Attendees:** OBS engineering manager, OBS tech lead, OBS engineers, Platform TPM (notes)

## Q2 recap

- Tracewell tail sampling shipped to all prod clusters. Trace volume down about 40% with no complaints about missing traces.
- Lookout rule evaluation latency improved after the Q2 sharding work.
- Missed: per-team cost reports for OpenSearch. Slipped to Q3.

## Q3 priorities (agreed)

1. **OpenSearch cost reports per team.** Show each team what its logs and traces cost so the noisiest services can be fixed. Owner: OBS tech lead.
2. **Per-service ingestion limits.** Make the temporary per-service limits permanent defaults. Follow-up from the March ingestion backlog postmortem.
3. **Alert quality review.** Work with each Platform team to delete alerts that haven't fired usefully in six months.
4. **Insight dogfooding.** Evaluate moving some internal dashboards to TechSync Insight, since it's now our own GA product. Exploratory only.

## Staffing

- One engineer on parental leave for most of the quarter.
- Requesting one contractor for the cost-report UI; decision pending with the VP.

## Risks

- OpenSearch cluster upgrade from AWS may land mid-quarter and pull people away.
- Ingestion limits could drop data for teams that log heavily; needs clear communication before rollout.

## Not doing this quarter

- Replacing PagerDuty integration.
- Log-based metrics redesign.

## Action items

| Owner | Item |
|---|---|
| OBS tech lead | Cost report design doc |
| OBS engineer | Ingestion limits RFC |
| TPM | Alert review schedule with each Platform team |
