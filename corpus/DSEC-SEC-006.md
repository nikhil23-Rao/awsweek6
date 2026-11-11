doc_id: DSEC-SEC-006
title: Sentinel False Positive Triage FAQ
doc_type: FAQ
scope_level: team
owner_team: SEC
owner_org: DSEC
author_role: Security Engineer
status: approved
last_updated: 2025-11-20
supersedes:
fact_ids:

# Sentinel False Positive Triage FAQ

**Q: Sentinel flagged something that is clearly not a problem. What now?**
Open the finding and choose **Mark as false positive**. Add a short reason. It goes to the SEC triage queue.

**Q: What makes a good reason?**
Say why the finding cannot be exploited in your context. "The vulnerable function is never called" is good. "Not an issue" is not.

**Q: Who decides?**
A Security Engineer on the triage rotation reviews each request. They may approve, ask for more detail, or reject.

**Q: How long does triage take?**
Usually within one business day.

**Q: What happens when it is approved?**
Sentinel suppresses the finding for that exact location and rule. The suppression has an expiry date, so it is rechecked later.

**Q: How long do suppressions last?**
Up to six months, depending on the reviewer's judgment. When one expires, the finding reappears and you can request it again with an updated reason.

**Q: Can I suppress a whole rule?**
No. Suppressions are per finding. If a rule is generally noisy, ask SEC to tune it instead.

**Q: What if I disagree with a rejection?**
Reply in the triage ticket with more evidence, or ask in the SEC channel. The SEC Tech Lead has the final say.

**Q: Does a suppression hide the finding from audit?**
No. Suppressions, reasons, and reviewers are retained in Sentinel's history.
