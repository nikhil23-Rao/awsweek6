doc_id: PROD-MOB-011
title: Mobile Accessibility Guidelines
doc_type: guideline
scope_level: team
owner_team: MOB
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2025-12-11
supersedes:
fact_ids: 

---

# Mobile Accessibility Guidelines

Everyone should be able to acknowledge an alert or approve a release from their phone. These guidelines apply to both apps.

## VoiceOver (iOS)

- Give every control an `accessibilityLabel` that describes its purpose, not its appearance.
- Use `accessibilityTraits` correctly: buttons are buttons, headers are headers.
- Group related elements so that a card is read as one item.
- Announce changes such as a new alert using `UIAccessibility.post`.

## TalkBack (Android)

- Set `contentDescription` on icons and image buttons; mark decorative images as not important for accessibility.
- Use semantic roles in Compose (`Role.Button`, `heading()`).
- Merge descendants where a row should be a single focus target.

## Text and layout

- Support dynamic type on iOS and font scaling on Android; layouts must not clip at the largest sizes.
- Touch targets are at least 44 points on iOS and 48 dp on Android.
- Keep contrast at least 4.5:1 for text.

## Motion and sound

Respect the system settings for reduced motion. Do not rely on sound alone to convey an alert.

## Testing

Before each release, one engineer walks through alerts, approvals and settings with each screen reader.
