doc_id: PROD-PAY-003
title: Billing Alerts Integration Guide (Pushline)
doc_type: integration guide
scope_level: team
owner_team: PAY
owner_org: PROD
author_role: Tech Lead
status: approved
last_updated: 2026-08-04
supersedes:
fact_ids: F-PROD-004

---

# Billing Alerts Integration Guide (Pushline)

**Team:** Payments  **Audience:** engineers working on billing alerts

## Overview

Ledger sends alerts to customers about billing events, such as an approaching usage limit or a failed payment. Alerts reach mobile users through Pushline.

## How it works

1. Ledger Core detects a billing event.
2. The alert service builds a message with the customer's notification preferences.
3. The message is sent to the Pushline API with a priority and an idempotency key.
4. Pushline delivers the message to the customer's phones.

## Message priorities

| Event | Priority |
|---|---|
| Payment failed | High |
| Usage limit reached | High |
| Usage limit approaching | Normal |
| Invoice available | Normal |

## Handling delivery failures

Pushline retries a failed delivery **up to 5 times** before moving the message to its dead-letter queue. Design alert flows with that in mind: a message may arrive minutes after it was first sent, so alert text should not rely on the exact time of delivery.

If a message reaches the dead-letter queue, Ledger falls back to sending an email. The fallback is triggered by a dead-letter notification from Pushline.

## Idempotency

Always send the same idempotency key when you resend an alert, so the customer does not receive duplicates.

## Testing

Use the Pushline sandbox in staging. It lets you simulate failures and check the fallback.

## Contacts

Payments Tech Lead for this guide; Mobile team for Pushline questions.
