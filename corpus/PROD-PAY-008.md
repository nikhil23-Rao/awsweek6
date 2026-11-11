doc_id: PROD-PAY-008
title: Ledger Core Invoice Finalization Runbook
doc_type: runbook
scope_level: team
owner_team: PAY
owner_org: PROD
author_role: SRE
status: approved
last_updated: 2026-01-12
supersedes:
fact_ids: 

---

# Ledger Core Invoice Finalization Runbook

**Team:** Payments  **Audience:** on-call engineers and finance operations

## What finalization does

At the end of each billing period, Ledger Core locks the period's usage, applies pricing, and produces a final invoice. After finalization, an invoice can only change through a credit note.

## Timing

**Invoices finalize 3 days after the billing period ends.** This leaves time for late usage events to arrive and for customers' disputes to be raised before invoices are locked.

## Daily job

The finalization job runs at 02:00 UTC. It selects billing periods that ended exactly three days earlier.

## Checks before finalizing

1. Meterflow reports all windows for the period as final.
2. Reconciliation shows no unresolved differences.
3. Pricing plan versions for the period are unchanged.

## If the job fails

- Check the job log for the first error.
- Fix the cause and rerun the job; it is safe to rerun, as finalization is idempotent.
- If more than one hour passes, tell the finance operations channel.

## Manual finalization

Requires approval from the Payments Engineering Manager. Run `ledgerctl finalize --period <id> --reason <ticket>` and record the ticket.

## After finalization

Invoices are published to customers and the archive. Confirm that the publication count matches the number of finalized invoices.
