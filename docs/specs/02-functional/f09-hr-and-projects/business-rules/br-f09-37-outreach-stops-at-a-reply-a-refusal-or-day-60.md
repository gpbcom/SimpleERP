🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-37 An outreach sequence stops at a reply, a refusal or day 60

# 📏 BR-F9-37 An outreach sequence stops at a reply, a refusal or day 60

**Status:** ✅ specified

## Statement

A sequence sends an invitation with a note on day 0 (a direct message when the person is already connected) and
follow-ups on days 7 and 21 by default; replies are checked every few hours; a reply stops that person's follow-ups at
once, a refusal ends their sequence, and on day 60 everything stops.

## Why

The owner's answer LS-3 ([D518](../../../06-decisions/f09-hr-and-projects/d518-linkedin-sourcing-through-unipile.md)):
"Invite, then 2 follow-ups (Recommended)", after asking to "check periodically the response (mot mode than 2 months)".

## Examples

| Case | Result |
|---|---|
| No reply | invitation on day 0, follow-ups on days 7 and 21, nothing after |
| A reply on day 9 | no follow-up after day 9 |
| "Not interested" on day 3 | declined, no follow-up |
| Already connected | a direct message on day 0 instead of an invitation |
| Follow-ups moved to days 10 and 30 | passes |
| A follow-up set on day 75 | fails: refused, after day 60 |
| Day 60 | the sequence ends; prospects without an answer end as "no answer" |

## Applies to

- [UC-F9-41 Run a LinkedIn outreach sequence](../use-cases/02-recruit/uc-f09-41-run-a-linkedin-outreach-sequence.md)
- [E-F9-46 Outreach sequence](../data/e-f09-46-outreach-sequence.md)
- [E-F9-47 Outreach message](../data/e-f09-47-outreach-message.md)
- [E-F9-45 Prospect](../data/e-f09-45-prospect.md)

## Exceptions

None; the 60-day end cannot be moved later.

## Configurable

Yes: the days of the two follow-ups, within day 60, and the interval of the reply check.

## Open questions

None.

---

⬅️ [BR-F9-36](br-f09-36-hr-approves-before-the-first-message.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-38](br-f09-38-sourced-people-told-at-the-first-contact.md)
