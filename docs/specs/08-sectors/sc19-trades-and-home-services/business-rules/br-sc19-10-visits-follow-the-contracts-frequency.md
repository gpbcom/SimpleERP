🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-10 Visits follow the contract's frequency

# 📏 BR-SC19-10 Visits follow the contract's frequency

**Status:** 🔄 waiting for the owner

## Statement

A household visit is planned according to the frequency and the hours of its contract and is never planned beyond them.
The same worker is kept when possible, and each visit done is recorded with its date and hours.

## Why

Too few visits break the contract and too many are not paid; the hours done feed the invoice and the certificate
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)).

## Examples

| Case | Result |
|---|---|
| Weekly contract | one visit a week on the preferred day |
| Worker absent | replacement proposed, household told |
| Household absent | visit marked not done with its reason |
| Visit beyond the contract's hours | refused |
| No network on the phone | hours kept and sent later |

## Applies to

- [UC-SC19-10](../use-cases/03-home-services-tax-credit/uc-sc19-10-plan-recurring-household-visits.md)
- [E-SC19-06 Household contract](../data/e-sc19-06-household-contract.md)
- [E-F9-17](../../../02-functional/f09-hr-and-projects/data/e-f09-17-timesheet-line.md)

## Exceptions

None.

## Configurable

Whether a visit missed by the household is charged, set in the contract.

## Open questions

None.

---

⬅️ [BR-SC19-09 Only eligible services carry the tax credit](br-sc19-09-only-eligible-services-carry-the-tax-credit.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC19-11 Certificates list paid amounts only](br-sc19-11-certificates-list-paid-amounts-only.md)
