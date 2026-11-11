doc_id: DSEC-SEC-015
title: Vaultline Policy-as-Code Conventions
doc_type: standard
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Tech Lead
status: draft
last_updated: 2026-09-02
supersedes:
fact_ids:

# Vaultline Policy-as-Code Conventions (DRAFT)

**Status: first draft for SEC review.** Comments welcome in the document or in the SEC channel.

## Purpose

Vaultline mounts, policies, and auth roles are managed with Terraform in the policy-as-code repository. These conventions keep that repository consistent as more teams add to it.

## Repository layout

```
vaultline-policy/
  mounts/
    <team>/<service>.tf
  policies/
    <team>/<service>-read.hcl
    <team>/<service>-write.hcl
  roles/
    <team>/<service>.tf
```

## Naming

- Mount paths follow `<team>/<service>/`.
- Policy files are named `<service>-read.hcl` and `<service>-write.hcl`.
- Auth roles use the service account name.

## Policy guidelines

1. Prefer explicit paths to wildcards.
2. Split read and write policies.
3. One policy per service.
4. Add a comment at the top of each policy file naming the owner team and the channel.

## Review

- Each pull request needs approval from a Security Engineer.
- The reviewer checks that paths match the team's namespace and that no policy grants access to another team's secrets.
- CI runs lint checks for naming, wildcard usage, and missing owner comments.

## Applying

Merge to main triggers the pipeline. Applies to dev and staging are automatic; prod applies need the SEC tech lead's approval.

## Open questions

1. Should wildcard use require an exception ticket?
2. Do we want separate repositories per org?
3. How should we handle emergency access changes?
