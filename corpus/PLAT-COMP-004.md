---
doc_id: PLAT-COMP-004
title: Kestrel Control-Plane Alert Playbook
doc_type: runbook
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2026-04-15
supersedes: ""
fact_ids: ""
---

# Kestrel Control-Plane Alert Playbook

SRE runbook for the Compute rotation.

Each section below matches an alert name in Lookout. Start with **Impact**, then work down.

---

## KestrelAPIServerErrorRateHigh

**Impact:** deploys, autoscaling, and kubectl access may fail. Running pods usually keep serving traffic.

1. Open the Kestrel control-plane dashboard. Check whether errors are concentrated on one verb or resource.
2. Look for a client hammering the API server (`apiserver_request_total` by user agent). A runaway controller is the most common cause.
3. If one client is responsible, scale it to zero and contact the owning team.
4. If errors are broad, check the AWS Health Dashboard for EKS issues in the region.

## KestrelEtcdDBSizeHigh

**Impact:** writes to the cluster may start failing if the database hits its size limit.

1. Identify the largest object types. Large numbers of Events or Secrets are the usual suspects.
2. Check for a controller creating objects in a loop.
3. Open an AWS support case if compaction appears stuck.

## KestrelSchedulerPendingPodsHigh

**Impact:** new pods aren't starting. Scale-ups and deploys stall.

1. `kubectl get pods -A --field-selector=status.phase=Pending` and look at events.
2. Quota errors: point the team to the quota increase process.
3. "No nodes available": check Karpenter logs for provisioning failures, especially instance capacity errors.

## KestrelNodeNotReady

**Impact:** pods on the node are rescheduled. Usually self-healing.

1. If one node: let Karpenter replace it; confirm within 15 minutes.
2. If many nodes in one AZ: suspect an AZ issue and check AWS Health.
3. If many nodes across AZs: suspect a bad node image. Pause the node-image rollout.

---

Escalate to the COMP tech lead if you're stuck for 30 minutes on anything customer-impacting.
