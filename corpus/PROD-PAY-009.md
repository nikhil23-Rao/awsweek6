doc\_id: PROD-PAY-009 title: Postmortem: Duplicate Usage Events during Kafka Rebalance doc\_type: postmortem scope\_level: team owner\_team: PAY owner\_org: PROD author\_role: SRE status: approved last\_updated: 2026-03-16 supersedes: fact\_ids:

---

# Postmortem: Duplicate Usage Events during Kafka Rebalance

**Severity:** Sev2  **Incident date:** 2026-03-09  **Published: 2026-03-16**  **Author:** SRE (PAY)

## Summary

During a Kafka consumer rebalance, a set of usage events was processed twice for about 25 minutes. Roughly 0.3% of that period's events were double counted. The error was corrected before any invoice was finalized.

## Detection

A reconciliation alert showed that usage totals for several customers exceeded the number of events received.

## Timeline (UTC)

- **14:02** A scaling change added consumers, triggering a rebalance.  
- **14:05** Some consumers committed offsets late, so events were redelivered.  
- **14:31** The reconciliation alert fired.  
- **14:40** The on-call engineer paused aggregation.  
- **15:20** The deduplication window was extended and aggregation resumed.  
- **17:00** A correction job fixed the affected totals.

## Root cause

The deduplicator relied on a short in-memory window that was reset by the rebalance. Redelivered events were seen as new.

## What went well

The reconciliation alert caught the problem quickly. Correction was done without customer impact.

## What went badly

The scaling change was made without considering consumer rebalance behavior.

## Action items

1. Persist the deduplication window outside the process (owner: Staff Engineer).  
2. Add a rebalance-safe scaling procedure to the runbook (owner: SRE).  
3. Alert on duplicate rate (owner: SRE).