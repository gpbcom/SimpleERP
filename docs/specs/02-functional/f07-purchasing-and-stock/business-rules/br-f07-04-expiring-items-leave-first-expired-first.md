🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-04 Expiring items leave first-expired-first

# 📏 BR-F7-04 Expiring items leave first-expired-first

**Status:** ✅ specified

## Statement

Items with expiry dates are picked by FEFO; an item past its removal date is never reserved; expiry alerts go to the
warehouse and the buyer.

## Why

See [D271](../../../06-decisions/f07-purchasing-and-stock/d271-warehouse-operations.md).

## Examples

| Case | Result |
|---|---|
| Two lots, expiring March and June | March picked first |
| A lot past its removal date | Blocked |

## Applies to

Every F7 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F7-03 Supplier invoices are matched](br-f07-03-supplier-invoices-are-matched.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F7-05 Every move is traced](br-f07-05-every-move-is-traced.md)
