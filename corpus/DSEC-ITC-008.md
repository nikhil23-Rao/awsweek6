doc_id: DSEC-ITC-008
title: SOC 2 Type II Audit Prep Runbook
doc_type: runbook
scope_level: team
owner_team: ITC
owner_org: DSEC
author_role: Compliance Analyst
status: approved
last_updated: 2026-02-03
supersedes:
fact_ids:

# SOC 2 Type II Audit Prep Runbook

This runbook is for ITC compliance analysts coordinating the SOC 2 Type II audit. It covers the work from kickoff through the auditor's report. Engineers who supply evidence should read the org-wide audit calendar and the evidence handbook instead.

## Roles

| Role | Responsibility |
|---|---|
| Lead analyst | Runs the plan, talks to auditors |
| Analysts | Own a share of the controls and chase evidence |
| ITC Engineering Manager | Removes blockers, reviews status |
| CISO's office | Signs the management assertion and receives findings |

## Phase 1: Kickoff (March)

1. Confirm the audit period and scope with the auditors.
2. Export the control list from Compass and check that every control has an owning team.
3. Send the control owners a message with their list and the evidence calendar.
4. Create a tracker with one row per control: owner, evidence status, due date.

## Phase 2: Evidence collection (April to May)

1. Owners upload evidence to Compass as described in the evidence handbook.
2. Each week, run the gap check:
   - List controls with no evidence in the current period.
   - Open a ticket for each, assigned to the control owner.
   - Post the summary in the compliance channel.
3. Review uploaded evidence for quality: timestamps, names, and period selected. Send back anything unclear.
4. Escalate controls still open after two reminders to the owner's engineering manager.

## Phase 3: Fieldwork (June)

1. Create a shared folder for auditor requests and an index of what is in it.
2. Brief any engineer an auditor wishes to speak to; share the questions in advance when you can.
3. Log each auditor request with the date, the response, and who answered.
4. Hold a daily 15-minute check-in during fieldwork with the lead analyst, analysts, and the auditors.

## Phase 4: Findings and report (July to August)

1. Log every auditor finding with the control, the cause, and a proposed fix.
2. Agree fixes with owners and set due dates.
3. Review the draft report with the CISO's office before it is final.
4. After the report is issued, run a lessons-learned session with all control owners.

## Checklist before fieldwork

- [ ] Every control has an owner and evidence for the whole audit period
- [ ] Evidence index is up to date
- [ ] Auditor access to Compass is configured and tested
- [ ] Engineers likely to be interviewed have been briefed
- [ ] Previous findings show as remediated
- [ ] Management assertion draft is ready

## Tips from past audits

- Auditors value consistency. If a control is described differently in two places, fix it before they notice.
- Keep a list of "who knows how this works" for each control.
- Do not argue with auditors in front of engineers; take it offline.
- Write down the answers you give, so the next analyst can reuse them.

## After the audit

Update this runbook with anything that went differently from the plan. Archive the tracker and the evidence index for the following year's team.

## Contacts

The lead analyst, the compliance channel, and the CISO's office for formal communications.
