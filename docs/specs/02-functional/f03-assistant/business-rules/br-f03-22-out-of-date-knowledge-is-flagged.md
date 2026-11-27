🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-22 Out-of-date knowledge is flagged

# 📏 BR-F3-22 Out-of-date knowledge is flagged

**Status:** ✅ specified

## Statement

Each item has an owner and a review date, one year after its last review by default; past it, the owner is reminded
(then,, every month), the item shows "to review", and the AI assistant adds "This may be out of date (last
reviewed <date>)" when it uses it.

## Why

An old procedure said with confidence misleads. See
[D175](../../../06-decisions/f03-assistant/d175-knowledge-freshness.md).

## Examples

| Case | Result |
|---|---|
| Reviewed 14 months ago | The answer warns, the owner is reminded |
| The owner marks it reviewed | A new review date in one year |
| The owner leaves the company | The folder's editors become owners |

## Applies to

- [UC-F3-07](../use-cases/07-manage-knowledge/uc-f03-07-manage-the-company-knowledge-base.md); every AI assistant answer
  using knowledge (UC-F3-01, UC-F3-05).

## Exceptions

None.

## Configurable

Yes: the review period per item or folder (3, 6, 12, 24 months, never).

## Open questions

None.

---

⬅️ [BR-F3-21 Knowledge stays within its audience](br-f03-21-knowledge-stays-within-its-audience.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F3-23 Proposals need an editor](br-f03-23-proposals-need-an-editor.md)
