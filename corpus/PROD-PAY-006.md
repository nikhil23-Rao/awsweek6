doc_id: PROD-PAY-006
title: Meterflow Usage Event Ingestion Design
doc_type: design doc
scope_level: team
owner_team: PAY
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2025-10-08
supersedes:
fact_ids: 

---

# Meterflow Usage Event Ingestion Design

**Author:** Staff Engineer (PAY)  **Status:** Approved

## Problem

Customers send millions of usage events per hour. We must count each event exactly once, even when senders retry or networks fail.

## Overview

Events arrive at the ingestion API, are validated, and are published to Kafka on Streamline. Aggregation workers consume the topic and update usage totals.

## Components

1. **Ingestion API.** Validates the schema, authenticates the sender and assigns a receipt ID.
2. **Kafka topic.** Partitioned by customer ID so one customer's events stay in order.
3. **Deduplicator.** Uses the event's idempotency key and a rolling window in Redis to drop duplicates.
4. **Aggregator.** Writes hourly counts to PostgreSQL.

## Idempotency

Senders include an `event_id`. The deduplicator remembers IDs for 72 hours. Events with an unseen ID are accepted; seen IDs are acknowledged but not counted again.

## Failure handling

- If Kafka is unavailable, the API returns a retryable error.
- If the deduplicator is down, events are accepted and deduplicated later by a reconciliation job.

## Scaling

Add partitions and consumers together. The system has been tested at four times current peak.

## Alternatives considered

Deduplicating in the database alone was simpler but too slow at peak.
