---
doc_id: ORG-PLAT-018
title: Platform Engineering Release Standard
doc_type: standard
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-06-11
supersedes: ""
fact_ids: F-PLAT-004
---

# Platform Engineering Release Standard

**Scope:** every service and system owned by a Platform Engineering team (Compute, Networking, Observability, Developer Tooling)
**Owner:** Platform Engineering leadership, maintained by the Platform staff engineers

## Why we have this standard

Platform systems sit underneath everything else. When Kestrel, Meridian Mesh, EdgeGate, Lookout, or Gatekeeper CI has a bad release, every product team feels it at once. This standard sets the minimum bar for how Platform-owned services move to production. Teams can add stricter steps of their own.

## Requirements

### 1. Release through Gatekeeper CI

All Platform releases run through Gatekeeper CI. No manual `kubectl apply` or console changes to production.

### 2. Staging before prod

Every release deploys to staging before prod. Staging must run the same build artifact, not a rebuild.

### 3. Staging soak

Each release must soak in staging for **at least 60 minutes** before promotion to prod. During the soak, the release owner confirms that error rate, latency, and saturation are within normal bounds on the service's Lookout dashboard. Sixty minutes is long enough to catch slow memory leaks, connection pool exhaustion, and certificate or token refresh failures that don't appear in the first few minutes.

### 4. Progressive rollout in prod

Roll out to a subset of prod capacity first (a cell, a canary, or a single cluster), verify health, then expand.

### 5. Rollback plan

Every release has a tested rollback path that can complete in under 15 minutes. If a release includes a schema or config migration that can't be rolled back, say so in the release ticket and get a second Platform engineer to review it.

### 6. Announce

Post the release in the owning team's release channel and in #platform-releases.

## Exceptions

Exceptions to this standard must be approved in writing by the VP Platform Engineering and recorded in the Platform exceptions register on Confluence. An exception names the specific systems and the time period it covers.

## Review

This standard is reviewed annually by the Platform staff engineers.
