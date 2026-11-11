---
doc_id: PLAT-DEVT-006
title: Scaffold Service Template Guide
doc_type: guide
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2026-02-18
supersedes: ""
fact_ids: F-PLAT-003
---

# Scaffold Service Template Guide

Developer Tooling (DEVT)

Scaffold is how you start a new service at TechSync. Run one command and you get a repository with a working service, a Gatekeeper CI pipeline, Kestrel manifests, dashboards, and Tracewell instrumentation already wired up. This guide explains what each template generates so you know what you're inheriting.

## Choosing a template

| Template | Language | Use it for |
|---|---|---|
| `go-grpc` | Go | Internal gRPC services |
| `go-http` | Go | HTTP APIs behind EdgeGate |
| `py-worker` | Python | Kafka consumers on Streamline, batch jobs |
| `ts-bff` | TypeScript | Backends-for-frontends serving Console |
| `kotlin-service` | Kotlin | JVM services (mostly Payments) |

```
scaffold new --template go-http --name ledger-exports --team PAY
```

## What gets generated

**Code.** A minimal service with health checks (`/healthz`, `/readyz`), structured logging, and a graceful-shutdown handler.

**Kestrel manifests.** Deployment, Service, HorizontalPodAutoscaler, PodDisruptionBudget, and a service account. Resource requests start small; tune them after your first load test.

**Mesh settings.** Templates don't set a route timeout. Services inherit the Meridian Mesh default request timeout of 30 seconds, which suits nearly every API we run. If one of your routes legitimately takes longer (large exports, report generation), add an override in `mesh.yaml`.

**Pipeline.** A Gatekeeper CI pipeline file with build, test, image scan, and deploy stages for dev, staging, and prod.

**Observability.** A Lookout dashboard with the standard panels and a starter set of alerts, plus Tracewell SDK setup.

## After scaffolding

1. Push the repo and confirm the first pipeline run is green.
2. Ask your team's on-call lead to review the starter alerts.
3. Delete anything the template generated that you don't need. Unused alerts are worse than none.

## Updating an existing service

Templates evolve. Run `scaffold upgrade` to see a diff between your service and the current template version. Upgrades are never applied automatically.

## Getting help

#devt-scaffold, or file a ticket in the DEVT Jira project.
