---
doc_id: CO-PLAT-004
title: Postmortem Writing Guide and Template
doc_type: guide
scope_level: company
owner_team: SRE guild
owner_org: PLAT
author_role: Technical Writer
status: approved
last_updated: 2024-11-05
supersedes: ""
fact_ids: ""
---

# Postmortem Writing Guide and Template

*Technical Writing, with the SRE guild*

A good postmortem helps the whole company learn from an incident. This guide explains how to write one, and includes the template.

## Principles

- **Blameless.** Describe what people did and why it made sense to them at the time. Focus on the system that allowed the mistake.
- **Specific.** Times, numbers, links to graphs.
- **Honest about luck.** If something went well by accident, say so.
- **Action-oriented.** Every contributing factor should lead to an action item or an explicit decision not to act.

## Template

**Title:** Postmortem: <short description> (<Sev>, <Month Year>)

**Summary.** Two or three sentences: what broke, for how long, and the impact.

**Customer impact.** Who was affected and how. Numbers if possible.

**Timeline.** Times in one time zone, stated at the top. Include detection, escalation, key decisions, mitigation, and resolution.

**Contributing factors.** Usually several. Avoid "root cause" as a single thing; incidents rarely have one.

**What went well.**

**What didn't go well.**

**Where we got lucky.**

**Action items.** A table with item, owner (team), and Jira ticket.

## Tips

- Start the timeline during the incident; the scribe's notes are your best source.
- Pull graphs before they age out of hot storage.
- Ask "why did that make sense?" not "why did you do that?"
- Get a reviewer from another team. Outsiders spot assumptions.

## Publishing

Publish in Confluence under the owning team's postmortem section and link it in #incident-room.
