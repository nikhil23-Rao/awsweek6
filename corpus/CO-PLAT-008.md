---
doc_id: CO-PLAT-008
title: Incident Postmortem Policy
doc_type: policy
scope_level: company
owner_team: SRE guild
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2023-09-19
supersedes: ""
fact_ids: F-POL-04
---

# Incident Postmortem Policy

**Policy owner:** SRE guild
**Applies to:** all incidents at TechSync

## When a postmortem is required

A written postmortem is required for every **Sev1** and **Sev2** incident. Postmortems for Sev3 and Sev4 incidents are encouraged when there's something worth learning, but not required.

## Deadline

Postmortems for Sev1 and Sev2 incidents are **due within 5 business days** of the incident being resolved. "Due" means the document is complete, reviewed by the owning team's engineering manager, and published on Confluence.

## Content

Every postmortem includes:

- A summary and customer impact
- A timeline
- Contributing factors
- What went well and what didn't
- Action items, each with an owner and a Jira ticket

Use the company postmortem template.

## Ownership

The team that owns the system where the incident started owns the postmortem. If several teams were involved, the incident commander names one owning team before the incident channel is closed. Other teams contribute sections for their parts of the timeline.

## Review

Each org runs a regular incident review meeting where completed postmortems are presented. Postmortems with customer impact are also shared with Customer Support.

## Blamelessness

Postmortems describe what happened and why the system allowed it. They don't assign blame to individuals.

## Follow-through

The SRE guild tracks open action items from Sev1 and Sev2 postmortems and reports on them monthly to the CTO.

## Questions

#sre-guild
