doc_id: DSEC-SEC-005
title: Sentinel Rule Tuning Guide
doc_type: guide
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2026-03-04
supersedes:
fact_ids:

# Sentinel Rule Tuning Guide

Sentinel ships with a default rule set, and AppSec adjusts it so that findings are useful and noise is low. This guide describes how we tune rules and how you can propose changes. It is written for Security Engineers, though service owners with an opinion about a noisy rule are welcome to contribute.

## Rule anatomy

A rule has an ID, a language or ecosystem, a pattern, a severity, and a message explaining the problem and how to fix it. Rules live in the `sentinel-rules` repository and are loaded by Sentinel on its next rule refresh.

## When to tune

Tune a rule when at least one of the following is true:

- More than half of its findings are marked false positive in triage.
- The message does not tell the reader what to do.
- The severity does not match the real-world impact.
- It misses a class of issue found by a pen test or a bug bounty report.

## How to tune

1. Gather evidence: link at least five findings that show the problem.
2. Draft the change in a branch of `sentinel-rules`.
3. Run the rule test suite. Each rule has positive and negative sample files.
4. Add a sample that reproduces the original problem.
5. Open a pull request and request review from a second Security Engineer.
6. After merge, watch the rule's finding volume for a week.

## Severity guidance

| Severity | Typical meaning |
|---|---|
| Critical | Directly exploitable with high impact, such as remote code execution |
| High | Exploitable under realistic conditions, or leaks sensitive data |
| Medium | Needs unusual conditions or has limited impact |
| Low | Hygiene issue |

When in doubt, rate lower and revisit once a real exploit path is shown.

## Writing good messages

Say what is wrong, why it matters, and the fix, in that order. Link to internal guidance if it exists.

## Retiring rules

A rule that has produced no true positives in a year may be retired. Record the decision in the rule's changelog.
