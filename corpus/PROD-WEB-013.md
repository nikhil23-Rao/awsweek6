doc_id: PROD-WEB-013
title: Prism Accessibility Testing Checklist
doc_type: checklist
scope_level: team
owner_team: WEB
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-06-12
supersedes:
fact_ids: 

---

# Prism Accessibility Testing Checklist

Use this checklist when you add or change a Prism component. Automated checks catch some problems; the manual steps catch the rest.

## Automated

- [ ] The component passes axe checks in Storybook for every story.
- [ ] Unit tests cover keyboard interactions.
- [ ] Visual tests render correctly in light and dark themes.

## Keyboard

- [ ] Every interactive part can be reached with Tab and Shift+Tab, in a logical order.
- [ ] Enter and Space activate buttons; arrow keys move within composite widgets.
- [ ] Focus is never trapped, except in modals, which return focus when closed.
- [ ] A visible focus indicator appears on every focusable element.

## Screen reader

- [ ] The component's role, name and state are announced.
- [ ] Dynamic changes use live regions where needed.
- [ ] Decorative icons are hidden from assistive technology.

## Visual

- [ ] Text contrast is at least 4.5:1 (3:1 for large text).
- [ ] The component works at 200% zoom without losing content.
- [ ] Information is not conveyed by color alone.

## Record the result

Add a short note to the pull request describing what you tested and with which screen reader.
