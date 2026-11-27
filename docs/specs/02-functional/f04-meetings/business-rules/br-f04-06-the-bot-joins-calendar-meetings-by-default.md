🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-06 The bot joins calendar meetings by default

# 📏 BR-F4-06 The bot joins calendar meetings by default

**Status:** ✅ specified

## Statement

Every online meeting in a user's connected calendar is recorded by default, by the source the organiser chose
(BR-F4-07); the user can switch a meeting off beforehand, and set their own default to off; HR meetings
follow UC-F4-07. The bot announces itself as BR-F4-01 says.

## Why

Recording is the norm, skipping it a choice. See
[D216](../../../06-decisions/f04-meetings/d216-bot-joins-by-default.md).

## Examples

| Case | Result |
|---|---|
| A Teams meeting in Léa's calendar | Recorded |
| Léa switches it off | Not recorded |
| A meeting with no link (in person) | Not concerned: UC-F4-03 |

## Applies to

- [UC-F4-01](../use-cases/01-record-an-online-meeting/uc-f04-01-record-an-online-meeting-with-the-bot.md)
- [UC-F4-02](../use-cases/01-record-an-online-meeting/uc-f04-02-import-a-platform-s-own-transcript.md)

## Exceptions

None.

## Configurable

Yes: per meeting; each user's default; an administrator can turn it off for the company.

## Open questions

None.

---

⬅️ [BR-F4-05 Summaries in the reader's language](br-f04-05-summaries-in-the-reader-s-language.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-07 The organiser picks the source](br-f04-07-the-organiser-picks-the-source.md)
