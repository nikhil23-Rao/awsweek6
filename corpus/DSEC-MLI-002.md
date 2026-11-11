doc_id: DSEC-MLI-002
title: Foundry Research Sandbox Security Review Exception
doc_type: policy exception
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: Security Engineer
status: approved
last_updated: 2026-03-24
supersedes:
fact_ids: F-DSEC-006

# Foundry Research Sandbox Security Review Exception

**Approved by:** Rachel Goldstein, VP Data & Security | **Approved:** March 2026 | **Owner:** ML Infrastructure (MLI)

## Summary

Researchers using Foundry need to spin up exploratory environments quickly. The full threat-model security review that DSEC requires before a service reaches staging is too heavy for short-lived experimentation. This document grants a narrow exception: the three **named Foundry research sandboxes** listed below complete a **lightweight checklist** instead of the full review.

## Sandboxes covered

| Sandbox | Purpose |
|---|---|
| `rs-nlp-explore` | Language model experiments |
| `rs-vision-explore` | Image model experiments |
| `rs-tabular-explore` | Tabular modeling experiments |

No other Foundry environment is covered. In particular, Foundry production serving, FeatureHub, and any service that is customer-facing are **not** covered and follow the full review.

## Conditions

All of the following must remain true. If any stops being true, the exception ends for that sandbox immediately.

- The sandbox is not customer-facing.
- It contains **no production data**. Only public or synthetic datasets may be loaded.
- It has no network path to production systems, enforced by a deny-egress network policy in Kestrel.
- It holds no production credentials from Vaultline.
- It never runs in the staging or prod environments.

## Lightweight checklist

The sandbox owner completes this once at creation and again at each six-month review:

1. Name a human owner and backup.
2. Attest that no production data is present, with the dataset inventory attached.
3. Confirm the deny-egress policy is applied.
4. Confirm no production secrets are mounted.
5. Confirm Keystone group access is limited to named researchers.
6. A MLI Security Engineer countersigns in the checklist ticket.

## Promotion

A sandbox workload that is to be promoted toward staging or prod, or that is given any production data, leaves this exception and must pass the full DSEC review first.

## Contact

Questions go to the MLI Engineering Manager or the MLI Security Engineer on rotation.
