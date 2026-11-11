doc_id: DSEC-DATA-014
title: "ADR: Streamline Topic Compaction"
doc_type: ADR
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2025-08-05
supersedes:
fact_ids:

# ADR: Streamline Topic Compaction

**Status:** Accepted | **Date:** August 2025 | **Deciders:** Data Platform tech lead, engineering manager, two staff engineers

## Context

Several consumers rebuild their local state by reading a topic from the beginning. For entity-state topics, such as account profile changes, most of that data is overwritten by later messages for the same key, so rebuilds are slow and wasteful. We needed a way to let consumers rebuild quickly without a separate snapshot store.

## Decision

Entity-state topics will use Kafka log compaction, keeping the latest message per key. Topics that hold compacted state carry the `.compacted` suffix and a mandatory key.

## Consequences

**Positive**
- Rebuilds read only the latest state, which is much faster.
- No separate snapshot system to run.
- Consistent with the naming standard.

**Negative**
- Consumers lose intermediate history on compacted topics. Anyone who needs history must use a separate event topic.
- Deleting a record requires a tombstone message.
- Compaction adds some broker load.

## Alternatives considered

1. **Snapshots in PostgreSQL.** Familiar, but adds an extra system and a consistency problem between the snapshot and the topic.
2. **Rebuild from full history.** Simple, but slow, and gets slower as volume grows.
3. **Snapshots in Reservoir.** Adds latency and couples event consumers to the lake.

## Follow-up

- Update the topic request form to ask whether the topic is state or event.
- Add a lint check that rejects `.compacted` topics without keys.
