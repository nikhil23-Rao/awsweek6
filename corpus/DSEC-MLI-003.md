doc_id: DSEC-MLI-003
title: Foundry Operator Onboarding Guide
doc_type: onboarding guide
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: Tech Lead
status: unmarked
last_updated: 2025-08-13
supersedes:
fact_ids: F-POL-10

# Foundry Operator Onboarding Guide

Welcome to ML Infrastructure! This guide gets you from "new laptop" to "can run and watch a training job on Foundry" in about three days. Don't try to do it all on day one; we've ordered things so that the slow parts (access requests) start first.

## Day 1: access

Open the access requests below in the Keystone request portal. Most are approved within a business day.

- Group `foundry-users`: submit jobs and read dashboards
- Group `foundry-operators`: manage clusters and quotas (needed for on-call)
- Group `featurehub-readers`: read the feature store
- Your team's GPU quota pool (ask your manager which one)

While you wait, install the tooling:

```
brew install foundry-cli kubectl
foundry login
```

## Day 1: multi-factor setup for production

Foundry operators need production access for on-call work. Production sign-ins use multi-factor authentication, and **an authenticator app is acceptable** for this. Install one on your phone, register it in Keystone under Security settings, and save your recovery codes in the company password manager. Test it by signing in to the production Foundry console. If it prompts you for a six-digit code and lets you in, you are done.

## Day 2: your first job

1. Clone the `ml-examples` repo.
2. Pick the `hello-gpu` example. It trains a tiny model for about two minutes.
3. Submit it with `foundry job submit -f hello-gpu.yaml`.
4. Watch it with `foundry job logs <id> --follow`.
5. Find the run in the experiment tracker and confirm that metrics were logged.

If the job stays Pending, check that your quota pool has free GPUs. The FAQ explains how to ask for more.

## Day 3: serving and rollouts

Read the Model Serving Rollout Guide and shadow an on-call engineer during a canary rollout. You will not be asked to run one alone until your second month.

## On-call readiness checklist

- [ ] In the `foundry-operators` group
- [ ] Production sign-in tested
- [ ] Added to the paging rota
- [ ] Read the training job and serving runbooks
- [ ] Introduced yourself in the ML Infrastructure channel

## Who to ask

Your onboarding buddy first, then the ML Infrastructure Tech Lead. There are no silly questions here; our best runbooks started as someone's confused message.
