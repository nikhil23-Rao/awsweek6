doc_id: CO-DSEC-006
title: Secrets Rotation Policy (2023)
doc_type: policy
scope_level: company
owner_team: SEC
owner_org: DSEC
author_role: Security Engineer
status: deprecated
last_updated: 2025-01-14
supersedes:
fact_ids: F-POL-07

> **DEPRECATED (January 2025).** This policy was replaced by CO-DSEC-005, Secrets Rotation Policy, which sets a shorter interval. It is kept for audit history only and must not be followed.

# Secrets Rotation Policy (2023)

**Owner:** AppSec | **Effective:** 2023

## 1. Policy

Secrets are rotated **every 180 days**.

## 2. Scope

Service API keys, database passwords, signing keys, and integration credentials stored in Vaultline.

## 3. Process

Owners create a new secret, deploy it beside the old one, verify, and revoke the old one. The rotation date is recorded in Vaultline.

## 4. Exceptions

Exceptions require written AppSec approval with an end date.
