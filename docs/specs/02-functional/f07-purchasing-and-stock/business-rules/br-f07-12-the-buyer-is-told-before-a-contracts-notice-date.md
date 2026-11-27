🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-12 The buyer is told before a contract's notice date

# 📏 BR-F7-12 The buyer is told before a contract's notice date

**Status:** ✅ specified

## Statement

A buyer is told before each contract's notice date (default: 30 days before), with the choices to renew, renegotiate or
end.

## Why

A missed notice date renews a contract the company wanted to change.

## Examples

| Case | Result |
|---|---|
| Notice 2027-09-30 | Told on 2027-08-31 |

## Applies to

- [UC-F7-18 Manage supplier contracts and price agreements](../use-cases/07-supplier-agreements-and-performance/uc-f07-18-manage-supplier-contracts-and-price-agreements.md)

## Exceptions

None.

## Configurable

Days before (default: 30).

## Open questions

None.

---

⬅️ [BR-F7-11 Contract prices apply within their validity](br-f07-11-contract-prices-apply-within-their-validity.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F7-13](br-f07-13-catalogue-and-punch-out-carts-become-requests.md)
