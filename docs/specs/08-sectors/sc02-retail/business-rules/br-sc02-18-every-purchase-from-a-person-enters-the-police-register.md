🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🛍️ [SC02 Retail](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC02-18 Every purchase from a person enters the police register

# 📏 BR-SC02-18 Every purchase from a person enters the police register

**Status:** 🔄 waiting for the owner

## Statement

Every purchase of an object from a person is written in the second-hand register, with the seller's identity checked on
a document and the description of the object, before any payment is made. A saved line is never edited: a mistake is
corrected by a dated new line.

## Why

The register is how the authorities trace stolen goods; a dealer without it is liable. The owner asked for second-hand
buy-back ([D546](../../../06-decisions/sectors/d546-benchmark-gaps-sc02-retail.md)). (Proposed) The France-pack rule is
written later.

## Examples

| Case | Result |
|---|---|
| Seller with an identity card, watch at 120.00 EUR | line written, payment allowed |
| No identity document | refused |
| Seller is a company with an invoice | ordinary purchase, no line |
| Wrong serial number noticed later | a dated correction line |

## Applies to

- [UC-SC02-18](../use-cases/06-books-furniture-second-hand-franchise/uc-sc02-18-buy-back-second-hand-goods.md)
- [E-SC02-15 Second-hand purchase](../data/e-sc02-15-second-hand-purchase.md)
- [E-F7-06 Item](../../../02-functional/f07-purchasing-and-stock/data/e-f07-06-item.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-228 Second-hand purchase register](../../../10-country-packs/france/trade/cr-fr-228-second-hand-register.md)

## Exceptions

Purchases from businesses, made with an invoice.

## Configurable

The documents accepted as identity, as data of the country pack.

## Open questions

None.

---

⬅️ [BR-SC02-17](br-sc02-17-dates-follow-the-suppliers-confirmed-lead-time.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC02-19 Royalties follow the franchise agreement](br-sc02-19-royalties-follow-the-franchise-agreement.md)
