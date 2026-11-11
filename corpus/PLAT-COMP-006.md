---
doc_id: PLAT-COMP-006
title: Kestrel Workload Identity and Secrets Guide
doc_type: how-to guide
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2026-03-10
supersedes: ""
fact_ids: F-DSEC-002
---

# Kestrel Workload Identity and Secrets Guide

*Compute team, for anyone running services on Kestrel*

## Why this exists

Services on Kestrel constantly need credentials: a database password, an API token for a partner, a Kafka client cert for Streamline. We want every workload to get those from a short-lived source tied to its own identity, not from a long-lived secret pasted into a ConfigMap. This guide describes the supported path.

## Workload identity

Every pod on Kestrel runs with a Kubernetes service account. Kestrel maps each service account to a workload identity with the form:

```
kestrel://<cluster>/<namespace>/<service-account>
```

That identity is what other systems trust. Use one service account per service. Don't share a service account across deployments, and never use the `default` account in a namespace (the admission controller rejects it in staging and prod).

## Getting secrets into a pod

1. Declare the secrets your service needs in the `secrets:` block of your Scaffold service manifest.
2. At deploy time, Gatekeeper CI wires up the Kestrel secrets sidecar for your pods.
3. On startup, the sidecar authenticates with the pod's workload identity, fetches the credentials from Vaultline, and writes them to an in-memory volume at `/var/run/secrets/app/`.
4. The sidecar refreshes credentials in the background before they expire. Your process should re-read the file on change (most of our Go and Python libraries do this already).

## Credential lifetime

Secrets issued to workloads can live up to 4 hours. The sidecar renews them well before that point, so a healthy pod never sees an expired credential. If your service caches a credential in memory, size the cache TTL comfortably under that ceiling and rely on the file watcher.

## Common mistakes

- **Baking secrets into images.** Sentinel will flag this, and the build will fail.
- **Reading the secret once at boot and never again.** Long-running pods will eventually present an expired credential. Watch the file.
- **Using one identity for many services.** You lose the audit trail, and a compromise of one service exposes all of them.

## Debugging

```
kubectl -n <namespace> logs <pod> -c kestrel-secrets
```

Look for `renewed` lines. Repeated `auth denied` usually means the service account isn't bound to a Vaultline role; ask in #comp-help.

## Related

- Kestrel Namespace Provisioning Runbook
- Vaultline documentation (owned by AppSec)
