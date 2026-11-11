doc_id: DSEC-MLI-012
title: FeatureHub Backfill Playbook
doc_type: runbook
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: SRE
status: draft
last_updated: 2026-08-25
supersedes:
fact_ids:

# FeatureHub Backfill Playbook (DRAFT)

**Status: draft, under review by the MLI Tech Lead.** Do not use for production backfills until it is approved.

## When you need a backfill

- You added a new feature to an existing feature view and need historical values.
- A bug in a feature definition was fixed and past values must be recomputed.
- A source table gap was filled and downstream features should be recalculated.

## Before you start

1. Confirm the feature view's YAML change is merged.
2. Pick the date range. Keep it as small as you can; large backfills compete with regular materialization for resources.
3. Estimate the cost with `featurehub backfill plan` and attach the output to the ticket.
4. Check the Foundry capacity dashboard to confirm there is room.

## Procedure

1. Submit the backfill: `featurehub backfill submit --view <name> --from <date> --to <date>`.
2. The job runs in chunks. Watch progress in the FeatureHub dashboard.
3. If a chunk fails, FeatureHub retries it twice. After that the job pauses; do not restart from the beginning. Use `featurehub backfill resume <id>`.
4. When the job finishes, run `featurehub backfill verify <id>`. It compares row counts and a sample of values against the expected computation.

## Cutting over

Backfilled values are written to a shadow table. After verification:

1. Announce the cutover in the ML Infrastructure channel.
2. Run `featurehub backfill promote <id>`.
3. Watch dependent training jobs for one cycle.

## Rollback

`featurehub backfill revert <id>` restores the previous table. Keep the shadow table until at least one dependent job has trained successfully.

## Things that go wrong

- **Backfill is slow:** the range is too wide, or the pool is busy. Narrow the range.
- **Verification shows missing rows:** the source did not have data for that range; check with the source owner.
- **Dependent jobs behave differently:** a feature's definition changed along with the backfill. Review the YAML diff.

## Open items before approval

- Add expected runtimes by view size.
- Agree on the approval needed for large backfills.
