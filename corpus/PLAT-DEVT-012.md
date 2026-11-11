---
doc_id: PLAT-DEVT-012
title: "ADR: Single Repository for Scaffold Templates"
doc_type: ADR
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: Tech Lead
status: approved
last_updated: 2024-06-12
supersedes: ""
fact_ids: ""
---

# ADR: Single Repository for Scaffold Templates

**Status:** Accepted
**Date:** June 2024
**Deciders:** Developer Tooling tech lead, Developer Tooling engineering manager

## Context

Scaffold templates live in five separate repositories, one per template. Shared pieces (Kestrel manifests, dashboards, alert rules, pipeline files) are copied between them. Fixes regularly land in one template and not the others, and template versions drift.

## Decision

Move all Scaffold templates into one repository, `scaffold-templates`, with shared components in a common directory and per-language layers on top. Version all templates together with a single version number.

## Consequences

**Positive**
- Shared fixes apply to every template at once.
- One version number makes `scaffold upgrade` simpler.
- Easier to test that every template still builds.

**Negative**
- A change for one language triggers tests for all templates. Acceptable; the full test suite runs in under 15 minutes.
- Language owners lose some independence. Mitigated with CODEOWNERS per directory.

## Migration

1. Create the new repo with shared components.
2. Port templates one at a time, starting with `go-http`.
3. Archive the old repositories after all templates are ported.

## Alternatives considered

- **Shared library package** consumed by separate template repos. Adds a release step, and still allows drift.
- **Status quo.** Rejected.
