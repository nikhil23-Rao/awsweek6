doc_id: DSEC-SEC-008
title: Vaultline Audit Log Export Guide
doc_type: guide
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Security Engineer
status: approved
last_updated: 2026-02-12
supersedes:
fact_ids:

# Vaultline Audit Log Export Guide

Vaultline records every request it receives. This guide explains how to get those audit events out of Vaultline and into places where teams can search them.

## What an audit event contains

Each event describes who made the request (the authenticated identity), what they asked for (the path and operation), when, and whether it succeeded. Secret values are never written to the audit log; values are hashed.

## How export works

1. Vaultline writes audit events to an audit device configured by SEC.
2. A shipper forwards events to a Streamline topic, `security.vaultline.audit.v1`.
3. A consumer indexes the events into OpenSearch, where the security dashboards read them.

You do not configure the audit device yourself; SEC manages it. You may request access to the dashboards or a filtered feed for your team.

## Requesting a feed for your team

Teams that want to see access to their own secret paths can request a filtered view.

1. Open an intake request with the paths you own.
2. Name the Slack channel for any alerts.
3. SEC reviews and creates a filtered dashboard.

## Searching events

In the OpenSearch dashboard, useful fields are:

| Field | Meaning |
|---|---|
| `auth.display_name` | Identity making the request |
| `request.path` | Secret path requested |
| `request.operation` | read, create, update, delete, list |
| `response.status` | Success or error |

Example question: "Who read anything under `kv/payments/` yesterday?" Filter on `request.path` and `request.operation`.

## Investigations

For an investigation, SEC can join Vaultline events with Keystone sign-in events. Request this through a Security Engineer; do not export raw events to personal drives.

## Troubleshooting

- **Events missing:** check the shipper's status page; if it is unhealthy, page the SEC on-call.
- **Events delayed:** look at consumer lag on the audit topic.
- **Dashboard empty:** confirm your filter paths match the actual mount names.
