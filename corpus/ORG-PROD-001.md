doc_id: ORG-PROD-001
title: Product Engineering Team Directory and Escalation Paths
doc_type: directory
scope_level: org
owner_team: PROD
owner_org: PROD
author_role: TPM
status: approved
last_updated: 2026-03-05
supersedes: PROD-WEB-005
fact_ids: F-PROD-008

---

# Product Engineering Team Directory and Escalation Paths

Product Engineering (PROD) is led by VP Carlos Mendoza and has four teams. This directory lists who owns what and where to go when something needs attention. It is maintained by the TPM function and reviewed each quarter.

## Teams and owned systems

| Team | Code | Engineering Manager | Tech Lead | Owns |
|---|---|---|---|---|
| Web | WEB | Aisha Karim | Jonas Berg | Console, Prism design system |
| Mobile | MOB | Elena Petrova | Wei Chen | TechSync Mobile, Pushline |
| Payments | PAY | Samuel Adeyemi | Mira Kowalski | Ledger Core, Meterflow |
| Search | SRCH | Yuki Tanaka | Diego Fuentes | Quarry, Sieve |

## Who to contact

- **Console behavior, UI defects, Prism components:** the Web team, in #prod-web.
- **Mobile apps and Pushline delivery:** the Mobile team, in #prod-mobile.
- **Invoices, usage metering, billing questions:** the Payments team, in #prod-payments.
- **Search, indexing and query behavior:** the Search team, in #prod-search.

## Platform escalations

Product teams run on platform services owned by Platform Engineering. For cluster-level problems on Kestrel or build-runner problems on Forge, escalate to the Platform Compute team (Engineering Manager Marcus Oyelaran, Tech Lead Lin Zhao) in #comp-help. Console platform issues follow the same route: the Web team triages first, and Compute is brought in when the cause is in the cluster.

## Cross-org functions

Technical Program Management coordinates work that spans teams. The SRE guild supports reliability practice, and the Architecture Review Board, chaired by the CTO, reviews decisions that matter beyond one team.

## Keeping this page current

Engineering Managers should tell the TPM of any change in ownership or contacts within one week.
