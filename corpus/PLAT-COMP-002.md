---
doc_id: PLAT-COMP-002
title: Kestrel Namespace Naming and Labeling Conventions
doc_type: standard
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: Technical Writer
status: approved
last_updated: 2024-10-08
supersedes: ""
fact_ids: ""
---

# Kestrel Namespace Naming and Labeling Conventions

Compute team standard. Written by Technical Writing with the Compute team.

Consistent names and labels let us route alerts, allocate cost, and find owners quickly during an incident. The Kestrel admission controller enforces the rules marked **required**.

## Namespace names

Format: `<team-code>-<system>` in lowercase, using hyphens.

| Good | Bad | Why |
|---|---|---|
| `pay-ledger-core` | `LedgerCore` | uppercase, no team code |
| `srch-quarry` | `search` | no system name |
| `mli-foundry` | `mli_foundry` | underscores aren't allowed |

Names are at most 40 characters. The environment isn't part of the name; dev, staging, and prod are separate clusters.

## Required labels

Every namespace must carry:

- `techsync.io/team`: the team code, for example `WEB`.
- `techsync.io/org`: `PLAT`, `PROD`, or `DSEC`.
- `techsync.io/cost-center`: the finance cost center for the team.
- `techsync.io/oncall`: the PagerDuty service ID that should receive pages.

## Required labels on workloads

Deployments and StatefulSets must carry:

- `app.kubernetes.io/name`
- `app.kubernetes.io/version`
- `techsync.io/team`

## Recommended labels

- `techsync.io/data-region`: `us` or `eu`, for workloads handling EU customer data in eu-west-1.
- `techsync.io/experimental`: `true` for short-lived experiments.

## Renaming a namespace

Kubernetes namespaces can't be renamed. Create the new namespace, migrate workloads, and ask COMP to delete the old one through a ticket.

## Questions

#comp-help
