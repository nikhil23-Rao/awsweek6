doc_id: PROD-WEB-007
title: Prism Color Tokens and Theming Reference
doc_type: reference
scope_level: team
owner_team: WEB
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-05-06
supersedes:
fact_ids: 

---

# Prism Color Tokens and Theming Reference

## Why tokens

Design tokens give a name to each color so that themes can change without touching components. Components refer to tokens, never to raw values.

## Token families

| Family | Example | Used for |
|---|---|---|
| `color.bg` | `color.bg.surface` | Page and card backgrounds |
| `color.text` | `color.text.primary` | Body and heading text |
| `color.border` | `color.border.subtle` | Dividers and outlines |
| `color.accent` | `color.accent.default` | Buttons and links |
| `color.status` | `color.status.danger` | Success, warning, danger, info |

## Themes

Prism ships a light theme and a dark theme. Each theme maps every token to a value. A component that uses only tokens works in both.

## Dark mode

- Do not invert colors automatically; use the dark values defined for each token.
- Check status colors on dark backgrounds, because yellows and reds often need adjusting.
- Images with transparent backgrounds should be checked in both themes.

## Adding a token

Propose it in a Jira ticket with the intended use and values for both themes. New tokens must meet contrast requirements in both.

## Where tokens live

Tokens are defined in the `prism-tokens` package and compiled to CSS variables and a TypeScript map.
