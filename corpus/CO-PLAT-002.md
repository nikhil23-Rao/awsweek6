---
doc_id: CO-PLAT-002
title: Code Review Guidelines for Authors and Reviewers
doc_type: guide
scope_level: company
owner_team: DEVT
owner_org: PLAT
author_role: Staff Engineer
status: approved
last_updated: 2025-02-18
supersedes: ""
fact_ids: ""
---

# Code Review Guidelines for Authors and Reviewers

**Owner:** Developer Tooling, with input from Staff Engineers across all orgs

Code review is how we share knowledge, catch mistakes, and keep our codebase healthy. These guidelines describe what good review looks like at TechSync. Approval requirements are covered in the separate Code Review Policy.

## For authors

- **Keep PRs small.** Under 400 lines of change is a good target. Split refactors from behavior changes.
- **Explain why.** The description should say what problem you're solving and how you tested it.
- **Review your own diff first.** Catch the debug prints and stray files before others do.
- **Link the ticket.** Reviewers should be able to find the context.
- **Respond to every comment,** even if just "done."

## For reviewers

- **Respond within one business day.** A first pass counts.
- **Review the design, not just the lines.** Does this belong here? Is there a simpler approach?
- **Be specific and kind.** Suggest a fix, not just a problem.
- **Mark nits as nits.** Use the `nit:` prefix for things that shouldn't block merging.
- **Check tests.** Are the important cases covered? Do the tests actually fail when the code is wrong?

## Things to look for

- Error handling and timeouts on network calls.
- Logging customer data (don't).
- Backwards compatibility for APIs, config, and database schemas.
- Missing alerts or dashboards for new functionality.

## Disagreements

Talk it out on a call if a thread goes back and forth more than twice. If you still disagree, ask the tech lead of the code's owning team.

## Speed versus thoroughness

Both matter. Large or risky changes deserve a slow, careful review. Mechanical changes deserve a quick one.
