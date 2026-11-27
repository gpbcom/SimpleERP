🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-09 Only eligible services carry the tax credit

# 📏 BR-SC19-09 Only eligible services carry the tax credit

**Status:** ✅ specified

## Statement

Each service line of a household contract is marked eligible or not for the tax credit from the catalogue of the country
pack, and only eligible lines are counted in the certificate. A contract is activated only while the company's
declaration or approval is valid.

## Why

Claiming a credit on ineligible work exposes the household to a correction and the company to a penalty
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). The France-pack rules are
[CR-FR-103 Tax credit for home services and its yearly certificate](../../../10-country-packs/france/tax-and-vat/cr-fr-103-home-services-tax-credit.md)
(50 % of what the household paid, within the yearly ceilings) and
[CR-FR-102 Personal-services declaration, approval and authorisation](../../../10-country-packs/france/home-care/cr-fr-102-personal-services-registration.md)
(the declaration, or the approval for some services).

## Examples

| Case | Result |
|---|---|
| Weekly cleaning | eligible, counted in the certificate |
| A repair in the same visit | not eligible, on its own quote |
| Landlord for a rented flat | not eligible, the contract says so |
| Company declaration expired | contract not activated |
| Task not in the catalogue | marked ineligible until listed |

## Applies to

- [UC-SC19-09](../use-cases/03-home-services-tax-credit/uc-sc19-09-sell-cleaning-and-gardening-to-households.md)
- [E-SC19-06 Household contract](../data/e-sc19-06-household-contract.md)
- [E-SC19-06 Household contract](../data/e-sc19-06-household-contract.md)
- [E-SC04-09](../../sc04-home-care/data/e-sc04-09-tax-credit-certificate.md)

## Exceptions

None.

## Configurable

The catalogue of eligible services and the ceilings, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC19-08 The invoice follows the signed report](br-sc19-08-the-invoice-follows-the-signed-report.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC19-10 Visits follow the contract's frequency](br-sc19-10-visits-follow-the-contracts-frequency.md)
