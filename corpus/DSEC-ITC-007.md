doc_id: DSEC-ITC-007
title: Keystone Application Onboarding Checklist
doc_type: checklist
scope_level: team
owner_team: ITC
owner_org: DSEC
author_role: Tech Lead
status: approved
last_updated: 2026-04-14
supersedes:
fact_ids:

# Keystone Application Onboarding Checklist

Use this to integrate an internal application with Keystone. Copy it into your ticket and tick items as you go.

## Before you start

- [ ] The application has an owner team and an on-call channel.
- [ ] You know whether users are employees only, or employees and contractors.
- [ ] You have read the Role and Group Naming Standard.

## Registration

- [ ] Register the application in the Keystone request portal.
- [ ] Choose OIDC unless the app only supports SAML.
- [ ] Add redirect URIs separately for dev, staging, and prod.
- [ ] Record the client ID in your service's configuration, not the client secret. Store the secret in Vaultline.

## Groups and roles

- [ ] Create the groups the app needs, following the naming standard.
- [ ] Assign an owning team for every group.
- [ ] Map groups to application roles in your app's configuration.

## Provisioning

- [ ] Decide whether the app needs SCIM provisioning. If it keeps its own user records, it does.
- [ ] If yes, configure the SCIM endpoint and test joiner, mover, and leaver cases in staging.

## Testing

- [ ] Sign in as a user with each role and confirm the expected access.
- [ ] Sign in as a user with no group and confirm they are denied.
- [ ] Confirm sign-out behaves as intended.

## Go-live

- [ ] Review with an ITC engineer.
- [ ] Announce in the ITC channel.
- [ ] Add the application to the Compass inventory.

## Afterwards

Revisit your groups and roles whenever the app's features change.
