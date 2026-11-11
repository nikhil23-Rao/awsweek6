doc_id: DSEC-SEC-014
title: "Postmortem: Sentinel Scan Queue Backlog"
doc_type: postmortem
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: SRE
status: approved
last_updated: 2026-06-30
supersedes:
fact_ids:

# Postmortem: Sentinel Scan Queue Backlog

**Severity:** Sev3 | **Incident date:** 10 June 2026 | **Duration:** about 5 hours | **Authors:** SEC SRE

## Summary

On the morning of 10 June, the Sentinel scan queue grew until scans were waiting more than an hour to start. Engineers saw pipelines sitting in the `sentinel-scan` stage. No scans were skipped and no findings were lost, but many teams waited for their pipelines to finish. The queue drained after we added runner capacity and paused a large scheduled job.

## Impact

- Pipelines in many repositories were delayed by up to about 70 minutes.
- Developer complaints in the DSEC and DEVT channels.
- No data loss, and no security impact.

## Timeline (Pacific time)

| Time | Event |
|---|---|
| 07:45 | Queue depth begins to rise as the Pacific workday starts |
| 08:30 | Median wait passes 20 minutes; no alert fires |
| 09:10 | A developer reports slow pipelines in the DEVT channel |
| 09:25 | SEC on-call opens an incident |
| 09:50 | Cause identified: a weekly rescan of all repositories began at the same time as the morning load |
| 10:05 | Weekly rescan paused; extra runners requested from Compute |
| 10:40 | Extra runners available; queue begins to drain |
| 12:55 | Queue back to normal |

## Root cause

The weekly rescan of every repository against updated rules was scheduled at the start of the Pacific workday. It added many scan jobs in a short window, on top of normal pipeline traffic. Runner capacity for Sentinel was sized for the normal load and did not account for the rescan.

## Contributing factors

1. No alert on queue wait time, only on service availability.
2. The rescan schedule had not been changed since the repository count was much smaller.
3. Requests for temporary runner capacity relied on a manual ticket to Compute.

## What went well

- A developer reported the problem quickly, with clear symptoms.
- Pausing the rescan was safe and fast.
- Compute approved extra runners within 35 minutes.

## What went poorly

- We learned about the problem from users.
- The rescan could not be rescheduled without editing its configuration by hand.

## Action items

| Action | Owner | Due |
|---|---|---|
| Add an alert on median queue wait time | SEC SRE | July 2026 |
| Move the weekly rescan to Sunday evening | SEC Tech Lead | June 2026 |
| Document how to request temporary runner capacity | SEC Tech Lead | July 2026 |
| Review Sentinel runner sizing against repository growth | SEC Engineering Manager | August 2026 |
