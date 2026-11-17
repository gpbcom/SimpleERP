🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🛍️ [SC02 Retail](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC02-19 Royalties follow the franchise agreement

# 📏 BR-SC02-19 Royalties follow the franchise agreement

**Status:** 🔄 waiting for the owner

## Statement

The royalty and the marketing contribution of a month are computed only from the franchisee's reported sales and the
rates written in its agreement, and an agreement can be signed only after the disclosure document has been sent and the
minimum delay has passed.

## Why

A royalty that drifts from the agreement is a dispute; a signature without the disclosure document can void the
agreement. The owner asked for the franchise network
([D546](../../../06-decisions/sectors/d546-benchmark-gaps-sc02-retail.md)). The delay and the document are
the France-pack rule, written later.

## Examples

| Case | Result |
|---|---|
| Rate 5 % on 84,000.00 EUR | royalty 4,200.00 EUR |
| Disclosure sent today, signature today | blocked |
| First-year rate 3 % | applied for the first twelve months |
| Sales missing for a closed till | statement waits |

## Applies to

- [UC-SC02-19](../use-cases/06-books-furniture-second-hand-franchise/uc-sc02-19-run-a-franchise-network.md)
- [E-SC02-16 Franchisee](../data/e-sc02-16-franchisee.md)
- [E-F6-05 Invoice](../../../02-functional/f06-customers-and-sales/data/e-f06-05-invoice.md)
- France-pack rule, (Proposed) until its law is read:
  [CR-FR-253 Franchise disclosure document](../../../10-country-packs/france/trade/cr-fr-253-franchise-disclosure.md)

## Exceptions

None.

## Configurable

The rates, per agreement, by the owner; the minimum delay, as data of the country pack.

## Open questions

None.

---

⬅️ [BR-SC02-18](br-sc02-18-every-purchase-from-a-person-enters-the-police-register.md) · ⬆️ [Up](README.md)
