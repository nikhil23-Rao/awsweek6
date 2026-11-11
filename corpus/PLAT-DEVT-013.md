---
doc_id: PLAT-DEVT-013
title: "Build and Deploy Pipeline Guide: Ship, Gatekeeper CI, and Forge"
doc_type: guide
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: Tech Lead
status: approved
last_updated: 2026-05-27
supersedes: ""
fact_ids: F-PLAT-002
---

# Build and Deploy Pipeline Guide: Ship, Gatekeeper CI, and Forge

**Owner:** Developer Tooling (DEVT)
**Applies to:** every team at TechSync that builds or deploys software

## The short version

All builds and deploys at TechSync run through **TechSync Ship** and **Gatekeeper CI**. Jenkins was retired in May 2026, and the last Jenkins controllers were shut down that month. There is no other supported path to dev, staging, or prod.

## How the pieces fit together

**TechSync Ship** is our release orchestration product, and we use it internally too. Ship is the system of record for releases: what version of what service is running where, who approved it, and what changed.

**Gatekeeper CI** is the deploy pipeline. It reads the pipeline file in your repo, runs build, test, scan, and deploy stages, and enforces the gates (tests, Sentinel scans, approvals, canary analysis).

**Forge** is the fleet of build runners, owned by Compute. Gatekeeper CI schedules build and test jobs onto Forge runners. You don't interact with Forge directly unless you're debugging a runner problem.

```
git push → Gatekeeper CI pipeline → Forge runners (build/test) → Kestrel (dev → staging → prod) → recorded in Ship
```

## Getting a service onto the pipeline

New services created with Scaffold come with a Gatekeeper CI pipeline file already. For an existing service without one:

1. Run `scaffold pipeline init` in the repo root.
2. Review the generated `gatekeeper.yaml`. Set the service name, Kestrel namespace, and any team-specific gates.
3. Open a PR. The first pipeline run happens on the PR itself (build and test only).
4. Merge. Gatekeeper CI registers the service in Ship and deploys to dev.

## Deploying

Deploys happen automatically on merge to `main` through dev and staging. Promotion to prod is automatic unless your pipeline has a manual approval gate. You can watch progress in Console under **Releases**, or approve from TechSync Mobile.

## Rolling back

Use Ship's rollback, which redeploys the previous release artifact through Gatekeeper CI:

```
ship rollback <service> --env prod
```

or click **Roll back** on the release page in Console. Rollbacks go through the same health checks as a forward deploy, skipping the canary.

## Secrets, config, and environment variables

Declare them in the service manifest. Gatekeeper CI injects them at deploy time. Don't put credentials in pipeline files.

## FAQ

**Can I run a one-off script against prod?** Use a Gatekeeper CI `job` stage so it is logged in Ship. Ad hoc scripts from laptops aren't permitted.

**My old pipeline config still exists in the repo. Do I need it?** Delete any leftover CI configuration that isn't `gatekeeper.yaml`. It isn't read by anything.

**Who do I ask?** #devt-gatekeeper, or the DEVT on-call.
