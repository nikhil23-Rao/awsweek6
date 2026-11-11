---
doc_id: PLAT-NET-011
title: Meridian Mesh mTLS Certificate Rotation Runbook
doc_type: runbook
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2025-09-09
supersedes: ""
fact_ids: ""
---

# Meridian Mesh mTLS Certificate Rotation Runbook

Networking, SRE rotation

Meridian Mesh uses mTLS between every pair of services. Each sidecar gets a short-lived leaf certificate from the mesh certificate authority (CA). Leaf certificates renew automatically; nobody needs to do anything. This runbook is for rotating the **CA itself**, which is a planned operation, and for recovering if leaf issuance breaks.

## Planned CA rotation

The mesh uses an intermediate CA signed by the TechSync root CA (managed by AppSec). We rotate the intermediate on the schedule AppSec sets.

1. **Generate the new intermediate.** Request a signing ceremony with AppSec. The new intermediate is stored in Vaultline.
2. **Distribute trust.** Add the new intermediate to the mesh trust bundle alongside the current one. Roll this to every cluster and wait for all sidecars to pick up the new bundle (check `meridian_trust_bundle_version`).
3. **Switch issuance.** Point the mesh CA at the new intermediate. New leaf certificates are now signed by it.
4. **Wait.** Leave both intermediates trusted until every leaf certificate signed by the old one has expired.
5. **Remove the old intermediate** from the trust bundle.

Do each step in dev, then staging, then prod.

## Leaf issuance failures

Symptoms: new pods fail readiness; sidecar logs show `certificate request failed`.

1. Check that the mesh CA pods are running in `net-mesh-system`.
2. Check the CA's connection to Vaultline. Auth failures here need AppSec.
3. Existing pods keep working until their leaf certificate expires, so act quickly.

## Escalation

NET tech lead and AppSec on-call.
