doc_id: ORG-DSEC-007
title: Cross-Team Interface Contracts in DSEC
doc_type: standard
scope_level: org
owner_team: none (DSEC org-wide)
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2025-09-04
supersedes:
fact_ids:

# Cross-Team Interface Contracts in DSEC

DSEC teams depend on one another constantly: MLI reads from Reservoir, SEC provides secrets to everyone, ITC provides identity. A written contract keeps those dependencies from becoming surprises.

## 1. What needs a contract

Any interface that another DSEC team relies on: an API, an event stream, a table, a CLI, a queue. If you would be upset when it changed without notice, it needs a contract.

## 2. What a contract contains

1. **Owner:** the providing team and an on-call contact.
2. **Interface description:** endpoints, topics, or tables, with schemas.
3. **Compatibility promise:** what may change without notice and what needs a heads-up.
4. **Support:** channel and response expectations during business hours.
5. **Deprecation process:** how consumers are told, and how long they get to migrate.

## 3. Where contracts live

Each contract is a page in the providing team's documentation space, linked from the DSEC tooling landing page. The providing team keeps it current.

## 4. Changing a contract

- **Additive changes** (new optional fields, new endpoints) may ship with an announcement in the DSEC channel.
- **Breaking changes** require two weeks' notice to consumers, a migration path, and agreement from the main consuming teams.
- **Removal** requires that no consumer has used the interface for a full release cycle.

## 5. Consumer responsibilities

Read the contract before depending on an interface. Report problems to the owner instead of working around them. Do not rely on behaviour the contract does not promise.

## 6. Disagreements

If the two teams cannot agree on a change, tech leads meet first, then engineering managers, then the VP.
