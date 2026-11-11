doc_id: DSEC-SEC-013
title: AppSec Team Onboarding Guide
doc_type: onboarding guide
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Engineering Manager
status: approved
last_updated: 2026-04-21
supersedes:
fact_ids:

# AppSec Team Onboarding Guide

Welcome to AppSec. We build the tools that scan our code and guard our secrets, and we help every engineering team build securely. You will find the work varied, and the team friendly. This guide is on top of the DSEC org onboarding guide, which covers company tools and general first-month tasks.

## What we own

- **Sentinel:** code and dependency scanning
- **Vaultline:** secrets management
- Security reviews, threat modeling, and pen test coordination
- The company policies on vulnerability remediation, secrets, and open-source licenses

## Your first two weeks

**Week 1**
- Meet your buddy and the tech lead, Amara Okafor.
- Get access to the `sentinel-rules` and Vaultline policy-as-code repositories.
- Read the Sentinel and Vaultline documents linked from the DSEC tooling landing page.
- Sit in on a triage session and a security review.

**Week 2**
- Take a ticket from the triage queue, with your buddy reviewing your work.
- Shadow the on-call engineer for a day.
- Co-facilitate a threat modeling session using the workshop guide.

## How the team works

- Weekly sync on Tuesdays; notes go in Confluence.
- A triage rotation handles false-positive requests. You join the rota after your first month.
- An on-call rotation covers Sentinel and Vaultline availability. You join after your first three months.
- Pull requests to our repositories are reviewed under the company code review policy.
- We write decisions down as ADRs when they affect other teams.

## Habits we value

1. **Explain, do not just block.** A good finding message tells the engineer what to do next.
2. **Make the safe path the easy path.** If a control annoys people, find out why.
3. **Be honest about uncertainty.** "I do not know yet" is a good answer.
4. **Share what you learn.** Post interesting findings in the SEC channel.

## Who is who

| Role | Person |
|---|---|
| Engineering manager | Gareth Llewellyn |
| Tech lead | Amara Okafor |

## Questions

Your buddy first, then the SEC channel. Everyone remembers their first week.
