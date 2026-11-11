---
doc_id: PLAT-NET-013
title: Meridian Mesh Sidecar Troubleshooting FAQ
doc_type: FAQ
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2026-05-19
supersedes: ""
fact_ids: ""
---

# Meridian Mesh Sidecar Troubleshooting FAQ

Networking, SRE

**My service returns 503s, but the upstream pods look healthy.**

Check whether the upstream's readiness probe is passing. The mesh only routes to ready pods. Also check outlier detection: if a pod returned a run of `5xx` errors, the mesh may have ejected it temporarily. Look at `meridian_outlier_ejections_total`.

**I see "upstream connect error or disconnect/reset before headers".**

The connection to the upstream failed before a response arrived. Common causes: the upstream process crashed, it isn't listening on the port in the Service definition, or it closed an idle keepalive connection the sidecar was reusing. If it's the last one, make sure your server's idle timeout is longer than the mesh's connection idle timeout.

**The sidecar wasn't injected into my pod.**

Check that the namespace has the `meridian.techsync.io/inject=enabled` label, and that your pod doesn't have the opt-out annotation. Then restart the pod; injection only happens at creation time.

**My pod takes a long time to become ready after the sidecar was added.**

The sidecar needs to fetch its certificate and config before traffic flows. Set `holdApplicationUntilProxyStarts: true` (Scaffold templates already do).

**Jobs never finish because the sidecar keeps running.**

Use the `meridian-quit` helper at the end of your job, or use native sidecar containers on Kestrel.

**mTLS errors between two services.**

One side may be in a namespace without the mesh, or calling the pod IP directly instead of the Service name. Always call the Service name.

**Who can help?**

#net-mesh. Include namespace, pod name, and a sample request ID from Tracewell.
