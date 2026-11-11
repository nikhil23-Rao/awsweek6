# Retrieval Failures (No Authoritative Document in Top 5)

- **Index directory:** `index` (`chunk_tokens=300`)
- **Total failures:** `10` out of `90` questions

## Q-PLAT-004 (outdated | scope: team | plan: X-03)

- **Asker team:** `PAY` | **Hops:** `1`
- **Question:** Can I still trigger a Jenkins job to deploy a Ledger service?
- **Expected authoritative doc(s):** `PLAT-DEVT-013`
- **Distractor doc(s):** `PROD-WEB-002`
- **Distractor in top 5:** `True` (first distractor rank: `1`)
- **Gold answer:** No. Jenkins was retired in May 2026; all builds and deploys run through TechSync Ship and Gatekeeper CI.

### Retrieved Top 5 Chunks

| Rank | Score | Chunk ID | Doc ID | Title > Heading | Scope / Owner / Status / Updated | Preview |
| ---: | ---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.7252 | `PROD-WEB-002#005` | `PROD-WEB-002` | Console Production Deploy Runbook > After the deploy | `team / PROD:WEB / unmarked / 2025-06-17` | ## After the deploy - Update the release notes page with the deploy time and tag. - If you rolled back, open a ticket de |
| 2 | 0.6958 | `PROD-PAY-002#003` | `PROD-PAY-002` | Ledger Core Service Credentials Runbook > Rotation steps | `team / PROD:PAY / unmarked / 2024-08-06` | ## Rotation steps 1. Create a new key version in Vaultline with the same permissions as the current one. 2. Deploy the n |
| 3 | 0.6899 | `PROD-WEB-002#003` | `PROD-WEB-002` | Console Production Deploy Runbook > Deploying | `team / PROD:WEB / unmarked / 2025-06-17` | ## Deploying 1. Open Jenkins and find the job `console-prod`. 2. Choose **Build with Parameters** and enter the release  |
| 4 | 0.6815 | `PROD-WEB-002#004` | `PROD-WEB-002` | Console Production Deploy Runbook > Rolling back | `team / PROD:WEB / unmarked / 2025-06-17` | ## Rolling back If the canary or full rollout misbehaves: ``` jenkins-ctl rollback console-prod --to previous ``` Wait f |
| 5 | 0.6810 | `PROD-PAY-002#004` | `PROD-PAY-002` | Ledger Core Service Credentials Runbook > If a key is exposed | `team / PROD:PAY / unmarked / 2024-08-06` | ## If a key is exposed Rotate it immediately, outside the calendar, and tell the security team. Review access logs for t |

## Q-PLAT-016 (outdated | scope: team | plan: PLAT-OUT-2)

- **Asker team:** `COMP` | **Hops:** `1`
- **Question:** What is the minimum VM pool size for a new production service?
- **Expected authoritative doc(s):** `PLAT-COMP-009`
- **Distractor doc(s):** `PLAT-COMP-008`
- **Distractor in top 5:** `True` (first distractor rank: `1`)
- **Gold answer:** There is none. Services no longer get VM pools; since the 2019 Kubernetes migration every service runs in a Kestrel namespace.

### Retrieved Top 5 Chunks

| Rank | Score | Chunk ID | Doc ID | Title > Heading | Scope / Owner / Status / Updated | Preview |
| ---: | ---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.8022 | `PLAT-COMP-008#002` | `PLAT-COMP-008` | Service Capacity Runbook > Minimum pool | `team / PLAT:COMP / unmarked / 2018-09-14` | ## Minimum pool Each new service receives a **minimum pool of 3 VMs**, spread across three availability zones so one AZ  |
| 2 | 0.7584 | `PLAT-COMP-008#005` | `PLAT-COMP-008` | Service Capacity Runbook > Growing a pool | `team / PLAT:COMP / unmarked / 2018-09-14` | ## Growing a pool Add VMs through another capacity request. Mention current CPU and memory usage from the monitoring das |
| 3 | 0.7367 | `PLAT-COMP-008#001` | `PLAT-COMP-008` | Service Capacity Runbook > How services are hosted | `team / PLAT:COMP / unmarked / 2018-09-14` | # Service Capacity Runbook Core Engineering, Compute Infrastructure group This runbook explains how a new production ser |
| 4 | 0.7267 | `PLAT-COMP-008#004` | `PLAT-COMP-008` | Service Capacity Runbook > Instance sizes | `team / PLAT:COMP / unmarked / 2018-09-14` | ## Instance sizes \| Size \| vCPU \| Memory \| Typical use \| \|---\|---\|---\|---\| \| small \| 2 \| 4 GB \| internal tools, cron-sty |
| 5 | 0.7237 | `PLAT-COMP-008#003` | `PLAT-COMP-008` | Service Capacity Runbook > Requesting capacity | `team / PLAT:COMP / unmarked / 2018-09-14` | ## Requesting capacity 1. Fill out a **Compute capacity request** in Jira (project: COMPUTE). Include the service name,  |

## Q-PLAT-022 (team_vs_company | scope: company | plan: PLAT-TVC-2)

- **Asker team:** `COMP` | **Hops:** `2`
- **Question:** How many approvals do I need for a PR that changes the Kestrel scheduler configuration?
- **Expected authoritative doc(s):** `CO-PLAT-006`
- **Distractor doc(s):** `PLAT-COMP-005`
- **Distractor in top 5:** `True` (first distractor rank: `1`)
- **Gold answer:** 2. Kestrel is Tier 0, and the node-image exception doesn't cover scheduler or control-plane changes.

### Retrieved Top 5 Chunks

| Rank | Score | Chunk ID | Doc ID | Title > Heading | Scope / Owner / Status / Updated | Preview |
| ---: | ---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.7157 | `PLAT-COMP-005#001` | `PLAT-COMP-005` | Code Review Exception: Kestrel Node-Image Patch PRs > Code Review Exception: Kestrel Node-Image Patch PRs | `team / PLAT:COMP / approved / 2026-02-09` | # Code Review Exception: Kestrel Node-Image Patch PRs **Status:** Approved **Requested by:** Compute (COMP) **Approved b |
| 2 | 0.7069 | `PLAT-COMP-005#002` | `PLAT-COMP-005` | Code Review Exception: Kestrel Node-Image Patch PRs > Background | `team / PLAT:COMP / approved / 2026-02-09` | ## Background Compute rebuilds the Kestrel node images every week to pick up OS and kernel security patches. An automate |
| 3 | 0.7064 | `PLAT-COMP-003#002` | `PLAT-COMP-003` | Kestrel Cluster Upgrade Runbook > Before you start | `team / PLAT:COMP / approved / 2026-05-04` | ## Before you start - [ ] Read the EKS release notes for the target version and list deprecated Kubernetes APIs. - [ ] R |
| 4 | 0.7035 | `PLAT-COMP-003#001` | `PLAT-COMP-003` | Kestrel Cluster Upgrade Runbook > Overview | `team / PLAT:COMP / approved / 2026-05-04` | # Kestrel Cluster Upgrade Runbook **Owner:** Compute (COMP) **Who runs this:** the COMP engineer assigned to the upgrade |
| 5 | 0.7007 | `PLAT-COMP-001#005` | `PLAT-COMP-001` | Compute Team Charter > Goals for 2025 | `team / PLAT:COMP / approved / 2025-02-03` | ## Goals for 2025 1. Finish moving all Kestrel node autoscaling to Karpenter. 2. Cut median Forge queue time in half. 3. |

## Q-PROD-006 (outdated | scope: company | plan: X-09)

- **Asker team:** `PAY` | **Hops:** `1`
- **Question:** How often do Ledger Core service API keys have to be rotated?
- **Expected authoritative doc(s):** `CO-DSEC-005`
- **Distractor doc(s):** `PROD-PAY-002`
- **Distractor in top 5:** `True` (first distractor rank: `1`)
- **Gold answer:** Every 90 days.

### Retrieved Top 5 Chunks

| Rank | Score | Chunk ID | Doc ID | Title > Heading | Scope / Owner / Status / Updated | Preview |
| ---: | ---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.8889 | `PROD-PAY-002#002` | `PROD-PAY-002` | Ledger Core Service Credentials Runbook > Where keys live | `team / PROD:PAY / unmarked / 2024-08-06` | ## Where keys live Keys are stored in Vaultline. Applications read them at start-up through the secrets sidecar. No key  |
| 2 | 0.7935 | `PROD-PAY-002#003` | `PROD-PAY-002` | Ledger Core Service Credentials Runbook > Rotation steps | `team / PROD:PAY / unmarked / 2024-08-06` | ## Rotation steps 1. Create a new key version in Vaultline with the same permissions as the current one. 2. Deploy the n |
| 3 | 0.7627 | `CO-DSEC-006#002` | `CO-DSEC-006` | Secrets Rotation Policy (2023) > 1. Policy | `company / DSEC:SEC / deprecated / 2025-01-14` | # Secrets Rotation Policy (2023) **Owner:** AppSec \| **Effective:** 2023 ## 1. Policy Secrets are rotated **every 180 da |
| 4 | 0.7466 | `PROD-PAY-002#004` | `PROD-PAY-002` | Ledger Core Service Credentials Runbook > If a key is exposed | `team / PROD:PAY / unmarked / 2024-08-06` | ## If a key is exposed Rotate it immediately, outside the calendar, and tell the security team. Review access logs for t |
| 5 | 0.7244 | `PROD-PAY-002#001` | `PROD-PAY-002` | Ledger Core Service Credentials Runbook > Scope | `team / PROD:PAY / unmarked / 2024-08-06` | # Ledger Core Service Credentials Runbook **Team:** Payments **Audience:** SREs and engineers who operate Ledger Core ## |

## Q-PROD-024 (team_vs_company | scope: company | plan: PROD-TVC-3)

- **Asker team:** `WEB` | **Hops:** `2`
- **Question:** What service tier is Console, and how should it be supported?
- **Expected authoritative doc(s):** `CO-PROD-012; CO-PLAT-013`
- **Distractor doc(s):** `PROD-WEB-004`
- **Distractor in top 5:** `True` (first distractor rank: `1`)
- **Gold answer:** Tier 1, a customer-facing service, according to the Service Tiering Policy. Under the On-Call Policy (v3), Sev1 pages on Tier 1 services must be acknowledged within 5 minutes, so Console is supported around the clock, not only during business hours.

### Retrieved Top 5 Chunks

| Rank | Score | Chunk ID | Doc ID | Title > Heading | Scope / Owner / Status / Updated | Preview |
| ---: | ---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.8378 | `PROD-WEB-004#002` | `PROD-WEB-004` | Console Service Profile and Support Model > How we operate Console | `team / PROD:WEB / approved / 2025-12-09` | ## How we operate Console Console is operated as a Tier 2 service. The Web team's on-call engineer responds during busin |
| 2 | 0.8093 | `PROD-WEB-004#001` | `PROD-WEB-004` | Console Service Profile and Support Model > Summary | `team / PROD:WEB / approved / 2025-12-09` | # Console Service Profile and Support Model *Maintained by the Web Engineering Manager. Reviewed each quarter.* ## Summa |
| 3 | 0.7446 | `CO-PROD-005#004` | `CO-PROD-005` | Product Overview: TechSync Console > Who it is for | `company / PROD:Technical Writing / approved / 2026-07-22` | ## Who it is for Everyone who uses a TechSync product uses Console, from an engineer checking a deploy to a finance anal |
| 4 | 0.7351 | `PROD-WEB-004#004` | `PROD-WEB-004` | Console Service Profile and Support Model > Monitoring | `team / PROD:WEB / approved / 2025-12-09` | ## Monitoring Alerts for Console go to the Web on-call channel. Dashboards for latency, error rate and sign-in success a |
| 5 | 0.7179 | `PROD-WEB-012#001` | `PROD-WEB-012` | Console Browser Support Matrix > Policy | `team / PROD:WEB / approved / 2026-02-05` | # Console Browser Support Matrix ## Policy Console supports the current and previous major versions of the browsers belo |

## Q-PROD-025 (team_vs_company | scope: company | plan: PROD-TVC-3)

- **Asker team:** `SRCH` | **Hops:** `1`
- **Question:** Is Console a Tier 2 service supported only during business hours?
- **Expected authoritative doc(s):** `CO-PROD-012`
- **Distractor doc(s):** `PROD-WEB-004`
- **Distractor in top 5:** `True` (first distractor rank: `1`)
- **Gold answer:** No. Console is Tier 1 under the company Service Tiering Policy, and no exception is on file.

### Retrieved Top 5 Chunks

| Rank | Score | Chunk ID | Doc ID | Title > Heading | Scope / Owner / Status / Updated | Preview |
| ---: | ---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.8413 | `PROD-WEB-004#002` | `PROD-WEB-004` | Console Service Profile and Support Model > How we operate Console | `team / PROD:WEB / approved / 2025-12-09` | ## How we operate Console Console is operated as a Tier 2 service. The Web team's on-call engineer responds during busin |
| 2 | 0.7690 | `PROD-WEB-004#001` | `PROD-WEB-004` | Console Service Profile and Support Model > Summary | `team / PROD:WEB / approved / 2025-12-09` | # Console Service Profile and Support Model *Maintained by the Web Engineering Manager. Reviewed each quarter.* ## Summa |
| 3 | 0.6795 | `CO-PROD-005#004` | `CO-PROD-005` | Product Overview: TechSync Console > Who it is for | `company / PROD:Technical Writing / approved / 2026-07-22` | ## Who it is for Everyone who uses a TechSync product uses Console, from an engineer checking a deploy to a finance anal |
| 4 | 0.6708 | `PROD-WEB-005#003` | `PROD-WEB-005` | Console Ownership and Escalation Contacts > Platform issues | `team / PROD:WEB / unmarked / 2021-11-08` | ## Platform issues For problems that appear to come from the platform rather than from Console itself, escalate to Core  |
| 5 | 0.6675 | `CO-PROD-004#002` | `CO-PROD-004` | Product Overview: TechSync Insight > Availability by tier | `company / PROD:Technical Writing / approved / 2026-05-18` | ## Availability by tier Insight is generally available to **all customer tiers: Free, Team and Enterprise**. Usage limit |

## Q-DSEC-010 (contradicting | scope: org | plan: DSEC-CON-2)

- **Asker team:** `MLI` | **Hops:** `2`
- **Question:** We are taking a change to Foundry production serving to staging. Can we use the lightweight sandbox checklist?
- **Expected authoritative doc(s):** `ORG-DSEC-001`
- **Distractor doc(s):** `DSEC-MLI-002`
- **Distractor in top 5:** `True` (first distractor rank: `1`)
- **Gold answer:** No. The exception covers only the three named research sandboxes. Foundry production serving needs the full threat-model review before staging.

### Retrieved Top 5 Chunks

| Rank | Score | Chunk ID | Doc ID | Title > Heading | Scope / Owner / Status / Updated | Preview |
| ---: | ---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.7822 | `DSEC-MLI-002#004` | `DSEC-MLI-002` | Foundry Research Sandbox Security Review Exception > Lightweight checklist | `team / DSEC:MLI / approved / 2026-03-24` | ## Lightweight checklist The sandbox owner completes this once at creation and again at each six-month review: 1. Name a |
| 2 | 0.7166 | `DSEC-MLI-002#002` | `DSEC-MLI-002` | Foundry Research Sandbox Security Review Exception > Sandboxes covered | `team / DSEC:MLI / approved / 2026-03-24` | ## Sandboxes covered \| Sandbox \| Purpose \| \|---\|---\| \| `rs-nlp-explore` \| Language model experiments \| \| `rs-vision-expl |
| 3 | 0.7101 | `DSEC-MLI-002#001` | `DSEC-MLI-002` | Foundry Research Sandbox Security Review Exception > Summary | `team / DSEC:MLI / approved / 2026-03-24` | # Foundry Research Sandbox Security Review Exception **Approved by:** Rachel Goldstein, VP Data & Security \| **Approved: |
| 4 | 0.7022 | `DSEC-MLI-002#005` | `DSEC-MLI-002` | Foundry Research Sandbox Security Review Exception > Promotion | `team / DSEC:MLI / approved / 2026-03-24` | ## Promotion A sandbox workload that is to be promoted toward staging or prod, or that is given any production data, lea |
| 5 | 0.6970 | `DSEC-MLI-005#003` | `DSEC-MLI-005` | Foundry Model Serving Rollout Guide > Steps | `team / DSEC:MLI / approved / 2026-05-12` | ## Steps 1. Create the rollout: `foundry serve rollout create --model <name>:<version> --stage shadow`. 2. Compare shado |

## Q-DSEC-017 (outdated | scope: company | plan: DSEC-OUT-2)

- **Asker team:** `MLI` | **Hops:** `1`
- **Question:** A training job needs a partition that is 60 days old. Is it queryable in Quarry as it is?
- **Expected authoritative doc(s):** `CO-DSEC-007`
- **Distractor doc(s):** `DSEC-DATA-002`
- **Distractor in top 5:** `False` (first distractor rank: `N/A`)
- **Gold answer:** No. Hot storage is 30 days, so a 60-day-old partition is in archive. Open a ticket in the DATA queue to restore it.

### Retrieved Top 5 Chunks

| Rank | Score | Chunk ID | Doc ID | Title > Heading | Scope / Owner / Status / Updated | Preview |
| ---: | ---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.6967 | `PROD-SRCH-015#001` | `PROD-SRCH-015` | Design Doc: Quarry Result Caching > Context | `team / PROD:SRCH / approved / 2026-07-28` | # Design Doc: Quarry Result Caching **Author:** Staff Engineer (SRCH) **Status:** Approved ## Context Dashboards run the |
| 2 | 0.6958 | `PLAT-OBS-007#003` | `PLAT-OBS-007` | Tracewell Storage and Retention > Querying archived data | `team / PLAT:OBS / unmarked / 2024-03-05` | ## Querying archived data Archive data can't be searched from the normal Tracewell UI. To pull it: 1. File a ticket in t |
| 3 | 0.6956 | `PROD-SRCH-001#002` | `PROD-SRCH-001` | Quarry Query API Reference > Endpoint | `team / PROD:SRCH / approved / 2026-08-11` | ## Endpoint ``` POST /v1/query ``` ### Request \| Field \| Type \| Description \| \|---\|---\|---\| \| `query` \| string \| Query i |
| 4 | 0.6926 | `PROD-SRCH-011#004` | `PROD-SRCH-011` | Quarry Query Language Syntax Guide > Time | `team / PROD:SRCH / approved / 2025-12-17` | ## Time Use the time range control or `earliest=-1h latest=now` in the query. ## Examples Errors by service in the last  |
| 5 | 0.6915 | `PROD-SRCH-013#001` | `PROD-SRCH-013` | SRCH Team Onboarding Guide > First week | `team / PROD:SRCH / approved / 2026-04-17` | # SRCH Team Onboarding Guide Welcome to Search. We own Quarry, the query engine, and Sieve, the indexer. These two syste |

## Q-DSEC-021 (team_vs_company | scope: company | plan: DSEC-TVC-1)

- **Asker team:** `PAY` | **Hops:** `2`
- **Question:** A Critical finding is confirmed in Ledger Core. How long do we have to fix it, and how long for a High?
- **Expected authoritative doc(s):** `CO-DSEC-003`
- **Distractor doc(s):** `DSEC-SEC-003; CO-DSEC-004`
- **Distractor in top 5:** `True` (first distractor rank: `4`)
- **Gold answer:** Critical 7 days, High 30 days. The 3-day rule applies only to SEC-owned services.

### Retrieved Top 5 Chunks

| Rank | Score | Chunk ID | Doc ID | Title > Heading | Scope / Owner / Status / Updated | Preview |
| ---: | ---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.7170 | `PROD-PAY-015#002` | `PROD-PAY-015` | Ledger Core Tax Rate Table Update Procedure > Timeline | `team / PROD:PAY / approved / 2026-04-15` | ## Timeline \| When \| Step \| \|---\|---\| \| Six weeks before \| Finance supplies the new rates file \| \| Five weeks before \| E |
| 2 | 0.6980 | `PROD-PAY-011#002` | `PROD-PAY-011` | Payment Reconciliation Job Troubleshooting > Reading the report | `team / PROD:PAY / approved / 2026-05-14` | ## Reading the report The job writes a summary to the `#prod-payments-recon` channel: - **Matched:** counts agree. - **U |
| 3 | 0.6857 | `PROD-PAY-008#003` | `PROD-PAY-008` | Ledger Core Invoice Finalization Runbook > Checks before finalizing | `team / PROD:PAY / approved / 2026-01-12` | ## Checks before finalizing 1. Meterflow reports all windows for the period as final. 2. Reconciliation shows no unresol |
| 4 | 0.6854 | `DSEC-SEC-003#002` | `DSEC-SEC-003` | AppSec Critical Vulnerability Remediation Runbook > The 3-day clock | `team / DSEC:SEC / approved / 2025-02-11` | ## The 3-day clock \| Day \| What must happen \| \|---\|---\| \| Day 0 \| Finding confirmed. Page the SEC on-call, open a Critic |
| 5 | 0.6844 | `DSEC-SEC-003#001` | `DSEC-SEC-003` | AppSec Critical Vulnerability Remediation Runbook > Why we hold ourselves to a tighter clock | `team / DSEC:SEC / approved / 2025-02-11` | # AppSec Critical Vulnerability Remediation Runbook **Owner:** AppSec (SEC) \| **Covers:** services owned by SEC, which a |

## Q-DSEC-023 (team_vs_company | scope: company | plan: DSEC-TVC-2)

- **Asker team:** `DATA` | **Hops:** `2`
- **Question:** I'm on Data Platform and want a GPL library in an internal-only tool. Does the ITC exception let me skip legal review?
- **Expected authoritative doc(s):** `CO-DSEC-012`
- **Distractor doc(s):** `DSEC-ITC-004`
- **Distractor in top 5:** `True` (first distractor rank: `1`)
- **Gold answer:** No. The exception covers only ITC-owned internal tools. Copyleft in other teams' tools needs legal review via AppSec under the company policy.

### Retrieved Top 5 Chunks

| Rank | Score | Chunk ID | Doc ID | Title > Heading | Scope / Owner / Status / Updated | Preview |
| ---: | ---: | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.8290 | `DSEC-ITC-004#003` | `DSEC-ITC-004` | Open-Source License Exception for Internal-Only Tooling > What is allowed | `team / DSEC:ITC / approved / 2026-02-17` | ## What is allowed ITC engineers **may use GPL-licensed libraries (GPL and LGPL) in ITC internal-only tools without a pe |
| 2 | 0.7983 | `DSEC-ITC-004#005` | `DSEC-ITC-004` | Open-Source License Exception for Internal-Only Tooling > What is not covered | `team / DSEC:ITC / approved / 2026-02-17` | ## What is not covered - Anything shipped to customers. - Any tool owned by another team. - Any library under a license  |
| 3 | 0.7613 | `DSEC-ITC-004#002` | `DSEC-ITC-004` | Open-Source License Exception for Internal-Only Tooling > Why this exists | `team / DSEC:ITC / approved / 2026-02-17` | ## Why this exists ITC maintains small automation around Compass and Keystone: evidence collectors, export scripts, dire |
| 4 | 0.7605 | `DSEC-ITC-004#004` | `DSEC-ITC-004` | Open-Source License Exception for Internal-Only Tooling > Scope limits | `team / DSEC:ITC / approved / 2026-02-17` | ## Scope limits This exception applies only to tools that meet **all** of these conditions: - Owned by ITC. - Run only i |
| 5 | 0.7555 | `DSEC-ITC-004#001` | `DSEC-ITC-004` | Open-Source License Exception for Internal-Only Tooling > Open-Source License Exception for Internal-Only Tooling | `team / DSEC:ITC / approved / 2026-02-17` | # Open-Source License Exception for Internal-Only Tooling **Approved by:** Tamsin Reid (CISO) and Legal \| **Approved:**  |
