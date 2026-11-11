doc_id: ORG-DSEC-020
title: DSEC H1 2026 Retrospective
doc_type: meeting notes
scope_level: org
owner_team: none (DSEC org-wide)
owner_org: DSEC
author_role: TPM
status: unmarked
last_updated: 2026-07-15
supersedes:
fact_ids:

# DSEC H1 2026 Retrospective

**Date:** 14 Jul 2026 | **Facilitator:** TPM | **Present:** the four engineering managers, four tech leads, and about 25 engineers

We used the usual format: what went well, what did not, and what we will try. Sticky notes were clustered by theme; this is the summary.

## What went well

**Cross-team delivery**
- The Foundry autoscaling change landed with help from Platform Engineering, and several people said it was the smoothest cross-org effort of the half.
- The SBOM build step reached most Scaffold-based repositories ahead of the plan.
- The Keystone directory sync work finished with fewer escalations than we had feared.

**Documentation**
- Runbooks written alongside new systems were noticed by on-call engineers. A few people called out the Streamline playbooks as a model.
- The landing page made finding documents easier.

**People**
- New joiners reported that the onboarding guide and their buddies made the first month easier than at previous companies.

## What did not go well

**Planning**
- Late changes to the quarterly plan caused churn for two teams.
- Dependencies on other orgs were discovered late, mostly during the build rather than the plan.

**Operations**
- One serving latency incident showed that alerts did not cover slow-but-healthy endpoints.
- A scanning queue backlog in June slowed developers for a day.

**Communication**
- Some teams learned about interface changes from a failing job rather than an announcement.

## Themes and what we will try

| Theme | Experiment | Owner |
|---|---|---|
| Late dependencies | Review dependency table in week -2, not week -1 | TPM |
| Interface changes | Announce breaking changes in the DSEC channel two weeks ahead | Tech leads |
| Alert coverage | Add a "how would we notice a slow failure?" question to design reviews | Staff engineers |
| Plan churn | Lock the plan after week 0 except through the planning doc | Engineering managers |

## Shout-outs

Thanks to the SRE who drove the rollout gate changes, to the compliance analysts for their work through the audit season, and to the staff engineer who mentored three new joiners.

## Next retro

The next retrospective will cover Q3 and Q4 together.
