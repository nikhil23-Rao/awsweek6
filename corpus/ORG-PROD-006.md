doc_id: ORG-PROD-006
title: Customer-Facing Incident Communication Template
doc_type: template
scope_level: org
owner_team: PROD
owner_org: PROD
author_role: Technical Writer
status: approved
last_updated: 2026-02-09
supersedes:
fact_ids: 

---

# Customer-Facing Incident Communication Template

Use this template for status page updates and customer emails during an incident. Plain words, short sentences, no internal system names unless customers see them.

## Stages

1. **Investigating:** We know something is wrong and are looking into it.
2. **Identified:** We know the cause and are working on a fix.
3. **Monitoring:** A fix is in place and we are watching to be sure.
4. **Resolved:** The issue is over.

## Wording

**Investigating**
> We are investigating reports of [symptom] affecting [product or feature]. We will post another update within [time].

**Identified**
> We have identified the cause of [symptom] and are working on a fix. [Workaround, if any.]

**Monitoring**
> A fix has been applied. We are monitoring and will confirm when we are confident the issue is resolved.

**Resolved**
> The issue affecting [product or feature] has been resolved as of [time, with time zone]. We will publish a summary within [timeframe].

## Update cadence

For Sev1 incidents, post an update at least every 30 minutes. For Sev2, at least every hour. For Sev3 and Sev4, post when the status changes.

## Tone

Be direct. Say what customers can and cannot do right now. Do not speculate about cause until it is confirmed.
