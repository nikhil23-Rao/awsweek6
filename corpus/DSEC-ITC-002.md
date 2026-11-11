doc_id: DSEC-ITC-002
title: Keystone SSO Configuration Guide
doc_type: reference
scope_level: team
owner_team: ITC
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2026-06-11
supersedes:
fact_ids: F-DSEC-004

# Keystone SSO Configuration Guide

Reference for engineers integrating an application with Keystone SSO. Keystone is a Tier 0 service owned by IT & Compliance.

## 1. Session model

Keystone issues a session when a user signs in. Applications receive an ID token and a refresh token bound to that session.

**Keystone SSO sessions last at most 8 hours.** Applications that use Keystone SSO, including Console, cannot extend a session past that limit. When the 8 hours end, the user is sent back through sign-in.

## 2. Settings

| Setting | Value | Notes |
|---|---|---|
| `session_max_age` | 8h | Hard ceiling, not configurable per app |
| `session_idle_timeout` | 30m | May be lowered per app, never raised |
| `id_token_ttl` | 15m | Refreshed silently while the session lives |
| `refresh_token_ttl` | Bound to session | Cannot outlive `session_max_age` |

## 3. What applications may and may not do

- You **may** shorten the effective session by setting a lower idle timeout or forcing re-authentication for sensitive actions.
- You **may not** issue your own long-lived application cookie that keeps a user signed in after the Keystone session has ended.
- You **may not** exchange an expired refresh token for a new session.

## 4. Behaviour you should expect

- A user who signs in at 08:00 will be asked to sign in again by 16:00 at the latest, even if active the whole time.
- Single sign-out revokes all application sessions for that user within about a minute.
- Console and other first-party apps follow the same ceiling. Support engineers cannot extend a session on a user's behalf.

## 5. Integration checklist

1. Register the application in Keystone and select the OIDC flow.
2. Set redirect URIs for dev, staging, and prod separately.
3. Handle the expired-session redirect without losing unsaved work.
4. Test an idle timeout and a max-age expiry in staging.

## 6. Contact

ITC Keystone channel. For outages follow the Sev1 paging procedure.
