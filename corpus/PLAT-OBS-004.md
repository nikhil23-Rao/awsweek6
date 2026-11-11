---
doc_id: PLAT-OBS-004
title: Tracewell SDK Onboarding Guide (Go, Python, TypeScript)
doc_type: onboarding guide
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: Technical Writer
status: approved
last_updated: 2025-10-06
supersedes: ""
fact_ids: ""
---

# Tracewell SDK Onboarding Guide (Go, Python, TypeScript)

*Technical Writing with Observability*

Tracewell gives you distributed traces across TechSync services. Scaffold-generated services already include the SDK; this guide is for older services or anyone who wants to understand what's happening.

## Concepts

- A **trace** is the full path of one request across services.
- A **span** is one unit of work inside that path, like an HTTP handler or a database query.
- **Context propagation** passes the trace ID from service to service in request headers. Meridian Mesh forwards the headers; your code must pass context along inside the process.

## Go

```go
import "techsync.io/tracewell/go"

func main() {
    shutdown := tracewell.Init(tracewell.Config{Service: "quarry-api"})
    defer shutdown()
}
```

Wrap handlers with `tracewell.HTTPMiddleware`. Pass `ctx` into every downstream call.

## Python

```python
import tracewell
tracewell.init(service="ledger-exports")
```

The SDK auto-instruments `requests`, `httpx`, `psycopg`, and the Streamline Kafka client.

## TypeScript

```ts
import { init } from "@techsync/tracewell";
init({ service: "console-bff" });
```

Call `init` before importing your HTTP framework so auto-instrumentation can patch it.

## Adding custom spans

Add spans around expensive work you want to see:

```python
with tracewell.span("render_invoice_pdf", attrs={"invoice_id": inv.id}):
    render(inv)
```

Don't put customer personal data in span attributes. Use IDs.

## Verifying

Deploy to dev, send a request, and search by service in the Tracewell UI. You should see spans within a minute.

## Help

#obs-tracewell
