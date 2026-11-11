doc_id: DSEC-DATA-003
title: Streamline Topic Naming Conventions
doc_type: standard
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2025-06-17
supersedes:
fact_ids:

# Streamline Topic Naming Conventions

Streamline is TechSync's Kafka-based event bus. Consistent topic names make ownership obvious and tooling simple. This standard applies to every new topic; existing topics are renamed only when they are rebuilt.

## 1. Format

```
<domain>.<entity>.<event>.v<version>
```

Examples: `billing.invoice.finalized.v2`, `search.index.updated.v1`.

Rules:
- Lowercase letters, digits, and hyphens inside a segment; dots between segments.
- Domain is the owning product area, not a team name.
- Event is a past-tense verb (`created`, `updated`, `finalized`).
- Version increments only on a breaking schema change.

## 2. Special suffixes

| Suffix | Meaning |
|---|---|
| `.dlq` | Dead-letter topic for failed messages |
| `.retry` | Retry topic with delayed redelivery |
| `.compacted` | Topic using key compaction |

## 3. Ownership tags

Every topic carries three tags in the Streamline catalog:

- `owner_team`: the team code, for example `PAY`
- `oncall_channel`: the Slack channel for issues
- `data_class`: the classification label recorded in the catalog

## 4. Keys

Choose a key that keeps related events together, for example the account ID. Do not use random keys unless ordering is irrelevant, and document the choice in the catalog entry.

## 5. Requesting a topic

1. Open a request in the DATA queue.
2. Provide the name, owner, expected volume, key, and schema.
3. DATA reviews within two business days and creates the topic through Terraform.

## 6. Anti-patterns

- Team names in topic names, which break when teams are reorganized.
- Environment names in topic names; use separate clusters per environment instead.
- Reusing a topic for unrelated events.
