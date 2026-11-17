🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-26 A missing translation falls back to the company language

# 📏 BR-F2-26 A missing translation falls back to the company language

**Status:** ✅ specified

## Statement

A label, status or message without a translation in the user's language shows in the company's main language, never
empty.

## Why

An empty label is worse than one in another language.

## Examples

| Case | Result |
|---|---|
| No English for "À planifier" | "À planifier" shown |
| English added | "To plan" shown |

## Applies to

- [UC-F2-28 Translate custom labels and statuses](../use-cases/11-rights-translations-and-approvals/uc-f02-28-translate-custom-labels-and-statuses.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-25 Field rights apply on every channel](br-f02-25-field-rights-apply-on-every-channel.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F2-27](br-f02-27-every-approval-follows-its-chain-and-never-waits-forever.md)
