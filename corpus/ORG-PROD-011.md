doc_id: ORG-PROD-011
title: Product API Design Guidelines
doc_type: guideline
scope_level: org
owner_team: PROD
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2025-07-22
supersedes:
fact_ids: 

---

# Product API Design Guidelines

A consistent API is easier to learn. These guidelines cover shape and naming. They do not cover the lifecycle of versions.

## Resources and naming

- Use plural nouns for collections: `/invoices`, `/queries`.
- Use lower snake case for field names; use ISO 8601 for timestamps in UTC.
- Identifiers are opaque strings. Do not encode meaning in them.

## Pagination

Collections use cursor-based pagination. Responses include `next_cursor`; clients pass it back as `cursor`. Page size is set with `limit`, with a documented default and maximum.

## Filtering and sorting

Filter with query parameters named for the field (`status=open`). Sort with `sort=created_at` or `sort=-created_at` for descending.

## Errors

Use the standard error body from the Error Handling and Logging Conventions. Use HTTP status codes for the class of error and the `code` field for the specific cause.

## Idempotency

`POST` operations that create billable or irreversible effects accept an `Idempotency-Key` header and return the original result when it is repeated.

## Documentation

Every endpoint is described in OpenAPI, with an example request and response, before it ships.
