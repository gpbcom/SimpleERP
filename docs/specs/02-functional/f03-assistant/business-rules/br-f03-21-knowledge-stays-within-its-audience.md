🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-21 Knowledge stays within its audience

# 📏 BR-F3-21 Knowledge stays within its audience

**Status:** ✅ specified

## Statement

A knowledge item is found, shown or used by the AI assistant only for users in its audience: everyone, chosen roles,
chosen sites or teams; without its own audience, it has its folder's.

## Why

Some procedures are for some people only. See [D174](../../../06-decisions/f03-assistant/d174-knowledge-audience.md).

## Examples

| Case | Result |
|---|---|
| "Salary review procedure", audience HR | Never used for a sales person's question |
| Folder "Lyon site", audience Lyon | A Nantes employee does not get it |
| "Expense policy", everyone | Used for anyone |

## Applies to

- [UC-F3-07](../use-cases/07-manage-knowledge/uc-f03-07-manage-the-company-knowledge-base.md); every AI assistant answer
  using knowledge (UC-F3-01, UC-F3-05).

## Exceptions

None.

## Configurable

Yes: per item and folder, by its editors.

## Open questions

None.

---

⬅️ [BR-F3-20 Outside call caps](br-f03-20-outside-call-caps.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-22 Out-of-date knowledge is flagged](br-f03-22-out-of-date-knowledge-is-flagged.md)
