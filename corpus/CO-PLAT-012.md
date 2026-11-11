---
doc_id: CO-PLAT-012
title: Incident Severity Definitions
doc_type: standard
scope_level: company
owner_team: SRE guild
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2024-02-27
supersedes: ""
fact_ids: ""
---

# Incident Severity Definitions

**Owner:** SRE guild
**Applies to:** all incidents at TechSync

Use these definitions to choose a severity when declaring an incident. When unsure between two levels, pick the higher one. You can lower it later.

## Sev1: Critical

A major customer-facing outage or a serious security or data event.

Examples:
- Ship, Ledger, Insight, or Console unavailable or failing for a large share of customers.
- Ledger producing incorrect invoices.
- Confirmed customer data exposure.
- A complete failure of paging (Lookout down).

## Sev2: Major

Significant degradation, or an outage affecting a subset of customers or a key internal system.

Examples:
- A product unavailable in one region.
- Major features failing for many customers.
- Deploys blocked company-wide.
- Logs and traces delayed for all teams.

## Sev3: Minor

Limited impact with a workaround available.

Examples:
- One non-critical feature failing.
- Elevated errors for a small number of customers.
- An internal tool down for one team.

## Sev4: Low

Minimal impact. Often found before anyone notices.

Examples:
- A cosmetic bug in Console.
- A failed batch job that can be rerun.

## Who declares

Anyone can declare an incident. The on-call for the affected system becomes the initial incident commander unless someone else takes command.

## Changing severity

The IC can raise or lower severity at any time. Record the change and the reason in the incident channel.
