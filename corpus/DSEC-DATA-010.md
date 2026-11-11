doc_id: DSEC-DATA-010
title: Streamline Kafka Upgrade Playbook
doc_type: runbook
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: SRE
status: approved
last_updated: 2025-11-06
supersedes:
fact_ids:

# Streamline Kafka Upgrade Playbook

Rolling-upgrade procedure for the Streamline Kafka clusters. Follow it in order. Do not improvise steps in prod.

## 1. When to upgrade

Upgrade for security fixes, bug fixes we need, or when a version nears end of support. Plan upgrades on Tuesday through Thursday, with a second SRE available. Upgrade dev first, then staging, then prod, leaving at least one week between environments unless a security fix requires otherwise.

## 2. Pre-checks

- [ ] Release notes read; breaking changes noted
- [ ] All topics fully in sync (no under-replicated topics)
- [ ] No partition reassignments in progress
- [ ] Consumer lag normal on the main groups
- [ ] Recent broker backup of configuration
- [ ] Rollback plan reviewed
- [ ] Announcement posted in the DATA and DSEC channels

## 3. Upgrade procedure (per broker)

1. Pick the broker that is not the active controller.
2. Verify health: all topics in sync before you start.
3. Set the broker to a controlled shutdown.
4. Upgrade the broker image through Terraform and let Kestrel restart it.
5. Wait for the broker to rejoin and for every topic to be in sync again.
6. Check the broker's error rate and latency for 10 minutes.
7. Continue to the next broker. Upgrade the controller last.

Do not upgrade more than one broker at a time.

## 4. Protocol version

Keep the inter-broker protocol version on the old setting until every broker is upgraded and a day has passed without issue. Then raise it in a separate change.

## 5. Rollback

Before the protocol version is raised:

1. Stop the upgrade.
2. Roll the upgraded brokers back to the previous image one at a time, checking sync status after each.
3. Post what happened in the DATA channel.

After the protocol version is raised, rollback is not supported. Call the Tech Lead.

## 6. Verification

- Producers and consumers report no errors.
- Lag on main consumer groups returns to baseline.
- The schema registry is reachable.

## 7. Post-upgrade

Update the cluster inventory, close the ticket, and note any surprises in the playbook.

## 8. Contacts

DATA on-call through Lookout; DATA Tech Lead for rollback decisions.
