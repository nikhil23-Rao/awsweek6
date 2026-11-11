doc_id: DSEC-DATA-015
title: Data Platform Glossary
doc_type: reference
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: Technical Writer
status: approved
last_updated: 2026-02-27
supersedes:
fact_ids:

# Data Platform Glossary

Terms you will hear on the Data Platform team and in conversations with people who use our systems.

| Term | Meaning |
|---|---|
| **Backfill** | Loading or recomputing historical data after a change or a gap |
| **Batch job** | A scheduled job that loads data into Reservoir in groups rather than one event at a time |
| **Catalog** | The Reservoir registry of datasets, schemas, owners, and tags |
| **Compaction** | Rewriting data to remove stale or small pieces; applies to Kafka topics and to files in Reservoir |
| **Consumer group** | A set of consumers that share the work of reading a Streamline topic |
| **Dataset** | A table registered in the Reservoir catalog with an owner |
| **DLQ** | Dead-letter queue: a topic that holds messages that failed processing |
| **Idempotent** | An operation that gives the same result when run more than once |
| **Lag** | How far a consumer is behind the newest message in a topic |
| **Producer** | A service that writes messages to Streamline |
| **Quarry** | The query engine used to read Reservoir tables |
| **Reservoir** | The TechSync data lake |
| **Schema registry** | The service that stores message schemas and checks compatibility |
| **Streamline** | The Kafka-based event bus |
| **Tombstone** | A message with an empty value used to delete a key from a compacted topic |
| **Topic** | A named stream of messages in Streamline |

## Abbreviations

- **ADR:** architecture decision record
- **DATA:** the Data Platform team code
- **DSEC:** Data & Security, our org
- **SRE:** site reliability engineer

## Suggest a term

Post in the DATA channel or open a docs request in the intake queue.
