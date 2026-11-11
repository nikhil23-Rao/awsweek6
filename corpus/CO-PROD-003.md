doc_id: CO-PROD-003
title: Product Overview: TechSync Ledger
doc_type: product overview
scope_level: company
owner_team: Technical Writing
owner_org: PROD
author_role: Technical Writer
status: approved
last_updated: 2026-07-20
supersedes:
fact_ids:

---

# Product Overview: TechSync Ledger

**Launched:** 2021
**Category:** Usage metering and billing

## The problem Ledger solves

Companies that charge by usage need two things to be right: an accurate count of what each customer used, and a bill that reflects that count. Ledger does both. It collects usage events, aggregates them into billable quantities, and turns those quantities into invoices.

## Components

Ledger is made of two main pieces:

1. **Meterflow** receives usage events from your products, de-duplicates them, and rolls them up into hourly and daily totals.
2. **Ledger Core** is the billing engine. It applies pricing plans, computes charges, and produces invoices for each billing period.

## Highlights

- Flexible pricing plans, including tiered, volume and flat-plus-overage models.
- Usage exports so that customers can reconcile their own records.
- Plan changes that take effect mid-period, with prorated charges calculated for you.
- A public API for reading usage and billing data.
- Alerts for billing events can be delivered through other TechSync products.

## Audience

Finance teams use Ledger to understand revenue; product teams use it to understand consumption; engineering teams integrate it into the services that emit usage. Ledger is offered on all three customer tiers, with limits that vary by tier as described in your order form.

## Further reading

The Ledger public API documentation, the Meterflow export FAQ, and the Product Engineering directory are the best next stops.
