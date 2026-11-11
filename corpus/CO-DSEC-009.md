doc_id: CO-DSEC-009
title: Production Access Policy
doc_type: policy
scope_level: company
owner_team: ITC
owner_org: DSEC
author_role: Security Engineer
status: approved
last_updated: 2025-10-06
supersedes: CO-DSEC-010
fact_ids: F-POL-10

# Production Access Policy

**Owner:** IT & Compliance | **Effective:** October 2025 | **Applies to:** every person and automated agent that signs in to production systems

## 1. Policy

**A hardware security key is required for production access.** Authenticator apps and SMS codes are not accepted for any production sign-in.

## 2. What counts as a hardware security key

A FIDO2/WebAuthn-compliant physical key, issued by IT or purchased from the approved vendor list. Platform keys built into laptops are not a substitute for production access.

## 3. Enrollment

1. Request a key through the IT helpdesk, or use your own from the approved list.
2. Register it in Keystone under Security settings.
3. Register a second key as a backup. IT recommends keeping it in a separate location.
4. Complete a test sign-in to a production console before your current access expires.

## 4. Lost or damaged keys

Report the loss to the IT helpdesk immediately. IT revokes the key in Keystone, and your backup key keeps your access working. If both are lost, a manager must confirm your identity before a temporary replacement is issued.

## 5. Break-glass access

Break-glass accounts are held by the SRE guild. They also use hardware keys, kept in the sealed safe in the Denver office, and every use triggers a page to the CISO's office.

## 6. Responsibilities

- **Individuals:** keep keys safe and never share them.
- **Engineering managers:** make sure new starters in production roles enroll before their first on-call shift.
- **IT & Compliance:** operate enrollment, maintain the approved vendor list, report coverage monthly.

## 7. Exceptions

There are no standing exceptions. Short-term accommodations, for example for accessibility needs, are approved by the CISO and documented in Keystone.
