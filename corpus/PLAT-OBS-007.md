---
doc_id: PLAT-OBS-007
title: Tracewell Storage and Retention
doc_type: reference
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: Tech Lead
status: unmarked
last_updated: 2024-03-05
supersedes: ""
fact_ids: F-POL-08
---

# Tracewell Storage and Retention

Observability (OBS)

This page explains where Tracewell stores the logs and traces it collects, how long we keep them, and how to get at older data. It applies to all environments.

## Pipeline recap

Services emit spans through the Tracewell SDK and logs through the standard logging libraries. Tracewell collectors in each region batch the data and write it to two tiers of storage.

## Storage tiers

| Tier | Backing store | What it's for | Retention |
|---|---|---|---|
| Hot | OpenSearch clusters, per region | Search, dashboards, live debugging | **90 days** |
| Archive | S3 (compressed Parquet), per region | Audits, long-range investigations, compliance requests | **12 months** |

Logs and traces are kept **90 days hot and 12 months in archive.** After 90 days, data ages out of OpenSearch automatically and is only available from archive. After 12 months, archive objects are deleted by an S3 lifecycle rule.

EU customer data is stored and archived in eu-west-1 only.

## Querying archived data

Archive data can't be searched from the normal Tracewell UI. To pull it:

1. File a ticket in the OBS Jira project with the service, time range, and reason.
2. OBS restores the requested partitions into a temporary OpenSearch index.
3. The index is available for 7 days and then deleted.

Expect one to two business days for a restore.

## Cost notes

Hot storage is the expensive tier. Very chatty services (debug logging left on in prod) can push a cluster to its limits; OBS will reach out if your service is a top contributor.

## Questions

#obs-tracewell
