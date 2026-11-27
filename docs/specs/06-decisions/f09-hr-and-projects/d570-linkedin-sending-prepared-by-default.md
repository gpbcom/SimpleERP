🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D570 LinkedIn messages are prepared by default, sent with one click

# 📜 D570 LinkedIn messages are prepared by default, sent with one click

**Status:** ✅ decided

## Context

[D518](d518-linkedin-sourcing-through-unipile.md) decided LinkedIn sourcing through Unipile, with an invitation and two
follow-ups sent on the HR user's own LinkedIn account.
[Q18](../../07-questions/q18-linkedin-automation-and-its-user-agreement.md) asked whether SimpleERP may send them
automatically, given that LinkedIn's user agreement restricts automated activity on members' accounts.

## Options

- Automatic sending within the limits Unipile reports and the administrator's caps.
- Prepared only: SimpleERP prepares each message and HR sends each one with a click.
- Only through LinkedIn's own partner programmes for recruitment tools.

## Choice

By default SimpleERP **prepares** each invitation and follow-up of an outreach sequence, and the HR user **sends each
one with one click**: nothing goes out on LinkedIn without that click. **Automatic sending**, within the limits Unipile
reports for the account and the administrator's daily and weekly caps, is an **option** an administrator turns on when
connecting Unipile, accepting the risk that LinkedIn restricts the account.

## Decided by

The owner, on 2026-11-27.

## Consequences

- [UC-F9-41](../../02-functional/f09-hr-and-projects/use-cases/02-recruit/uc-f09-41-run-a-linkedin-outreach-sequence.md),
  [BR-F9-36](../../02-functional/f09-hr-and-projects/business-rules/br-f09-36-hr-approves-before-the-first-message.md),
  [BR-F9-37](../../02-functional/f09-hr-and-projects/business-rules/br-f09-37-outreach-stops-at-a-reply-a-refusal-or-day-60.md),
  [BR-F9-41](../../02-functional/f09-hr-and-projects/business-rules/br-f09-41-linkedin-account-limits-respected.md),
  the outreach entities, screens and flow, and the Unipile
  [tool connection](../../02-functional/f24-integrations-hub/data/e-f24-02-tool-connection.md) say so.
- The owner completed the prepared mode on 2026-11-27:
  - every outgoing LinkedIn message is prepared: the invitation, the follow-ups, the booking-link reply
    ([UC-F9-42](../../02-functional/f09-hr-and-projects/use-cases/02-recruit/uc-f09-42-turn-a-positive-reply-into-an-applicant.md))
    and the thank-you message on a refusal;
  - a prepared message waits as a task in the HR user's task list
    ([E-F9-18 Project and task](../../02-functional/f09-hr-and-projects/data/e-f09-18-project-and-task.md)), with a Send
    button in the task and on
    [S-F9-39 Prospect conversations](../../02-functional/f09-hr-and-projects/screens/02-recruit/s-f09-39-prospect-conversations.md);
  - a prepared message not sent within 7 days expires, and the prospect then follows the sequence's path as if not
    answered, so [E-F9-45 Prospect](../../02-functional/f09-hr-and-projects/data/e-f09-45-prospect.md) reaches its end
    state after day 60;
  - a change of sending mode by the administrator applies only to sequences started after it: a running sequence
    keeps the mode it started with
    ([E-F9-46](../../02-functional/f09-hr-and-projects/data/e-f09-46-outreach-sequence.md)).
- The owner settled the last details of the prepared mode on 2026-11-27:
  - a prospect whose first message (the invitation, or the direct message to a person already connected) expired
    unsent was never contacted and gets no follow-up; they end as "no answer" on day 60
    ([BR-F9-37](../../02-functional/f09-hr-and-projects/business-rules/br-f09-37-outreach-stops-at-a-reply-a-refusal-or-day-60.md));
  - a sequence returned to draft (a template changed) keeps its sending mode when HR approves it again
    ([BR-F9-36](../../02-functional/f09-hr-and-projects/business-rules/br-f09-36-hr-approves-before-the-first-message.md));
  - the 7 days run from the moment the message's task is created; a message HR clicked that a sending limit holds is
    no longer waiting for HR and never expires: it goes when the limit allows
    ([BR-F9-41](../../02-functional/f09-hr-and-projects/business-rules/br-f09-41-linkedin-account-limits-respected.md));
  - HR is not notified per message: the HR user gets one daily digest notification listing the messages to send and
    those expiring within 24 hours ([notifications](../../02-functional/f09-hr-and-projects/notifications.md)).
- With the option on, the sequence sends on its own after HR's one-time approval of the shortlist and the templates
  (BR-F9-36); the reply check, the stop at a reply, a refusal or day 60, and the account's limits apply in both modes.
- A lawyer still reads LinkedIn's user agreement before the build, for the automatic option.

## Related

- [D518 LinkedIn sourcing through Unipile](d518-linkedin-sourcing-through-unipile.md)
- [D571 LinkedIn sourcing uses the HR user's own search](d571-linkedin-sourcing-uses-the-users-search.md)
- [Q18 LinkedIn automation and its user agreement](../../07-questions/q18-linkedin-automation-and-its-user-agreement.md)

---

⬅️ [D569](../vision/d569-roadmap-option-a-in-twelve-phases.md) · ⬆️ [Up](README.md) ·
➡️ [D571](d571-linkedin-sourcing-uses-the-users-search.md)
