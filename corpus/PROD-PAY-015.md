doc_id: PROD-PAY-015
title: Ledger Core Tax Rate Table Update Procedure
doc_type: runbook
scope_level: team
owner_team: PAY
owner_org: PROD
author_role: Tech Lead
status: approved
last_updated: 2026-04-15
supersedes:
fact_ids: 

---

# Ledger Core Tax Rate Table Update Procedure

**Owner:** Tech Lead, Payments  **Frequency:** quarterly

## Background

Ledger Core calculates tax using a table of rates by jurisdiction. Rates change; we update the table each quarter, effective the first day of the quarter.

## Timeline

| When | Step |
|---|---|
| Six weeks before | Finance supplies the new rates file |
| Five weeks before | Engineer loads the file into staging and runs validation |
| Four weeks before | Finance reviews staging results |
| Two weeks before | Load into production with an effective date |
| Quarter start | New rates take effect automatically |

## Steps

1. Download the rates file from the shared finance folder and verify the checksum.
2. Run the validation script:
   ```
   taxctl validate --file rates-2026Q4.csv
   ```
3. Review the diff report. Large changes should be explained by Finance.
4. Load into staging with `taxctl load --env staging`.
5. Compare sample invoices before and after.
6. After approval, load into production.

## Rollback

Production loads are versioned. Roll back with `taxctl activate --version <previous>`, effective immediately for future calculations.

## Records

Save the validation report, the diff and the approvals in the quarter's folder.
