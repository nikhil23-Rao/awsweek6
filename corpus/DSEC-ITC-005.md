doc_id: DSEC-ITC-005
title: Compass Evidence Collection How-To
doc_type: guide
scope_level: team
owner_team: ITC
owner_org: DSEC
author_role: Compliance Analyst
status: approved
last_updated: 2026-03-12
supersedes:
fact_ids:

# Compass Evidence Collection How-To

A step-by-step guide to putting evidence into Compass, written for engineers who have never done it. For the rules about what evidence is needed and the naming convention, see the Compliance Evidence Handbook. This guide covers the clicks.

## What you need before you start

- Access to Compass (request the `co-compass-users` group in the Keystone request portal)
- The evidence itself, as a file or a link
- The name of the control it supports, from the request you received

## Uploading evidence

1. Sign in to Compass through Keystone.
2. Open **Controls** and search for the control by name or ID.
3. Choose **Add evidence**.
4. Attach the file, or paste the link if the evidence lives in Jira or Confluence.
5. Select the period the evidence covers. Compass offers the audit period by default.
6. Write one sentence describing what the file shows.
7. Select **Submit**. Compass records who uploaded it and when.

## What makes good evidence

- It names the system, the date, and the person who collected it.
- It can be read without special tools.
- It shows the control working, not just that it exists.

## Replacing or fixing evidence

You cannot edit submitted evidence. If you uploaded the wrong file, upload the correct one and add a comment on the old entry explaining why. A compliance analyst will mark the old one as replaced in the record.

## Linking a ticket

If your evidence is a Jira ticket, paste its URL. Compass keeps a link but not a copy, so make sure the ticket is accessible to auditors. If it is in a restricted project, ask a compliance analyst how to handle it.

## Bulk uploads

For many files at once, ask a compliance analyst for the bulk template. It takes a spreadsheet with one row per file.

## Common problems

| Problem | What to do |
|---|---|
| Cannot find the control | Search by ID; if it is missing, tell the compliance channel |
| Upload fails | Check the file size and type; compress large files |
| Wrong period selected | Upload again with the right one and comment on the old entry |
| No permission | Request the group again; approvals can take a day |

## Where to ask

The compliance channel, or a message to the analyst who sent the request.
