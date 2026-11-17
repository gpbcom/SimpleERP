🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-17 Calendars sync both ways

# 📏 BR-F4-17 Calendars sync both ways

**Status:** ✅ specified

## Statement

Each user's Google Calendar or Microsoft 365 calendar syncs with simple-ERP both ways: events and their changes arrive
live (push notifications), with a recording switch per meeting; a change made in either place shows in the other within
a minute; meetings simple-ERP creates (a follow-up, the next occurrence of a recurring meeting) are written to the
organiser's calendar and invite the participants; the agenda draft and the summary link are added to the event's
description. The recording switch is kept in the event's private properties, so other calendar apps ignore
it.

## Why

The meeting assistant must follow the user's real agenda. See
[D228](../../../06-decisions/f04-meetings/d228-calendar-two-way-sync.md).

## Examples

| Case | Result |
|---|---|
| Léa moves a meeting in Google Calendar | simple-ERP shows the new time within a minute; the bot follows |
| Léa switches recording off in simple-ERP | Kept with the event |
| The review creates a follow-up meeting | It appears in Léa's Google Calendar, participants invited |
| A meeting is checked | The summary link is added to the Google event |

## Applies to

- [UC-F4-01](../use-cases/01-record-an-online-meeting/uc-f04-01-record-an-online-meeting-with-the-bot.md)
- [UC-F4-08](../use-cases/06-set-up-meetings-and-calendars/uc-f04-08-set-up-meeting-sources-calendars-and-retention.md)
- [UC-F4-21 Book a meeting room and equipment](../use-cases/12-rooms-and-client-video/uc-f04-21-book-a-meeting-room-and-equipment.md)

## Exceptions

Private events: never recorded, and their details not read.

## Configurable

The connection mode, Workspace or personal (D229).

## Open questions

None.

---

⬅️ [BR-F4-16 Recurring meetings get their next agenda](br-f04-16-recurring-meetings-get-their-next-agenda.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F4-18 HR meetings stay with HR and the employee](br-f04-18-hr-meetings-are-recorded-for-hr-and-the-employee.md)
