🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-45 Add-ins use the user's own rights

# 📏 BR-F3-45 Add-ins use the user's own rights

**Status:** ✅ specified

## Statement

A spreadsheet add-in connects with the user's own sign-in and a personal read token, never a shared or service account,
so that it reads exactly what the user may read in simple-ERP: lists, fields and rows the user may not see are never
offered, and a colleague who refreshes a shared workbook sees data under their own rights.

## Why

A shared token would let a workbook leak data to everyone who opens it. The owner's answer: "Spreadsheet add-ins"
([D522](../../../06-decisions/f03-assistant/d522-benchmark-gaps-f03-assistant.md)); tokens follow
[BR-F1-27](../../f01-administration/business-rules/br-f01-27-tokens-are-scoped-dated-and-shown-once.md).

## Examples

| Case | Result |
|---|---|
| The accountant connects with her sign-in | she reads the ledgers her roles allow |
| A salary list the accountant may not see | not offered in the pane |
| A workbook shared with a colleague who may not see sales | his refresh shows a message, not values |
| A service account asks to connect | refused: add-ins use personal sign-ins |

## Applies to

- [UC-F3-22 Use ERP data in a spreadsheet add-in](../use-cases/13-voice-agents-and-briefings/uc-f03-22-use-erp-data-in-a-spreadsheet-add-in.md)
- [E-F3-25 Add-in connection](../data/e-f03-25-add-in-connection.md)
- [UC-F1-20 Create and revoke API tokens and service accounts](../../f01-administration/use-cases/12-portal-accounts-and-integrations/uc-f01-20-create-and-revoke-api-tokens-and-service-accounts.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-44 Ready-made agents start in suggestion mode](br-f03-44-ready-made-agents-start-in-suggestion-mode.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F3-46 Briefings show only what the reader may see](br-f03-46-briefings-show-only-what-the-reader-may-see.md)
