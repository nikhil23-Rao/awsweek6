doc_id: DSEC-SEC-004
title: Vaultline Dynamic Secrets Runbook
doc_type: runbook
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Security Engineer
status: approved
last_updated: 2026-06-16
supersedes:
fact_ids: F-DSEC-002

# Vaultline Dynamic Secrets Runbook

**Owner:** AppSec (SEC), which owns and operates Vaultline.

## 1. What dynamic secrets are

Vaultline can mint short-lived credentials on demand for databases, cloud roles, and internal services. A workload asks for a credential, receives it with a lease, and Vaultline revokes it automatically when the lease ends.

## 2. Lease limits

**Vaultline dynamic secrets have a maximum lease of 1 hour.**

| Setting | Value |
|---|---|
| Default lease | 15 minutes |
| Maximum lease | 1 hour |
| Renewal | Allowed until the 1-hour ceiling is reached |
| After the ceiling | Workload must request a new credential |

The maximum is enforced by Vaultline itself. A role configured with a longer value in Terraform is capped at 1 hour when credentials are issued, and the pipeline lint will fail the change.

## 3. Requesting dynamic credentials

1. Create a Vaultline role for the target engine through the policy-as-code repo.
2. Bind the role to the workload's Kestrel service account.
3. Have the workload call the credential endpoint at startup and again before the lease expires.
4. Log the lease ID with each request to make revocation and audit traceable.

## 4. Troubleshooting

- **Lease expired errors:** the workload held the credential longer than its lease. Add a renewal timer at about two-thirds of the lease.
- **Renewal denied:** the 1-hour ceiling was reached. Request a new credential instead of renewing.
- **Permission denied on request:** check the role binding and the namespace of the service account.
- **Credentials revoked early:** an operator may have revoked the lease; check the Vaultline audit log.

## 5. Manual revocation

Security Engineers can revoke all leases for a role with `vaultline lease revoke -prefix <role>`. Announce in the SEC channel before running it in prod.

## 6. Escalation

Page the SEC on-call through Lookout for Vaultline unavailability.
