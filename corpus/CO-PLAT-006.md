---
doc_id: CO-PLAT-006
title: Code Review Policy
doc_type: policy
scope_level: company
owner_team: DEVT
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2024-06-04
supersedes: ""
fact_ids: F-POL-02
---

# Code Review Policy

**Policy owner:** Developer Tooling
**Applies to:** all code merged into production repositories at TechSync

## Required approvals

The number of approvals required before merge depends on the tier of the service the code belongs to:

| Service tier | Required approvals |
|---|---|
| Tier 0 (core platform) | **2** |
| Tier 1 (customer-facing) | **2** |
| Tier 2 (internal) | **1** |
| Tier 3 (experimental) | **1** |

Approvals must come from engineers other than the author. At least one approver must be listed in the repository's CODEOWNERS for the files changed.

If a PR touches services of different tiers, the highest tier applies.

## Enforcement

GitHub Enterprise branch protection enforces the approval count on each repository's default branch. Developer Tooling syncs branch protection from the service catalog nightly, so the required count follows the service's tier automatically.

## Self-approval and bypass

- Authors cannot approve their own PRs.
- Admin bypass of branch protection is disabled on production repositories.
- Changes needed during an active Sev1 incident still require the normal approvals, but reviewers in the incident channel should prioritize them.

## Exceptions

Teams may request an exception for a narrowly defined class of changes. Exceptions must be approved by the Developer Tooling engineering manager and the VP of the requesting team's org, must name the exact repositories and change types covered, and must be recorded on Confluence.

## Related

- Code Review Guidelines for Authors and Reviewers
