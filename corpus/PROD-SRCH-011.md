doc_id: PROD-SRCH-011
title: Quarry Query Language Syntax Guide
doc_type: reference
scope_level: team
owner_team: SRCH
owner_org: PROD
author_role: Tech Lead
status: approved
last_updated: 2025-12-17
supersedes:
fact_ids: 

---

# Quarry Query Language Syntax Guide

A short reference to the Quarry Query Language (QQL).

## Basic form

```
source=app-logs level=error | stats count() by service
```

A query is a source, optional filters, then pipe-separated commands.

## Filters

| Syntax | Meaning |
|---|---|
| `field=value` | Equals |
| `field!=value` | Not equals |
| `field>10` | Greater than |
| `field~"abc*"` | Wildcard match |
| `field in (a,b,c)` | One of a list |

Combine filters with `AND`, `OR` and parentheses. A space between filters means `AND`.

## Commands

- `stats count() by field`: group and count.
- `sort -field`: sort descending.
- `head 20`: first 20 rows.
- `fields a,b`: keep only these columns.
- `rename a as b`: rename a column.
- `dedup field`: remove duplicate values.
- `eval total=a+b`: compute a new field.

## Time

Use the time range control or `earliest=-1h latest=now` in the query.

## Examples

Errors by service in the last hour:
```
source=app-logs level=error earliest=-1h | stats count() by service | sort -count
```

Slowest requests:
```
source=requests | sort -duration_ms | head 10
```

## Tips

Put the most selective filters first, and select only the fields you need.
