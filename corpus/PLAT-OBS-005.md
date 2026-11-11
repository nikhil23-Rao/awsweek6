---
doc_id: PLAT-OBS-005
title: "ADR: Store Lookout Alert Rules in Git"
doc_type: ADR
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: Tech Lead
status: approved
last_updated: 2024-09-24
supersedes: ""
fact_ids: ""
---

# ADR: Store Lookout Alert Rules in Git

**Status:** Accepted
**Date:** September 2024
**Deciders:** Observability tech lead, Observability engineering manager
**Consulted:** Compute, Networking, Payments, SRE guild

## Context

Alert rules in Lookout are created and edited in the Lookout UI. Over the years this has caused real problems:

- No review. Anyone with access can change a threshold that pages someone at 3 AM.
- No history. When an alert changes, nobody knows who changed it or why.
- Drift between environments. Staging and prod rules diverge silently.
- Rules for deleted services linger for months.

## Decision

Alert rules live in Git, next to the service code, in `lookout/rules.yaml`. Gatekeeper CI validates and applies them. The Lookout UI becomes read-only for rules, except for silences.

## Consequences

**Positive**
- Rules are reviewed like code.
- Full history in Git.
- Rules are deleted when a service's repo is archived.

**Negative**
- Changing a threshold during an incident takes a PR instead of a click. Mitigated by allowing silences in the UI and a fast-path review for incident fixes.
- Migration effort for every team.

## Migration plan

1. OBS exports existing UI rules into each owning team's repo (Q4 2024).
2. Teams review and merge their exported rules.
3. UI editing disabled per team once their migration is merged.
4. Remaining unowned rules are archived after a 30-day notice.

## Alternatives considered

- **Central rules repo.** Easier for OBS, worse ownership. Rejected.
- **Keep UI with audit log.** Doesn't solve review or drift.
