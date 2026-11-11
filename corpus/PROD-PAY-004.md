doc_id: PROD-PAY-004
title: Ledger Public API: Version Lifecycle and Deprecation
doc_type: policy
scope_level: team
owner_team: PAY
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-02-03
supersedes:
fact_ids: F-PROD-005

---

# Ledger Public API: Version Lifecycle and Deprecation

**Owner:** Payments (PAY)  **Applies to:** the Ledger public API

## Why we are careful

Customers build billing and finance processes on top of the Ledger API. Changing it too fast can break their month-end close. This policy sets how Ledger retires versions.

## Lifecycle

| Stage | Meaning |
|---|---|
| Current | Recommended for new integrations |
| Deprecated | Still works, but customers are asked to move |
| Sunset | No longer served |

## Support period

**A deprecated Ledger API version remains supported for 12 months after the deprecation notice is published.** During that time it receives security fixes and critical bug fixes.

## What we do when we deprecate

1. Publish a notice on the developer portal and in the changelog.
2. Email every customer account that has called the version in the previous 90 days.
3. Add `Deprecation` and `Sunset` headers to responses.
4. Offer a migration guide with side-by-side examples.
5. Remind customers at 6 months and at 90 days before sunset.

## Exceptions

A version may be sunset earlier only for a serious security reason, with approval from the Payments Engineering Manager and notice to customers.

## Approval

Approved by the Payments Engineering Manager and Tech Lead.
