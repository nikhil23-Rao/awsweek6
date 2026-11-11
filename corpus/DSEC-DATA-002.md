doc_id: DSEC-DATA-002
title: Reservoir Dataset Archive Guide
doc_type: guide
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: Tech Lead
status: unmarked
last_updated: 2025-09-10
supersedes:
fact_ids: F-POL-08

# Reservoir Dataset Archive Guide

How dataset archiving works in Reservoir, what it costs you, and how to get data back.

## The two tiers

Every dataset in Reservoir passes through two storage tiers:

1. **Hot (90 days).** The dataset's partitions sit in the active tier, with full query performance in Quarry.
2. **Archive (12 months).** After 90 days the partitions are moved to compressed archive storage. They are no longer visible in Quarry until restored.

After the 12 months in archive, the data is deleted by the lifecycle job.

## What this means for your queries

- Queries over a range older than 90 days will return empty results for that range unless you request a restore first.
- Dashboards that look back further than 90 days should be rebuilt from aggregates stored in a separate table.
- Training jobs that need older data should plan a restore a day ahead.

## Restoring archived data

1. Open a ticket in the DATA queue with the dataset name, date range, and reason.
2. DATA checks the classification of the dataset. Confidential data needs the data owner's approval.
3. The restore lands in a scratch prefix, typically within a few hours.
4. Scratch restores are deleted after 7 days.

## Costs

Archive storage is considerably cheaper than hot storage. Restores are metered per terabyte and appear on your team's cost report.

## FAQ

**Can I keep a dataset hot longer?** Not through this guide. Talk to your engineering manager about the business need.

**Does the archive clock restart on restore?** No. Restores are temporary copies.

**Who can approve a restore?** The DATA on-call engineer, with the data owner's agreement where required.
