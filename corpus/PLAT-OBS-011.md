---
doc_id: PLAT-OBS-011
title: Tracewell Sampling Configuration
doc_type: reference
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: Tech Lead
status: approved
last_updated: 2026-06-02
supersedes: ""
fact_ids: ""
---

# Tracewell Sampling Configuration

Observability, Tracewell tech lead

Tracewell doesn't keep every trace. Sampling keeps costs reasonable while making sure the traces you need for debugging are there. This page describes how sampling works and how to adjust it for your service.

## Head sampling

The SDK makes an initial decision when a trace starts, at the service that receives the request from EdgeGate. The default head sampling rate is 10%. The decision travels with the trace, so every downstream service follows it.

## Tail sampling

Collectors make a second decision after a trace is complete. Tail sampling **always keeps**:

- Traces containing any span with an error status.
- Traces slower than the service's latency threshold (default p99 of the last hour).
- Traces with the `tracewell.keep=true` attribute.

Everything else is kept at the head sampling rate.

## Per-service overrides

In your service's `tracewell.yaml`:

```yaml
sampling:
  head_rate: 0.25
  latency_threshold_ms: 800
```

Low-traffic services often raise the head rate to 100%. High-traffic services (Meterflow, EdgeGate) run at 1% to 2%.

## Forcing a trace

For debugging, send the header `X-Tracewell-Force: 1` on a request. The trace is kept regardless of sampling. Only works from internal networks.

## What sampling does not affect

Logs aren't sampled. Metrics aren't sampled.

## Changing defaults

Changes to the default rates go through OBS review, because they affect storage cost across the company.
