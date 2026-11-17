🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-10 Changes signed through the AI assistant

# 📏 BR-F3-10 Changes signed through the AI assistant

**Status:** ✅ specified

## Statement

Every change the AI assistant makes is signed "by <user>, through the assistant" in the record history, with a link to
the conversation, which opens for its owner and those it is shared with.

## Why

Hand-made and assistant changes must be told apart. See
[D160](../../../06-decisions/f03-assistant/d160-assistant-signature.md).

## Examples

| Case | Result |
|---|---|
| Marie has the AI assistant set a status | "Status Won, by Marie Dupont, through the assistant" |
| Paul, not shared, opens the link | "This conversation is private" |

## Applies to

- [UC-F3-03](../use-cases/03-act-through-the-assistant/uc-f03-03-have-the-assistant-create-or-change-records.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-09 Batch size limit](br-f03-09-batch-size-limit.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-11 Drafts follow the company style](br-f03-11-drafts-follow-the-company-style.md)
