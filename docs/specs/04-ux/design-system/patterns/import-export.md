🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧵 [Patterns](README.md) ›
🧵 Import export

# 🧵 Import export

**Status:** 🔄 waiting for the owner

## Purpose

How data comes into SimpleERP from files and other software, and goes out to users, accountants and other tools,
without losing or doubling anything.

## When to use

The setup's data import ([D61](../../../06-decisions/f01-administration/d61-setup-imports.md)), importers from other
ERPs ([D424](../../../06-decisions/technical/d424-importers.md)), the import of a configuration pack, as on
[S-F2-11 Packs](../../../02-functional/f02-no-code-configuration/screens/06-share-a-configuration/s-f02-11-packs.md),
the import step of the first-run guide, as on
[S-F21-09 Import](../../../02-functional/f21-onboarding-and-modules/screens/03-team-and-data/s-f21-09-import.md);
exports of lists, reports, the FEC, packs and support conversations.

## Anatomy

```text
Import                                                  Export
1. Source    [Spreadsheet template v] [Choose a file]   [Export v]
2. Mapping   Column "Raison sociale" -> Name            Format: CSV, Excel
3. Dry run   1,240 to add, 12 to update, 3 in error     Only the rows shown
4. Import    [Import 1,252 rows]                        [Download]
```

An import is a [Wizard pattern](wizard.md): source and file ([C-12 File upload](../components/c-12-file-upload.md)),
mapping of columns to fields with the AI assistant's help, a dry run that shows what will be added, changed and refused,
then the import with its report. An export is a button of the list or report, with its format.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/import-export-desktop-light.png) | ![Variants and states, dark](../images/import-export-desktop-dark.png) |

## Behaviour

- Sources: spreadsheet templates (CSV or Excel), the FEC of the previous software, and other ERPs through importers
  (Odoo, Dolibarr, Sage, EBP) on one mapping model
  ([D61](../../../06-decisions/f01-administration/d61-setup-imports.md),
  [D424](../../../06-decisions/technical/d424-importers.md)).
- A dry run always comes first; nothing is written before the user confirms
  ([D424](../../../06-decisions/technical/d424-importers.md)).
- Lines in error are listed with their message and can be downloaded, fixed and imported again; good lines are not
  blocked by bad ones (Proposed).
- An imported pack shows what it adds and changes before it applies, as on
  [S-F2-11 Packs](../../../02-functional/f02-no-code-configuration/screens/06-share-a-configuration/s-f02-11-packs.md).
- An export holds only what the user may see ([D12](../../../06-decisions/foundations/d12-permissions-model.md)); large
  exports run on the server and are offered when ready ([Performance](../../../05-non-functional/performance.md)).

## Accessibility

- Each step of an import is a page of the [Wizard pattern](wizard.md) with its title; the dry-run report is a table with
  headers.
- Progress and results are announced; the download link names its file and format.

## Used in

[S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md),
[S-F2-11 Packs](../../../02-functional/f02-no-code-configuration/screens/06-share-a-configuration/s-f02-11-packs.md),
[S-F21-09 Import](../../../02-functional/f21-onboarding-and-modules/screens/03-team-and-data/s-f21-09-import.md),
[S-F4-10 Share and export](../../../02-functional/f04-meetings/screens/08-share-and-reuse-outside/s-f04-10-share-and-export.md)
and
[S-F20-20 Export](../../../02-functional/f20-hosted-support-assistant/screens/04-govern-the-assistant/s-f20-20-export.md);
and the Export action of lists and reports.

---

⬅️ [Bulk actions](bulk-actions.md) · ⬆️ [Up](README.md)
