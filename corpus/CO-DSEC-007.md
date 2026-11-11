doc_id: CO-DSEC-007
title: Log, Trace and Dataset Retention Policy
doc_type: policy
scope_level: company
owner_team: DATA
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2026-01-12
supersedes: CO-DSEC-008
fact_ids: F-POL-08

# Log, Trace and Dataset Retention Policy

**Owner:** Data Platform (DATA) | **Effective:** January 2026

## 1. Policy

Logs, traces, and dataset archives are kept **30 days hot and 13 months in archive**. After the archive period ends, the data is deleted.

| Data | Hot storage | Archive |
|---|---|---|
| Logs | 30 days | 13 months |
| Traces | 30 days | 13 months |
| Dataset archives | 30 days | 13 months |

## 2. Definitions

- **Hot:** immediately queryable at full performance. For logs and traces this is OpenSearch-backed storage; for datasets it is the active Reservoir tier.
- **Archive:** compressed storage on S3 that can be restored on request. Restores take up to several hours.

## 3. Scope

The policy covers every product and internal system that emits logs or traces, and every dataset registered in Reservoir. It applies in all regions. EU customer data stays in eu-west-1, in both hot and archive tiers.

## 4. Responsibilities

- **Data Platform** operates the lifecycle jobs that move data from hot to archive and delete expired data.
- **Observability and product teams** configure their pipelines to use the standard tiers and must not set longer values.
- **Service owners** are responsible for data in their own services' pipelines.

## 5. Legal holds

Legal can place a hold on specific data. Held data is excluded from deletion until Legal releases the hold. Requests go through the CISO's office.

## 6. Restoring from archive

1. Open a ticket in the DATA queue with the data set, time range, and reason.
2. DATA confirms the classification and approves the restore.
3. The restore completes in the requested scratch location and is deleted after use.

## 7. Auditing

Lifecycle job runs are logged and sampled monthly by IT & Compliance. Evidence is stored in Compass for SOC 2 Type II and ISO 27001.

## 8. Changes

Requests to change retention values go to the Data Platform engineering manager and the CISO.
