doc_id: PROD-MOB-002
title: Pushline Operations Runbook
doc_type: runbook
scope_level: team
owner_team: MOB
owner_org: PROD
author_role: SRE
status: approved
last_updated: 2026-06-10
supersedes:
fact_ids: F-PROD-004

---

# Pushline Operations Runbook

**Owner:** Mobile (MOB)  **Audience:** on-call engineers and SREs supporting Pushline

## What Pushline does

Pushline accepts notification requests from TechSync services, queues them, and hands them to Apple Push Notification service (APNs) or Firebase Cloud Messaging (FCM) for delivery to phones.

## Delivery pipeline

1. A service calls the Pushline API with a recipient, payload and priority.
2. Pushline validates the request and writes it to the delivery queue.
3. Workers pick up messages and send them to APNs or FCM.
4. Delivery receipts are recorded.

## Retry behavior

When a delivery attempt fails with a retryable error, Pushline retries the delivery. **A failed delivery is retried at most 3 times; after the third failed retry the message is moved to the dead-letter queue.** Retries use exponential backoff starting at 5 seconds.

## Dead-letter queue

- Messages in the dead-letter queue are kept for seven days.
- The queue size is graphed on the Pushline dashboard. Investigate if it grows quickly.
- To replay a message, use the replay tool with the message ID.

## Common alerts

| Alert | First action |
|---|---|
| Delivery success rate low | Check APNs/FCM status pages and recent Pushline releases |
| Queue depth high | Check worker health and scale workers |
| Dead-letter queue growing | Inspect recent messages for a shared error |

## Escalation

Page the Mobile on-call engineer through Lookout. For platform problems, escalate to Platform Compute.
