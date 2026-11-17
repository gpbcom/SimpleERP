🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-09 Weighed items come from the scale

# 📏 BR-F10-09 Weighed items come from the scale

**Status:** ✅ specified

## Statement

A product sold by weight takes its weight from a connected scale; typing a weight needs a manager; the scale must be
legal for trade; in France:
[CR-FR-033 Scales used for sales](../../../10-country-packs/france/point-of-sale/cr-fr-033-legal-metrology-scales.md).

## Why

See [D295](../../../06-decisions/f10-point-of-sale/d295-pos-coverage.md).

## Examples

| Case | Result |
|---|---|
| 0.734 kg read | Line at 0.734 kg |
| Scale offline | Manager may type the weight, logged |

## Applies to

Every F10 use case concerned.

## Exceptions

None.

## Configurable

Which products are weighed.

## Open questions

None.

---

⬅️ [BR-F10-08 Prices, promotions and reference prices](br-f10-08-prices-and-promotions.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F10-10 Orders go to their preparation station](br-f10-10-orders-routed-to-their-station.md)
