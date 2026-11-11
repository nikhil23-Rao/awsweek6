---
doc_id: PLAT-NET-009
title: Internal DNS Architecture Overview
doc_type: design doc
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2023-10-11
supersedes: ""
fact_ids: ""
---

# Internal DNS Architecture Overview

Networking. Author: Staff Engineer.

## Zones

| Zone | Used for | Hosted in |
|---|---|---|
| `techsync.io` | Public names (API, Console, status page) | Route 53 public hosted zone |
| `internal.techsync.io` | Internal tools and services outside Kestrel | Route 53 private hosted zones, per region |
| `svc.kestrel` | Services inside Kestrel clusters | CoreDNS in each cluster |

## Split-horizon names

Some names, like `console.techsync.io`, resolve differently inside and outside our network. Internally they point to private EdgeGate listeners so internal traffic doesn't hairpin through the public internet.

## Resolution path from a Kestrel pod

1. The pod queries the node-local DNS cache.
2. Cache miss: CoreDNS in the cluster.
3. Names under `svc.kestrel` are answered by CoreDNS.
4. Everything else is forwarded to the VPC resolver, which answers `internal.techsync.io` from the private hosted zones and public names from the internet.

## Cross-region

Private hosted zones are associated with VPCs in us-east-1, us-west-2, and eu-west-1. During a regional failover, records for failed-over services are updated by the traffic shift runbook.

## Making changes

All zones are managed in Terraform in the `net-dns` repository. Changes need a NET reviewer. Never edit Route 53 records in the console; the next Terraform apply will overwrite them.

## Common pitfalls

- High TTLs on records that may change during failover. Keep failover-sensitive records at 60 seconds or less.
- Assuming `svc.kestrel` names work outside Kestrel. They don't.
