doc_id: PROD-WEB-003
title: Console Session Lifetime Notes
doc_type: technical reference
scope_level: team
owner_team: WEB
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-04-14
supersedes:
fact_ids: F-DSEC-004

---

# Console Session Lifetime Notes

**Audience:** Web engineers, Support

This page explains how long a signed-in Console session lasts and what happens when it ends.

## Session lifetime

Console sessions last **up to 12 hours** from sign-in. After that, the user is returned to the sign-in page and must authenticate again.

## Idle behavior

A user who is inactive for 30 minutes sees a prompt to continue. If they do not respond within five minutes, the session ends sooner than the maximum.

## What the user sees

- During the last five minutes of a session, a banner offers to save work.
- Unsaved dashboard edits are stored as local drafts and offered again at the next sign-in.
- Long-running exports continue in the background after a session ends.

## Implementation notes

- The session cookie is `HttpOnly` and `Secure`.
- Session state is stored server-side; the browser holds only an opaque identifier.
- Sign-out ends the session immediately on all tabs in the same browser.

## Common support questions

**"I was signed out in the middle of the day."** Check how long the session had been open and whether the user was idle.

**"Can I stay signed in longer?"** Console does not offer a longer session option.

## Contact

Questions go to #prod-web.
