🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-11 Contract prices apply within their validity

# 📏 BR-F7-11 Contract prices apply within their validity

**Status:** ✅ specified

## Statement

During a supplier contract's validity, its prices and discounts apply to orders; a different price is flagged before
sending, and purchases accrue the contract's volume rebate.

## Why

Agreed prices are only worth something if they are applied and checked.

## Examples

| Case | Result |
|---|---|
| Order at 12.40 EUR, contract 11.65 EUR | Flagged |
| Purchases pass 200,000 EUR | Rebate 2 % accrued |

## Applies to

- [UC-F7-18 Manage supplier contracts and price agreements](../use-cases/07-supplier-agreements-and-performance/uc-f07-18-manage-supplier-contracts-and-price-agreements.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F7-10 Third-party stock is reconciled daily](br-f07-10-third-party-stock-is-reconciled-daily.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F7-12](br-f07-12-the-buyer-is-told-before-a-contracts-notice-date.md)
