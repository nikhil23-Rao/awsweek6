---
doc_id: CO-PLAT-011
title: Production Deploy Freeze Policy (v1)
doc_type: policy
scope_level: company
owner_team: VP Platform Engineering
owner_org: PLAT
author_role: Engineering Manager
status: deprecated
last_updated: 2025-03-03
supersedes: ""
fact_ids: F-POL-01
---

# Production Deploy Freeze Policy (v1)

> **Deprecated.** This version of the policy was deprecated on March 3, 2025, and is superseded by the current *Production Deploy Freeze Policy*. The Friday freeze now begins at 2 PM PT. This page is kept for historical reference only.

**Policy owner:** VP Platform Engineering
**Originally effective:** 2022

## Policy

Production deploys are frozen:

- **Fridays from 4 PM PT** through the end of Sunday.
- On company holidays.

Dev and staging deploys are unaffected.

## Emergency changes

Fixes for active Sev1 or Sev2 incidents may be deployed during a freeze with incident commander approval.

## What counts as a production deploy

- Any deploy to the prod environment.
- Production configuration and feature flag changes that affect customers.
- Terraform changes to production infrastructure.

## Enforcement

Teams are expected to check the time before promoting to prod. Engineering managers review any production change made during a freeze window at the following Monday's operations review.

## Holidays

The company holiday calendar is published by People Operations each December. The freeze begins at the end of the last working day before each holiday.

## Background

Introduced in 2022 alongside the engineering reorganization into three orgs, to reduce weekend incidents caused by late-week deploys.
