doc_id: CO-DSEC-010
title: Production Access Policy v1
doc_type: policy
scope_level: company
owner_team: ITC
owner_org: DSEC
author_role: Security Engineer
status: deprecated
last_updated: 2025-10-06
supersedes:
fact_ids: F-POL-10

> **DEPRECATED (October 2025).** This version was replaced by CO-DSEC-009, Production Access Policy, and is outdated. Retained for audit history only. Do not follow it.

# Production Access Policy v1

**Owner:** IT & Compliance

## 1. Policy

Multi-factor authentication is required for production access. **An authenticator app (time-based one-time passwords) is acceptable.** SMS codes are not accepted.

## 2. Enrollment

Register the authenticator app in Keystone under Security settings. Keep recovery codes in the company password manager.

## 3. Lost devices

Report a lost phone to the IT helpdesk, who will reset the factor in Keystone after identity confirmation.

## 4. Break-glass

Break-glass accounts are held by the SRE guild and every use is reviewed by the CISO's office.
