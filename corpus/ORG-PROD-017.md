doc_id: ORG-PROD-017
title: Customer Escalation Handling with Support
doc_type: runbook
scope_level: org
owner_team: PROD
owner_org: PROD
author_role: Engineering Manager
status: approved
last_updated: 2026-05-26
supersedes:
fact_ids: 

---

# Customer Escalation Handling with Support

This runbook describes how Support brings customer problems to Product Engineering and what Support can expect in return.

## Severity levels

| Level | Meaning |
|---|---|
| Sev1 | Widespread customer-facing impact |
| Sev2 | Significant impact for one or more customers |
| Sev3 | Limited impact, workaround available |
| Sev4 | Question or minor issue |

## Steps

1. **Support triages** the ticket and chooses a severity based on the table above.
2. **Sev3 and Sev4:** Support files a Jira ticket in the owning team's queue, using the product component field.
3. **Sev1 and Sev2:** Support pages the owning team's on-call engineer through Lookout and opens an incident channel.
4. **The on-call engineer** confirms the severity, starts the incident process and tells Support who is leading.
5. **Support relays updates** to the customer using the Customer-Facing Incident Communication Template.
6. **After resolution,** Support closes the ticket with a plain-language summary.

## Finding the right team

Use the Product Engineering Team Directory to map a product area to a team.

## Feedback loop

Each month, the TPM and the Support lead review recurring tickets and decide which to fix at the source.
