🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-11 Certificates list paid amounts only

# 📏 BR-SC19-11 Certificates list paid amounts only

**Status:** 🔄 waiting for the owner

## Statement

A tax-credit certificate lists only the eligible amounts the household actually paid in the year, net of what the
advance already paid, and a corrected payment gives a corrected certificate that replaces the first.

## Why

A certificate with unpaid or ineligible amounts makes the household claim too much
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). (Proposed) The France-pack
rule is written later.

## Examples

| Case | Result |
|---|---|
| Invoice fully paid | the eligible amount is listed |
| Invoice half paid | only the paid half is listed |
| Payment received in January | counted in the new year |
| Invoice cancelled after the certificate | corrected certificate, first marked replaced |
| Ineligible line | never listed |

## Applies to

- [UC-SC19-11](../use-cases/03-home-services-tax-credit/uc-sc19-11-issue-the-tax-credit-certificate.md)
- [E-SC04-09](../../sc04-home-care/data/e-sc04-09-tax-credit-certificate.md)
- [E-SC19-06 Household contract](../data/e-sc19-06-household-contract.md)

## Exceptions

None.

## Configurable

The sending date and the form, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC19-10 Visits follow the contract's frequency](br-sc19-10-visits-follow-the-contracts-frequency.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC19-12 The advance needs the customer's consent](br-sc19-12-the-advance-needs-the-customers-consent.md)
