doc_id: PROD-PAY-005
title: Ledger Core Architecture Decision Requirements
doc_type: policy
scope_level: team
owner_team: PAY
owner_org: PROD
author_role: Engineering Manager
status: approved
last_updated: 2026-03-12
supersedes:
fact_ids: F-POL-11; F-PROD-010

---

# Ledger Core Architecture Decision Requirements

**Owner:** Payments (PAY)  **Approved by:** Payments Engineering Manager and Tech Lead

## Purpose

Ledger Core produces invoices that customers pay and auditors read. Mistakes are expensive and hard to undo. For this reason, Payments records the reasoning behind important design choices in Architecture Decision Records (ADRs).

## Requirement

**An ADR is required for any change to the Ledger Core invoice schema or the Ledger public API, even when only the Payments team is affected.**

The ADR must be approved by the Payments Engineering Manager and the Payments Tech Lead before work starts.

## What the ADR should cover

- The change and why it is needed
- Impact on stored invoices and on customers' integrations
- Migration and rollback plan
- Tests that show the change is safe
- Effect on reports and exports

## Process

1. The author drafts the ADR in the architecture records space and tags both approvers.
2. Approvers review within three working days.
3. Once both approve, the ADR is marked Accepted and linked in the pull request.

## Out of scope

Changes that do not touch the invoice schema or the public API follow normal review.

## Review

This requirement is reviewed each March.
