---
doc_id: PLAT-NET-002
title: Networking Team Charter
doc_type: team charter
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: Engineering Manager
status: approved
last_updated: 2025-01-28
supersedes: ""
fact_ids: ""
---

# Networking Team Charter

**Team:** Networking (NET), Platform Engineering
**Engineering manager:** Priya Raman
**Tech lead:** Tomas Vidal

## Mission

Every request into TechSync, and every call between our services, travels over infrastructure Networking runs. Our job is to make that path fast, secure, and invisible.

## Systems we own

- **Meridian Mesh**: the service mesh on Kestrel. Service-to-service mTLS, routing, retries, timeouts, and traffic policy.
- **EdgeGate**: the API gateway and ingress for all external traffic to Ship, Ledger, Insight, Console, and TechSync Mobile backends. TLS termination, routing, rate limiting, and WAF.
- **Network foundations**: VPCs, Transit Gateways, internal DNS, and cross-region connectivity, all managed in Terraform.

## Shared responsibilities

- **Kestrel cluster networking** (CNI, node networking) is shared with Compute; Compute owns cluster lifecycle, we own the mesh on top.
- **WAF rules** are proposed with AppSec and operated by us.
- **Certificates**: we run issuance automation for EdgeGate and the mesh CA; AppSec sets the requirements.

## Interfaces

- Route onboarding requests: NET Jira.
- Questions: #net-help, #net-mesh, #net-edgegate.
- Production issues: page NET on-call through PagerDuty.

## 2025 priorities

1. Locality-aware load balancing in the mesh across all prod clusters.
2. EdgeGate cells in eu-west-1 at parity with us-east-1.
3. Automated certificate rotation with no manual steps.
4. IPv6 readiness plan.

## Disaster recovery owners

Primary: NET tech lead. Backup: senior SRE on the NET rotation.
