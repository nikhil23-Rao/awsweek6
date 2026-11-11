doc_id: CO-DSEC-012
title: Open-Source License Policy
doc_type: policy
scope_level: company
owner_team: SEC
owner_org: DSEC
author_role: Security Engineer
status: approved
last_updated: 2025-06-10
supersedes:
fact_ids: F-POL-12

# Open-Source License Policy

**Owner:** AppSec, with Legal | **Applies to:** all code, libraries, and tools used at TechSync, in products and in internal tooling

## 1. Policy

Only open-source software under an **approved license** may be used. **Copyleft-licensed software requires legal review** before first use. This applies whether or not the software will ever be distributed outside the company.

## 2. Approved licenses

- MIT
- Apache License 2.0
- BSD 2-Clause and 3-Clause
- ISC

Components under any license not on this list are not approved until reviewed.

## 3. Copyleft

Licenses in the GPL family (GPL, LGPL, AGPL) and other strong copyleft licenses need a legal review. Open a request through AppSec; AppSec routes it to Legal. Do not merge code that depends on the library until the review is granted.

## 4. How Sentinel helps

Sentinel detects licenses in dependencies and flags anything not on the approved list on the pull request. Flagged dependencies need either a swap to an approved alternative or a legal review request.

## 5. Records

AppSec keeps an inventory of all approved reviews. Each entry names the library, version, intended use, and reviewer.

## 6. Exceptions

Exceptions to this policy must be approved in writing by the CISO and Legal and must state their scope.
