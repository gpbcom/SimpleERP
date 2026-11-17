🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-07 Intercompany mirrored and eliminated

# 📏 BR-F8-07 Intercompany mirrored and eliminated

**Status:** ✅ specified

## Statement

An invoice between two companies of the group creates the mirror bill in the other company; at consolidation,
intercompany balances, sales and purchases are eliminated, and differences listed.

## Why

See [D281](../../../06-decisions/f08-accounting/d281-consolidation-eliminations.md).

## Examples

| Case | Result |
|---|---|
| Acme Bâtiment invoices Acme Services 10,000 EUR | Mirror bill in Acme Services |
| Consolidation | The 10,000 EUR eliminated |

## Applies to

Every F8 use case concerned.

## Exceptions

None.

## Configurable

Yes: group and mapping.

## Open questions

None.

---

⬅️ [BR-F8-06 Balanced entries, continuous numbers](br-f08-06-balanced-entries-continuous-numbers.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F8-08 New IBANs are checked](br-f08-08-new-ibans-are-checked.md)
