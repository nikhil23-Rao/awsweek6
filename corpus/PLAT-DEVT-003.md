---
doc_id: PLAT-DEVT-003
title: GitHub Enterprise Repository Conventions
doc_type: standard
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-04-09
supersedes: ""
fact_ids: ""
---

# GitHub Enterprise Repository Conventions

Developer Tooling standard

These conventions apply to every repository in TechSync's GitHub Enterprise organization.

## Naming

- Lowercase, hyphen-separated: `ledger-core`, `kestrel-node-images`.
- Prefix with the system name, not the team name. Teams change; systems persist.
- No `-new`, `-v2`, or `-final` suffixes. If you're rebuilding something, give it a real name.

## Required files

| File | Purpose |
|---|---|
| `README.md` | What it is, how to run it locally, who owns it |
| `CODEOWNERS` | Teams responsible for each path |
| `gatekeeper.yaml` | Pipeline definition (for deployable services) |
| `.depbot.yaml` | Dependency bot config (optional) |

## CODEOWNERS

- Use GitHub teams, not individual usernames: `@techsync/srch`.
- Cover every path. A catch-all line at the top is fine.
- Keep it current when ownership moves.

## Branches

- Default branch is `main`.
- Short-lived feature branches. Delete after merge (GitHub does this automatically).
- No long-lived release branches; releases are tracked in Ship.

## Branch protection

Branch protection on `main` is managed centrally by Developer Tooling and synced nightly. Don't change it by hand. It requires passing Gatekeeper CI checks, CODEOWNERS review, and a linear history.

## Archiving

Archive repositories you no longer use. Archived repos are read-only and their alert rules and dashboards are cleaned up automatically.

## Visibility

All repos are internal by default. Public repos (open-source releases) need approval through the open-source process run by AppSec.
