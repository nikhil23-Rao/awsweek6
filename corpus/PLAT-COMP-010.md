---
doc_id: PLAT-COMP-010
title: Forge Runner Image Release Notes (2026)
doc_type: release notes
scope_level: team
owner_team: COMP
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2026-08-20
supersedes: ""
fact_ids: ""
---

# Forge Runner Image Release Notes (2026)

Release notes for the Forge build runner images. New images roll out to the runner fleet over two days; pin `forge_image` in your pipeline only if you need to delay an upgrade.

---

### 2026.08.2 (August 20, 2026)

- Go toolchain 1.27.0 added; 1.25 removed.
- Python 3.13 is now the default; 3.11 remains available.
- Node.js 24 LTS added.
- Fixed: Docker layer cache occasionally reported a full disk on large-runner pools.

### 2026.07.1 (July 9, 2026)

- Kotlin 2.2 and Gradle 9 added.
- Swift toolchain updated on macOS runners for TechSync Mobile builds.
- Terraform 1.12 added.

### 2026.05.3 (May 22, 2026)

- Faster runner boot: image size reduced by about 18%.
- Base OS updated with May security patches.

### 2026.04.1 (April 6, 2026)

- `forge-large-arm` runners moved to the newest Graviton instance generation.
- `buildx` updated; multi-arch builds are about 30% faster.

### 2026.02.2 (February 17, 2026)

- PostgreSQL 17 test container added for integration tests.
- Fixed: intermittent DNS failures in the test network sandbox.

### 2026.01.1 (January 13, 2026)

- Go 1.26 added.
- Python 3.10 removed. Update pipelines still pinned to it.

---

**Questions:** #comp-forge. Report broken toolchains with the job URL and the image version from the job log header.
