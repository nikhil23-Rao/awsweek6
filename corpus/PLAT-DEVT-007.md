---
doc_id: PLAT-DEVT-007
title: Flaky Test Quarantine Policy
doc_type: policy
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: Engineering Manager
status: approved
last_updated: 2025-09-30
supersedes: ""
fact_ids: ""
---

# Flaky Test Quarantine Policy

**Owner:** Developer Tooling
**Applies to:** all repositories built through Gatekeeper CI

## Problem

A flaky test passes and fails on the same code. Flaky tests waste Forge time, block merges for unrelated changes, and train engineers to click "retry" without reading failures.

## Detection

Gatekeeper CI tracks every test's result history. A test is marked **flaky** when it both passes and fails on the same commit, three or more times in 7 days.

## Quarantine

When a test is marked flaky:

1. Gatekeeper CI moves it to quarantine automatically. Quarantined tests still run, but their failures don't block merges.
2. A Jira ticket is opened for the owning team (from CODEOWNERS) with the failure history.
3. The team gets a Slack notification.

## Fixing

- The owning team has **14 days** to fix or delete a quarantined test.
- After 14 days, the ticket is escalated to the team's engineering manager.
- After 30 days, the test is disabled entirely, and the ticket stays open.

## Coverage warning

Quarantined tests aren't protecting anything. If a test covers critical behavior (payments, billing calculation, auth), fix it first.

## Leaving quarantine

Once fixed, the test must pass 50 consecutive runs before it leaves quarantine automatically.

## Reports

The weekly DEVT reliability report lists each team's quarantined test count.
