doc_id: PROD-PAY-007
title: Meterflow Aggregation Windows Reference
doc_type: reference
scope_level: team
owner_team: PAY
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-01-30
supersedes:
fact_ids: 

---

# Meterflow Aggregation Windows Reference

## Windows

Meterflow rolls up usage into fixed windows.

| Window | Boundary | Used for |
|---|---|---|
| Hourly | Top of the hour, UTC | Near-real-time dashboards |
| Daily | 00:00 UTC | Usage exports, daily summaries |
| Billing period | Customer's billing cycle | Invoices |

## Late events

Events can arrive after their window closes. Meterflow accepts late events for 48 hours and updates the affected window. After that, they go to a correction queue reviewed by the Payments team.

## Time zones

All windows are in UTC. Customers see their own time zone in the user interface, but windows are never shifted.

## Rounding

Quantities are stored as decimals with six places and rounded only when an invoice is produced.

## Querying

The aggregates API returns windows with `start`, `end`, `quantity` and a `final` flag. A window is final once its late-event period has passed.

## Common questions

**Why did the hourly total change?** A late event arrived within the 48-hour period.

**Why do daily totals differ slightly from the sum of hours?** They shouldn't; if they do, open a ticket with the customer ID and date.

## Owner

Meterflow Staff Engineer.
