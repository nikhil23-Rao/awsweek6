doc_id: PROD-MOB-005
title: Mobile Architecture Overview
doc_type: design doc
scope_level: team
owner_team: MOB
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-01-13
supersedes:
fact_ids: 

---

# Mobile Architecture Overview

## Goals

Two native apps, one product. We want iOS and Android to feel native, share behavior where it helps and stay easy to test.

## Platform stacks

- **iOS:** Swift, SwiftUI, Combine.
- **Android:** Kotlin, Jetpack Compose, coroutines.

## Module layout

Both apps use the same module boundaries:

| Module | Responsibility |
|---|---|
| `core` | Networking, authentication, storage |
| `alerts` | Alert list, detail and acknowledge flows |
| `approvals` | Deploy approval requests and decisions |
| `settings` | Preferences and quiet hours |
| `ui-kit` | Shared visual components |

## Shared contracts

The team keeps a shared API schema, and both apps generate their network models from it. Analytics events are defined once in the Analytics Event Catalog.

## Data flow

Screens observe view models, which call use cases, which call repositories. Repositories decide between the network and local storage.

## Notifications

The apps register for push notifications on first launch. Incoming notifications open the relevant alert or approval screen.

## Testing

Unit tests for view models and use cases; snapshot tests for key screens; a small suite of UI tests for core journeys.

## Decisions pending

Moving shared business rules into a common library is under discussion.
