🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-32 Merges keep every link and an undo window

# 📏 BR-F2-32 Merges keep every link and an undo window

**Status:** ✅ specified

## Statement

A merge re-points every document, history entry, task, file and relation of the merged records to the surviving record,
archives the others with a link to the survivor, never deletes a record, and can be undone for 30 days; records under a
legal hold or in a locked status are never merged.

## Why

A merge that loses an invoice link or cannot be reversed is a data loss. The owner's answer: "Data cleaning"
([D521](../../../06-decisions/f02-no-code-configuration/d521-benchmark-gaps-f02-no-code-configuration.md));
archive-never-delete is [BR-F2-01](br-f02-01-archive-never-delete.md).

## Examples

| Case | Result |
|---|---|
| Dupont SA and Dupont S.A., 9 invoices | all 9 invoices point to the survivor |
| Two different tax numbers | the user must choose, nothing merges until then |
| Undo on day 12 | the archived record returns with its own links |
| Undo on day 40 | refused: the 30 days have passed |
| A customer under a legal hold | never proposed |

## Applies to

- [UC-F2-35 Clean duplicates and stale records](../use-cases/13-low-code-bulk-and-cleaning/uc-f02-35-clean-duplicates-and-stale-records.md)
- [E-F2-34 Cleaning rule](../data/e-f02-34-cleaning-rule.md)
- [UC-F2-32 Edit records in bulk](../use-cases/13-low-code-bulk-and-cleaning/uc-f02-32-edit-records-in-bulk.md)

## Exceptions

None.

## Configurable

Yes: the undo window, between 7 and 90 days.

## Open questions

None.

---

⬅️ [BR-F2-31 In-place translations ship as packs](br-f02-31-in-place-translations-ship-as-packs.md) ·
⬆️ [Up](README.md)
