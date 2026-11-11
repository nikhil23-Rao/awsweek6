---
doc_id: PLAT-DEVT-014
title: Writing a New Scaffold Template
doc_type: how-to guide
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-07-29
supersedes: ""
fact_ids: ""
---

# Writing a New Scaffold Template

Developer Tooling, Staff Engineer

Most teams never need a new template. If your language or framework is already covered, use the existing template and customize after generation. If you need something genuinely new (a new language, or a service shape we don't support), this guide is for you.

## Talk to us first

Open a thread in #devt-scaffold describing what you need and why existing templates don't fit. We'll tell you if something similar is in progress.

## Repository layout

Templates live in `scaffold-templates`:

```
common/          # shared manifests, dashboards, alerts, pipeline
templates/
  go-http/
  py-worker/
  your-template/
    template.yaml
    files/
```

## `template.yaml`

```yaml
name: rust-http
description: HTTP API in Rust
inputs:
  - name
  - team
uses_common: [manifests, dashboards, alerts, pipeline]
```

## Files

Files under `files/` are rendered with Go templates. Use `{{ .Name }}` and `{{ .Team }}`.

## Requirements for new templates

- Health endpoints (`/healthz`, `/readyz`).
- Graceful shutdown on SIGTERM.
- Tracewell instrumentation and the standard logger.
- A Dockerfile using an approved base image.
- Unit tests that pass in Gatekeeper CI.
- Use the `common/` components instead of copying them.

## Testing

`make test-template NAME=your-template` generates a service, builds it on Forge, and deploys it to a scratch namespace in dev.

## Ownership

The contributing team co-owns the template with DEVT and is listed in CODEOWNERS for its directory.
