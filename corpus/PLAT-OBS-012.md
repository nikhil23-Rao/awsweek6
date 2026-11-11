---
doc_id: PLAT-OBS-012
title: Lookout Silences and Maintenance Windows FAQ
doc_type: FAQ
scope_level: team
owner_team: OBS
owner_org: PLAT
author_role: SRE
status: approved
last_updated: 2026-01-27
supersedes: ""
fact_ids: ""
---

# Lookout Silences and Maintenance Windows FAQ

Observability, SRE

**What's a silence?**

A silence stops matching alerts from notifying anyone for a set period. The alerts still evaluate and show in the Lookout UI as "silenced," so you can see what would have fired.

**When should I use one?**

During planned work you know will trigger alerts: a database failover test, a load test in staging, a cluster upgrade. Also for a known issue already being worked on, so the on-call isn't paged repeatedly.

**How do I create one?**

In the Lookout UI under **Silences**, or with the CLI:

```
lookout silence create --match team=SRCH --match service=sieve --duration 2h --comment "Sieve reindex, SRCH-1342"
```

Always include a comment and a ticket link.

**What's the maximum duration?**

24 hours. Longer silences need to be renewed. This stops silences from being forgotten.

**Can I silence another team's alerts?**

Only if you're the on-call for an incident affecting them, and you tell them in their channel. Lookout logs who created every silence.

**What's a maintenance window?**

A recurring silence attached to a schedule, for things like weekly batch jobs that predictably spike a metric. Maintenance windows are defined in `lookout/maintenance.yaml` and reviewed like code.

**My silence didn't work.**

Check the matchers. Labels are case-sensitive, and `team=srch` doesn't match `team=SRCH`.

**Do silences apply to the Lookout heartbeat?**

No. The external heartbeat monitor can't be silenced from Lookout.
