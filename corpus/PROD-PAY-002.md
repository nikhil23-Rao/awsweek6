doc_id: PROD-PAY-002
title: Ledger Core Service Credentials Runbook
doc_type: runbook
scope_level: team
owner_team: PAY
owner_org: PROD
author_role: SRE
status: unmarked
last_updated: 2024-08-06
supersedes:
fact_ids: F-POL-07; F-PROD-003

---

# Ledger Core Service Credentials Runbook

**Team:** Payments  **Audience:** SREs and engineers who operate Ledger Core

## Scope

This runbook covers the service API keys that Ledger Core uses to call internal services and external payment providers.

## Where keys live

Keys are stored in Vaultline. Applications read them at start-up through the secrets sidecar. No key should appear in code, environment files or tickets.

## Rotation schedule

**Ledger Core service API keys rotate every 180 days.** The rotation calendar is kept in the Payments on-call handbook, and a reminder is created in Jira 14 days before each rotation.

## Rotation steps

1. Create a new key version in Vaultline with the same permissions as the current one.
2. Deploy the new version to staging and run the integration tests.
3. Roll the new version to production one instance at a time.
4. Watch error rates for 30 minutes.
5. Disable the old key version, and delete it after seven days if nothing has failed.
6. Record the rotation in the credentials log.

## If a key is exposed

Rotate it immediately, outside the calendar, and tell the security team. Review access logs for the period the key was exposed.

## Checks

After each rotation, confirm that both Ledger Core and Meterflow report healthy and that billing jobs ran on schedule.

## Contacts

Payments on-call engineer; AppSec for questions about Vaultline.
