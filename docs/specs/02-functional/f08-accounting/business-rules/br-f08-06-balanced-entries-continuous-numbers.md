🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-06 Balanced entries, continuous numbers

# 📏 BR-F8-06 Balanced entries, continuous numbers

**Status:** ✅ specified

## Statement

Every entry is balanced (debit equals credit, per currency converted); each journal numbers its entries in a continuous
sequence per fiscal year.

## Why

See [D277](../../../06-decisions/f08-accounting/d277-accounting-coverage.md).

Legal values from the France country pack:
[CR-FR-004 Balanced entries, continuous numbers](../../../10-country-packs/france/accounting/cr-fr-004-balanced-entries-continuous-numbers.md).

## Examples

| Case | Result |
|---|---|
| An unbalanced manual entry | Refused, with the difference |

## Applies to

Every F8 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F8-05 Expenses need a receipt and an approval](br-f08-05-expenses-need-a-receipt-and-an-approval.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F8-07 Intercompany mirrored and eliminated](br-f08-07-intercompany-mirrored-and-eliminated.md)
