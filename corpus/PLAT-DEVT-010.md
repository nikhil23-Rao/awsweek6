---
doc_id: PLAT-DEVT-010
title: Scaffold CLI Reference
doc_type: reference
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: Technical Writer
status: approved
last_updated: 2026-06-24
supersedes: ""
fact_ids: ""
---

# Scaffold CLI Reference

*Technical Writing, Developer Tooling*

## Install

Installed with TechSync Dev Tools. Check your version with `scaffold version`.

## Commands

### `scaffold new`

Create a new service from a template.

```
scaffold new --template <name> --name <service> --team <CODE> [--dir <path>]
```

| Flag | Description |
|---|---|
| `--template` | `go-grpc`, `go-http`, `py-worker`, `ts-bff`, `kotlin-service` |
| `--name` | Service name, lowercase with hyphens |
| `--team` | Owning team code |
| `--dir` | Output directory (defaults to the service name) |

### `scaffold upgrade`

Show and optionally apply changes from the latest template version.

```
scaffold upgrade [--apply] [--only <component>]
```

Components: `manifests`, `pipeline`, `dashboards`, `alerts`, `code`.

### `scaffold pipeline init`

Generate a `gatekeeper.yaml` for an existing repo.

### `scaffold ns describe`

Show a Kestrel namespace's labels, policies, and resource settings.

```
scaffold ns describe <namespace> --env <dev|staging|prod>
```

### `scaffold doctor`

Check your local toolchain. `--fix-git` sets up Git signing.

### `scaffold templates list`

List available templates and their versions.

## Global flags

- `--verbose`: print debug output.
- `--json`: machine-readable output where supported.

## Exit codes

| Code | Meaning |
|---|---|
| 0 | Success |
| 1 | User error (bad flags, missing files) |
| 2 | Remote error (GitHub, Kestrel, or Ship unreachable) |

## Reporting bugs

#devt-scaffold, with the command and `--verbose` output.
