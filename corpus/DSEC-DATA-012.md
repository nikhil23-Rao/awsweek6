doc_id: DSEC-DATA-012
title: Data Quality Checks Standard
doc_type: standard
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: Tech Lead
status: approved
last_updated: 2025-09-30
supersedes:
fact_ids:

# Data Quality Checks Standard

**Owner:** Data Platform | **Applies to:** every dataset that other teams consume from Reservoir

## 1. Why

A dataset that is late, empty, or wrong costs every consumer time. Checks catch the problem at the source.

## 2. Required checks

Every consumed dataset must have these checks, defined in its job file:

| Check | What it verifies |
|---|---|
| Freshness | The dataset has been updated within its freshness target |
| Volume | Row counts are within an expected range compared with recent history |
| Nulls | Key columns have no unexpected nulls |
| Uniqueness | Declared keys are unique |
| Schema | Columns and types match the registered schema |

## 3. Thresholds

Each dataset declares its own thresholds in the job file. Defaults: volume within 30 percent of the trailing median; freshness target set to the job's schedule plus a tolerance of one hour.

## 4. Failures

- A failed check marks the run as failed and sends a Lookout alert to the dataset owner.
- Downstream jobs wait until the check passes.
- Owners must acknowledge and explain a failure in the alert ticket.

## 5. Skipping or changing a check

A check may only be disabled temporarily with a ticket stating the reason, owner, and date by which it will return. Permanent changes to thresholds are made in the job file through a pull request.

## 6. Reporting

DATA publishes a monthly quality report listing failed checks by dataset and owner.

## 7. Adding checks

Teams are encouraged to add checks beyond the required set, for example distribution checks on key metrics. Share useful ones in the DATA channel.
