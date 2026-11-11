doc_id: PROD-WEB-008
title: Console Feature Flag Conventions
doc_type: FAQ
scope_level: team
owner_team: WEB
owner_org: PROD
author_role: Staff Engineer
status: approved
last_updated: 2026-01-22
supersedes:
fact_ids: 

---

# Console Feature Flag Conventions

**Q: Why do we use feature flags?**
So we can ship code before a feature is ready for everyone, test with a small group, and turn something off without a new release.

**Q: How do I name a flag?**
Use lower kebab case with a team prefix and the feature: `web-new-dashboard-layout`. Avoid dates and the word "test."

**Q: What kinds of flags are there?**
- *Release flags* hide unfinished work and are short lived.
- *Experiment flags* split users between variants.
- *Ops flags* let us disable expensive behavior in an emergency and may live for a long time.

**Q: Who owns a flag?**
The engineer who creates it. Put your name and a cleanup date in the flag description.

**Q: When do I remove a flag?**
A release flag should be removed within two sprints of reaching everyone. A reminder is posted in #prod-web on the cleanup date.

**Q: Can flags depend on each other?**
Avoid it. If you must, document the dependency in both descriptions.

**Q: What should the default be?**
Off. Flags are enabled deliberately.

**Q: How do I test with a flag on?**
Use the flag override panel in staging, or set the flag for your own user.
