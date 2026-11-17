🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-31 In-place translations ship as packs

# 📏 BR-F2-31 In-place translations ship as packs

**Status:** ✅ specified

## Statement

Translations made in place are stored per language as a pack of entries, not as edits to the product's own files: a pack
survives updates, can be exported and imported, an entry whose source text changed is marked outdated and keeps its old
text until reviewed, and a pack carries texts only, never data.

## Why

Translations must survive an update and be reusable by other companies without copying data
([BR-F2-15](br-f02-15-packs-carry-no-data.md)). The owner's answer: "In-place translation"
([D521](../../../06-decisions/f02-no-code-configuration/d521-benchmark-gaps-f02-no-code-configuration.md)).

## Examples

| Case | Result |
|---|---|
| 118 entries published in German | they ship as the German pack of the company |
| A product update changes a source text | the entry is outdated, its old text still shows |
| A pack exported and imported in another company | entries added as drafts |
| A pack that holds a customer's name | refused: texts of screens only |

## Applies to

- [UC-F2-34 Translate the screens in place](../use-cases/13-low-code-bulk-and-cleaning/uc-f02-34-translate-the-screens-in-place.md)
- [E-F2-33 Translation entry](../data/e-f02-33-translation-entry.md)
- [UC-F2-11 Export or import a configuration as a pack](../use-cases/06-share-a-configuration/uc-f02-11-export-or-import-a-configuration-as-a-pack.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-30](br-f02-30-time-based-rules-run-once-per-record-and-period.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-32 Merges keep every link and an undo window](br-f02-32-merges-keep-every-link-and-an-undo-window.md)
