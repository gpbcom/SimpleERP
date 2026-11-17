🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-12 Links are suggested, then confirmed

# 📏 BR-F4-12 Links are suggested, then confirmed

**Status:** ✅ specified

## Statement

Each recording gets suggested links: by the caller's or callee's phone number for calls, by the calendar event or the
user's current task for in-person meetings; suggestions are confirmed or changed at review (UC-F4-05); until then the
meeting is visible to its participants only.

## Why

Wrong links would show summaries to the wrong readers (BR-F4-04). See
[D223](../../../06-decisions/f04-meetings/d223-links-suggested-confirmed.md).

## Examples

| Case | Result |
|---|---|
| A call from +33 4 72 ... | Suggested: Durand SA, contact J. Durand |
| A meeting during visit V-212 | Suggested: visit V-212 and its customer |
| An unknown number | No suggestion; linked by hand at review |

## Applies to

- [UC-F4-03](../use-cases/02-record-in-person-or-by-phone/uc-f04-03-record-an-in-person-meeting.md)
- [UC-F4-04](../use-cases/02-record-in-person-or-by-phone/uc-f04-04-record-a-phone-call.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F4-11 Business calls recorded only when switched on](br-f04-11-business-calls-are-recorded.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F4-13 Summaries follow the meeting kind](br-f04-13-summaries-follow-the-meeting-kind.md)
