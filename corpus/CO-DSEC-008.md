doc_id: CO-DSEC-008
title: Log Retention Policy (previous)
doc_type: policy
scope_level: company
owner_team: DATA
owner_org: DSEC
author_role: Staff Engineer
status: deprecated
last_updated: 2026-01-12
supersedes:
fact_ids: F-POL-08

> **DEPRECATED (January 2026).** This policy is outdated. It was replaced by CO-DSEC-007, Log, Trace and Dataset Retention Policy. Retained for audit history only. Do not follow it.

# Log Retention Policy

**Owner:** Data Platform (DATA)

## 1. Policy

Application logs and traces are kept **90 days hot and 12 months in archive**. After the archive period the data is deleted.

## 2. Scope

Logs and traces emitted by products and internal systems. Datasets in Reservoir are handled under team guides.

## 3. Responsibilities

Data Platform runs the lifecycle jobs. Teams configure their pipelines to use the standard tiers.

## 4. Legal holds

Held data is excluded from deletion until Legal releases the hold.
