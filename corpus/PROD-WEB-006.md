doc_id: PROD-WEB-006
title: Prism Component Contribution Guide
doc_type: guide
scope_level: team
owner_team: WEB
owner_org: PROD
author_role: Tech Lead
status: approved
last_updated: 2026-03-02
supersedes:
fact_ids: 

---

# Prism Component Contribution Guide

Prism is TechSync's design system, and the Web team stewards it. Anyone at the company can propose a component. This guide explains how.

## Before you propose

Check the component library. Many needs are met by an existing component with different options. If you are not sure, ask in #prism.

## Proposal

1. Open a Jira ticket in the Prism project with a short description, a sketch or screenshot, and examples of where it would be used.
2. A Web Tech Lead or Staff Engineer will triage the ticket within a week.
3. If accepted, you and a Prism maintainer agree on an API (props, events, accessibility behavior).

## Building

- Write the component in TypeScript with React.
- Add stories showing every variant and state.
- Use design tokens, never hard-coded colors or spacing.
- Meet the Accessibility Standard for Product UIs: keyboard operable, labeled, correct contrast.

## Review

Two reviewers, including one Prism maintainer, must approve the pull request. Visual regression tests must pass.

## Release

Prism releases twice a month. Release notes list new components and any breaking changes.

## Getting help

Office hours with a maintainer are held Thursdays at 11:00 Pacific.
