🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 📦 [SC15 Wholesale and distribution](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC15-18 The invoice uses the weighed quantity

# 📏 BR-SC15-18 The invoice uses the weighed quantity

**Status:** ✅ specified

## Statement

An item sold by catch weight is invoiced on the sum of the weights of the cases delivered, at the price per kilo of the
order, and never on the nominal weight once weights exist. Each case has its own weight before the line can be
delivered.

## Why

Invoicing the nominal weight overcharges or undercharges the customer by the difference, and a delivery without weights
cannot be defended. The owner asked for catch weight
([D559](../../../06-decisions/sectors/d559-benchmark-gaps-sc15-wholesale-and-distribution.md)). The
France-pack rule is written later.

## Examples

| Case | Result |
|---|---|
| 10 cases weighing 51.4 kg at 18.00 EUR per kg | 925.20 EUR |
| Case without a weight | line not delivered |
| Weight typed by hand | accepted and flagged |
| Scale not verified | weighing refused |
| Case returned | credited at its weight and the same price per kilo |

## Applies to

- [UC-SC15-23](../use-cases/06-beverages-vans-weights-and-devices/uc-sc15-23-sell-by-catch-weight.md)
- [E-F6-05 Invoice](../../../02-functional/f06-customers-and-sales/data/e-f06-05-invoice.md)
- [E-F6-04 Order](../../../02-functional/f06-customers-and-sales/data/e-f06-04-order.md)

## Exceptions

None.

## Configurable

The tolerance of the difference with the nominal weight, by sales.

## Open questions

None.

---

⬅️ [BR-SC15-17 The van's stock is counted at each reload](br-sc15-17-the-vans-stock-is-counted-at-each-reload.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC15-19 Every lot is traceable by its UDI](br-sc15-19-every-lot-is-traceable-by-its-udi.md)
