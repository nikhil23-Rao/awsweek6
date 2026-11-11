doc_id: PROD-MOB-003
title: Mobile Release Checklist
doc_type: checklist
scope_level: team
owner_team: MOB
owner_org: PROD
author_role: Tech Lead
status: unmarked
last_updated: 2025-10-14
supersedes:
fact_ids: F-PROD-009

---

# Mobile Release Checklist

Use this for every TechSync Mobile release, whether iOS or Android. Copy it into the release ticket.

## One week before

- [ ] Release branch cut and version number agreed.
- [ ] Release notes drafted.
- [ ] Translations complete for all supported languages.

## Platform requirements

- [ ] The iOS build targets **iOS 15** as the minimum supported version.
- [ ] The Android build targets the minimum API level listed in the Supported Platforms page.
- [ ] Devices on the oldest supported versions are included in the manual test pass.

## Three days before

- [ ] Regression suite is green on both platforms.
- [ ] Internal beta build has been in testers' hands for at least three days.
- [ ] Crash-free rate in beta is above the team's threshold.

## Release day

- [ ] Build uploaded and submitted for review.
- [ ] Phased rollout set to the agreed percentage.
- [ ] Release announced in #prod-mobile.

## After release

- [ ] Watch crash-free rate and push delivery for 48 hours.
- [ ] Update the support team with known issues.
- [ ] Hold a short retrospective if anything went wrong.

## Owner

Tech Lead, Mobile. Update this list after every release if something was missing.
