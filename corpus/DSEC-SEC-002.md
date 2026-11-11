doc_id: DSEC-SEC-002
title: SEC Weekly Sync, August 2026
doc_type: meeting notes
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Engineering Manager
status: unmarked
last_updated: 2026-08-18
supersedes:
fact_ids: F-DSEC-007

# SEC Weekly Sync, 18 Aug 2026

**Attendees:** Gareth Llewellyn (notes), Amara Okafor, two security engineers, one staff engineer

## 1. Pen test scheduling
- Vendor slots for the autumn engagement are open; security engineers will propose dates by Friday.
- Need a point of contact in IT & Compliance for the scoping call.

## 2. Sentinel scan timing (main discussion)
- Developers keep complaining that waiting on scans slows their pull requests, especially during mornings in the Pacific time zone when the queue is deepest.
- **Proposal floated:** run the full Sentinel scan **nightly on the main branch** instead of on each pull request, and only run a quick lockfile diff check on PRs.
- For: faster PR turnaround, lower runner cost on Forge, more predictable queue.
- Against: a vulnerable dependency could sit in main until the next nightly run; the staff engineer is concerned about the audit story.
- Amara would like to see queue latency and finding-introduced-per-PR data before anyone commits to anything.
- Gareth wants a recommendation before the end of Q3.
- **Action:** Amara to pull queue latency stats and draft an options write-up.

## 3. Vaultline policy-as-code
- Tech lead is drafting Terraform conventions; target is a first draft in early September.

## 4. SBOM generation
- Rollout is on track; two repos left to enable.

## 5. AOB
- Reminder to update the on-call swap calendar.
- Next sync: 25 Aug.
