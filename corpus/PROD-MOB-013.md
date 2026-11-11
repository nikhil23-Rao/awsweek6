doc_id: PROD-MOB-013
title: Mobile Strings and Localization Workflow
doc_type: how-to
scope_level: team
owner_team: MOB
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-03-31
supersedes:
fact_ids: 

---

# Mobile Strings and Localization Workflow

How text gets from a developer's keyboard to a translated app.

## Principles

- No user-visible text is hard-coded in views.
- Every string has a key and a comment for translators.
- Sentences are never built by joining pieces.

## iOS

Strings live in `Localizable.strings` and `Localizable.stringsdict` (for plurals). Use `String(localized:)` in code.

## Android

Strings live in `res/values/strings.xml` with translations in `values-xx/`. Use plurals resources for counts.

## Steps

1. Add the string in the base language with a comment.
2. Run the sync script to push new strings to the translation tool.
3. Translators work on the new strings. Reviewers check them in context using screenshots.
4. When translations are complete, the sync script opens a pull request.
5. A teammate reviews the pull request and merges it.

## Checking your work

Use the pseudo-localization build to find hard-coded text and layouts that break with long words.

## Languages

The current language list is kept in the repository's `LANGUAGES.md`.

## Contact

Ask the Staff Engineer who owns localization.
