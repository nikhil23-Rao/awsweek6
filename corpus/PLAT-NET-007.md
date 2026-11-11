---
doc_id: PLAT-NET-007
title: EdgeGate Route Onboarding Guide
doc_type: onboarding guide
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: Technical Writer
status: approved
last_updated: 2026-03-02
supersedes: ""
fact_ids: ""
---

# EdgeGate Route Onboarding Guide

*Written by Technical Writing with the Networking team*

This guide walks you through exposing a new API route to customers or to TechSync Mobile through EdgeGate.

## Before you begin

- Your service is running on Kestrel and reachable through Meridian Mesh.
- You know the public path, for example `/v2/insight/queries`.
- You've decided how the route is authenticated.

## Step 1: Add the route config

In your service repo, create `edgegate/routes.yaml`:

```yaml
- path: /v2/insight/queries
  methods: [GET, POST]
  upstream: srch-quarry/quarry-api
  auth: customer_token
  rate_limits: default
```

## Step 2: Choose authentication

| Option | When |
|---|---|
| `customer_token` | Customer API calls with a TechSync API token |
| `console_session` | Calls from the Console web app |
| `mobile_session` | Calls from TechSync Mobile |
| `none` | Public endpoints like health or status (rare; needs NET review) |

## Step 3: Open a PR

Gatekeeper CI validates the config: path conflicts, valid upstream, auth set. A NET engineer is auto-assigned as a reviewer for new routes.

## Step 4: Test in staging

Once merged, the route appears on the staging EdgeGate. Test with:

```
curl -H "Authorization: Bearer $STAGING_TOKEN" https://api.staging.techsync.io/v2/insight/queries
```

## Step 5: Promote

Promotion to prod happens through the normal Gatekeeper CI flow.

## Step 6: Document

Update the public API reference for customer-facing routes, and add the route to your service's runbook.

## Help

#net-edgegate, or file a ticket in the NET Jira project.
