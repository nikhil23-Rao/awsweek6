doc_id: DSEC-ITC-004
title: Open-Source License Exception for Internal-Only Tooling
doc_type: policy exception
scope_level: team
owner_team: ITC
owner_org: DSEC
author_role: Compliance Analyst
status: approved
last_updated: 2026-02-17
supersedes:
fact_ids: F-POL-12, F-DSEC-009

# Open-Source License Exception for Internal-Only Tooling

**Approved by:** Tamsin Reid (CISO) and Legal | **Approved:** February 2026 | **Owner:** IT & Compliance (ITC)

## Why this exists

ITC maintains small automation around Compass and Keystone: evidence collectors, export scripts, directory helpers. Several of the best libraries for these jobs are GPL-licensed. Because our scripts never leave the company, a separate legal review for every library adds delay without reducing risk.

## What is allowed

ITC engineers **may use GPL-licensed libraries (GPL and LGPL) in ITC internal-only tools without a per-use legal review.** Each use must be logged in the ITC license register with the library, version, tool, and date.

## Scope limits

This exception applies only to tools that meet **all** of these conditions:

- Owned by ITC.
- Run only inside TechSync infrastructure.
- **Never distributed outside TechSync**, in any form: not to customers, not to partners, not to contractors outside our network, and not bundled in any product artifact.

It does not cover AGPL libraries, which require legal review in every case.

## What is not covered

- Anything shipped to customers.
- Any tool owned by another team.
- Any library under a license other than GPL or LGPL.

## If a tool's use changes

If an internal tool is ever proposed for distribution outside TechSync, the exception stops applying to it. The tool must go through legal review before release.

## Register review

The ITC engineering manager reviews the license register each quarter and reports to AppSec.
