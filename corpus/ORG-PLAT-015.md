---
doc_id: ORG-PLAT-015
title: Terraform Module Standards
doc_type: standard
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: Tech Lead
status: approved
last_updated: 2025-10-14
supersedes: ""
fact_ids: ""
---

# Terraform Module Standards

**Owner:** Platform tech leads

All Platform infrastructure is defined in Terraform. These standards keep our modules consistent and safe to reuse.

## Repository layout

```
modules/
  kestrel-cluster/
  edgegate-cell/
  vpc/
live/
  us-east-1/
  us-west-2/
  eu-west-1/
```

Modules are in `modules/`; environments that use them are in `live/`.

## Module structure

Each module has:

- `main.tf`, `variables.tf`, `outputs.tf`
- `versions.tf` pinning the Terraform and provider versions
- `README.md` with inputs, outputs, and an example
- Tests under `tests/` using `terraform test`

## Variables

- Every variable has a `description` and a `type`.
- Avoid defaults for anything environment-specific.
- Validate inputs with `validation` blocks where it prevents mistakes.

## Versioning

Modules are versioned with Git tags (`kestrel-cluster/v3.2.0`). `live/` configs pin a module version. Breaking changes bump the major version.

## Tags

Modules apply the required cost-allocation tags from their inputs. Don't add tags by hand in `live/`.

## State

Remote state in S3 with DynamoDB locking, one state file per environment per stack. Never edit state by hand; use `terraform state` commands and record what you did in the ticket.

## Review

Every Terraform PR shows the plan output in Gatekeeper CI. Reviewers read the plan, not just the code.

## Drift

A nightly job runs `terraform plan` on every stack and reports drift in #platform-drift.
