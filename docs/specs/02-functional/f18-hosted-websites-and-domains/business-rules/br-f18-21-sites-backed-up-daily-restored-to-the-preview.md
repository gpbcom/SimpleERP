🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-21 Sites backed up daily, restored to the preview

# 📏 BR-F18-21 Sites backed up daily, restored to the preview

**Status:** ✅ specified

## Statement

Each site, its content and its forms' settings are backed up daily and kept 30 days; a restore always goes to
the private preview first, then through the checks and the owner's approval.

## Why

A site can be broken or lost (D475); publication always goes through the preview (BR-F18-03).

## Examples

| Case | Result |
|---|---|
| Backup of 2026-11-10 restored | passes: preview shows it, owner publishes after checks |
| Restore straight to the live site | fails: refused |
| Backup older than the retention | fails: no longer available |

## Applies to

- [UC-F18-27 Back up and restore the site](../use-cases/05-run-the-site/uc-f18-27-back-up-and-restore-the-site.md)

## Exceptions

None.

## Configurable

The owner may keep monthly backups longer.

## Open questions

None.

---

⬅️ [BR-F18-20 Search basics from public data only](br-f18-20-search-basics-from-public-data-only.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F18-22 Tests end at significance or their end date](br-f18-22-tests-end-at-significance-or-their-end-date.md)
