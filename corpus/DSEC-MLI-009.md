doc_id: DSEC-MLI-009
title: Foundry Experiment Tracking Guide
doc_type: guide
scope_level: team
owner_team: MLI
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2026-06-03
supersedes:
fact_ids:

# Foundry Experiment Tracking Guide

Experiment tracking lets you answer "what did we run, with which settings, and what happened?" six months from now. This guide covers how to log runs from Foundry training jobs.

## The basics

Every training job is automatically linked to an experiment with the job name. Inside your training code, you can log parameters, metrics, and artifacts.

```python
from foundry import tracking

with tracking.run(experiment="search-ranker") as run:
    run.log_params({"lr": 0.001, "batch_size": 256})
    for step, loss in enumerate(train()):
        run.log_metric("loss", loss, step=step)
    run.log_artifact("model.pt")
```

## What to log

- **Parameters:** everything that affects the result, including the random seed.
- **Metrics:** training and validation metrics at regular intervals.
- **Data references:** the FeatureHub views and versions used.
- **Code version:** Foundry records the commit automatically; do not override it.
- **Artifacts:** the model file and any evaluation reports.

## Naming

Experiments are named for the task, such as `search-ranker`. Runs get an automatic ID; add a short human-friendly note with `run.set_note("larger batch")`.

## Comparing runs

In the tracking UI, select multiple runs and choose Compare to see parameters and metrics side by side. You can chart any metric against steps or time.

## Linking to the registry

When a run produces a model you want to keep, register it from the run page. The registry entry links back to the run, so reviewers can find the evidence.

## Tips

- Log early. A run that crashed at step 20 can still teach you something.
- Do not log large files as metrics; use artifacts.
- Tag runs that are part of a sweep with the same `sweep_id`.
