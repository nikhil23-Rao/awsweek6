---
doc_id: PLAT-OBS-014
title: Log-to-Trace Correlation How-To
doc_type: how-to guide
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: Technical Writer
status: approved
last_updated: 2025-08-19
supersedes: ""
fact_ids: ""
---

# Log-to-Trace Correlation How-To

*Technical Writing with Observability*

When you find a suspicious log line, you usually want the full trace for that request. When you're looking at a slow trace, you want the logs from that request. Tracewell links the two if your logs include the trace ID.

## Step 1: Use the standard logging libraries

The TechSync logging libraries for Go (`techsync.io/log`), Python (`techsync_log`), and TypeScript (`@techsync/log`) automatically add `trace_id` and `span_id` to every log line, as long as there's an active Tracewell context.

## Step 2: Pass context through your code

In Go, pass `ctx` to the logger:

```go
log.Info(ctx, "invoice rendered", "invoice_id", id)
```

In Python, the context is picked up automatically from the current task or thread. If you hand work to a thread pool, use `tracewell.wrap()` so context goes with it.

## Step 3: Check it's working

Search for your service's logs in Tracewell. Lines with trace context show a **View trace** link. If the field is empty, the log call happened outside an active span.

## From trace to logs

Open a trace and click any span. The **Logs** tab shows log lines with that span ID, across every service in the trace.

## Common gaps

- **Background jobs** without an incoming request have no trace. Start a span at the beginning of each job iteration.
- **Kafka consumers** on Streamline need the Tracewell Kafka middleware to continue traces from producers.
- **Third-party libraries** using their own loggers won't include trace IDs. Route them through the standard logger where possible.

## Help

#obs-tracewell
