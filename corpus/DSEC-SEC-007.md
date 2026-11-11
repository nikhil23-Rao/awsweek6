doc_id: DSEC-SEC-007
title: Vaultline Secrets Engine Setup Guide
doc_type: guide
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Tech Lead
status: approved
last_updated: 2025-09-23
supersedes:
fact_ids:

# Vaultline Secrets Engine Setup Guide

This guide shows how to mount a secrets engine in Vaultline for a new team or service. It is aimed at engineers who have never done this before.

## Concepts in one minute

- **Secrets engine:** a plugin that stores or generates a type of secret.
- **Mount path:** where the engine lives, such as `kv/payments/`.
- **Policy:** a set of permissions bound to paths.
- **Auth method:** how a workload proves who it is. At TechSync, workloads authenticate with their Kestrel service account.

## Choosing an engine

| Need | Engine |
|---|---|
| Static values such as API keys | KV (version 2) |
| Database access | Database engine |
| TLS certificates | PKI |
| Cloud permissions | AWS engine |

## Setup steps

1. **Pick a path.** Use `<team>/<service>/`.
2. **Write the Terraform.** Add a mount and a policy file to the policy-as-code repo.
3. **Open a pull request.** A SEC engineer reviews paths and permissions.
4. **Apply.** After merge, the pipeline mounts the engine.
5. **Bind the auth role.** Link your service account's namespace to the policy.
6. **Test.** From a pod in dev, read a test value.

## Policy basics

- Grant the minimum paths and capabilities the workload needs.
- Separate read and write policies.
- Use one policy per service, not per person.

## Audit

Vaultline logs every request to the audit log. Teams can export audit events through the audit export guide.

## Common mistakes

- Using the root path for application secrets.
- Sharing one policy across unrelated services.
- Copying a secret into an environment variable file.

## Help

SEC channel in Slack; for outages, page the SEC on-call.
