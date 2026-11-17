🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-25 Field rights apply on every channel

# 📏 BR-F2-25 Field rights apply on every channel

**Status:** ✅ specified

## Statement

A field hidden or masked for a role is hidden or masked on screens, lists, exports, reports, the API, the MCP tools, the
AI assistant's answers and documents for that role's users.

## Why

A field hidden only on screen still leaks through an export (BR-F2-07).

## Examples

| Case | Result |
|---|---|
| Salary hidden for Manager, export | No salary column |
| Assistant asked a salary by a manager | Says it cannot show it |

## Applies to

- [UC-F2-27 Set field-level rights and validation rules](../use-cases/11-rights-translations-and-approvals/uc-f02-27-set-field-level-rights-and-validation-rules.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-24](br-f02-24-local-changes-are-kept-unless-a-legal-block-changed.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-26](br-f02-26-a-missing-translation-falls-back-to-the-company-language.md)
