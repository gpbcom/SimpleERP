🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-01 Contracts list the legal yearly check-ups

# 📏 BR-SC19-01 Contracts list the legal yearly check-ups

**Status:** 🔄 waiting for the owner

## Statement

Every equipment on a maintenance contract carries the legal check-up of its kind, and a contract is activated only when
the customer has signed and each equipment has its check-up. A check-up the law requires cannot be removed from a
contract.

## Why

A contract that forgets the legal check-up leaves the customer in breach and the company without proof of its service.
The owner asked for trades and home services
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). (Proposed) The France-pack
rule is written later.

## Examples

| Case | Result |
|---|---|
| Gas boiler added | the yearly check-up is added and kept |
| Heat pump added | the interval of the pack is added |
| Equipment of an unknown kind | the contract stays in draft |
| Check-up removed by the owner | refused with the reason |
| Contract unsigned after the offer's validity | expired as a draft |

## Applies to

- [UC-SC19-01](../use-cases/01-maintenance-contracts/uc-sc19-01-sell-a-maintenance-contract.md)
- [E-SC19-01 Maintenance contract](../data/e-sc19-01-maintenance-contract.md)
- [E-F6-07](../../../02-functional/f06-customers-and-sales/data/e-f06-07-subscription-contract.md)
- [UC-SC19-02](../use-cases/01-maintenance-contracts/uc-sc19-02-generate-recurring-visits.md)

## Exceptions

None.

## Configurable

The equipment kinds, their check-ups and intervals (from the country pack) and the validity of an offer.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [BR-SC19-02](br-sc19-02-visits-are-planned-before-the-legal-due-date.md)
