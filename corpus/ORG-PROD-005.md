doc_id: ORG-PROD-005
title: Product Engineering SLA Exceptions Register
doc_type: register
scope_level: org
owner_team: PROD
owner_org: PROD
author_role: TPM
status: approved
last_updated: 2026-04-22
supersedes:
fact_ids: F-POL-14; F-PROD-011

---

# Product Engineering SLA Exceptions Register

This register lists approved exceptions to published availability targets for Product Engineering services. An exception applies only to the scope written against it. Anything not listed here follows the standard customer commitments.

## Register

| ID | Scope | Exception | Approved by | Date approved | Review |
|---|---|---|---|---|---|
| EX-001 | Pushline push delivery to the Apple Push Notification service (APNs) and Firebase Cloud Messaging (FCM) | Enterprise availability target for this delivery path is **99.9%** | CTO Arjun Mehta and VP Carlos Mendoza | 2026-04-22 | April 2027 |

## Reasoning for EX-001

The last step of a push notification passes through APNs and FCM, which TechSync does not operate. Their availability limits what we can promise for that single step. TechSync-operated parts of Pushline, such as accepting and queueing messages, are not covered by this exception.

## Rules for this register

1. An exception needs written approval from the CTO and the VP of the owning org before it takes effect.
2. Each entry names a specific system or path. Entries cannot cover a whole product.
3. Each entry has a review date. Expired entries are removed unless they are re-approved.
4. The TPM function keeps this register and publishes it to Support.
