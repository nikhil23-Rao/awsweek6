doc_id: CO-PROD-013
title: Product and Engineering Glossary
doc_type: reference
scope_level: company
owner_team: Technical Writing
owner_org: PROD
author_role: Technical Writer
status: approved
last_updated: 2026-06-09
supersedes:
fact_ids:

---

# Product and Engineering Glossary

A quick reference for terms you will meet in TechSync documents. Where a term has its own policy, the entry points you there instead of restating it.

## Environments

| Term | Meaning |
|---|---|
| dev | Where engineers try changes first |
| staging | A production-like environment for final checks |
| prod | What customers use |

## Incident severities

| Level | Rough meaning |
|---|---|
| Sev1 | Most serious customer-facing impact |
| Sev2 | Significant impact, workaround may exist |
| Sev3 | Limited impact |
| Sev4 | Minor issue, no customer-visible effect |

## Systems (a selection)

| Name | What it is |
|---|---|
| Kestrel | Internal Kubernetes platform |
| Forge | Build runners |
| Meridian Mesh | Service mesh |
| EdgeGate | API gateway and ingress |
| Lookout | Alerting and paging |
| Tracewell | Tracing pipeline |
| Scaffold | Service templates and CLI |
| Gatekeeper CI | Deploy pipeline |
| Pushline | Notification service |
| Ledger Core | Billing engine |
| Meterflow | Usage metering |
| Quarry | Query engine |
| Sieve | Indexer |
| Reservoir | Data lake |
| Streamline | Kafka event bus |
| Foundry | ML training and serving |
| Vaultline | Secrets management |
| Keystone | SSO and IAM |
| Compass | Compliance evidence tracker |

## General terms

- **ADR:** Architecture Decision Record. See the ADR Policy.
- **ARB:** the Architecture Review Board.
- **RPO / RTO:** how much data we can lose, and how long we can take to recover, in a disaster. See the disaster recovery policy.
- **SLA:** the commitment made to customers. See the Customer SLA.
- **Tier:** a measure of how critical a service is. See the Service Tiering Policy.
- **TPM:** Technical Program Manager.
- **Prism:** TechSync's design system.

## Suggesting changes

Technical Writing maintains this page. Send additions through the documentation request form.
