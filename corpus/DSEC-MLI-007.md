doc_id: DSEC-MLI-007
title: Foundry GPU Capacity FAQ
doc_type: FAQ
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: Technical Writer
status: approved
last_updated: 2026-02-19
supersedes:
fact_ids:

# Foundry GPU Capacity FAQ

**How do I get GPU quota?**
Each team has a quota pool. Ask your engineering manager which pool you belong to, then request access to it through the Keystone request portal.

**What if my team's pool is full?**
Check usage on the Foundry capacity dashboard. If other jobs are idle, ask the owner to release them. If the pool is genuinely too small, open a quota request.

**How do I request more quota?**
Open a ticket in the MLI queue with the GPU type, the count, how long you need it, and which project it supports. Requests are reviewed weekly.

**How long does it take?**
Temporary increases of a few days are often approved the same week. Permanent increases follow the annual budget cycle and need your VP's agreement.

**Which GPU types exist?**
Foundry offers a few GPU classes. Check the capacity dashboard for what is available today; availability changes with procurement.

**Can I run on spot capacity?**
Yes, for jobs that checkpoint regularly. Spot jobs can be interrupted, and Foundry will resume from the last checkpoint if you set `resume_from`.

**Why is my job Pending?**
Usually because the pool has no free GPUs of the type you requested. See the training job runbook for the other causes.

**Who pays?**
Costs are charged back to your team through the `cost_center` tag in the job spec.

**Where can I ask other questions?**
In the ML Infrastructure channel.
