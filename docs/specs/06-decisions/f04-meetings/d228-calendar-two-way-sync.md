🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎙️ [Decisions: F4 Meetings](README.md) ›
📜 D228 Calendars sync both ways

# 📜 D228 Calendars sync both ways

**Status:** ✅ decided

## Context

The owner: "Make sure that the Meeting assitant is synchronied with the user Google Agenda."

## Options

- Two-way.
- Read only.
- Read and links.

## Choice

Two-way: events flow in live with their recording switch; changes in either place show in the other within a minute;
meetings SimpleERP creates (follow-ups, the next occurrence) are written to the calendar; the agenda draft and the
summary link are added to the event.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F4-17; the calendar is the meetings' source of truth for times and participants.

## Related

- [F4 Meetings](../../02-functional/f04-meetings/README.md)

---

⬅️ [D227 Reusing past meetings](d227-meeting-reuse.md) · ⬆️ [Up](README.md) ·
➡️ [D229 Connecting calendars](d229-calendar-connection.md)
