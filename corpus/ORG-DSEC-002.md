doc_id: ORG-DSEC-002
title: Compliance Evidence Handbook
doc_type: handbook
scope_level: org
owner_team: none (DSEC org-wide)
owner_org: DSEC
author_role: Compliance Analyst
status: approved
last_updated: 2026-05-18
supersedes:
fact_ids: F-DSEC-010

# Compliance Evidence Handbook

A practical guide for DSEC teams on collecting, naming, and storing evidence for audits and internal reviews. Evidence is what lets us show an auditor that a control actually operated. It lives in Compass.

## 1. What counts as evidence

- System exports (access lists, configuration dumps) with a visible timestamp
- Tickets showing a decision and its follow-up work
- Signed approvals (Jira sign-off is fine)
- Screenshots, only when no export is possible

Evidence must be readable without special tooling and must identify the system, the date, and the person who collected it.

## 2. Naming

Use `<system>_<control>_<YYYY-MM-DD>_<collector>`. For example: `keystone_access-list_2026-04-03_analyst1`.

## 3. Uploading to Compass

1. Open the control in Compass and choose **Add evidence**.
2. Attach the file or link and select the review period.
3. Add one sentence describing what the file proves.
4. Submit within 5 business days of the work being completed.

## 4. Access review evidence

Each quarterly access review produces three items: the exported access list, the reviewer decisions, and the removal tickets.

- **Tier 0, Tier 1, and Tier 2 services:** all three items are uploaded to Compass.
- **Tier 3 experimental services:** uploading to Compass is **optional**. A reviewer sign-off recorded in the Jira review ticket is sufficient, since these services hold no customer data and change frequently.

## 5. Audit seasons

During SOC 2 Type II and ISO 27001 audit windows, the Compliance Analysts run a weekly gap check. Teams with missing evidence get a Slack reminder and a Jira ticket.

## 6. Common mistakes

- Uploading a screenshot when an export was available.
- Missing timestamps.
- Leaving the review period blank.

## 7. Questions

Ask in the compliance channel or open a ticket with the IT & Compliance team.
