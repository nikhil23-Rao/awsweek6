doc_id: DSEC-SEC-009
title: Threat Modeling Workshop Guide
doc_type: guide
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2025-12-11
supersedes:
fact_ids:

# Threat Modeling Workshop Guide

A guide for engineers who want to run a threat modeling workshop with their team. The aim is to find the ways a system could be attacked or misused, early enough that it is cheap to design them away. You do not need to be a security expert. You need to know your system and be curious about how it could go wrong.

## Who to invite

Four to eight people is ideal:

- The service's tech lead and one or two engineers who built it
- A Security Engineer from AppSec as co-facilitator
- Someone from a neighboring team that calls or depends on the service
- Optionally, a product representative who knows how customers use it

## Before the workshop (about two days)

1. **Describe the system.** One page: what it does, who uses it, what data it holds.
2. **Draw a first data-flow diagram.** Boxes for components, arrows for data, dashed lines for trust boundaries. It does not need to be perfect.
3. **List assets.** What would hurt if it were stolen, changed, or unavailable?
4. **Share both documents** with the invitees a day before.

## Running the session (90 minutes)

| Minutes | Activity |
|---|---|
| 0-10 | Walk through the diagram; correct mistakes |
| 10-20 | Agree on assets and trust boundaries |
| 20-60 | Go through each element and each boundary using STRIDE |
| 60-80 | Rate and group the threats |
| 80-90 | Assign actions and owners |

### Using STRIDE

For each element, ask:

- **Spoofing:** can someone pretend to be this user or service?
- **Tampering:** can data be changed in transit or at rest?
- **Repudiation:** could someone deny an action, and could we prove otherwise?
- **Information disclosure:** where could data leak?
- **Denial of service:** how could this be made unavailable?
- **Elevation of privilege:** can someone gain access they should not have?

Write each threat as a sentence: "An attacker who can ... could ... which would ...". Avoid solutions in the first pass.

## Rating threats

Use a simple scale of high, medium, low, based on likelihood and impact. Resist the temptation to debate precision. If the group is split, round up and move on.

## After the workshop

- Turn each high and medium threat into a Jira ticket with an owner.
- Update the diagram with what you learned.
- Store the diagram and threat list next to the service's design document.
- Revisit when the architecture changes in a meaningful way.

## Facilitator tips

- Keep quiet people involved by asking for their view directly.
- Park solution debates; note them and move on.
- Celebrate finding things. A long threat list is a success, not a failure.

## Help

Ask in the SEC channel to find a co-facilitator.
