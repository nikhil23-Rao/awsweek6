doc_id: PROD-WEB-014
title: Console Localization Guide
doc_type: guide
scope_level: team
owner_team: WEB
owner_org: PROD
author_role: Staff Engineer
status: draft
last_updated: 2026-08-03
supersedes:
fact_ids: 

---

# Console Localization Guide

> Draft. Sections marked TODO are not finished.

## Goal

Make Console usable in more languages without changing application code for each one.

## Strings

All user-visible text lives in locale files, not in components. Each string has a key, the default English text, and an optional description for translators.

```
dashboard.empty.title = "No dashboards yet"
```

## Extracting strings

Run the extraction script to collect new keys from the source into the base locale file. Commit the updated file with your change.

## Locale files

One JSON file per language under `locales/`. Missing keys fall back to English.

## Formatting

Use the formatting helpers for dates, numbers and currencies so they follow the user's locale. Do not concatenate sentences from fragments.

## Right-to-left languages

TODO: describe layout mirroring and which Prism components are ready.

## Translation workflow

TODO: agree on the vendor and how translations come back into the repository.

## Testing

TODO: pseudo-localization build for catching hard-coded strings.

## Open questions

- Which languages come first?
- How do we handle plural rules for languages with several forms?
