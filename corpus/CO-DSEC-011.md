doc_id: CO-DSEC-011
title: Data Classification Standard
doc_type: standard
scope_level: company
owner_team: SEC
owner_org: DSEC
author_role: Compliance Analyst
status: approved
last_updated: 2025-04-22
supersedes:
fact_ids: F-POL-15, F-DSEC-003

# Data Classification Standard

**Owner:** Office of the CISO | **Applies to:** all TechSync data in any system

## 1. Levels

TechSync classifies data into four levels.

| Level | Meaning |
|---|---|
| Public | Approved for release outside the company |
| Internal | For employees and contractors; not for release |
| Confidential | Sensitive business or customer information |
| Restricted | The most sensitive data, with the tightest handling |

## 2. Default classification

**Customer-derived data is Confidential by default.** This covers data that customers send to our products and data computed from it, such as usage records, logs that contain customer content, and aggregated customer metrics.

**Restricted is reserved for credentials, payment card data, and regulated identifiers.**

## 3. Handling by level

| Requirement | Internal | Confidential | Restricted |
|---|---|---|---|
| Encryption at rest | Yes | Yes | Yes, with dedicated keys |
| Encryption in transit | Yes | Yes | Yes |
| Access | All employees | Need-to-know group | Named individuals |
| Storage outside approved AWS regions | Not allowed | Not allowed | Not allowed |
| Sharing with third parties | Contract needed | Contract and review | Not permitted without CISO approval |

## 4. Labelling

Datasets registered in Reservoir, tables in Quarry, and buckets in Terraform carry a `classification` tag. Untagged assets are treated as Confidential until reviewed.

## 5. Declassification

Moving data to a lower level requires the data owner and a Security Engineer to sign off in a Jira ticket.

## 6. Questions

Contact the compliance channel. Disputes on classification go to the CISO, Tamsin Reid.
