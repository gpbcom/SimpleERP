🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-47 To-dos are private unless shared

# 📏 BR-F3-47 To-dos are private unless shared

**Status:** ✅ specified

## Statement

A to-do or memo is private to its owner: no administrator, manager or role can read it; it becomes visible only to the
colleagues the owner chooses, who may tick and comment but not change or delete it, and the owner can stop sharing at
any time.

## Why

Personal notes are only useful if the owner trusts them to be private. The owner's answer: "Personal to-dos and memos"
([D522](../../../06-decisions/f03-assistant/d522-benchmark-gaps-f03-assistant.md)); sharing follows
[BR-F3-26](br-f03-26-share-only-with-chosen-colleagues.md).

## Examples

| Case | Result |
|---|---|
| Marc writes a memo about a candidate | only Marc sees it |
| An administrator searches for 'candidate' | finds nothing of Marc's memos |
| Marc shares a to-do with Claire | Claire sees it, can tick and comment |
| Marc stops sharing | the to-do disappears from Claire's list |
| Marc leaves the company | his private to-dos are deleted with his data ([BR-F1-10](../../f01-administration/business-rules/br-f01-10-leavers-assistant-history-deleted.md)) |

## Applies to

- [UC-F3-24 Keep personal to-dos and memos](../use-cases/13-voice-agents-and-briefings/uc-f03-24-keep-personal-to-dos-and-memos.md)
- [E-F3-27 To-do](../data/e-f03-27-to-do.md)
- [S-F3-28 My to-dos](../screens/13-voice-agents-and-briefings/s-f03-28-my-to-dos.md)

## Exceptions

A to-do that is converted to a task of the company stops being private, with the owner's confirmation.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-46 Briefings show only what the reader may see](br-f03-46-briefings-show-only-what-the-reader-may-see.md) ·
⬆️ [Up](README.md)
