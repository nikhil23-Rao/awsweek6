doc_id: PROD-SRCH-009
title: Relevance Tuning Basics FAQ
doc_type: FAQ
scope_level: team
owner_team: SRCH
owner_org: PROD
author_role: Tech Lead
status: approved
last_updated: 2026-01-27
supersedes:
fact_ids: 

---

# Relevance Tuning Basics FAQ

**What is relevance?**
How well search results match what the user was looking for. Better relevance means the right result is near the top.

**What can I tune?**
- Which fields are searched
- How much each field counts (boosts)
- How text is split into terms (analyzers)
- How recent results are ranked

**What is a boost?**
A multiplier on a field's contribution. A match in the title might count three times as much as a match in the body.

**What is an analyzer?**
The recipe for breaking text into terms: lowercasing, splitting on spaces, removing endings (stemming) and so on.

**How do I know a change helped?**
Use the evaluation harness. It runs a set of sample queries and compares ranking quality before and after.

**Why did my change break something?**
Relevance is a trade-off. A boost that helps one query can hurt another. Always run the whole set.

**Should I tune per customer?**
Rarely. Start with defaults, and only add account-specific settings when there is a clear reason.

**Where do I ask for help?**
#prod-search, or find the Tech Lead during office hours on Wednesdays.
