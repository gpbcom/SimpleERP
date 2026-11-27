🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 📦 [SC15 Wholesale and distribution](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC15-06 Offline orders synced

# 📏 BR-SC15-06 Offline orders synced

**Status:** ✅ specified

## Statement

Orders taken offline follow the shared offline orders,
[BR-F6-14 Offline orders are checked again on sync](../../../02-functional/f06-customers-and-sales/business-rules/br-f06-14-offline-orders-are-checked-again-on-sync.md),
they keep the prices and stock of their last sync and are rechecked on sync.

## Why

See [D359](../../../06-decisions/sectors/d359-wholesale-sector-coverage.md).

## Examples

| Case | Result |
|---|---|
| Stock gone at sync | Back-order proposed |

## Applies to

Every SC15 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-SC15-05 EDI orders validated](br-sc15-05-edi-orders-validated.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC15-07 Back-orders kept or cancelled](br-sc15-07-back-orders-kept-or-cancelled.md)
