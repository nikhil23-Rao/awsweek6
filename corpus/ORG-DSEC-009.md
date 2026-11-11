doc_id: ORG-DSEC-009
title: DSEC Architecture Principles
doc_type: standard
scope_level: org
owner_team: none (DSEC org-wide)
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2025-08-19
supersedes:
fact_ids:

# DSEC Architecture Principles

These principles guide design in Data & Security. They are not rules to be applied mechanically; they are the questions a design reviewer will ask, and the answers they will want to hear. We keep them short so that people remember them.

## 1. Safe by default

The easiest way to use a system should also be the safest. Defaults should be restrictive, secrets should never appear in code or configuration files, and a new service should get least privilege without anyone asking. If a design requires users to remember a security step, ask how to automate it.

## 2. Minimize the data you hold

Collect and keep only what you need. Prefer derived or aggregated data to raw data when it serves the purpose. Every copy of customer-derived data is a liability that has to be protected, tracked, and eventually removed.

## 3. Make failure cheap

Assume dependencies will fail. Design so that a failed component degrades one feature, not the whole service. Prefer timeouts, retries with backoff, and idempotent operations. A job that can safely run twice is worth more than a clever job that must run once.

## 4. Boring technology

We run on Kubernetes on EKS, PostgreSQL, Kafka, OpenSearch, and Terraform for a reason. Use the established stack unless a design shows a need it cannot meet. A new technology needs an owner, a support plan, and a way out.

## 5. Observable from day one

A system you cannot see is a system you cannot fix. Emit structured logs, expose metrics, and propagate trace context from the first deployed version. Alerts must have an owner and an action; an alert nobody can act on is noise.

## 6. Design for the operator

Write the runbook while designing the system. If the runbook is hard to write, the system is hard to operate. Include the failure modes, the dashboards, and the rollback path.

## 7. Compatible by default

Other teams build on our interfaces. Prefer additive changes, version interfaces explicitly, and give consumers time to migrate. Breaking a consumer without notice costs more trust than the change is worth.

## 8. Mind the regions

Our primary region is us-east-1, with disaster recovery in us-west-2 and EU customer data in eu-west-1. Designs must say where data lives and how it moves between regions.

## 9. Cost is a design constraint

Estimate cost in the design, in order of magnitude. A design that scales cost linearly with a growing dataset needs a plan for the day the bill is a surprise.

## 10. Write it down

Decisions with long-term consequences are recorded so that new team members can understand why a system looks the way it does. A decision that lives only in someone's head disappears when they change teams.

## Review checklist

Reviewers will ask:

- What are the trust boundaries, and who can cross them?
- What data does it hold, and where?
- What happens when each dependency is down?
- How do we know it is working?
- How does an operator roll it back?
- What does it cost at ten times today's load?
- Which interface does another team consume, and is that interface documented?

## Using this document

Bring these principles to the design review as a starting point. If a design departs from one, explain why; reviewers are looking for a reasoned answer, not for compliance.
