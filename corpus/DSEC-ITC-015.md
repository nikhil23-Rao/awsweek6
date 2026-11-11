doc_id: DSEC-ITC-015
title: "Postmortem: Keystone Directory Sync Failure"
doc_type: postmortem
scope_level: team
owner_team: ITC
owner_org: DSEC
author_role: SRE
status: approved
last_updated: 2026-04-30
supersedes:
fact_ids:

# Postmortem: Keystone Directory Sync Failure

**Severity:** Sev3 | **Incident date:** 21 April 2026 | **Duration:** about 20 hours | **Authors:** ITC SRE

## Summary

A change in the HR directory's export format caused Keystone's directory sync to fail from the evening of 20 April until the following afternoon. During that time, group membership changes did not apply and four new employees could not sign in on their first day. Existing users were not affected, and no access was granted incorrectly.

## Impact

- Four new hires without accounts on their start day, delayed by about half a day.
- About thirty group membership requests delayed by one business day.
- Increased load on the IT helpdesk.
- No incorrect access was granted and no accounts were lost.

## Timeline (Pacific time)

| Time | Event |
|---|---|
| Mon 18:05 | HR directory deploys a change that renames a field in its export |
| Mon 18:30 | Overnight sync run fails with a schema mismatch; alert goes to a low-priority channel |
| Tue 08:40 | The helpdesk reports that new hires cannot sign in |
| Tue 09:10 | ITC on-call opens an incident |
| Tue 10:30 | Cause found: the renamed field breaks the mapping file |
| Tue 12:15 | Mapping updated and tested in staging |
| Tue 13:40 | Mapping deployed; full sync run started |
| Tue 14:10 | Sync completes; new accounts appear |
| Tue 15:00 | Incident closed after the backlog of group changes is applied |

## Root cause

The HR directory team renamed a field without telling ITC. Our mapping file referred to the old name, so the sync run failed on every record.

## Contributing factors

1. The sync failure alert was routed to a channel that nobody watched overnight.
2. No contract existed between the HR directory team and ITC describing which fields we depend on.
3. New-hire accounts were created only by the overnight sync, with no manual path documented.

## What went well

- The helpdesk escalated quickly with a clear description.
- The mapping fix was small and the staging test was fast.
- No incorrect access resulted.

## What went poorly

- The first alert was missed.
- Recovery depended on the on-call engineer knowing the mapping file well.

## Action items

| Action | Owner | Due |
|---|---|---|
| Route sync failure alerts to the ITC on-call through Lookout | ITC SRE | May 2026 |
| Write an interface contract with the HR directory team | ITC Tech Lead | June 2026 |
| Document the manual account creation procedure | ITC SRE | May 2026 |
| Add a schema check on the export before each run | ITC Tech Lead | July 2026 |
