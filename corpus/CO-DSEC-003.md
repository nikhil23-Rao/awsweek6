doc_id: CO-DSEC-003
title: Vulnerability Remediation SLA Policy
doc_type: policy
scope_level: company
owner_team: SEC
owner_org: DSEC
author_role: Security Engineer
status: approved
last_updated: 2024-11-05
supersedes: CO-DSEC-004
fact_ids: F-POL-06

# Vulnerability Remediation SLA Policy

**Owner:** AppSec | **Effective:** November 2024 | **Applies to:** all engineering teams

## 1. Policy

Vulnerabilities in TechSync services and their dependencies must be fixed within the following times:

| Severity | Fix within |
|---|---|
| Critical | 7 days |
| High | 30 days |

Medium and Low findings are handled in each team's regular backlog review and have no fixed deadline.

## 2. When the clock starts

The clock starts when Sentinel, a pen test report, or a bug bounty report confirms the finding. If a finding is disputed, the clock keeps running until AppSec records the dispute as resolved.

## 3. What "fixed" means

A finding is fixed when the vulnerable code or dependency is no longer present in production, or when a verified mitigation has been deployed and AppSec has accepted it in the ticket.

## 4. Responsibilities

- **Service owners** triage within one business day, plan the fix, and ship it.
- **AppSec** confirms severity, verifies fixes, and reports SLA performance monthly.
- **Engineering managers** are accountable for overdue findings in their teams.

## 5. Extensions

An extension needs written approval from AppSec with a compensating control and a new due date. Critical findings can only be extended by the CISO.

## 6. Reporting

AppSec publishes a monthly dashboard showing open findings, age, and breaches by team. Repeated breaches are reviewed with the VP of the owning org.
