---
doc_id: ORG-PLAT-009
title: Internal API Deprecation Process
doc_type: process
scope_level: org
owner_team: PLAT (org-wide)
owner_org: PLAT
author_role: Tech Lead
status: approved
last_updated: 2025-09-02
supersedes: ""
fact_ids: ""
---

# Internal API Deprecation Process

**Scope:** internal APIs and CLIs owned by Platform Engineering
**Owner:** Platform tech leads

Platform APIs have many consumers we don't always know about. This process makes sure removing or changing an API doesn't break them.

## When this applies

- Removing an API endpoint, CLI command, or flag.
- Changing an API's behavior in a way that could break callers.
- Removing a configuration option from Scaffold, Gatekeeper CI, Lookout, or Tracewell config files.

## Steps

1. **Find consumers.** Use Tracewell service maps, GitHub code search, and API access logs. List every known caller.
2. **Announce.** Post in #eng-announce and the owning team's channel with: what's changing, why, the replacement, and the removal date.
3. **Warn.** Add deprecation warnings: response headers for APIs, stderr warnings for CLIs, Gatekeeper CI validation warnings for config.
4. **Notice period.** At least **90 days** between announcement and removal. Longer for anything used by many teams.
5. **Track.** Keep a list of remaining callers and reach out to each owning team directly.
6. **Remove.** Remove on the announced date only if known callers have migrated. Otherwise, extend the date and announce it.

## Emergency removals

Security issues can shorten the notice period, with approval from AppSec and the VP Platform Engineering.

## Records

Keep a deprecation page in Confluence for each removal, with dates and the caller list.
