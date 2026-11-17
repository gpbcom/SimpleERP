🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📦 [F7 Purchasing and stock](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F7-13 Catalogue and punch-out carts become requests

# 📏 BR-F7-13 Catalogue and punch-out carts become requests

**Status:** ✅ specified

## Statement

A cart from the approved catalogue or a punch-out site returns as purchase request lines that follow the approval chain;
items off contract are flagged for the buyer.

## Why

Self-service buying must not bypass approvals (BR-F7-01).

## Examples

| Case | Result |
|---|---|
| Cart of 140 EUR | Request to approve |
| Item off contract | Flagged |

## Applies to

- [UC-F7-20 Order from an approved catalogue or punch-out](../use-cases/08-catalogues-and-stock-levels/uc-f07-20-order-from-an-approved-catalogue-or-punch-out.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F7-12](br-f07-12-the-buyer-is-told-before-a-contracts-notice-date.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F7-14 Safety stock triggers a suggestion](br-f07-14-safety-stock-triggers-a-suggestion.md)
