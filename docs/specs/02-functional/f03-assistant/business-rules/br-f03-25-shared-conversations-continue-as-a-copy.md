🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-25 Shared conversations continue as a copy

# 📏 BR-F3-25 Shared conversations continue as a copy

**Status:** ✅ specified

## Statement

A colleague opening a shared conversation reads it as its author saw it (D144), read only. "Continue" creates the
colleague's own copy; every new answer in the copy uses only the colleague's rights (BR-F3-02); the author's
conversation never changes because of them.

## Why

What the author chose to share is shown; new questions never borrow the author's rights. See
[D177](../../../06-decisions/f03-assistant/d177-continue-as-a-copy.md).

## Examples

| Case | Result |
|---|---|
| Paul reads Marie's shared turnover analysis | He sees Marie's figures as she saw them |
| Paul continues: "and for Lyon?" | His copy answers with what Paul may see |
| Marie deletes her conversation | Paul's copy stays; the shared original is gone |

## Applies to

- [UC-F3-08](../use-cases/08-manage-and-share-conversations/uc-f03-08-manage-and-share-conversations.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-24 Synced sources follow their origin](br-f03-24-synced-sources-follow-their-origin.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-26 Share only with chosen colleagues](br-f03-26-share-only-with-chosen-colleagues.md)
