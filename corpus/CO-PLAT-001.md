---
doc_id: CO-PLAT-001
title: Incident Commander Handbook
doc_type: guide
scope_level: company
owner_team: SRE guild
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2025-10-28
supersedes: ""
fact_ids: ""
---

# Incident Commander Handbook

**Owner:** SRE guild
**Applies to:** anyone acting as incident commander (IC) at TechSync

## What the IC does

The incident commander coordinates the response. The IC doesn't usually fix the problem; they make sure the right people are working on it, decisions get made, and everyone knows what's happening.

## Taking command

1. Declare yourself: "I'm IC for this incident" in the incident channel.
2. Confirm the severity using the *Incident Severity Definitions*. Raise or lower it as you learn more.
3. Open a dedicated channel: `#inc-<date>-<short-name>`.
4. Start the incident doc from the template and assign a scribe.

## Running the response

- **Assign roles.** Operations lead (hands on keyboard), communications lead, scribe. For small incidents one person may hold several roles.
- **Set a rhythm.** Ask for status updates at regular intervals. Keep them short: what we know, what we're trying, what's next.
- **Make decisions.** If responders disagree on an approach, the IC decides. Rolling back is usually the right first move.
- **Pull in help.** Page other teams early. It's cheaper to release someone than to wait for them.
- **Protect responders.** Keep spectators out of the working channel. Answer leadership in a separate thread.

## Communicating

The communications lead posts updates to #incident-room and, for customer-impacting incidents, the status page, following the *Incident Communication Standard*.

## Handing off

For long incidents, hand off IC every four hours. Do it explicitly in the channel and summarize the current state.

## Ending the incident

1. Confirm impact has ended and metrics are normal.
2. Announce resolution in the channel and #incident-room.
3. Assign a postmortem owner for incidents that need one.

## Becoming an IC

Shadow two incidents, then lead one with an experienced IC as backup. The SRE guild runs IC training each quarter.
