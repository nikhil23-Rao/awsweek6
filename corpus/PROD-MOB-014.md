doc_id: PROD-MOB-014
title: Mobile Analytics Event Catalog
doc_type: reference
scope_level: team
owner_team: MOB
owner_org: PROD
author_role: Staff Engineer
status: draft
last_updated: 2026-09-02
supersedes:
fact_ids: 

---

# Mobile Analytics Event Catalog

> Draft. Event names and properties may change before the catalog is approved.

## Conventions

- Event names are lower snake case, in the form `object_action`: `alert_opened`, `approval_submitted`.
- Properties use lower snake case.
- Do not send personal data. Use opaque identifiers.

## Events

| Event | When it fires | Properties |
|---|---|---|
| `app_opened` | App comes to foreground | `source` (icon, notification) |
| `alert_opened` | User opens an alert | `severity`, `source` |
| `alert_acknowledged` | User acknowledges an alert | `severity`, `time_to_ack_ms` |
| `approval_viewed` | User opens an approval request | `pipeline_id` |
| `approval_submitted` | User approves or rejects | `decision`, `pipeline_id` |
| `preferences_changed` | User saves preferences | `group` |

## To be decided

- Whether to include the app version in each event or add it at ingest.
- How to handle events sent while offline.
- Names for the quiet hours events.

## Sampling

None for now.

## Ownership

Staff Engineer, Mobile. Comments in the Confluence page.
