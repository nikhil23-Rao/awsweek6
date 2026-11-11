doc_id: ORG-DSEC-016
title: Customer Security Questionnaire Handling
doc_type: process
scope_level: org
owner_team: none (DSEC org-wide)
owner_org: DSEC
author_role: Compliance Analyst
status: approved
last_updated: 2026-02-24
supersedes:
fact_ids:

# Customer Security Questionnaire Handling

Enterprise customers often send security questionnaires before they sign or renew. This process describes how DSEC answers them accurately and quickly. Sales and Support bring the request to us; we own the answers.

## 1. Intake

1. The account team opens a request in the DSEC intake queue and attaches the questionnaire, the customer name, and the deadline.
2. A compliance analyst on the rota acknowledges within one business day and becomes the coordinator.
3. The coordinator reads the questionnaire and sorts the questions into topics: identity, development, data handling, availability, and certifications.

## 2. The answer library

We keep a library of approved answers in Confluence. Each entry has an owner, a last-reviewed date, and a link to the source document for the claim.

- Reuse library answers wherever they fit the question.
- Do not paraphrase an answer in a way that changes its meaning.
- If a question has no library answer, route it to the owning team (see below) and add the new answer to the library once it is approved.

## 3. Who answers what

| Topic | Route to |
|---|---|
| Single sign-on and identity | IT & Compliance |
| Code scanning and secrets | AppSec |
| Data lake and event data | Data Platform |
| Machine learning systems | ML Infrastructure |
| Availability and recovery | SRE guild |
| Legal and contract terms | Legal |

Owning teams answer within three business days and cite the source document.

## 4. Certifications and reports

TechSync holds SOC 2 Type II and ISO 27001 certifications. Customers can receive the current SOC 2 report and the ISO certificate under a non-disclosure agreement. The coordinator requests them through the CISO's office; do not send reports directly.

## 5. Review and sending

1. The coordinator assembles the answers and checks them for consistency.
2. A Security Engineer reviews anything about technical controls.
3. The CISO's office approves answers that make new commitments.
4. The account team sends the response, not DSEC.

## 6. Commitments

If a customer asks us to commit to something we do not already do, such as a bespoke contractual term, it is not answered here. Escalate it to Legal and the VP.

## 7. After the response

- Save the final questionnaire and answers on the request ticket.
- Update the library with any new approved answers.
- Note recurring questions in the monthly review; they are candidates for a public trust page.
