doc_id: PROD-PAY-011
title: Payment Reconciliation Job Troubleshooting
doc_type: runbook
scope_level: team
owner_team: PAY
owner_org: PROD
author_role: SRE
status: approved
last_updated: 2026-05-14
supersedes:
fact_ids: 

---

# Payment Reconciliation Job Troubleshooting

**Team:** Payments  **Audience:** on-call engineers

## What reconciliation does

Every night, the reconciliation job compares usage received by Meterflow with usage counted in Ledger Core, and compares invoices against payment provider records. It reports differences.

## Reading the report

The job writes a summary to the `#prod-payments-recon` channel:

- **Matched:** counts agree.
- **Unmatched usage:** Ledger Core has usage that Meterflow does not.
- **Unmatched payments:** a payment exists with no matching invoice, or the reverse.

## Common failures

| Symptom | Likely cause | Action |
|---|---|---|
| Job did not run | Scheduler issue | Check the scheduler; rerun the job |
| Job timed out | Large backlog after an incident | Rerun with a smaller date range |
| Many unmatched payments | Provider settlement delay | Wait a day and rerun |
| A few unmatched usage rows | Late events | Check the correction queue |

## Rerunning

```
reconcile --date 2026-05-10 --customer-batch 1
```

Reruns are safe and do not change data; they only recompute the report.

## Escalating

If differences persist after two reruns, open a ticket in the Payments queue and tag the Staff Engineer. For possible customer impact, page the on-call engineer.
