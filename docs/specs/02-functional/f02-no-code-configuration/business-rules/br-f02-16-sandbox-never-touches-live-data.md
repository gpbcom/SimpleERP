🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-16 A sandbox never touches live data

# 📏 BR-F2-16 A sandbox never touches live data

**Status:** ✅ specified

## Statement

A sandbox is a full copy of the company where changes and AI-built items are tried; nothing in it is sent, posted, paid
or filed, and only a published change reaches the live company.

## Why

See [D300](../../../06-decisions/f02-no-code-configuration/d300-f2-benchmark-gaps.md).

## Examples

| Case | Result |
|---|---|
| Invoice validated in the sandbox | Marked SANDBOX, never sent or e-invoiced |

## Applies to

UC-F2-16

## Exceptions

None.

## Configurable

Who may open one.

## Open questions

None.

---

⬅️ [BR-F2-15 Packs carry no data](br-f02-15-packs-carry-no-data.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-17 What the AI builds is a draft](br-f02-17-ai-built-items-are-drafts.md)
