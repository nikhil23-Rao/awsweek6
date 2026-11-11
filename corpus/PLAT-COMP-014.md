---
doc_id: PLAT-COMP-014
title: Kestrel Pod Disruption Budget Guidelines
doc_type: standard
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-08-27
supersedes: ""
fact_ids: ""
---

# Kestrel Pod Disruption Budget Guidelines

Compute team standard

## Why PDBs matter

Kestrel replaces nodes all the time: weekly node-image patches, Karpenter consolidation, cluster upgrades, spot interruptions. A PodDisruptionBudget (PDB) tells Kubernetes how many of your pods can be taken down voluntarily at once. Without one, a node drain can evict all your replicas together. With a badly written one, drains get stuck and block cluster maintenance for everyone.

## Rules of thumb

1. **Every Deployment with 2 or more replicas needs a PDB.** Scaffold templates generate one.
2. **Use `maxUnavailable`, not `minAvailable`.** `maxUnavailable: 1` (or 25% for large services) keeps working as your replica count changes.
3. **Never set `maxUnavailable: 0`.** It blocks all voluntary evictions. Our admission controller rejects it in staging and prod.
4. **Single-replica services:** don't add a PDB. Accept the brief disruption, or run 2 replicas.
5. **Stateful services** (Kafka brokers in Streamline, OpenSearch nodes): use `maxUnavailable: 1` and make sure readiness probes reflect actual data health, not just process health.

## Examples

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: quarry-api
spec:
  maxUnavailable: 25%
  selector:
    matchLabels:
      app.kubernetes.io/name: quarry-api
```

## What happens when a drain is blocked

Karpenter retries for up to 1 hour, then pages the COMP on-call. We'll contact the owning team. Repeated blocked drains are raised at the Platform monthly operational review.

## Checking your PDBs

```
kubectl get pdb -n <namespace>
```

`ALLOWED DISRUPTIONS` should be at least 1 during normal operation.
