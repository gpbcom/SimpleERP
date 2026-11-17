🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-08 Read-only per status on every channel

# 📏 BR-F2-08 Read-only per status on every channel

**Status:** ✅ specified

## Statement

A field locked from a status on can no longer be changed once the record reaches it, through the screens, the
API, the AI assistant, MCP and A2A alike.

## Why

Locking is a business rule (no price change after "Sent"), not a presentation. See
[D108](../../../06-decisions/f02-no-code-configuration/d108-form-layout-options.md).

## Examples

| Case | Result |
|---|---|
| Change the price of a quote in "Sent" on the form | The field is read-only |
| The same change through the API | Refused, with the status named |
| Move the quote back to "Draft" (if a transition allows it) | The field is editable again |

## Applies to

- [UC-F2-03](../use-cases/01-configure-a-record-type/uc-f02-03-arrange-a-form.md); T5, T6.

## Exceptions

None.

## Configurable

Yes: which fields, from which status.

## Open questions

None.

---

⬅️ [BR-F2-07 Layout is not security](br-f02-07-layout-is-not-security.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-09 New record types start closed](br-f02-09-new-record-types-start-closed.md)
