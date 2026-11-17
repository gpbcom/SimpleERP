🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-13 Delivery orders through connectors

# 📏 BR-F10-13 Delivery orders through connectors

**Status:** ✅ specified

## Statement

Delivery-platform orders arrive through T12 connectors, are accepted or refused with a reason, and go to preparation
like any order.

## Why

See [D298](../../../06-decisions/f10-point-of-sale/d298-delivery-platforms-through-connectors.md).

## Examples

| Case | Result |
|---|---|
| New platform order | Shown to accept, then routed |

## Applies to

Every F10 use case concerned.

## Exceptions

None.

## Configurable

Platforms enabled.

## Open questions

None.

---

⬅️ [BR-F10-12 Loyalty needs a customer, vouchers follow VAT rules](br-f10-12-loyalty-and-vouchers.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F10-14 Training mode is marked](br-f10-14-training-mode-is-marked.md)
