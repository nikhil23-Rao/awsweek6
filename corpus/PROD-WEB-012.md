doc_id: PROD-WEB-012
title: Console Browser Support Matrix
doc_type: policy
scope_level: team
owner_team: WEB
owner_org: PROD
author_role: Tech Lead
status: approved
last_updated: 2026-02-05
supersedes:
fact_ids: 

---

# Console Browser Support Matrix

## Policy

Console supports the current and previous major versions of the browsers below. We do not support browsers that no longer receive security updates.

## Desktop

| Browser | Supported versions |
|---|---|
| Chrome | Current and previous major version |
| Edge | Current and previous major version |
| Firefox | Current and previous major version, plus the latest extended support release |
| Safari | Current and previous major version |

## Mobile web

Console is usable in the current versions of Safari on iOS and Chrome on Android, but the mobile apps are the recommended experience for alerts and approvals.

## What "supported" means

- Layout, features and accessibility behave as designed.
- Bugs that appear only in a supported browser are triaged as normal bugs.
- Unsupported browsers may work, but we do not test them.

## Testing

Automated end-to-end tests run on Chrome and Firefox on every merge. Safari and Edge are covered by a nightly run.

## Changes to this list

When a browser version leaves the supported range, we post a notice in the help center at least a month before we stop testing it.

## Owner

Tech Lead, Web.
