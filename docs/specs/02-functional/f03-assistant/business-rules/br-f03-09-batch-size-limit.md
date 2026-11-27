🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-09 Batch size limit

# 📏 BR-F3-09 Batch size limit

**Status:** ✅ specified

## Statement

One confirmation covers at most the batch size: 100 records by default; the setting offers other sizes and "No limit". A
larger request is split into batches, each confirmed, or the AI assistant opens the bulk-edit screen with the records
selected.

## Why

A confirmation must stay readable. See [D159](../../../06-decisions/f03-assistant/d159-assistant-batch-size.md).

## Examples

| Case | Result |
|---|---|
| 40 records, default size | One confirmation listing 40 |
| 250 records, default size | 3 batches (100, 100, 50), or the bulk-edit screen |
| 250 records, "No limit" | One confirmation listing 250 |

## Applies to

- [UC-F3-03](../use-cases/03-act-through-the-assistant/uc-f03-03-have-the-assistant-create-or-change-records.md)

## Exceptions

None.

## Configurable

Yes: by the administrator, in the AI assistant settings (F1); choices 20, 50, 100, 500, No limit; default 100.

## Open questions

None.

---

⬅️ [BR-F3-08 A batch is undone as a whole](br-f03-08-a-batch-is-undone-as-a-whole.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-10 Changes signed through the AI assistant](br-f03-10-changes-signed-through-the-assistant.md)
