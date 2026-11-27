🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-46 Briefings show only what the reader may see

# 📏 BR-F3-46 Briefings show only what the reader may see

**Status:** ✅ specified

## Statement

A briefing is built for one reader and contains only items the reader may see under their own roles and record rules at
the moment it is made; a briefing sent by email or chat carries only titles and counts for sensitive sections, and every
figure comes from a query with a source.

## Why

A briefing that mixes in what the reader may not see leaks data in the most read message of the day. The owner's answer:
"Daily briefing" ([D522](../../../06-decisions/f03-assistant/d522-benchmark-gaps-f03-assistant.md)); it applies
[BR-F3-02](br-f03-02-answers-use-only-what-the-user-may-see.md) and [BR-F3-03](br-f03-03-figures-come-from-queries.md)
to a scheduled message.

## Examples

| Case | Result |
|---|---|
| The owner's briefing | includes sales, approvals and payroll alerts he may see |
| A salesperson's briefing | has no payroll section |
| A briefing sent by email | sensitive sections show a count and a link to the app |
| A figure that cannot be queried | not shown, the item says it is unavailable |

## Applies to

- [UC-F3-23 Read the daily briefing](../use-cases/13-voice-agents-and-briefings/uc-f03-23-read-the-daily-briefing.md)
- [E-F3-26 Briefing](../data/e-f03-26-briefing.md)
- [S-F3-27 Daily briefing](../screens/13-voice-agents-and-briefings/s-f03-27-daily-briefing.md)

## Exceptions

None.

## Configurable

Yes: which sections count as sensitive for email and chat, by the administrator.

## Open questions

None.

---

⬅️ [BR-F3-45 Add-ins use the user's own rights](br-f03-45-add-ins-use-the-users-own-rights.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-47 To-dos are private unless shared](br-f03-47-to-dos-are-private-unless-shared.md)
