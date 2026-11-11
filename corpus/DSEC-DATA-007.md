doc_id: DSEC-DATA-007
title: Reservoir Dataset Onboarding FAQ
doc_type: FAQ
scope_level: team
owner_team: DATA
owner_org: DSEC
author_role: Technical Writer
status: approved
last_updated: 2026-05-21
supersedes:
fact_ids:

# Reservoir Dataset Onboarding FAQ

**What is a dataset?**
A table registered in the Reservoir catalog with a named owner team. Unregistered files are not supported.

**How do I register one?**
Open a request in the DATA queue with the dataset name, owner team, description, and the schema. DATA reviews within two business days.

**Who should be the owner?**
A team, not a person. The owner answers questions and keeps the schema and checks current.

**What do I need before I load data?**
A schema, a source, a job definition in the `reservoir-jobs` repo, and the required data quality checks described in the Data Quality Checks Standard.

**Which domain prefix should I use?**
Choose the product area the data belongs to, such as `payments` or `search`. If none fits, ask in the DATA channel.

**Do I need to tag the dataset?**
Yes. Datasets carry `owner_team`, `service`, and `classification` tags. Untagged datasets are flagged in the monthly cost report.

**How do I read the data?**
Through Quarry. Ask for read access in the Keystone request portal; group names follow the naming standard.

**Can I share a dataset with another team?**
Yes. The owner approves access requests. For questions about how sensitive the data is, see the company data classification standard.

**What if the upstream schema changes?**
Tell the DATA channel before the change. Jobs fail on schema mismatch, and we would rather plan the migration than fix it at night.

**Who do I ask for help?**
The DATA channel, or the intake queue for anything that needs work.
