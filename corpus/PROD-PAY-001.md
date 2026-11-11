doc_id: PROD-PAY-001
title: Ledger Invoice Data Handling and Classification
doc_type: policy
scope_level: team
owner_team: PAY
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-01-20
supersedes:
fact_ids: F-POL-15; F-PROD-002

---

# Ledger Invoice Data Handling and Classification

**Owner:** Payments (PAY)  **Applies to:** everyone with access to Ledger Core invoice records

## Classification

Ledger invoice data is classified **Restricted**. That includes invoice line items, billing contact details on an invoice, tax amounts, totals, payment status and the generated PDF of an invoice.

## Handling rules

1. **Access.** Only members of the Payments team and approved Finance Systems staff may read invoice data in production. Access is requested through the access portal and reviewed quarterly.
2. **Storage.** Invoice data is stored only in Ledger Core's encrypted databases and the invoice archive bucket. Do not copy invoice data into spreadsheets, tickets or chat.
3. **Transit.** Use only internal services and TLS when moving invoice data between systems.
4. **Test data.** Use generated sample invoices in development and staging. Production invoice data must not be loaded into non-production environments.
5. **Logs.** Never write full invoice contents to logs. Log the invoice ID and status only.
6. **Support.** Support staff see a masked view. Requests to see more go to the on-call Payments engineer.

## Exports

Customers can download their own invoices through Ledger. Internal exports require approval from the Payments Engineering Manager and are logged.

## Incidents

If invoice data may have been exposed, page the Payments on-call engineer and notify the security team immediately.

## Questions

#prod-payments, or the Payments Staff Engineer.
