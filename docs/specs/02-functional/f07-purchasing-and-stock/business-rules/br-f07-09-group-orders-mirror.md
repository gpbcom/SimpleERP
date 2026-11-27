🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-09 Orders between group companies mirror each other

# 📏 BR-F7-09 Orders between group companies mirror each other

**Status:** ✅ specified

## Statement

A purchase from another company of the group creates the matching sale there, at the agreed transfer price, and both
stay in step.

## Why

See [D305](../../../06-decisions/f07-purchasing-and-stock/d305-f7-benchmark-gaps.md).

## Examples

| Case | Result |
|---|---|
| PO from Lyon to Paris | Sales order in Paris |

## Applies to

UC-F7-15

## Exceptions

None.

## Configurable

Transfer prices.

## Open questions

None.

---

⬅️ [BR-F7-08 No negative stock](br-f07-08-no-negative-stock.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F7-10 Third-party stock is reconciled daily](br-f07-10-third-party-stock-is-reconciled-daily.md)
