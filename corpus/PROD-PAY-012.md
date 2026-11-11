doc_id: PROD-PAY-012
title: Ledger Core PostgreSQL Migration Playbook
doc_type: runbook
scope_level: team
owner_team: PAY
owner_org: PROD
author_role: Tech Lead
status: approved
last_updated: 2025-11-26
supersedes:
fact_ids: 

---

# Ledger Core PostgreSQL Migration Playbook

**Owner:** Tech Lead, Payments

## Principles

Never take Ledger Core offline for a database change. Every migration should be reversible, observable and small.

## The expand and contract pattern

1. **Expand:** add new columns, tables or indexes in a way that old code still works.
2. **Migrate:** backfill data in batches and deploy code that writes to both old and new structures.
3. **Switch:** change reads to the new structure.
4. **Contract:** after a stable period, remove the old structure.

## Practical rules

- Add columns as nullable; set defaults in a later step.
- Create indexes with `CONCURRENTLY`.
- Backfill in batches of 10,000 rows with a pause between batches.
- Use lock timeouts so that a migration never blocks traffic.
- Test on a staging copy that is at least as large as production.

## Before running

- [ ] Migration reviewed by a second engineer.
- [ ] Rollback script written and tested.
- [ ] Dashboards open for lock waits, replication lag and error rates.

## During

Run during a low-traffic period, watch the dashboards, and stop at the first sign of trouble.

## After

Record the migration in the change log and delete temporary scripts.
