🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F7-03 Supplier invoices are matched

# 📏 BR-F7-03 Supplier invoices are matched

**Status:** ✅ specified

## Statement

A supplier invoice is matched to its order and receipt; within tolerances (2 % on price, none on quantity, D274), it
goes to accounting; beyond, or for goods not received, it is held with the differences listed.

## Why

See [D269](../../../06-decisions/f07-purchasing-and-stock/d269-supplier-invoices-in.md).

## Examples

| Case | Result |
|---|---|
| Same quantities, price +1 % | Sent to accounting |
| 10 units billed, 8 received | Held |

## Applies to

Every F7 use case concerned.

## Exceptions

None.

## Configurable

Yes: tolerances.

## Open questions

None.

---

⬅️ [BR-F7-02 Reorders are suggested, then confirmed](br-f07-02-reorders-are-suggested-then-confirmed.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F7-04 Expiring items leave first-expired-first](br-f07-04-expiring-items-leave-first-expired-first.md)
