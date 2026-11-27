🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-02 Visits are planned before the legal due date

# 📏 BR-SC19-02 Visits are planned before the legal due date

**Status:** 🔄 waiting for the owner

## Statement

A visit is planned so that its window ends before the legal due date of its check-up. A visit that cannot meet that date
is marked Overdue and the dispatcher is warned at once. A technician without the qualification the check-up needs is
never proposed.

## Why

The customer is responsible for the check-up and the company must be able to show it offered and did it in time
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). (Proposed) The France-pack
rule is written later.

## Examples

| Case | Result |
|---|---|
| Due date 30 April | the window ends on 15 April |
| Due date already past | Overdue, warning to the dispatcher |
| Technician without the qualification | not proposed |
| Customer asks for a day after the window | refused, the nearest day inside it is offered |
| Two visits a year | spaced half a year apart |

## Applies to

- [UC-SC19-02](../use-cases/01-maintenance-contracts/uc-sc19-02-generate-recurring-visits.md)
- [E-SC19-02 Planned visit](../data/e-sc19-02-planned-visit.md)
- [E-SC19-01 Maintenance contract](../data/e-sc19-01-maintenance-contract.md)
- [E-F9-12](../../../02-functional/f09-hr-and-projects/data/e-f09-12-certification.md)

## Exceptions

None.

## Configurable

The margin before the due date in days, set by the owner.

## Open questions

None.

---

⬅️ [BR-SC19-01 Contracts list the legal yearly check-ups](br-sc19-01-contracts-list-the-legal-yearly-check-ups.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC19-03 Certificates are given to the customer](br-sc19-03-certificates-are-given-to-the-customer.md)
