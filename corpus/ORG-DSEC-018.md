doc_id: ORG-DSEC-018
title: DSEC Terraform Module Conventions
doc_type: standard
scope_level: org
owner_team: none (DSEC org-wide)
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2025-10-28
supersedes:
fact_ids:

# DSEC Terraform Module Conventions

DSEC teams manage their infrastructure with Terraform. These conventions keep modules readable and reusable across the four teams.

## 1. Repository layout

```
modules/
  <module-name>/
    main.tf
    variables.tf
    outputs.tf
    README.md
environments/
  dev/
  staging/
  prod/
```

Each environment folder contains only module calls and environment-specific values.

## 2. Naming

- Resources use `snake_case` names that describe their role: `reservoir_raw_bucket`, not `bucket1`.
- Variables and outputs are described in `variables.tf` and `outputs.tf`; every one has a description.
- Module names are nouns: `kafka_topic`, `s3_bucket`, `keystone_app`.

## 3. Versioning

Modules are versioned with tags (`v1.2.0`). Environments pin a version. Breaking changes bump the major version and are announced in the DSEC channel.

## 4. State

State lives in S3 with locking, one state per environment per component. Never share a state file between teams.

## 5. Secrets

Do not put secrets in variables or in version control. Reference them through the Vaultline data sources and mark sensitive outputs as `sensitive`.

## 6. Review and apply

1. Open a pull request. CI runs `terraform fmt`, `validate`, and `plan`.
2. A teammate reviews the plan output, not just the code.
3. Apply to dev and staging from the pipeline. Prod applies require approval from the team's tech lead.

## 7. Tags

Every resource carries `owner_team`, `service`, and `environment` tags so costs and ownership are visible.

## 8. Deprecating modules

Announce at least one release cycle ahead and keep the old version available for that time.
