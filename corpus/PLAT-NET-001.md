---
doc_id: PLAT-NET-001
title: VPC Peering and Transit Gateway Request Process
doc_type: how-to guide
scope_level: team
owner_team: NET
owner_org: PLAT
author_role: Tech Lead
status: approved
last_updated: 2024-08-07
supersedes: ""
fact_ids: ""
---

# VPC Peering and Transit Gateway Request Process

Networking (NET)

Most services never need this: anything running on Kestrel already reaches other Kestrel services through Meridian Mesh. You need this process when a workload outside Kestrel (a managed AWS service, a data warehouse VPC, a vendor's PrivateLink endpoint) has to talk to something in another VPC.

## Which option do I need?

| Situation | What we use |
|---|---|
| Two TechSync VPCs in the same region | Transit Gateway attachment |
| Two TechSync VPCs in different regions | Transit Gateway peering between regional TGWs |
| A vendor or SaaS endpoint | AWS PrivateLink |
| A one-off VPC peering connection | Not offered; use the Transit Gateway |

We stopped creating direct VPC peering connections in 2023. They don't scale and they're hard to audit.

## How to request

1. Open a ticket in the NET Jira project using *Network Connectivity Request*.
2. Include source and destination VPC IDs, the CIDR ranges, the ports and protocols, and the business reason.
3. If either side handles EU customer data in eu-west-1, say so. Cross-region paths out of eu-west-1 need AppSec review.
4. NET reviews requests every Monday and Thursday.

## What NET checks

- No overlapping CIDRs.
- The narrowest possible security group and route table rules.
- Routes are added in Terraform, never by hand in the AWS console.

## Turnaround

Same-region attachments: about 3 business days. Cross-region or PrivateLink: about 1 to 2 weeks, depending on the vendor.

## Removing connectivity

When a connection isn't needed anymore, file a ticket so we can remove the routes. We audit unused attachments every quarter.
