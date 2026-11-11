doc_id: PROD-SRCH-001
title: Quarry Query API Reference
doc_type: API reference
scope_level: team
owner_team: SRCH
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-08-11
supersedes:
fact_ids: F-PROD-006

---

# Quarry Query API Reference

**Owner:** Search (SRCH)  **Audience:** engineers calling Quarry

## Overview

Quarry executes search and analytics queries over data indexed by Sieve. This page documents the query endpoint and its limits.

## Endpoint

```
POST /v1/query
```

### Request

| Field | Type | Description |
|---|---|---|
| `query` | string | Query in Quarry Query Language |
| `time_range` | object | `start` and `end`, ISO 8601 |
| `limit` | integer | Maximum rows to return (default 1,000; maximum 10,000) |
| `timeout_ms` | integer | Optional per-request timeout |

### Response

Returns `rows`, `stats` (scanned, matched, took_ms) and a `cursor` when more rows are available.

## Limits

- **Default query timeout: 120 seconds.** A request may set a lower `timeout_ms`; it may not exceed the maximum configured for the account.
- Maximum query length: 8,192 characters.
- Concurrent queries per account: 20.

## Errors

| Code | Meaning |
|---|---|
| `INVALID_QUERY` | The query could not be parsed |
| `TIMEOUT` | The query ran longer than the timeout |
| `RATE_LIMITED` | Too many concurrent queries |

## Pagination

Pass the `cursor` from a response to fetch the next page.

## Versioning

This is version 1 of the API. Changes follow the Product API Versioning Standard.
