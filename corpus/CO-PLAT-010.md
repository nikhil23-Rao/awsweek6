---
doc_id: CO-PLAT-010
title: Production Deploy Freeze Policy
doc_type: policy
scope_level: company
owner_team: VP Platform Engineering
owner_org: PLAT
author_role: TPM
status: approved
last_updated: 2025-03-03
supersedes: CO-PLAT-011
fact_ids: F-POL-01
---

# Production Deploy Freeze Policy

**Policy owner:** VP Platform Engineering
**Effective:** March 3, 2025
**Applies to:** all production deploys at TechSync, all orgs and teams

## Policy

TechSync freezes production deploys at these times:

1. **Fridays, beginning at 2 PM PT**, through the end of Sunday.
2. **Company holidays**, beginning at 2 PM PT on the last working day before the holiday, through the end of the holiday.

During a freeze, no changes may be deployed to production. Deploys to dev and staging are unaffected.

## Why

Most of our serious incidents in 2024 began with a deploy late in the week, when fewer engineers were online to notice and respond. An earlier Friday cutoff gives teams time to watch their changes through the afternoon while the full team is still working.

## What counts as a production deploy

- Any Gatekeeper CI deploy to the prod environment.
- Production configuration changes, including feature flag changes that alter customer-visible behavior.
- Infrastructure changes to production through Terraform.

## Emergency changes

Changes needed to resolve or mitigate an active Sev1 or Sev2 incident may be deployed during a freeze. The incident commander approves the change in the incident channel, and the change is recorded in the incident timeline.

## Enforcement

Gatekeeper CI blocks production deploys during freeze windows. Incident commanders can unlock a single deploy using the emergency override, which is logged and reviewed weekly by Platform Engineering.

## Holiday calendar

The company holiday calendar is published by People Operations each December for the following year and is loaded into Gatekeeper CI automatically.

## Questions

#platform-releases
