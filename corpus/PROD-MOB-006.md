doc_id: PROD-MOB-006
title: Deploy Approvals Feature: User Guide
doc_type: FAQ
scope_level: team
owner_team: MOB
owner_org: PROD
author_role: Technical Writer
status: approved
last_updated: 2026-05-27
supersedes:
fact_ids: 

---

# Deploy Approvals Feature: User Guide

## What are deploy approvals?

When a release is waiting for a person to say yes, TechSync can send the request to your phone. You review what is changing and approve or reject it.

## Getting requests

1. Turn on notifications for TechSync Mobile when prompted.
2. In **Settings > Approvals**, choose which pipelines you want to hear about.
3. When a request arrives, tap the notification to open it.

## Reviewing a request

The screen shows the service, the version, who started the release, the list of changes, and the checks that have passed. Tap **View details** to see the full change list.

## Approving or rejecting

- **Approve** continues the release to the next stage.
- **Reject** stops it and lets the author know. You can add a comment.

## Frequently asked questions

**Can someone else approve for me?**
Only people named as approvers for the pipeline can approve.

**What if I miss the notification?**
Open the app and look under **Approvals**. Pending requests stay there until they are decided.

**Is my decision recorded?**
Yes. Decisions appear in the same audit trail as decisions made in the web console.

**Can I undo an approval?**
No. If something is wrong, ask the author to stop the release.
