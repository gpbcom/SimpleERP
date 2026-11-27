🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F7-08 No negative stock

# 📏 BR-F7-08 No negative stock

**Status:** ✅ specified

## Statement

A move that would make an item's stock negative in a location is refused, with the quantity missing and where stock
exists; a manager can allow negative stock per warehouse for urgent cases, each such move flagged and a count scheduled.

## Why

See [D275](../../../06-decisions/f07-purchasing-and-stock/d275-no-negative-stock.md).

## Examples

| Case | Result |
|---|---|
| Picking 10, 6 in stock | Refused: 4 missing, 20 in Villeurbanne |
| Allowed in the Lyon warehouse | Done, flagged, count scheduled |

## Applies to

Every stock move.

## Exceptions

Warehouses where a manager allows it.

## Configurable

Yes: per warehouse, by a manager.

## Open questions

None.

---

⬅️ [BR-F7-07 Costing method per category](br-f07-07-costing-method-per-category.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F7-09 Orders between group companies mirror each other](br-f07-09-group-orders-mirror.md)
