---
doc_id: PLAT-COMP-012
title: Forge Build Cache Troubleshooting FAQ
doc_type: FAQ
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2026-01-22
supersedes: ""
fact_ids: ""
---

# Forge Build Cache Troubleshooting FAQ

Compute, Forge

**My build is suddenly much slower than usual. Is the cache broken?**

Maybe. Look at the job log header for `cache: hit` or `cache: miss` lines. A full miss usually means one of three things: your lockfile changed (expected), the runner image was updated and base layers were rebuilt (expected for a day or two after a release), or the cache key includes something that changes every build, like a timestamp. Check your pipeline's `cache.key`.

**I'm getting checksum errors restoring Go modules.**

This is almost always a corrupted entry from an interrupted upload. Re-run the job with `FORGE_CACHE_BYPASS=1`; the next successful run will write a fresh entry. If it keeps happening, post the job URL in #comp-forge.

**Docker says "no space left on device".**

The runner's NVMe filled up. This happens with very large images or many intermediate layers. Use multi-stage builds, clean package caches in the same `RUN` step, or move the job to `forge-large`, which has bigger disks.

**Can I share a cache between two repositories?**

Yes, if they use the same `cache.namespace` in the pipeline file. Only do this for repos owned by the same team; cache poisoning across teams is a real risk.

**How long are cache entries kept?**

Entries that aren't read for 14 days are evicted. Frequently used entries stay indefinitely.

**Can I clear the cache for my repo?**

Run `forge cache purge --repo <org/repo>`. It takes effect for the next job.

**Is the cache shared between regions?**

No. The standby us-west-2 runners have their own, colder cache.

**Who do I talk to?**

#comp-forge. Include the job URL, runner pool, and image version.
