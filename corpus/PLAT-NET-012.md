---
doc_id: PLAT-NET-012
title: EdgeGate WAF Rule Change Process
doc_type: process
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: Security Engineer
status: approved
last_updated: 2026-01-13
supersedes: ""
fact_ids: ""
---

# EdgeGate WAF Rule Change Process

Networking with AppSec. Author: Security Engineer.

EdgeGate's web application firewall (WAF) blocks malicious traffic before it reaches our services. WAF changes can easily block real customers, so we treat them with the same care as code.

## Who can request a change

- **AppSec**, for new threats or findings from Sentinel and penetration tests.
- **Any service team**, for false positives affecting their routes.
- **Support**, on behalf of customers, through a Jira ticket.

## Process

1. **Request.** File a ticket in the NET Jira project using *WAF Rule Change*. Include the route, the example request (redact customer data), and the desired behavior.
2. **Draft.** The NET engineer on WAF duty writes the rule in the `edgegate-waf` repository.
3. **Review.** Every rule change needs review from one NET engineer and one AppSec engineer.
4. **Count mode.** New blocking rules first run in **count mode** in prod for at least 24 hours. Count mode logs what would be blocked without blocking it.
5. **Analyze.** Check the count-mode hits in Tracewell. Make sure legitimate traffic isn't caught.
6. **Enforce.** Switch the rule to block mode through Gatekeeper CI.

## Emergency rules

During an active attack, the NET on-call can deploy a blocking rule directly to enforce mode with AppSec approval in the incident channel. The rule gets a normal review within one business day afterward.

## False positives

If customers report blocked requests, first check `edgegate_waf_blocks_total` by rule ID. Disabling a single rule is preferred over loosening the whole rule group.

## Records

All WAF changes are tracked in Jira and logged to Compass for audit evidence.
