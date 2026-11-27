🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F10-05 Manager approval for sensitive till actions

# 📏 BR-F10-05 Manager approval for sensitive till actions

**Status:** ✅ specified

## Statement

A refund above the limit, a discount above the limit, a price change, a drawer opened without a sale and a
receipt reprint need a manager's PIN or badge, and are logged.

## Why

Usual till practice against errors and fraud; limits per role.

## Examples

| Case | Result |
|---|---|
| Discount 10 %, limit 15 % | Allowed |
| Discount 30 % | Manager PIN asked |

## Applies to

Every F10 use case concerned.

## Exceptions

None.

## Configurable

The limits, per role.

## Open questions

None.

---

⬅️ [BR-F10-04 Refunds link the original sale](br-f10-04-refunds-link-the-original.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F10-06 Offline, the till keeps selling](br-f10-06-offline-keeps-selling.md)
