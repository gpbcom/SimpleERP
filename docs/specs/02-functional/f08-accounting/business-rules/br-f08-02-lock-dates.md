🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-02 Lock dates

# 📏 BR-F8-02 Lock dates

**Status:** ✅ specified

## Statement

Periods can be locked: for everyone but the accountants, for everyone, and for taxes once a return is filed; after the
year-end closing and earnings allocation, a hard lock that no one can lift; each exception is logged.

## Why

See [D280](../../../06-decisions/f08-accounting/d280-bookkeepers.md).

Legal values from the France country pack:
[CR-FR-003 Posted entries are inalterable](../../../10-country-packs/france/accounting/cr-fr-003-posted-entries-are-inalterable.md).

## Examples

| Case | Result |
|---|---|
| An invoice dated in a locked month | Refused, with the lock date |
| The accountant posts an adjustment before the hard lock | Allowed, logged |

## Applies to

Every F8 use case concerned.

## Exceptions

None.

## Configurable

Yes: dates, by the accountants.

## Open questions

None.

---

⬅️ [BR-F8-01 Posted entries never change](br-f08-01-posted-entries-never-change.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-03 Every bank line is reconciled](br-f08-03-every-bank-line-is-reconciled.md)
