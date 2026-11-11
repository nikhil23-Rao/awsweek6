---
doc_id: PLAT-OBS-003
title: Observability Team Charter
doc_type: team charter
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: Engineering Manager
status: approved
last_updated: 2025-02-10
supersedes: ""
fact_ids: ""
---

# Observability Team Charter

**Team:** Observability (OBS), Platform Engineering
**Engineering manager:** Ingrid Solheim
**Tech lead:** Kofi Mensah

## Mission

Help every engineer at TechSync know what their software is doing in production, and make sure the right person finds out fast when it misbehaves.

## Systems we own

- **Lookout**: alerting and paging. Evaluates alert rules against metrics and routes notifications to PagerDuty, Slack, and TechSync Mobile.
- **Tracewell**: the tracing and log pipeline. Collectors, sampling, storage, and the query interface.
- Shared **dashboard standards** and the standard dashboards Scaffold generates.

## What teams own themselves

- Their alert rules and thresholds (we provide tooling and review).
- Instrumentation in their own code (we provide the SDKs).
- Their on-call rotations and response.

## Relationship to TechSync Insight

Insight is TechSync's customer-facing observability product, built by Product Engineering. OBS runs the internal observability stack. We share ideas and some libraries, but they are separate systems with separate owners.

## How to reach us

- Questions: #obs-help, #obs-tracewell, #obs-lookout.
- Requests: OBS Jira project.
- Lookout or Tracewell outages: page the OBS on-call.

## 2025 goals

1. Tail-based sampling in Tracewell.
2. Alert rules as code for all teams.
3. Standard dashboards for every Scaffold service.
4. Cut OpenSearch spend per GB ingested by 20%.

## Disaster recovery owners

Primary: OBS tech lead. Backup: senior SRE on the OBS rotation.
