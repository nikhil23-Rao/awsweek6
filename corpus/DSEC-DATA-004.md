doc_id: DSEC-DATA-004
title: Streamline Consumer Lag Troubleshooting
doc_type: runbook
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: SRE
status: approved
last_updated: 2026-02-05
supersedes:
fact_ids:

# Streamline Consumer Lag Troubleshooting

Use this runbook when a Lookout alert reports consumer lag on a Streamline topic, or when a team reports that events are arriving late.

## 1. Confirm the symptom

1. Open the Streamline lag dashboard and select the consumer group.
2. Note the current lag and whether it is growing, flat, or shrinking.
3. Check the time the lag started, and compare against recent deploys of the consuming service.

A flat or shrinking lag means the consumer is catching up; keep watching but do not intervene.

## 2. Decide the cause

| Pattern | Likely cause |
|---|---|
| Lag grows steadily on one consumer group only | Slow or stuck consumer |
| Lag grows on many groups at once | Broker or network issue |
| Lag jumps after a deploy | New code is slower or failing |
| Lag spikes then recovers daily | A batch job or traffic peak |

## 3. Slow or stuck consumer

1. Look at the consuming service's logs for exceptions, repeated retries, or long processing times.
2. Check pod restarts in Kestrel.
3. If one instance is stuck, delete that pod and let Kestrel reschedule it.
4. If all instances are slow, scale the deployment up by about 50 percent and watch the dashboard.
5. If a poison message is repeatedly failing, send it to the topic's `.dlq` and move on.

## 4. Broker or network issue

1. Check the broker health panel for under-replicated topics or leader elections.
2. Check the Meridian Mesh dashboard for elevated errors between the consumers and brokers.
3. Page the DATA on-call through Lookout if broker health is degraded. Do not restart brokers yourself.

## 5. After a deploy

Roll the consumer back first, then investigate. A rollback is cheap and restores flow while you diagnose.

## 6. Closing out

- Confirm lag has returned to normal for 30 minutes.
- Post a summary in the DATA channel.
- If a poison message was found, open a ticket for the producing team.
