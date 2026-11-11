---
doc_id: PLAT-DEVT-005
title: New Engineer Local Development Setup
doc_type: onboarding guide
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: Technical Writer
status: approved
last_updated: 2026-04-07
supersedes: ""
fact_ids: ""
---

# New Engineer Local Development Setup

*Technical Writing with Developer Tooling*

Welcome. This guide gets your laptop ready to build and run TechSync services. It should take about two hours.

## 1. Sign in

Your laptop arrives with Keystone SSO configured by IT & Compliance. Sign in, then open the self-service app catalog.

## 2. Install the toolchain

From the app catalog, install **TechSync Dev Tools**. It installs:

- Go, Python, and Node.js at the versions Forge uses
- Docker Desktop
- `kubectl`, configured for the Kestrel dev clusters
- The `scaffold` and `gatekeeper` CLIs
- Terraform

Check everything with:

```
scaffold doctor
```

## 3. GitHub Enterprise

1. Accept the GitHub invite in your email.
2. Ask your manager to add you to your team's GitHub team.
3. Set up an SSH key and commit signing (`scaffold doctor --fix-git` walks you through it).

## 4. Access to dev

You get the dev environment automatically through your team membership. You can deploy to dev and read dev logs and traces from day one.

## 5. Run a service locally

```
git clone git@github.techsync.io:techsync/scaffold-examples.git
cd scaffold-examples/go-http
make run
```

Visit `http://localhost:8080/healthz`.

## 6. Slack channels to join

- Your team channel
- #eng-announce
- #devt-help
- #incident-room (read-only is fine at first)

## Stuck?

Ask in #devt-help. Mention you're new; people are friendly.
