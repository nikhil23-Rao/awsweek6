doc_id: ORG-PROD-010
title: Accessibility Standard for Product UIs
doc_type: standard
scope_level: org
owner_team: PROD
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2025-12-03
supersedes:
fact_ids: 

---

# Accessibility Standard for Product UIs

## Target

All customer-facing web and mobile interfaces meet WCAG 2.2 Level AA.

## Requirements

1. **Keyboard:** every interactive element is reachable and usable with a keyboard alone, with a visible focus indicator.
2. **Contrast:** text has a contrast ratio of at least 4.5:1 against its background; large text at least 3:1.
3. **Labels:** every form control has a programmatic label. Icons used as buttons have accessible names.
4. **Structure:** pages use semantic headings and landmarks.
5. **Motion:** animations can be reduced or turned off through the operating system setting.
6. **Mobile:** touch targets are at least 44 by 44 points; screen readers announce state changes.

## Use shared components

Web interfaces should use Prism components, which include accessibility behavior by default. Mobile apps follow the platform guidelines and the Mobile team's accessibility guide.

## Audits

Each product is audited twice a year. Findings are logged in Jira with the label `a11y` and are prioritized with other work.

## Ownership

Staff Engineers in Web and Mobile jointly maintain this standard.
