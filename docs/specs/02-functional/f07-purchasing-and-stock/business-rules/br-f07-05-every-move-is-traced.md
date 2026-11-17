🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F7-05 Every move is traced

# 📏 BR-F7-05 Every move is traced

**Status:** ✅ specified

## Statement

Every stock move records its item, quantity, locations, lot or serial when tracked, who and when; moves are never
deleted, only reversed.

## Why

See [D266](../../../06-decisions/f07-purchasing-and-stock/d266-purchasing-and-stock-scope.md).

Legal values from the France country pack:
[CR-FR-061 Food traceability](../../../10-country-packs/france/products/cr-fr-061-food-traceability.md).

## Examples

| Case | Result |
|---|---|
| A wrong receipt | Reversed by a new move, both kept |

## Applies to

Every F7 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F7-04 Expiring items leave first-expired-first](br-f07-04-expiring-items-leave-first-expired-first.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F7-06 Count differences need approval](br-f07-06-count-differences-need-approval.md)
