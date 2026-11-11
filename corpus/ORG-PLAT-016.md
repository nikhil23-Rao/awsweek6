---
doc_id: ORG-PLAT-016
title: Platform Roadmap H2 2026
doc_type: roadmap
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: TPM
status: approved
last_updated: 2026-07-01
supersedes: ""
fact_ids: ""
---

# Platform Roadmap H2 2026

**Owner:** Platform TPM, approved by VP Platform Engineering
**Published:** July 1, 2026

## Themes

1. **Faster, safer delivery**
2. **Cost efficiency**
3. **Regional resilience**

## Compute

- Kestrel EKS upgrades on schedule in all regions.
- GPU capacity planning with ML Infrastructure for Foundry's 2027 training calendar.
- Spot instances for more `forge-standard` capacity.

## Networking

- IPv6 dual-stack on staging EdgeGate (Q3), prod plan (Q4).
- Mesh control-plane upgrade across all clusters.
- WAF duty rotation and rule-quality metrics.

## Observability

- Per-team OpenSearch cost reports.
- Alert quality reviews with every Platform team.
- Evaluate TechSync Insight for some internal dashboards.

## Developer Tooling

- Deploy speed improvements for small changes, through the Gatekeeper CI working group.
- Flaky test rate under 1%.
- `scaffold upgrade` adoption above 60%.

## Cross-team

- A full us-west-2 failover exercise with the SRE guild in Q4.
- Monthly night-page reduction reports.

## Not planned for H2

- Replacing PagerDuty.
- Multi-cloud.

## Dependencies on other orgs

- **ML Infrastructure:** Foundry training calendar for GPU planning.
- **Product Engineering:** deploy speed requirements and Insight evaluation access.
- **SRE guild:** failover exercise scheduling.
- **AppSec:** WAF rule priorities and certificate requirements.

## Review

Progress reviewed at the Q3 quarterly review in October. Teams update their roadmap items in Jira by the first of each month so the TPM can publish a status summary in #platform.
