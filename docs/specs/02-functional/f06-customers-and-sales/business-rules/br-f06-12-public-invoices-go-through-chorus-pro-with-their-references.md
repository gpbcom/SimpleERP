🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F6-12 Public invoices go through Chorus Pro with their references

# 📏 BR-F6-12 Public invoices go through Chorus Pro with their references

**Status:** ✅ specified

## Statement

An invoice to a public buyer is deposited on Chorus Pro with the buyer's SIRET, the service code and the engagement
number when the buyer requires them; without them it cannot be validated.

## Why

Public buyers accept only invoices through Chorus Pro (CR-FR-091).

## Examples

| Case | Result |
|---|---|
| Town hall requires an engagement number | Asked before validation |
| Rejected by the buyer | Credit note and new invoice |

## Applies to

- [UC-F6-19 Invoice a public buyer through Chorus Pro](../use-cases/07-special-invoicing/uc-f06-19-invoice-a-public-buyer-through-chorus-pro.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F6-11 Over the credit limit, orders are held](br-f06-11-over-the-credit-limit-orders-are-held.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F6-13 Each payer pays its share up to its cap](br-f06-13-each-payer-pays-its-share-up-to-its-cap.md)
