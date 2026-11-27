🏠 [Specs](../README.md) › ❓ [Questions](README.md) › ❓ Q18 LinkedIn automation and its user agreement

# ❓ Q18 LinkedIn automation and its user agreement

**Status:** ❓ open question

## Question

May SimpleERP send LinkedIn invitations and follow-ups automatically through Unipile, given that LinkedIn's user
agreement restricts automated activity on members' accounts?

## Why it matters

The outreach sequence of
[UC-F9-41](../02-functional/f09-hr-and-projects/use-cases/02-recruit/uc-f09-41-run-a-linkedin-outreach-sequence.md)
sends on the HR user's own LinkedIn account. If LinkedIn restricts that account, the company loses its sourcing and the
HR user their network. The limits of
[BR-F9-41](../02-functional/f09-hr-and-projects/business-rules/br-f09-41-linkedin-account-limits-respected.md) lower the
risk; they do not remove it. [D518](../06-decisions/f09-hr-and-projects/d518-linkedin-sourcing-through-unipile.md)
decided the feature; this question decides how far it goes.

## Options

- (Proposed) Automatic sending within the limits Unipile reports and the administrator's caps; the administrator accepts
  the risk when connecting Unipile, and the HR user when linking their account.
- Prepared only: SimpleERP prepares each invitation and follow-up and HR sends each one with a click.
- Only through LinkedIn's own partner programmes for recruitment tools, once SimpleERP qualifies.

## Owner

The owner of SimpleERP; a lawyer reads LinkedIn's user agreement before the build.

## Answer

Open.

---

⬅️ [Q17 Country-rule penalties and start dates still to read](q17-unread-penalties-and-dates.md) · ⬆️ [Up](README.md) ·
➡️ [Q19 Which LinkedIn search sourcing uses](q19-which-linkedin-search-sourcing-uses.md)
