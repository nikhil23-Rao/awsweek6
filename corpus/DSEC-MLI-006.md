doc_id: DSEC-MLI-006
title: FeatureHub Feature Definition Standard
doc_type: standard
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: Tech Lead
status: approved
last_updated: 2025-10-16
supersedes:
fact_ids:

# FeatureHub Feature Definition Standard

**Owner:** ML Infrastructure | **Applies to:** every feature view registered in FeatureHub

## 1. Naming

- Feature names use `snake_case`, are descriptive, and include the unit or window: `txn_count_1h`, `avg_basket_value_30d`.
- View names are named for the entity and subject area: `account_payments`, `user_search_activity`.
- Do not include team names or version numbers in names. Versions are tracked by FeatureHub.

## 2. Ownership

1. Every feature view has an owner team, recorded in its YAML.
2. Every feature has a description that explains what it measures in one sentence.
3. Owners are responsible for answering questions and for removal when the feature is no longer used.

## 3. Types and nulls

- Declare the data type of every feature.
- State how nulls are handled: `drop`, `zero`, or `default:<value>`.
- Never leave null handling implicit.

## 4. Documentation fields

| Field | Required |
|---|---|
| `description` | Yes |
| `owner_team` | Yes |
| `entities` | Yes |
| `freshness_target` | Yes |
| `notes` | No |

## 5. Deprecation

Mark a feature `deprecated: true` and announce it in the ML Infrastructure channel. Remove it only after no consumer has read it for a full release cycle.

## 6. Review

Each new or changed view is reviewed by an MLI engineer who is not the author, following the company code review policy.
