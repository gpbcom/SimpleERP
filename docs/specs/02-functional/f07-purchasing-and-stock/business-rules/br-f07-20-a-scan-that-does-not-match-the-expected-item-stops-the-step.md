🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-20 A scan that does not match the expected item stops the step

# 📏 BR-F7-20 A scan that does not match the expected item stops the step

**Status:** 🔄 waiting for the owner

## Statement

A scan that does not match the item, the lot or the location the step expects stops the step: nothing is moved, the
phone shows the expected and the scanned code, and only a corrected scan or a supervisor's override with a reason lets
the step go on.

## Why

A wrong item moved silently corrupts the stock and the traceability
([BR-F7-05 Every move is traced](br-f07-05-every-move-is-traced.md)); the owner asked for a warehouse barcode app
([D526](../../../06-decisions/f07-purchasing-and-stock/d526-benchmark-gaps-f07-purchasing-and-stock.md)).

## Examples

| Case | Result |
|---|---|
| Expected oak plank, scanned oak plank | match, the line turns green |
| Expected oak plank, scanned brass hinge | stop, nothing is moved |
| Expected lot L-4412, scanned lot L-4390 | stop for a lot-tracked item |
| Expected location A-12-3, scanned B-02-1 | stop, the operator goes to the right location |
| A supervisor override with a reason | the line goes on and the override is audited |

## Applies to

- [UC-F7-26](../use-cases/10-consignment-scanning-and-edi/uc-f07-26-scan-in-the-warehouse-app.md)
- [E-F7-06 Item](../data/e-f07-06-item.md)
- [E-F7-10 Lot or serial](../data/e-f07-10-lot-or-serial.md)

## Exceptions

An item without any barcode may be typed; the entry is marked as typed and counted for the supervisor.

## Configurable

Yes: per item, whether the lot must be scanned (lot-tracked items always).

## Open questions

None.

---

⬅️ [BR-F7-19 Consigned stock is never valued as own stock](br-f07-19-consigned-stock-is-never-valued-as-own-stock.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F7-21 Periodic valuation posts only at period end](br-f07-21-periodic-valuation-posts-only-at-period-end.md)
