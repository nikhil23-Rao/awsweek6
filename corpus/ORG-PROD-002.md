doc_id: ORG-PROD-002
title: Product API Versioning Standard
doc_type: standard
scope_level: org
owner_team: PROD
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2025-03-12
supersedes:
fact_ids: F-PROD-005

---

# Product API Versioning Standard

**Applies to:** every public and partner-facing API owned by a Product Engineering team.

## 1. Version numbers

APIs use semantic versioning. The major version appears in the request path (for example `/v2/`). Minor and patch changes must stay backward compatible within a major version.

## 2. What counts as a breaking change

Removing or renaming a field, changing a field's type, tightening validation, changing an error code, or changing default behavior in a way that alters results.

## 3. Deprecation

When a team decides to retire a version, it must:

1. Publish a deprecation notice in the API changelog and on the developer portal.
2. Add `Deprecation` and `Sunset` headers to responses from the affected version.
3. Notify customers who have called the version in the previous 30 days.

**A deprecated version remains supported for a minimum of 6 months after the deprecation notice is published.** Teams may support it longer; they may not support it for less time without written approval from the VP of Product Engineering.

## 4. Sunset

On the sunset date the version may return `410 Gone`. Sunset dates are published at least 30 days before they take effect.

## 5. Changelog

Every team keeps a changelog in the developer portal with the date, version and a plain-language summary of each change.

## 6. Questions

Ask in #prod-api-standards or contact the owning Staff Engineer.
