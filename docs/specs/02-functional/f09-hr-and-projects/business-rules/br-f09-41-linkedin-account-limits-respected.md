🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-41 The LinkedIn account's limits are respected

# 📏 BR-F9-41 The LinkedIn account's limits are respected

**Status:** 🔄 waiting for the owner

## Statement

Searches, invitations and messages stay within the limits Unipile reports for the HR user's LinkedIn account; when a
limit is reached, the rest waits for the next day or week; (Proposed) the administrator sets daily and weekly caps per
account, never above those limits.

## Why

A restricted account would stop the company's sourcing and harm the HR user's own account
([D518](../../../06-decisions/f09-hr-and-projects/d518-linkedin-sourcing-through-unipile.md),
[Q18](../../../07-questions/q18-linkedin-automation-and-its-user-agreement.md)).

## Examples

| Case | Result |
|---|---|
| A limit reached at 14:00 | the remaining messages wait for the next day; HR sees "paused until tomorrow" |
| (Proposed) A cap of 20 invitations a day, 30 planned | 20 today, 10 tomorrow, each follow-up counted from its own invitation |
| Unipile reports the account restricted | the sequence pauses; HR and the administrator are told |

## Applies to

- [UC-F9-40 Search and rank LinkedIn profiles](../use-cases/02-recruit/uc-f09-40-search-and-rank-linkedin-profiles.md)
- [UC-F9-41 Run a LinkedIn outreach sequence](../use-cases/02-recruit/uc-f09-41-run-a-linkedin-outreach-sequence.md)
- [E-F9-46 Outreach sequence](../data/e-f09-46-outreach-sequence.md)
- [E-F9-47 Outreach message](../data/e-f09-47-outreach-message.md)
- [E-F24-02 Tool connection](../../f24-integrations-hub/data/e-f24-02-tool-connection.md)

## Exceptions

None.

## Configurable

(Proposed) The caps per account, by the administrator.

## Open questions

- [Q18 LinkedIn automation and its user agreement](../../../07-questions/q18-linkedin-automation-and-its-user-agreement.md)

---

⬅️ [BR-F9-40 No search criterion the law forbids in hiring](br-f09-40-no-criterion-the-law-forbids-in-hiring.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F9-42 Remote-work allowances follow the agreement](br-f09-42-remote-work-allowances-follow-the-agreement.md)
