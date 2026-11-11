doc_id: ORG-DSEC-006
title: DSEC FY2026 Roadmap Summary
doc_type: roadmap
scope_level: org
owner_team: none (DSEC org-wide)
owner_org: DSEC
author_role: TPM
status: draft
last_updated: 2026-07-08
supersedes:
fact_ids:

# DSEC FY2026 Roadmap Summary

**Status: draft for engineering manager review.** Milestones are targets, not commitments, and dates may move after the Q4 planning cycle.

## Purpose

This page summarizes what the four DSEC teams intend to deliver across the remainder of FY2026. It is a map for stakeholders in other orgs, not a replacement for each team's OKR page.

## Themes

1. **Scale the data foundation.** More predictable cost and performance in Reservoir and Streamline as volume grows.
2. **Make ML serving efficient.** Better use of GPUs and safer model rollouts in Foundry.
3. **Strengthen the software supply chain.** Build-time inventories of what we ship, and tighter integration of Sentinel into the pipeline.
4. **Modernize identity.** Standard provisioning for applications integrating with Keystone.
5. **Automate compliance.** Less manual evidence gathering through Compass.

## Milestones by team

### Data Platform (DATA)
| Quarter | Milestone |
|---|---|
| Q3 2026 | Per-team cost breakdown in Reservoir dashboards |
| Q3 2026 | Streamline schema registry lint added to CI for all producers |
| Q4 2026 | Streamline broker capacity plan agreed for next year |

### ML Infrastructure (MLI)
| Quarter | Milestone |
|---|---|
| Q3 2026 | Latency and queue-depth gates in the automatic rollback |
| Q3 2026 | FeatureHub backfill playbook published |
| Q4 2026 | GPU quota self-service tooling |

### AppSec (SEC)
| Quarter | Milestone |
|---|---|
| Q3 2026 | SBOM generation enabled for all Scaffold-based repositories |
| Q4 2026 | Vaultline policy-as-code conventions adopted by all teams |
| Q4 2026 | Annual pen test engagement completed |

### IT & Compliance (ITC)
| Quarter | Milestone |
|---|---|
| Q3 2026 | Directory sync hardening completed |
| Q4 2026 | SCIM provisioning live for the largest internal applications |
| Q4 2026 | Evidence collection automated for the main control families |

## Dependencies

- DATA needs Platform Engineering's help with Kestrel capacity for the cost tooling.
- SEC depends on Developer Tooling for build-stage changes in Gatekeeper CI.
- ITC depends on Product Engineering teams to migrate their applications to SCIM.

## Risks

- Hiring: open roles in MLI and SEC could slow Q4 milestones.
- Audit season will reduce ITC capacity in the first quarter of the next fiscal year.
- Several milestones depend on other orgs, whose plans are not yet final.

## Open questions for reviewers

1. Is the Q4 load on SEC realistic?
2. Should the evidence automation milestone be split in two?
3. Are there company-level initiatives we have missed?
