doc_id: ORG-PROD-018
title: Product Test Strategy Standard
doc_type: standard
scope_level: org
owner_team: PROD
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2025-09-30
supersedes:
fact_ids: 

---

# Product Test Strategy Standard

## Principles

Tests exist to give us confidence to change code. Prefer fast, reliable tests close to the code, and a few end-to-end tests for the journeys customers depend on.

## The test pyramid

| Layer | Purpose | Share of tests |
|---|---|---|
| Unit | Logic in isolation | Most |
| Integration | Components with real dependencies such as a database | Some |
| End-to-end | Key customer journeys | Few |

## Expectations

- New code ships with tests. Bug fixes ship with a test that fails without the fix.
- Teams aim for at least 80% line coverage on new code. Coverage is a prompt for conversation, not a goal in itself.
- Tests must not depend on the network, wall-clock time or execution order.
- A flaky test is fixed or removed within one sprint.

## Environments

Integration tests run against containers in CI. End-to-end tests run in staging after each merge to the main branch.

## Reporting

Each team reviews its flaky-test list and test duration at the end of every sprint.

## Questions

Ask a Staff Engineer on your team, or post in #prod-quality.
