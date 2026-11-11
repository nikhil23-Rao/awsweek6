doc_id: DSEC-SEC-012
title: "ADR: Sentinel SBOM Generation"
doc_type: ADR
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2025-10-07
supersedes:
fact_ids:

# ADR: Sentinel SBOM Generation

**Status:** Accepted | **Date:** October 2025

## Context

Customers and auditors increasingly ask for a software bill of materials (SBOM) for what we ship. Today Sentinel works out the dependency list on demand, which is not repeatable: the same release can produce different results depending on when it is analyzed. We need an SBOM that is tied to a specific build.

## Decision

An SBOM in CycloneDX format will be generated **at build time** in the Gatekeeper CI pipeline, on Forge runners, for every deployable artifact. The SBOM is stored next to the artifact in the artifact registry, and Sentinel reads it from there.

## Consequences

**Positive**
- Each release has an immutable, auditable SBOM.
- Customer SBOM requests can be answered from stored files.
- Sentinel can look up a released artifact's components without rebuilding the dependency tree.

**Negative**
- A small increase in build time, estimated at under a minute for typical services.
- Teams with unusual build steps may need custom configuration.
- SBOM storage grows with each build.

## Alternatives considered

1. **Generate on request.** Cheap, but not reproducible.
2. **Third-party SBOM service.** Adds cost and a new vendor review.
3. **Generate in Sentinel only.** Couples SBOM content to Sentinel's analysis rather than the build.

## Rollout

SEC will add the build step to Scaffold templates first, then work with service owners to enable it in existing repositories.
