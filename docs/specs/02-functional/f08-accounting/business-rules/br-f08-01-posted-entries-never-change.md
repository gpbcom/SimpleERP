🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-01 Posted entries never change

# 📏 BR-F8-01 Posted entries never change

**Status:** ✅ specified

## Statement

A posted entry can no longer be changed or deleted; it is corrected by a reversal or a new entry; posted entries are
chained by a hash so that any tampering shows (data inalterability, as French law requires for accounting and the FEC).

## Why

See [D277](../../../06-decisions/f08-accounting/d277-accounting-coverage.md).

Legal values from the France country pack:
[CR-FR-003 Posted entries are inalterable](../../../10-country-packs/france/accounting/cr-fr-003-posted-entries-are-inalterable.md).

## Examples

| Case | Result |
|---|---|
| A wrong amount on a posted entry | Reversal, then a new entry |
| A database edit outside simple-ERP | The inalterability check reports the broken chain |

## Applies to

Every F8 use case concerned.

- [UC-F8-26 Provision doubtful debts](../use-cases/08-year-end-duties/uc-f08-26-provision-doubtful-debts.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [BR-F8-02 Lock dates](br-f08-02-lock-dates.md)
