🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-28 The auditor reads only and every view is logged

# 📏 BR-F8-28 The auditor reads only and every view is logged

**Status:** ✅ specified

## Statement

The statutory auditor has read-only access to the books and their documents for the dates of their engagement; they can
change, post, delete or upload nothing in the books, and every page they open, search they run and file they download is
logged with the time and the record.

## Why

An auditor must see what they need without being able to alter it, and the company must be able to show who saw what.
The owner asked for a statutory auditor workspace
([D527](../../../06-decisions/f08-accounting/d527-benchmark-gaps-f08-accounting.md)); posted entries are inalterable
([BR-F8-01 Posted entries never change](br-f08-01-posted-entries-never-change.md)).

## Examples

| Case | Result |
|---|---|
| The auditor opens an entry | shown, the view is logged |
| The auditor tries to edit an entry | refused, the attempt is logged |
| The auditor downloads the ledger | allowed and logged with the file name |
| The auditor signs in after the engagement ended | refused |
| The auditor asks for a correction | accounting posts it; the auditor never does |

## Applies to

- [UC-F8-36](../use-cases/12-audit-leases-and-special-books/uc-f08-36-open-the-books-to-the-statutory-auditor.md)
- [E-F8-40 Audit request](../data/e-f08-40-audit-request.md)
- [E-F8-03 Journal entry](../data/e-f08-03-journal-entry.md)
- [E-F8-22 Annual accounts file](../data/e-f08-22-annual-accounts-file.md)
- France-pack rule:
  [CR-FR-213 When a statutory auditor is required](../../../10-country-packs/france/accounting/cr-fr-213-statutory-auditor-thresholds.md)

## Exceptions

None.

## Configurable

Yes: the engagement dates and which books the auditor sees, by accounting.

## Open questions

None.

---

⬅️ [BR-F8-27 Recurring entries stop at their end date](br-f08-27-recurring-entries-stop-at-their-end-date.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F8-29 Leases follow the book's standard](br-f08-29-leases-follow-the-books-standard.md)
