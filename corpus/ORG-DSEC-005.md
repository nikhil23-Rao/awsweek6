doc_id: ORG-DSEC-005
title: DSEC Technical Writing Style Guide
doc_type: style guide
scope_level: org
owner_team: none (DSEC org-wide)
owner_org: DSEC
author_role: Technical Writer
status: approved
last_updated: 2025-11-14
supersedes:
fact_ids:

# DSEC Technical Writing Style Guide

Good documentation is a product. This guide sets the shared conventions for runbooks, standards, guides, and other documents written by DSEC teams. It is short on purpose: follow it, and when it does not cover something, choose clarity.

## 1. Know the document type

Every document is one of a small set of types, and the type decides the shape.

| Type | Reader's question | Shape |
|---|---|---|
| Runbook | "Something is happening; what do I do?" | Numbered steps, expected output, escalation |
| Standard | "What must I do?" | Numbered requirements, scope, owner |
| Guide | "How do I get started?" | Narrative with examples |
| Reference | "What exactly does this setting do?" | Tables, no story |
| FAQ | "Quick question" | Question, short answer, link |
| ADR | "Why did we choose this?" | Context, decision, consequences |
| Meeting notes | "What was said?" | Attendees, discussion, actions |

Do not mix types in one document. If a runbook needs background, link to a guide.

## 2. The header block

Start each page with an owner, a status, and a last-reviewed date. Readers use these to judge whether to trust the page. Use these status words: draft, approved, deprecated.

## 3. Voice and tone

- Write to one reader, using "you".
- Use the active voice. "Restart the consumer" beats "The consumer should be restarted".
- Prefer short sentences. If a sentence has three commas, split it.
- Avoid jokes in runbooks. A tired on-call engineer at 3 a.m. should not have to decode them.
- Guides can be warm. Welcome the reader and explain why, not just how.

## 4. Structure

1. Lead with the purpose in one or two sentences.
2. Put prerequisites before steps.
3. Number steps that must happen in order; bullet items that need not.
4. Put the most likely failure next to the step where it occurs.
5. End with who to ask.

## 5. Names and terms

Use the canonical names of systems exactly: Reservoir, Streamline, Foundry, FeatureHub, Sentinel, Vaultline, Keystone, Compass. Spell out an abbreviation on first use. Refer to people by role unless the document requires a name.

## 6. Formatting

- Headings in sentence case.
- Code and commands in fenced blocks, with the language noted.
- Tables for comparisons of three or more items.
- Avoid screenshots of text; paste the text.
- Link rather than copy. Copies drift.

## 7. Examples

Weak: "Failures may occur during the job."
Better: "If the job fails with `OOMKilled`, raise `memory` in the spec and resubmit."

## 8. Review

Ask one person who did not write the page to follow it from start to finish. Every place they hesitate is a place to fix.

## 9. Help

Technical Writing holds office hours every Thursday, and you can post drafts in the DSEC docs channel.
