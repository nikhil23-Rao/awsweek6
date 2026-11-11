---
doc_id: PLAT-OBS-010
title: Lookout Alert Rule Authoring Guide
doc_type: how-to guide
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2026-02-11
supersedes: ""
fact_ids: ""
---

# Lookout Alert Rule Authoring Guide

Observability, Staff Engineer

Good alerts page people for things that matter and nothing else. This guide shows how to write rules in `lookout/rules.yaml`.

## Anatomy of a rule

```yaml
- name: QuarryAPIHighErrorRate
  expr: |
    sum(rate(http_requests_total{service="quarry-api",code=~"5.."}[5m]))
      / sum(rate(http_requests_total{service="quarry-api"}[5m])) > 0.02
  for: 10m
  severity: page
  labels:
    team: SRCH
  annotations:
    summary: "Quarry API error rate above 2%"
    runbook: "https://confluence.internal.techsync.io/srch/runbooks/quarry-api"
```

## Rules of thumb

1. **Alert on symptoms, not causes.** Page on errors and latency users feel. Send high CPU to a ticket, not a page.
2. **Use `for:`** to avoid paging on brief blips. Ten minutes is a sensible default for error rates.
3. **Every paging rule needs a runbook link.** Gatekeeper CI rejects paging rules without one.
4. **Prefer SLO burn-rate alerts** where you have SLOs defined.
5. **Keep label cardinality low.** Don't put pod names or request IDs in labels.

## Severity values

| `severity` | Goes to |
|---|---|
| `page` | PagerDuty, pages the on-call |
| `ticket` | Creates a Jira ticket for the owning team |
| `info` | Slack channel only |

## Testing rules

Run `lookout rules test` locally against recorded metrics. In dev, rules route to Slack only.

## Reviews

OBS reviews new paging rules for teams that ask. Every team should review its own rules twice a year and delete ones that never lead to action.
