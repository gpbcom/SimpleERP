🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-15 Unreviewed meetings publish as not checked

# 📏 BR-F4-15 Unreviewed meetings publish as not checked

**Status:** ✅ specified

## Statement

An unreviewed meeting reminds its organiser after 1 working day; after 3 working days its summary is published to the
participants marked "not checked"; its links stay suggestions (so the linked records' readers do not see it) and no task
is created.

## Why

Participants need the summary even when the organiser is busy. See
[D226](../../../06-decisions/f04-meetings/d226-unreviewed-meetings.md).

## Examples

| Case | Result |
|---|---|
| Not reviewed by Wednesday for a Monday meeting | Reminder |
| Not reviewed by Thursday | Published to participants, "not checked" |

## Applies to

- [UC-F4-05](../use-cases/03-review-a-meeting/uc-f04-05-review-a-meeting.md)

## Exceptions

HR meetings follow UC-F4-07.

## Configurable

The delays, by an administrator.

## Open questions

None.

---

⬅️ [BR-F4-14 Colleagues get tasks, outsiders the follow-up](br-f04-14-colleagues-get-tasks-outsiders-the-follow-up.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F4-16 Recurring meetings get their next agenda](br-f04-16-recurring-meetings-get-their-next-agenda.md)
