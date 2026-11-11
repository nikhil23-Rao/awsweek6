---
doc_id: ORG-PLAT-005
title: Platform Cost Allocation and Tagging Standard
doc_type: standard
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-03-04
supersedes: ""
fact_ids: ""
---

# Platform Cost Allocation and Tagging Standard

**Scope:** all AWS resources created by or for Platform Engineering, and all Kestrel namespaces
**Owner:** Platform staff engineers, with Finance

## Why

TechSync's AWS bill is one of its largest costs. Finance and each VP need to see who is spending what. That only works if every resource is tagged consistently.

## Required AWS tags

Every taggable AWS resource created through Terraform must carry:

| Tag | Example | Notes |
|---|---|---|
| `techsync:team` | `COMP` | Team code |
| `techsync:org` | `PLAT` | `PLAT`, `PROD`, or `DSEC` |
| `techsync:cost-center` | `CC-4120` | From Finance |
| `techsync:system` | `kestrel` | The system the resource belongs to |
| `techsync:env` | `prod` | `dev`, `staging`, or `prod` |

The Platform Terraform modules add these automatically from module inputs.

## Kestrel namespaces

Namespaces carry the equivalent labels (see the Kestrel naming conventions). Kestrel costs are split across namespaces by requested CPU and memory, using the labels.

## Shared costs

Some costs are shared, like Kestrel control planes, EdgeGate, and Lookout. Those are allocated to Platform and then distributed to orgs monthly by a formula Finance publishes.

## Enforcement

- Terraform plans fail in Gatekeeper CI if required tags are missing.
- A weekly report lists untagged resources by account. Owning teams have two weeks to fix them.

## Reports

Monthly cost reports per team and per system are published by Finance in Confluence.
