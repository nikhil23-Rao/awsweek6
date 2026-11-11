doc_id: DSEC-DATA-006
title: Streamline Schema Registry Guide
doc_type: guide
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2025-12-09
supersedes:
fact_ids:

# Streamline Schema Registry Guide

Every message on Streamline has a schema registered in the schema registry. This guide explains how to register a schema, how to change it safely, and what the compatibility checks mean.

## Why schemas

Producers and consumers are developed by different teams. A registered schema gives consumers something to code against, and the registry blocks changes that would break them.

## Registering a schema

1. Write the Avro schema in your service repo under `schemas/`.
2. Open a pull request. CI registers the schema in a test registry and runs the compatibility check.
3. After merge, the deploy pipeline registers it in the production registry.

## Compatibility mode

All subjects use **backward compatibility**: consumers using the new schema can read data written with the previous schema.

| Change | Allowed? |
|---|---|
| Add an optional field with a default | Yes |
| Remove an optional field | Yes |
| Add a required field without a default | No |
| Rename a field | No |
| Change a field's type | No |

## Breaking changes

When you must break compatibility, create a new topic version (for example `.v2`) and run both for a migration period. Tell consumers in the DSEC channel before you start.

## Common errors

- **Incompatible schema:** you added a required field. Give it a default.
- **Subject not found:** the topic name does not match the registered subject.
- **Unknown magic byte:** the producer is not using the registry serializer.

## Tips

Add a `doc` string to every field. Prefer enums with an `UNKNOWN` default for values that may grow. Never reuse a field name for a different meaning.
