🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F6-13 Each payer pays its share up to its cap

# 📏 BR-F6-13 Each payer pays its share up to its cap

**Status:** ✅ specified

## Statement

A line funded by several payers is split by each agreement's share, within its cap and period; what passes a cap or an
expired agreement goes to the next payer, finally the beneficiary.

## Why

The shared multi-payer capability of D457 for home care, health, training and grants.

## Examples

| Case | Result |
|---|---|
| 46 h, funder 70 % up to 40 h | Funder 28 h, beneficiary 12 h + 6 h |
| Agreement expired mid-month | Rest to the beneficiary, accounting warned |

## Applies to

- [UC-F6-20 Invoice several payers with funders and caps](../use-cases/07-special-invoicing/uc-f06-20-invoice-several-payers-with-funders-and-caps.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F6-12](br-f06-12-public-invoices-go-through-chorus-pro-with-their-references.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-14 Offline orders are checked again on sync](br-f06-14-offline-orders-are-checked-again-on-sync.md)
