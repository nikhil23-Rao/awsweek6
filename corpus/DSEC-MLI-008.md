doc_id: DSEC-MLI-008
title: Model Registry Conventions
doc_type: standard
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2025-12-18
supersedes:
fact_ids:

# Model Registry Conventions

Rules for registering models and tracking versions in the Foundry model registry.

## 1. Model names

- Lowercase letters, digits, and hyphens: `search-ranker`, `fraud-scorer`.
- The name identifies the task, not the architecture.
- One name per production use case. Experimental variants use a `-exp` suffix.

## 2. Versions

Use semantic versions: `MAJOR.MINOR.PATCH`.

- **MAJOR:** the input or output contract changes.
- **MINOR:** retrained on new data or with a new architecture, same contract.
- **PATCH:** configuration or packaging fix, no change to behavior.

## 3. Stages

A registered version moves through stages: `dev`, `staging`, `prod`. Promotion to `prod` requires:

1. Offline evaluation results attached.
2. A model card.
3. A reviewer from outside the model's team.
4. A completed release ticket.

## 4. Required metadata

| Field | Example |
|---|---|
| `owner_team` | `search` |
| `training_run` | link to the experiment |
| `feature_views` | FeatureHub views used |
| `metrics` | AUC, latency, and so on |
| `contact` | team channel |

## 5. Model cards

Every `prod` model has a card describing purpose, training data, known limitations, and evaluation. Update it with every MINOR or MAJOR version.

## 6. Retiring models

Mark the model `deprecated` and tell consumers. Remove it once nothing has called it for a full release cycle.
