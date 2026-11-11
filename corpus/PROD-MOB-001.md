doc_id: PROD-MOB-001
title: App-Store Submissions During the Production Freeze
doc_type: policy exception
scope_level: team
owner_team: MOB
owner_org: PROD
author_role: Engineering Manager
status: approved
last_updated: 2025-03-18
supersedes:
fact_ids: F-POL-01; F-PROD-001

---

# App-Store Submissions During the Production Freeze

**Status:** Approved, March 2025
**Approved by:** VP Dana Whitfield and VP Carlos Mendoza
**Owner:** Mobile (MOB)

## Summary

The Mobile team has an approved exception that lets it submit mobile applications to the app stores during the production deploy freeze. The exception is limited to store submissions.

## Why

Apple and Google review and release applications on their own schedules. Store release trains are fixed, and missing a train can delay a customer-facing fix by days. Submitting during the freeze does not change anything running in TechSync's production environment.

## What the exception allows

**App-store submissions may go out during the freeze.** That covers uploading a build to App Store Connect or Google Play Console, submitting it for review, and releasing it once it is approved.

## What it does not allow

All other Mobile deploys stay frozen, including deploys of Pushline. Backend services, configuration changes and Pushline releases wait until the freeze ends.

## How to use the exception

1. Tell #prod-mobile that you are submitting during the freeze.
2. Confirm in the release ticket that the change contains no backend or Pushline deploy.
3. Record the submission in the release log.

## Scope

This exception applies only to the Mobile team. No other team may rely on it.

## Review

The Engineering Manager reviews this exception each March and reports to both approving VPs.
