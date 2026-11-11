doc_id: DSEC-SEC-001
title: Sentinel Dependency Scanning Standard
doc_type: standard
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Security Engineer
status: approved
last_updated: 2026-04-08
supersedes:
fact_ids: F-DSEC-007

# Sentinel Dependency Scanning Standard

**Owner:** AppSec (SEC) | **Applies to:** every repository hosted in GitHub Enterprise that builds a deployable artifact

## 1. Purpose

Sentinel is our code and dependency scanner. This standard defines when scans run and what a scan result is allowed to do to a change.

## 2. Requirements

**2.1 Scan trigger.** Sentinel scans **run on every pull request**. The scan is a stage in the Gatekeeper CI pipeline, executed on Forge runners, and is added automatically to repositories created from Scaffold templates. Repositories not created from a template must add the `sentinel-scan` stage before their first production deploy.

**2.2 Merge gating.** A pull request **cannot be merged while it has an open Critical finding**. The merge check is enforced as a required status check in GitHub Enterprise and cannot be bypassed by repository admins.

**2.3 High and lower findings.** High findings do not block the merge. Sentinel opens a tracking ticket assigned to the owning team and posts a summary comment on the pull request. Medium and Low findings are reported in the weekly digest only.

**2.4 Scan scope.** Each scan covers direct and transitive dependencies resolved from lockfiles, container base images referenced by Dockerfiles, and first-party source files for the supported languages (Go, Python, TypeScript, Kotlin, Swift).

## 3. Waivers and false positives

A finding believed to be a false positive is marked through the triage workflow described in the False Positive Triage FAQ. A SEC engineer must approve the suppression, and suppressions are recorded with an expiry date. Waivers for true findings are not available for Critical severity.

## 4. Responsibilities

- Service owners keep the `sentinel-scan` stage enabled and respond to tickets.
- SEC maintains rule sets and the scan queue.
- DEVT maintains the Gatekeeper CI stage definitions.

## 5. Review

This standard is reviewed by the SEC tech lead and engineering manager each year.
