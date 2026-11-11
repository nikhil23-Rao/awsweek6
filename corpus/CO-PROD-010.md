doc_id: CO-PROD-010
title: ADR Policy
doc_type: policy
scope_level: company
owner_team: Architecture Review Board
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2025-04-02
supersedes:
fact_ids: F-POL-11; F-PROD-010

---

# Architecture Decision Record (ADR) Policy

**Owner:** Architecture Review Board (chaired by the CTO)

## 1. Why we write ADRs

Architectural choices outlive the people who make them. An Architecture Decision Record captures what was decided, why, and what else was considered, so that the next team does not have to rediscover it.

## 2. When an ADR is required

**An ADR is required whenever a change affects more than one team.**

"Affects" means that another team must change its code or configuration, relies on behavior that will change, or carries operational responsibility that changes as a result of the decision.

## 3. What an ADR contains

Every ADR includes:

1. **Title and ID.** A short title and a sequential identifier.
2. **Context.** The situation and constraints.
3. **Decision.** What was chosen, in one or two clear sentences.
4. **Alternatives.** Other options considered, and why they were not chosen.
5. **Consequences.** What gets easier, what gets harder, and who is affected.
6. **Affected teams.** Each team named, with a contact.

## 4. Statuses

- **Proposed:** open for comment.
- **Accepted:** approved by the Architecture Review Board.
- **Rejected:** reviewed and declined, kept for the record.
- **Deprecated:** no longer in effect, with a pointer to what replaced it.

## 5. Review

The author submits the ADR to the Architecture Review Board. The Board reviews proposals on its regular cadence and may ask the author to involve affected teams before it decides. An ADR takes effect only once it is marked Accepted.

## 6. Storage

Accepted ADRs are stored in the shared Confluence space for architecture records. Authors link the ADR from related pull requests and design documents.

## 7. Questions

Contact the Architecture Review Board through its Slack channel, or see the ADR Review Process FAQ.
