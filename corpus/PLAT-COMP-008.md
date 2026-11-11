---
doc_id: PLAT-COMP-008
title: Service Capacity Runbook
doc_type: runbook
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: Tech Lead
status: unmarked
last_updated: 2018-09-14
supersedes: ""
fact_ids: F-PLAT-006
---

# Service Capacity Runbook

Core Engineering, Compute Infrastructure group

This runbook explains how a new production service gets machines. Read it before you schedule a launch date, because capacity takes time to arrive.

## How services are hosted

Every production service runs on its own pool of virtual machines in us-east-1. Pools are built from the standard Compute base image (Ubuntu with our config-management agent baked in) and sit behind an internal load balancer. Services do not share VMs with other services.

## Minimum pool

Each new service receives a **minimum pool of 3 VMs**, spread across three availability zones so one AZ outage can't take the service down. Small services almost never need more than the minimum at launch. Larger services can request a bigger starting pool.

## Requesting capacity

1. Fill out a **Compute capacity request** in Jira (project: COMPUTE). Include the service name, expected requests per second, memory footprint per process, and your launch date.
2. Compute Infrastructure reviews requests every Tuesday and Thursday.
3. Once approved, we provision the pool, register it with the load balancer, and add it to the config-management inventory. Plan for **5 to 7 business days** from approval to usable machines.

If your launch is fixed and the request is late, talk to the Compute Infrastructure on-call. We can sometimes pull VMs from the shared spare pool, but no promises.

## Instance sizes

| Size | vCPU | Memory | Typical use |
|---|---|---|---|
| small | 2 | 4 GB | internal tools, cron-style workers |
| medium | 4 | 16 GB | most API services |
| large | 8 | 32 GB | Ship build coordinators, data-heavy services |

## Growing a pool

Add VMs through another capacity request. Mention current CPU and memory usage from the monitoring dashboards. Pools can't be shrunk below 3.

## Decommissioning

When a service is shut down, file a capacity release request so the VMs return to the spare pool. Unused pools get flagged in the quarterly capacity review.

## Contacts

Compute Infrastructure on-call (pager), or the #compute-infra channel.
