🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-04 Renewals follow the notice and index clauses

# 📏 BR-SC19-04 Renewals follow the notice and index clauses

**Status:** 🔄 waiting for the owner

## Statement

A contract is renewed or ended on its notice date, and its price changes only by the index clause written in it. The
renewal notice is sent before the notice date, and a notice date that has passed moves the renewal to the next period.

## Why

A price change without a clause, or a renewal without a reminder, is a dispute the company loses
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). (Proposed) The France-pack
rule is written later.

## Examples

| Case | Result |
|---|---|
| Index clause, notice date in 30 days | new price computed and notice sent |
| No index clause | price kept unless the customer agrees |
| Notice date passed | renewal proposed for the next period |
| Customer ends the contract in time | Ended at the end date |
| Index not available | price not computed, contract listed |

## Applies to

- [UC-SC19-04](../use-cases/01-maintenance-contracts/uc-sc19-04-renew-and-index-contracts.md)
- [E-SC19-01 Maintenance contract](../data/e-sc19-01-maintenance-contract.md)
- [E-F6-07](../../../02-functional/f06-customers-and-sales/data/e-f06-07-subscription-contract.md)

## Exceptions

None.

## Configurable

The index, its base month and the days of notice, from the contract.

## Open questions

None.

---

⬅️ [BR-SC19-03 Certificates are given to the customer](br-sc19-03-certificates-are-given-to-the-customer.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC19-05](br-sc19-05-the-nearest-qualified-technician-is-proposed.md)
