No

---

## doc\_id: PLAT-DEVT-015 title: Gatekeeper CI Deployment Stages Reference doc\_type: reference scope\_level: team owner\_team: DEVT owner\_org: PLAT author\_role: Tech Lead status: approved last\_updated: 2026-07-09 supersedes: "" fact\_ids: F-PLAT-005

# Gatekeeper CI Deployment Stages Reference

Developer Tooling, Gatekeeper CI team

This page describes what happens, stage by stage, when Gatekeeper CI deploys a service to production. It is the reference for how the deploy pipeline behaves today. If you are writing a pipeline file, also see the *Gatekeeper CI Pipeline YAML Reference*.

## Stage overview

| \# | Stage | What happens | Gate to proceed |
| :---- | :---- | :---- | :---- |
| 1 | Build | Forge runners build the image from the commit. | Build succeeds |
| 2 | Test | Unit and integration tests. | All required checks pass |
| 3 | Scan | Sentinel scans the image and dependencies. | No blocking findings |
| 4 | Deploy dev | Rollout to dev. | Health checks pass |
| 5 | Deploy staging | Rollout to staging. | Health checks and any team-defined soak |
| 6 | Prod canary | New version receives a slice of prod traffic. | Automated analysis passes |
| 7 | Prod rollout | Remaining prod pods updated in waves. | Wave health checks |
| 8 | Post-deploy | Release recorded in Ship; notifications sent. | — |

## Prod canary (stage 6\)

- The canary receives **5% of production traffic**.  
- It runs for **15 minutes**.  
- Gatekeeper CI compares the canary against the baseline on error rate, p50/p99 latency, and saturation, using metrics from Lookout.  
- If analysis fails at any point, Gatekeeper CI routes all traffic back to the baseline and marks the deploy failed. No human action is needed for the automatic rollback.

These canary settings apply to every service deployed through Gatekeeper CI and aren't configurable per pipeline.

## Prod rollout (stage 7\)

After a passing canary, pods are updated in waves of 25%. Each wave waits for readiness probes and two minutes of healthy metrics before the next wave starts.

## Manual approval

Pipelines can add a `manual_approval` gate before stage 6\. Approvals can be granted in Console or from TechSync Mobile.

## Where to look when something fails

- Canary failures: the deploy page in Console shows the metric that failed analysis.  
- Wave failures: check pod events in Kestrel and the service's Lookout dashboard.  
- See the *Gatekeeper CI Troubleshooting FAQ* for common errors.