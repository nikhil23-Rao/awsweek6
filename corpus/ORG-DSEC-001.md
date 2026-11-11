doc_id: ORG-DSEC-001
title: Security Review Process
doc_type: process
scope_level: org
owner_team: none (DSEC org-wide)
owner_org: DSEC
author_role: Security Engineer
status: approved
last_updated: 2026-01-20
supersedes:
fact_ids: F-DSEC-006

# Security Review Process

**Applies to:** all services built by teams in Data & Security (DATA, MLI, SEC, ITC)

## Why we review

Every service we ship can touch credentials, customer-derived data, or internal identity. The security review is how DSEC makes sure risks are found while changes are still cheap to make.

## The rule

A **full threat-model review must be completed before any new service, or any service with a major architectural change, is deployed to staging.** Services that have not passed review may run in dev only.

## What a full review contains

1. **Intake.** The service owner opens a review request in the DSEC intake queue with a one-page description, the data classes handled, and an architecture diagram.
2. **Threat model.** The owner, with an AppSec reviewer, produces a data-flow diagram and a STRIDE-based threat model. Trust boundaries, external dependencies, and secrets usage must be listed explicitly.
3. **Review meeting.** A 60-minute session with an AppSec Security Engineer and a Staff Engineer from a different DSEC team.
4. **Findings.** Findings are logged in Jira with owner and severity. High and Critical findings must be fixed or formally accepted by the engineering manager before staging.
5. **Sign-off.** The AppSec reviewer signs off in the review ticket, and the ticket link is added to the service's Compass record.

Reviews are scheduled within 10 business days of a complete intake.

## When to re-review

Re-run the full process if the service adds a new external integration, changes the data classes it handles, changes its authentication model, or moves between tiers.

## Roles

- **Service owner:** prepares materials, fixes findings.
- **AppSec reviewer:** leads the threat model and signs off.
- **Staff Engineer reviewer:** challenges design assumptions.
- **Engineering manager:** accepts residual risk.

## Records

All review artifacts are kept with the Jira ticket and linked from Compass for audit.
