doc_id: PROD-MOB-015
title: Design Doc: Offline Alert Cache
doc_type: design doc
scope_level: team
owner_team: MOB
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-06-18
supersedes:
fact_ids: 

---

# Design Doc: Offline Alert Cache

**Author:** Staff Engineer (MOB)  **Status:** Approved by the Mobile Tech Lead

## Context

When a phone has no signal, the alerts screen is empty even for alerts the user has already seen. People on call often check alerts in basements, elevators or on planes.

## Goals

- Show the most recent alerts without a network connection.
- Keep the data fresh when the network returns.
- Keep storage small and secure.

## Non-goals

Acknowledging alerts offline. That needs separate design.

## Proposal

Store the latest 200 alerts in an on-device database (SQLite via Room on Android and Core Data on iOS). Each alert records its ID, title, severity, time and state.

On launch, the app shows cached alerts immediately and refreshes in the background. When the refresh completes, the list updates in place.

## Security

The database is stored in the app's protected storage and cleared on sign-out. Alert bodies are not cached, only summaries.

## Alternatives

1. **No cache.** Simple, but poor experience.
2. **Cache everything.** More useful, but a bigger privacy and storage cost.

## Risks

Stale data may mislead. The screen will show "last updated" and an offline badge.

## Rollout

Behind a feature flag; internal beta first.
