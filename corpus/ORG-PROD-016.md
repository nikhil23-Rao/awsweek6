doc_id: ORG-PROD-016
title: Dependency and Library Upgrade Cadence
doc_type: policy
scope_level: org
owner_team: PROD
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-02-24
supersedes:
fact_ids: 

---

# Dependency and Library Upgrade Cadence

## Policy

Product Engineering teams upgrade third-party dependencies on a quarterly cadence so that updates stay small and predictable.

## Upgrade windows

Each quarter has a two-week upgrade window, starting the second Monday of the quarter. During the window, teams:

1. Review the dependency report produced by Sentinel.
2. Upgrade minor and patch versions of direct dependencies.
3. Plan major-version upgrades as separate work with their own tickets.
4. Run the full test suite and the staging checks before merging.

## Keeping it manageable

- Upgrade one ecosystem at a time (for example, Go modules, then npm packages).
- Keep upgrade pull requests free of unrelated changes.
- Record notable behavior changes in the pull request description.

## Out-of-cycle upgrades

A team may upgrade outside the window when it needs a specific fix. It should tell its Tech Lead and note the reason in the pull request.

## Ownership

Staff Engineers across the four teams maintain this policy. Suggested changes go to #prod-engineering-standards.
