doc_id: ORG-DSEC-003
title: DSEC Org Charter and Team Map
doc_type: overview
scope_level: org
owner_team: none (DSEC org-wide)
owner_org: DSEC
author_role: Technical Writer
status: approved
last_updated: 2026-03-02
supersedes:
fact_ids:

# DSEC Org Charter and Team Map

## Mission

Data & Security (DSEC) builds and runs the data, machine-learning, security, and compliance foundations that every other TechSync org builds on. We aim to make the safe way the easy way for engineers across the company.

## Where we sit

DSEC is one of three engineering orgs, alongside Platform Engineering and Product Engineering. Our VP is **Rachel Goldstein**, who reports to the CTO, **Arjun Mehta**. Security policy is sponsored by the CISO, **Tamsin Reid**. The three-org structure dates from 2022, when the former Core Eng and Apps Eng groups were reorganized.

## Teams

| Team | Code | Eng manager | Tech lead | Owns |
|---|---|---|---|---|
| Data Platform | DATA | Naveen Iyer | Sofia Marchetti | Reservoir, Streamline |
| ML Infrastructure | MLI | Olivia Brandt | Hassan Qureshi | Foundry, FeatureHub |
| AppSec | SEC | Gareth Llewellyn | Amara Okafor | Sentinel, Vaultline |
| IT & Compliance | ITC | Beatriz Alves | Nikolai Petrov | Keystone, Compass |

### Data Platform
Runs the data lake and the event bus. Customers of DATA include analytics, product teams, and ML Infrastructure.

### ML Infrastructure
Provides training and serving infrastructure and the feature store. Researchers and product teams submit jobs and deploy models through it.

### AppSec
Builds the scanning and secrets tools and advises teams on secure design. SEC engineers run threat-model reviews.

### IT & Compliance
Runs identity for the company, maintains the compliance evidence tracker, and works with auditors.

## How we work together

- **Interface contracts.** When one DSEC team depends on another's system, the contract is written down and owned by the providing team.
- **Planning.** Teams plan on a shared quarterly calendar run by Technical Program Management.
- **Escalation.** Cross-team disagreements go first to the two tech leads, then to the two engineering managers, then to the VP.
- **Intake.** Requests from outside DSEC come through the DSEC intake queue and are routed to the owning team.

## Cross-org functions we work with

Technical Program Management, the SRE guild, Technical Writing, and the Architecture Review Board, which the CTO chairs.

## Working agreements

1. Documentation is part of the work. Every system has a runbook with a named owner.
2. We name decisions in ADRs when more than one team is affected.
3. We prefer boring, reliable technology: Kubernetes on EKS, PostgreSQL, Kafka, OpenSearch, Terraform.
4. We are remote-first, so write things down and favor async updates.

## Where to start

New to DSEC? Read the onboarding guide, then the tooling landing page for links to each system's documentation.
