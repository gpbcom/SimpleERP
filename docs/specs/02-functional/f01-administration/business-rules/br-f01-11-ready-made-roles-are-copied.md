🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-11 Ready-made roles are copied

# 📏 BR-F1-11 Ready-made roles are copied

**Status:** ✅ specified

## Statement

A ready-made role cannot be edited; it can be copied, and the copy edited.

## Why

Ready-made roles receive updates; a company's own roles are never overwritten. See
[D78](../../../06-decisions/f01-administration/d78-ready-made-roles-copied.md).

## Examples

| Case | Result |
|---|---|
| Edit the ready-made Sales role | Refused; "Copy" is offered |
| Copy Sales as "Sales Lyon" and add own-site only | Allowed |
| An update adds a row to Sales | The ready-made Sales gets it; "Sales Lyon" does not, and the administrator is told |

## Applies to

- [UC-F1-06](../use-cases/04-edit-a-role/uc-f01-06-edit-a-role-and-its-record-rules.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-10 A leaver's AI assistant history is deleted](br-f01-10-leavers-assistant-history-deleted.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F1-12 Record rule kinds](br-f01-12-record-rule-kinds.md)
