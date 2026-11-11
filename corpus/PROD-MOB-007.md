doc_id: PROD-MOB-007
title: Alert Preferences UX Spec
doc_type: spec
scope_level: team
owner_team: MOB
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-02-16
supersedes:
fact_ids: 

---

# Alert Preferences UX Spec

**Status:** Approved for implementation

## Problem

Users on call want fewer, better notifications. Today, preferences are a single list, which makes it hard to tell which settings matter.

## Goals

1. Let people choose alerts by severity.
2. Let them set quiet hours without turning everything off.
3. Make the effect of each setting obvious.

## Screens

### Preferences home
A list of groups: Alerts, Approvals, Quiet hours. Each row shows its current summary (for example, "Sev1 and Sev2").

### Alerts
A control for each severity, Sev1 to Sev4, with three options: **Interrupt**, **Quiet**, **Off**. A preview line shows what each choice means ("Sound and banner" and so on).

### Quiet hours
Start time, end time and days. A toggle allows Sev1 alerts to break through.

### Approvals
Pipelines the user can approve, each with an on/off toggle.

## Behavior

- Changes save immediately and show a brief confirmation.
- Preferences sync across the user's devices.
- Defaults: Sev1 and Sev2 interrupt; Sev3 quiet; Sev4 off.

## Accessibility

All controls are labeled and operable with a screen reader. Option summaries are read aloud.

## Open questions

Do we need per-service overrides in the first release?
