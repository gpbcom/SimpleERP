🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F7-06 Count differences need approval

# 📏 BR-F7-06 Count differences need approval

**Status:** ✅ specified

## Statement

A count difference above a threshold (5 % or 500 EUR, D274) needs a manager's approval before the stock is adjusted;
smaller ones apply at once; every adjustment is valued and posted.

## Why

See [D272](../../../06-decisions/f07-purchasing-and-stock/d272-valuation-and-counts.md).

## Examples

| Case | Result |
|---|---|
| 180 counted, 200 expected, 16 EUR | Applied |
| 10 % on a costly item | Waits for a manager |

## Applies to

Every F7 use case concerned.

## Exceptions

None.

## Configurable

Yes: thresholds.

## Open questions

None.

---

⬅️ [BR-F7-05 Every move is traced](br-f07-05-every-move-is-traced.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F7-07 Costing method per category](br-f07-07-costing-method-per-category.md)
