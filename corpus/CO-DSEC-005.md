doc_id: CO-DSEC-005
title: Secrets Rotation Policy
doc_type: policy
scope_level: company
owner_team: SEC
owner_org: DSEC
author_role: Security Engineer
status: approved
last_updated: 2025-01-14
supersedes: CO-DSEC-006
fact_ids: F-POL-07

# Secrets Rotation Policy

**Owner:** AppSec | **Effective:** January 2025

## 1. Policy

**Secrets are rotated every 90 days.** This interval shortens the previous 180-day rule, and all secrets must meet it from the effective date.

## 2. Scope

The policy covers long-lived secrets managed in Vaultline or stored in any other system:

- Service API keys
- Database passwords
- Signing keys and tokens
- Integration credentials for third parties

Short-lived credentials issued by Vaultline with automatic leases are governed by the Vaultline runbooks, not by this policy.

## 3. Responsibilities

- **Service owners** rotate their secrets and confirm each rotation in Vaultline.
- **AppSec** reports any secret older than the interval in the monthly review.
- **Engineering managers** are accountable for overdue secrets in their teams.

## 4. Process

1. Vaultline sends a reminder 14 days before the interval ends.
2. The owner creates the new secret and deploys it alongside the old one.
3. After verification, the old secret is revoked.
4. The rotation date is recorded in Vaultline metadata.

## 5. Exceptions

A secret that cannot be rotated on schedule needs a written exception from AppSec with a compensating control and an end date.
