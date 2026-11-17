🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F7-07 Costing method per category

# 📏 BR-F7-07 Costing method per category

**Status:** ✅ specified

## Statement

Each item category has one costing method (standard, average or FIFO) and a valuation mode (perpetual or periodic);
a method changes only at the start of an accounting period, with the stock revalued and logged.

## Why

See [D272](../../../06-decisions/f07-purchasing-and-stock/d272-valuation-and-counts.md).

## Examples

| Case | Result |
|---|---|
| Electrical in FIFO | Cost from the oldest receipts |
| Change to average in July | Applied on 1 January |

## Applies to

Every F7 use case concerned.

## Exceptions

None.

## Configurable

Yes: per category.

## Open questions

None.

---

⬅️ [BR-F7-06 Count differences need approval](br-f07-06-count-differences-need-approval.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F7-08 No negative stock](br-f07-08-no-negative-stock.md)
