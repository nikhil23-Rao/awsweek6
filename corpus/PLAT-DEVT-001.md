---
doc_id: PLAT-DEVT-001
title: Dependency Update Bot Guide
doc_type: how-to guide
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-12-09
supersedes: ""
fact_ids: ""
---

# Dependency Update Bot Guide

Developer Tooling

The dependency update bot opens pull requests to keep your third-party libraries current. Keeping dependencies fresh makes security fixes cheap: a one-line bump instead of a painful multi-version jump during an emergency.

## What it does

- Scans every repository with a supported manifest: `go.mod`, `requirements.txt` and `pyproject.toml`, `package.json`, Gradle files, and Terraform provider versions.
- Opens PRs for new versions on a weekly schedule (Tuesday mornings PT).
- Opens PRs immediately when Sentinel flags a vulnerable version.

## Grouping

To avoid PR floods, updates are grouped:

| Group | Contents |
|---|---|
| `minor-and-patch` | All non-major updates in one PR per ecosystem |
| `major-<package>` | One PR per major version bump |
| `security` | Vulnerability fixes, never grouped with anything else |

## Configuring it

Add `.depbot.yaml` to your repo root:

```yaml
schedule: weekly
ignore:
  - package: "github.com/legacy/thing"
    reason: "Pinned until SRCH-1220 is done"
groups:
  aws-sdk:
    patterns: ["github.com/aws/aws-sdk-go-v2/*"]
```

Every `ignore` entry needs a reason.

## Reviewing bot PRs

- Gatekeeper CI runs your full test suite on every bot PR.
- Read the changelog link in the PR description for major bumps.
- Bot PRs go through normal review; the bot account can't approve or merge anything.

## Auto-close

Bot PRs that sit unmerged for 30 days are closed and reopened on the next run with the latest version.

## Help

#devt-help
