🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 📦 [SC15 Wholesale and distribution](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC15-19 Every lot is traceable by its UDI

# 📏 BR-SC15-19 Every lot is traceable by its UDI

**Status:** 🔄 waiting for the owner

## Statement

Every device lot is received with its UDI, shipped only when released, and linked to the customers who received it, so
that any customer of a lot can be found from its UDI. A quarantined or recalled lot cannot be shipped.

## Why

A safety notice is useless if the distributor cannot say who has the device. The owner asked for medical devices
([D559](../../../06-decisions/sectors/d559-benchmark-gaps-sc15-wholesale-and-distribution.md)). The
France-pack rule is written later.

## Examples

| Case | Result |
|---|---|
| Lot released after its checks | shipments allowed |
| Lot shipped to 3 customers then recalled | the 3 customers are listed |
| Quarantined lot | shipment refused |
| Unreadable UDI | no reception |
| Lot past its expiry | blocked and listed |

## Applies to

- [UC-SC15-24](../use-cases/06-beverages-vans-weights-and-devices/uc-sc15-24-distribute-medical-devices.md)
- [E-SC15-17 Device lot](../data/e-sc15-17-device-lot.md)
- [E-F7-10](../../../02-functional/f07-purchasing-and-stock/data/e-f07-10-lot-or-serial.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-247 Medical device UDI traceability](../../../10-country-packs/france/products/cr-fr-247-medical-device-udi.md)

## Exceptions

None.

## Configurable

The checks of each device family and the reminder before expiry, by the quality manager.

## Open questions

None.

---

⬅️ [BR-SC15-18 The invoice uses the weighed quantity](br-sc15-18-the-invoice-uses-the-weighed-quantity.md) ·
⬆️ [Up](README.md)
