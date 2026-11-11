doc_id: PROD-SRCH-012
title: Sieve Schema Mapping Guide
doc_type: draft guide
scope_level: team
owner_team: SRCH
owner_org: PROD
author_role: Staff Engineer
status: draft
last_updated: 2026-09-05
supersedes:
fact_ids: 

---

# Sieve Schema Mapping Guide

> Draft. Not reviewed. Examples may change.

## What is a mapping?

A mapping tells Sieve how to turn incoming records into fields in an index: names, types and whether a field is searchable.

## Default mapping

If an account has no mapping, Sieve uses dynamic mapping: strings become text and keyword fields, numbers become numeric, and timestamps are detected.

## Defining your own

A mapping file looks like this:

```
fields:
  - name: timestamp
    type: date
  - name: level
    type: keyword
  - name: message
    type: text
  - name: duration_ms
    type: long
```

## Field types

| Type | Use for |
|---|---|
| `keyword` | Exact matches, grouping |
| `text` | Full-text search |
| `long`, `double` | Numbers |
| `date` | Time values |
| `ip` | IP addresses |

## Changing a mapping

Adding a field is easy. Changing the type of an existing field needs a reindex.

## TODO

- Describe nested fields
- Explain how mapping versions are rolled out
- Add guidance on field count limits
- Review with the Tech Lead
