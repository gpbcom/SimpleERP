🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-02 Reorders are suggested, then confirmed

# 📏 BR-F7-02 Reorders are suggested, then confirmed

**Status:** ✅ specified

## Statement

Reordering rules and the AI forecast produce suggested orders; a buyer confirms them, except items set to automatic,
whose orders are created by themselves within their rules.

## Why

See [D268](../../../06-decisions/f07-purchasing-and-stock/d268-ai-reorder.md).

## Examples

| Case | Result |
|---|---|
| Cable under its minimum | Suggested order of 800 m |
| Gloves set to automatic | Order created at night |

## Applies to

Every F7 use case concerned.

- [UC-F7-21 Set safety stock and min/max per item](../use-cases/03-replenish/uc-f07-21-set-safety-stock-and-min-max-per-item.md)

## Exceptions

None.

## Configurable

Yes: automatic per item.

## Open questions

None.

---

⬅️ [BR-F7-01 Purchases approved by amount and budget](br-f07-01-purchases-approved-by-amount-and-budget.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F7-03 Supplier invoices are matched](br-f07-03-supplier-invoices-are-matched.md)
