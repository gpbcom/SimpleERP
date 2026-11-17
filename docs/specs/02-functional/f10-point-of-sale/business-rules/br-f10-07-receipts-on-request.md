🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F10-07 Paper receipts on request

# 📏 BR-F10-07 Paper receipts on request

**Status:** ✅ specified

## Statement

The receipt is printed only when the customer asks or the country pack requires it; otherwise it is offered by email,
SMS or a QR code; in France:
[CR-FR-031 Paper receipts on request only](../../../10-country-packs/france/point-of-sale/cr-fr-031-paper-receipt-on-request.md).

## Why

See [D295](../../../06-decisions/f10-point-of-sale/d295-pos-coverage.md).

## Examples

| Case | Result |
|---|---|
| Customer declines | No print, receipt kept |
| Customer asks | Printed |

## Applies to

Every F10 use case concerned.

## Exceptions

None.

## Configurable

The digital channels offered.

## Open questions

None.

---

⬅️ [BR-F10-06 Offline, the till keeps selling](br-f10-06-offline-keeps-selling.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F10-08 Prices, promotions and reference prices](br-f10-08-prices-and-promotions.md)
