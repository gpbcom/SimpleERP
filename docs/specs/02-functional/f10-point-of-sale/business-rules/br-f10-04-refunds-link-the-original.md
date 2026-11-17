🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-04 Refunds link the original sale

# 📏 BR-F10-04 Refunds link the original sale

**Status:** ✅ specified

## Statement

A paid order is never deleted or edited: a refund or exchange is a new order with negative lines, linked to the original
receipt.

## Why

See [D296](../../../06-decisions/f10-point-of-sale/d296-till-certified-before-france.md).

## Examples

| Case | Result |
|---|---|
| Refund of 1 of 3 items | Negative line linked to receipt 2026-000184 |
| Refund with no receipt | Allowed only for a manager (BR-F10-05) |

## Applies to

Every F10 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F10-03 Cash within the legal limit](br-f10-03-cash-within-the-legal-limit.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F10-05 Manager approval for sensitive till actions](br-f10-05-manager-pin-for-sensitive-actions.md)
