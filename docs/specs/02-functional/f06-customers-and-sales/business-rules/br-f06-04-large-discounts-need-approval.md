🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F6-04 Large discounts need approval

# 📏 BR-F6-04 Large discounts need approval

**Status:** ✅ specified

## Statement

A quote whose discount exceeds the sales person's threshold (15 % by default, set per role) or whose margin falls below
the company's floor goes to a manager's approval before it can be sent.

## Why

See [D255](../../../06-decisions/f06-customers-and-sales/d255-discount-approval.md).

## Examples

| Case | Result |
|---|---|
| 12 % discount by a sales person | Sent |
| 18 % | Waits for a manager |
| Margin 8 %, floor 10 % | Waits for a manager |

## Applies to

Every F6 use case concerned.

## Exceptions

None.

## Configurable

Yes: thresholds per role, the margin floor.

## Open questions

None.

---

⬅️ [BR-F6-03 The portal shows only the customer's own](br-f06-03-portal-shows-only-the-customer-s-own.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F6-05 Reminders run on their own](br-f06-05-reminders-run-on-their-own.md)
