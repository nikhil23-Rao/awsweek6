---
doc_id: PLAT-DEVT-008
title: Gatekeeper CI Troubleshooting FAQ
doc_type: FAQ
scope_level: team
owner_team: DEVT
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2026-08-26
supersedes: ""
fact_ids: ""
---

# Gatekeeper CI Troubleshooting FAQ

Developer Tooling, SRE

**My pipeline is stuck at "Waiting for runner".**

All runners in that Forge pool are busy. Check queue times in #comp-forge or the Forge dashboard. If it's been more than 30 minutes, ask Compute. Large builds should use `forge-large`.

**Build fails with "image too large".**

Images are capped at 4 GB. Use multi-stage builds and slim base images.

**Sentinel scan is blocking my deploy.**

The scan found a blocking vulnerability or license issue. The scan output links to the finding. Update the dependency, or talk to AppSec if you think it's a false positive. DEVT can't override Sentinel results.

**Deploy to staging succeeded but promotion to prod didn't start.**

Check for a `manual_approval` gate or a team-defined soak in your `gatekeeper.yaml`. Pending approvals show in Console under **Releases**.

**Prod canary failed, but my metrics look fine.**

Open the deploy in Console. It shows which metric failed analysis. Often it's a latency regression in a single endpoint that's hidden in service-wide averages.

**"Namespace not found" during deploy.**

The `namespace` in `gatekeeper.yaml` doesn't match a real Kestrel namespace, or your team doesn't have access. Check spelling and ask COMP if needed.

**Pipeline passes locally, fails in CI.**

Environment differences. Forge runners use specific toolchain versions; check the image version in the job log header and match it locally.

**How do I rerun a single failed step?**

`gatekeeper rerun --job <job-id> --step <name>`

**Still stuck?**

#devt-gatekeeper with the pipeline URL.
