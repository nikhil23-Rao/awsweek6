doc_id: DSEC-ITC-006
title: Keystone Role and Group Naming Standard
doc_type: standard
scope_level: team
owner_team: ITC
owner_org: DSEC
author_role: Staff Engineer
status: approved
last_updated: 2025-10-21
supersedes:
fact_ids:

# Keystone Role and Group Naming Standard

Consistent names make access easy to understand and to review. This standard applies to all groups and roles created in Keystone.

## 1. Group names

```
<scope>-<system>-<role>
```

- **scope:** `org` code, or `co` for company-wide
- **system:** the lowercase system or application name
- **role:** what the group can do

Examples: `dsec-foundry-users`, `plat-kestrel-admins`, `co-console-viewers`.

## 2. Standard role words

| Role | Meaning |
|---|---|
| `viewers` | Read-only |
| `users` | Normal use |
| `operators` | Operate and configure |
| `admins` | Full control, including access management |
| `oncall` | Members of the paging rota |

Do not invent synonyms such as `power-users` or `superusers`.

## 3. Ownership

Every group has an owner in Keystone: a team, not an individual. The owner approves membership requests.

## 4. Lifecycle

- Create groups through the Keystone request portal.
- Rename only through a ticket; renaming breaks downstream references.
- A group with no members for 12 months is flagged for removal.

## 5. Role bundles

Roles that apply across several systems use the prefix `role-`, for example `role-sre-baseline`. Only IT & Compliance creates role bundles.

## 6. Anti-patterns

- Groups named for people.
- Groups that mix unrelated systems.
- Using `admins` where `operators` is enough.
