doc_id: PROD-WEB-002
title: Console Production Deploy Runbook
doc_type: runbook
scope_level: team
owner_team: WEB
owner_org: PROD
author_role: Tech Lead
status: unmarked
last_updated: 2025-06-17
supersedes:
fact_ids: F-PLAT-002

---

# Console Production Deploy Runbook

**Team:** WEB  **Audience:** engineers on the Console release rota

## Overview

Console is deployed to production by the `console-prod` Jenkins job. A deploy takes about twelve minutes end to end. Rollbacks are done with `jenkins-ctl`.

## Before you deploy

1. Confirm that the build you want has passed on the main branch and is green in staging.  
2. Check the on-call channel for any ongoing incident.  
3. Post in #prod-web that you are about to deploy.

## Deploying

1. Open Jenkins and find the job `console-prod`.  
2. Choose **Build with Parameters** and enter the release tag (for example `console-2025.06.3`).  
3. Leave `CANARY_PERCENT` at 10 unless the release notes say otherwise.  
4. Start the job and watch the console output. The job pauses after the canary stage.  
5. Check the error-rate and latency dashboards for five minutes. If they look normal, approve the pause to continue to full rollout.

## Rolling back

If the canary or full rollout misbehaves:

```
jenkins-ctl rollback console-prod --to previous
```

Wait for the job to report success, then confirm the dashboards recover. Post the result in #prod-web.

## After the deploy

- Update the release notes page with the deploy time and tag.  
- If you rolled back, open a ticket describing what happened.

## Troubleshooting

- **Job stuck at canary:** check that the canary pods are ready.  
- **`jenkins-ctl` cannot authenticate:** refresh your token from the Jenkins user page.
