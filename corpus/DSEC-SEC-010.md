doc_id: DSEC-SEC-010
title: Sentinel and Gatekeeper CI Integration
doc_type: guide
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Tech Lead
status: approved
last_updated: 2026-05-26
supersedes:
fact_ids:

# Sentinel and Gatekeeper CI Integration

How the `sentinel-scan` stage is wired into a Gatekeeper CI pipeline, and how to troubleshoot it. Read this if you are adding the stage to a repository that was not created from a Scaffold template, or if the stage misbehaves.

## Pipeline overview

A repository's pipeline is defined in `pipeline.yaml`. Stages run on Forge runners in the order given. The Sentinel stage sits after the build and before the deploy stages.

```yaml
stages:
  - build
  - test
  - sentinel-scan
  - package
  - deploy-staging
  - deploy-prod
```

## Adding the stage

1. Add `sentinel-scan` to `pipeline.yaml` using the snippet from the Scaffold template.
2. Make sure the repository has lockfiles committed. The stage reads them to resolve dependencies.
3. Set the service's owner team in the `CODEOWNERS` file so findings are routed.
4. Run the pipeline in a branch and confirm the stage reports a result.

## Reading the result

The stage outputs a summary with finding counts by severity and a link to the detailed report in Sentinel. The same summary is posted to the pull request.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Stage times out | Large dependency tree or a busy queue | Retry once; if it repeats, ask SEC about runner capacity |
| "No lockfile found" | Lockfile not committed | Commit the lockfile |
| Stage passes but no summary appears | Missing permissions for the comment bot | Check the repository's app installation |
| Unexpected finding on unchanged code | Rule update | Check the rule changelog in `sentinel-rules` |
| Stage cannot reach Sentinel | Network policy | Check egress to the Sentinel service in Meridian Mesh |

## Runner and cache tips

- Use the shared dependency cache to speed up resolution.
- Do not install your own scanner; use the stage.
- Pin the stage version only if you have a reason; the default tracks the latest tested version.

## Who owns what

- SEC owns the Sentinel service and the stage's behavior.
- DEVT owns Gatekeeper CI and the pipeline framework.
- Service owners own their pipeline file and the findings in it.

## Getting help

The SEC channel for scanner questions, and the DEVT channel for pipeline questions.
