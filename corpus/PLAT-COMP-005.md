---
doc_id: PLAT-COMP-005
title: "Code Review Exception: Kestrel Node-Image Patch PRs"
doc_type: policy exception
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: Engineering Manager
status: approved
last_updated: 2026-02-09
supersedes: ""
fact_ids: "F-PLAT-008; F-POL-02"
---

# Code Review Exception: Kestrel Node-Image Patch PRs

**Status:** Approved
**Requested by:** Compute (COMP)
**Approved by:** Hannah Brecker (Engineering Manager, Developer Tooling, owner of the company code review policy) and Dana Whitfield (VP, Platform Engineering)
**Effective:** February 9, 2026
**Review date:** February 2027

## Background

Compute rebuilds the Kestrel node images every week to pick up OS and kernel security patches. An automated pipeline opens one pull request per week against the `kestrel-node-images` repository. Each PR bumps base-image digests and package versions. The diff is generated, the image is built and booted in dev and staging by Gatekeeper CI before the PR can merge, and the change is reviewed in aggregate during the weekly COMP patch sync.

Waiting for a second reviewer on these mechanical PRs has delayed security patches by up to four days in several weeks of 2025, mostly when the team is short-staffed during holidays.

## Exception granted

Pull requests that meet **all** of the following conditions require **1 approval** from a COMP engineer before merge:

1. The PR is opened by the `kestrel-image-bot` service account.
2. The PR modifies only files under `images/node/` in the `kestrel-node-images` repository.
3. The PR changes only base-image digests, OS package pins, or kernel version pins.
4. The dev and staging boot checks in Gatekeeper CI passed.

## What this exception does not cover

- Any human-authored PR to `kestrel-node-images`, even if it touches only `images/node/`.
- Any change to the Kestrel control plane, scheduler, admission controllers, networking, or Terraform.
- Any other Compute-owned repository, including Forge.
- Any other team.

All of the above follow the standard company code review policy without modification.

## Safeguards

- The bot PR template links the Gatekeeper CI test run and a package diff summary.
- COMP reviews all merged image PRs at the weekly patch sync and records it in the sync notes.
- If an image change causes a Sev1 or Sev2, this exception is suspended until Developer Tooling and the VP Platform Engineering re-review it.
