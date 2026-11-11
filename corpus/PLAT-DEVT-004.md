---
doc_id: PLAT-DEVT-004
title: Developer Tooling Team Charter
doc_type: team charter
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: Engineering Manager
status: approved
last_updated: 2025-01-21
supersedes: ""
fact_ids: ""
---

# Developer Tooling Team Charter

**Team:** Developer Tooling (DEVT), Platform Engineering
**Engineering manager:** Hannah Brecker
**Tech lead:** Ravi Subramanian

## Mission

Make the path from idea to production short, safe, and the same for everyone.

## Systems we own

- **Scaffold**: service templates and the `scaffold` CLI.
- **Gatekeeper CI**: the build, test, and deploy pipeline.
- **GitHub Enterprise administration**: org settings, branch protection sync, and repository conventions.
- **The dependency update bot.**
- **Company code review policy.**

## What we don't own

- **Build machines**: Forge runners belong to Compute.
- **Release records**: TechSync Ship is a Product Engineering product; we're its biggest internal customer.
- **Security scanning rules**: Sentinel belongs to AppSec. We run it in the pipeline.

## How to reach us

- #devt-help for general questions; #devt-gatekeeper and #devt-scaffold for specific tools.
- DEVT Jira project for requests.
- Page the DEVT on-call if pipelines are broken for many teams.

## 2025 goals

1. Every service on Gatekeeper CI with a Scaffold-compatible layout.
2. Median merge-to-prod time under 30 minutes.
3. Flaky test rate below 1% of runs.
4. `scaffold upgrade` adopted by at least half of services.

## Rituals

- Weekly planning, Monday.
- Gatekeeper CI working group, every other week, open to all orgs.
- Quarterly developer survey.
