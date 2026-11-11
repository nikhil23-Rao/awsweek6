doc_id: DSEC-MLI-010
title: ML Infra Weekly Sync, July 2026
doc_type: meeting notes
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: TPM
status: unmarked
last_updated: 2026-07-29
supersedes:
fact_ids:

# ML Infra Weekly Sync, 28 Jul 2026

**Attendees:** Olivia Brandt, Hassan Qureshi, three engineers, one SRE, TPM (notes)

## 1. Rollout gates (follow-up from May)
- Latency and queue-depth thresholds are in review; the SRE expects to merge this week.
- Soak period spanning peak traffic: design agreed, implementation next.
- Alert on queue depth at minimum replicas is already live.

## 2. GPU capacity
- Utilization on the shared pool is up; two teams are close to their quota.
- Self-service quota tooling is on the Q4 list. Hassan will write a short proposal.
- Procurement update: the next batch of GPUs arrives in September.

## 3. FeatureHub
- Backfill playbook draft is with the SRE for review.
- Question from a product team about adding a new entity type; Hassan to reply with the process.

## 4. Experiment tracking
- Adoption is good; a few older projects still use ad hoc notebooks.
- Action: write a short migration note.

## 5. Hiring
- One staff-level role open; two candidates in the loop.

## 6. AOB
- Reminder to fill in the planning doc before Friday.
- Brown bag next week on cost allocation.

## Actions
- SRE: merge rollout gate changes.
- Hassan: quota tooling proposal; FeatureHub reply.
- TPM: circulate planning reminders.
