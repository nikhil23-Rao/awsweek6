doc_id: DSEC-MLI-014
title: ML Infrastructure Team Charter
doc_type: overview
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: Engineering Manager
status: approved
last_updated: 2025-07-01
supersedes:
fact_ids:

# ML Infrastructure Team Charter

## Mission

ML Infrastructure (MLI) gives machine-learning practitioners at TechSync a reliable, efficient, and safe way to train, evaluate, and serve models. We want researchers to spend their time on models, not on clusters.

## Who we are

MLI is one of four teams in Data & Security. Olivia Brandt is the engineering manager and Hassan Qureshi is the tech lead.

## What we own

- **Foundry:** ML training and serving platform
- **FeatureHub:** the feature store
- The model registry, experiment tracking, and GPU capacity

## What we do not own

- The data lake (Reservoir) or the event bus (Streamline); these belong to Data Platform.
- Identity and secrets for our systems; these belong to IT & Compliance and AppSec.
- The models themselves; model owners belong to the product teams that build them.

## Who we serve

Product teams in Product Engineering, search and billing teams using models, and researchers.

## Principles

1. **Self-service first.** If a task needs a ticket, we try to automate it.
2. **Safe rollouts.** Every production model change goes through a staged rollout.
3. **Cost visible.** Every GPU-hour is attributable to a team.
4. **Reproducible.** A run can be reconstructed from its recorded inputs.

## How we work

- Weekly sync, monthly retrospective, and shared quarterly planning with the rest of DSEC.
- Requests come through the DSEC intake queue.
- Operational issues are handled by the MLI on-call through Lookout.

## Success measures

Time from experiment to serving, GPU utilization, rollout failure rate, and satisfaction of our users measured in a twice-yearly survey.

## Review

This charter is reviewed each year by the engineering manager and the tech lead.
