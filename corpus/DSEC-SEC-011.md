doc_id: DSEC-SEC-011
title: Pen Test Coordination Process
doc_type: process
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Security Engineer
status: approved
last_updated: 2026-01-27
supersedes:
fact_ids:

# Pen Test Coordination Process

AppSec coordinates external penetration tests so that vendors get what they need and engineering teams are not surprised. This describes the steps.

## 1. Planning

- Each year, AppSec proposes the list of systems to test, based on risk, changes, and customer requirements.
- The CISO's office approves the list and budget.
- AppSec books vendors well in advance, since good testers have long lead times.

## 2. Scoping

For each engagement, a Security Engineer writes a scope document:

- Systems and environments in scope
- Systems explicitly out of scope
- Accounts and test data the vendor will use
- Testing windows
- Rules of engagement

Owning teams review the scope and confirm the testing window works for them.

## 3. Before testing

1. Sign the contract and any required non-disclosure agreements.
2. Create vendor accounts through Keystone with limited access.
3. Tell the owning teams, SRE, and the support team of the testing window.
4. Make sure the on-call engineer for the target system knows how to reach the AppSec coordinator.

## 4. During testing

- The AppSec coordinator is the vendor's single point of contact.
- If the vendor finds something serious, they notify the coordinator immediately and do not wait for the final report.
- Testers must stay in scope. If the vendor needs to go beyond it, the coordinator and the owning team decide together.

## 5. After testing

1. The vendor delivers a report.
2. AppSec reviews it, confirms findings, and rates severity.
3. Findings enter the normal vulnerability remediation process.
4. Owning teams get a briefing from AppSec and the vendor.
5. A summary goes to the CISO's office.

## 6. Retesting

Where appropriate, AppSec asks the vendor to retest fixed findings.

## 7. Contacts

AppSec coordinator on the engagement; the SEC channel for general questions.
