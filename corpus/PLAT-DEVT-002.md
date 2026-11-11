---
doc_id: PLAT-DEVT-002
title: Gatekeeper CI Pipeline YAML Reference
doc_type: reference
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: Technical Writer
status: approved
last_updated: 2026-08-05
supersedes: ""
fact_ids: ""
---

# Gatekeeper CI Pipeline YAML Reference

*Technical Writing with Developer Tooling*

Every repository deployed through Gatekeeper CI has a `gatekeeper.yaml` at its root. This reference describes every top-level key.

## Minimal example

```yaml
service: quarry-api
team: SRCH
namespace: srch-quarry
build:
  dockerfile: Dockerfile
  pool: forge-standard
test:
  - name: unit
    run: make test
deploy:
  environments: [dev, staging, prod]
```

## Top-level keys

| Key | Required | Description |
|---|---|---|
| `service` | yes | Service name as registered in Ship |
| `team` | yes | Owning team code |
| `namespace` | yes | Kestrel namespace |
| `build` | yes | How to build the image |
| `test` | no | List of test steps |
| `scan` | no | Overrides for Sentinel scan settings |
| `deploy` | yes | Environments and gates |
| `jobs` | no | One-off or scheduled job stages |
| `notify` | no | Slack channels for pipeline events |

## `build`

- `dockerfile`: path to the Dockerfile.
- `pool`: Forge runner pool. Defaults to `forge-standard`.
- `cache.key` / `cache.namespace`: see the Forge cache FAQ.

## `test`

A list of steps. Each step has `name`, `run`, and optional `pool`, `timeout`, and `env`.

## `deploy`

```yaml
deploy:
  environments: [dev, staging, prod]
  gates:
    prod:
      manual_approval: true
```

- `soak`: how long to wait in an environment before promoting, as a duration string. Follow your org's release standard when choosing a value.
- `manual_approval`: require a human approval before the stage.

## `jobs`

```yaml
jobs:
  - name: backfill-2026-q3
    run: python scripts/backfill.py
    env: prod
```

Job runs are logged in Ship.

## `notify`

```yaml
notify:
  slack: ["#srch-deploys"]
```

## Validating locally

```
gatekeeper validate
```
