doc_id: PROD-SRCH-006
title: Sieve Reindexing Runbook
doc_type: runbook
scope_level: team
owner_team: SRCH
owner_org: PROD
author_role: SRE
status: approved
last_updated: 2026-05-12
supersedes:
fact_ids: 

---

# Sieve Reindexing Runbook

**Owner:** Search SRE  **When to use:** after schema mapping changes or index corruption

## Choose the type

- **Partial reindex** rebuilds a time range or one account. Use for small corrections.
- **Full reindex** rebuilds every index for an account. Use when the mapping changes in a way that affects existing data.

## Before you start

1. Confirm approval in the Jira ticket from the Search Tech Lead.
2. Check OpenSearch capacity; reindexing doubles write load.
3. Notify #prod-search and Support.

## Partial reindex

```
sieve reindex --account <id> --from 2026-05-01 --to 2026-05-07
```

The job reads the source data, rewrites documents into a new index, and switches an alias when it finishes.

## Full reindex

1. Create the new index with the updated mapping.
2. Start the reindex job with `--full`.
3. Watch progress on the Sieve dashboard.
4. When the job reports complete, compare document counts between old and new indexes.
5. Switch the alias.
6. Keep the old index for 48 hours, then delete it.

## Troubleshooting

- **Job stalls:** look for a bulk rejection in OpenSearch; lower the batch size.
- **Counts differ:** rerun the affected range.

## After

Record the work in the ticket and update the account's mapping version.
