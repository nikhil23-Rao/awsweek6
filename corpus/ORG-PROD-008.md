doc_id: ORG-PROD-008
title: Error Handling and Logging Conventions
doc_type: standard
scope_level: org
owner_team: PROD
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2025-08-14
supersedes:
fact_ids: 

---

# Error Handling and Logging Conventions

## Errors

- Every API error returns a JSON body with `code`, `message` and `request_id`.
- Error codes are upper snake case and stable: `INVALID_ARGUMENT`, `NOT_FOUND`, `RATE_LIMITED`.
- Messages are written for the caller, not for us. Never include stack traces, SQL or internal hostnames.
- Retryable errors should say so with a `retryable` flag.

## Logs

Services write structured JSON logs to standard output. Required fields:

| Field | Meaning |
|---|---|
| `ts` | UTC timestamp, ISO 8601 |
| `level` | debug, info, warn or error |
| `service` | Service name |
| `request_id` | Correlation ID, propagated across services |
| `msg` | Short human-readable message |

## Levels

- **error:** something failed and needs attention.
- **warn:** something unexpected happened but the request succeeded.
- **info:** normal significant events.
- **debug:** developer detail, off by default in production.

## What never goes in a log

Passwords, tokens, full payment card numbers, and message bodies containing customer content. If in doubt, log an identifier instead.

## Tracing

Propagate the trace context headers on every outbound call so that Tracewell can stitch a request together.
