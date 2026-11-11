---
doc_id: PLAT-COMP-009
title: Kestrel Namespace Provisioning Runbook
doc_type: runbook
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2026-06-18
supersedes: PLAT-COMP-008
fact_ids: "F-PLAT-001; F-PLAT-006"
---

# Kestrel Namespace Provisioning Runbook

**Owner:** Compute (COMP) · **Audience:** any team onboarding a new service or a new team to Kestrel · **On-call contact:** #comp-oncall

## Purpose

This runbook covers how a team gets a home on Kestrel, TechSync's internal Kubernetes platform on EKS. Every service at TechSync runs inside a Kestrel namespace. If you are standing up a brand-new team or launching your first service, this is where you start.

Compute owns this process end to end. Please don't create namespaces by hand with `kubectl` or by copying another team's Terraform; namespaces created outside this flow are missing quota, network policy, and cost tags, and they get cleaned up by the weekly reconciler.

## Before you start

You will need:

- A team code (for example `WEB`, `DATA`) and the engineering manager's approval on the request ticket.
- A cost-allocation tag. See the *Kestrel Namespace Naming and Labeling Conventions* doc for the required labels.
- At least one service scaffolded with Scaffold, or a plan to do so in the first sprint.

## Step 1: File the request

Open a Jira ticket in the **COMP** project using the *New Kestrel Namespace* template. Fill in:

| Field | Example |
|---|---|
| Team code | `SRCH` |
| Namespace name | `srch-quarry` |
| Environments | dev, staging, prod |
| Expected services | Quarry query API, Quarry workers |
| Owning manager | Engineering Manager, Search |

Tickets are triaged by the COMP on-call within two business days.

## Step 2: What you get by default

When the namespace is created, Compute applies the standard team baseline:

- **40 CPU cores** of request quota per new team namespace, in each environment.
- A matching memory quota, sized by the reconciler from the CPU quota.
- Default network policies (deny-all ingress, allow from Meridian Mesh sidecars and EdgeGate).
- Lookout alert routing to the team's PagerDuty service.
- Tracewell collector injection.

Most teams run comfortably inside the default for their first two or three quarters.

## Step 3: Requesting more capacity

Quota increases go through a ticket to COMP. Use the *Kestrel Quota Increase* template in the COMP Jira project and include:

1. The namespace and environment.
2. The new CPU and memory totals you are asking for.
3. A link to a Lookout dashboard showing current utilization (we look for sustained usage above roughly 70% of quota).
4. Whether the need is permanent or tied to a launch or migration.

Please don't ask in Slack for a quota bump and don't edit the `ResourceQuota` object directly. Manual edits are reverted by the reconciler within the hour, and the ticket is how we keep capacity planning honest across all three orgs.

## Step 4: Verify

Once the ticket is resolved, confirm:

```
scaffold ns describe <namespace> --env prod
```

You should see the quota, network policies, and labels listed. Deploy your first service through Gatekeeper CI and confirm it schedules.

## Troubleshooting

- **Pods stuck in `Pending` with "exceeded quota":** you've hit the namespace quota. File a quota increase ticket (Step 3).
- **Namespace missing labels:** re-run the request; the reconciler will repair labels but not cost tags.
- **Need a namespace for a short-lived experiment:** use the dev environment only and mark the ticket "experimental."

## Revision history

- 2026-06-18: Refreshed templates and the verification command for the current Scaffold CLI.
- 2025-09-03: Added memory-quota sizing note.
