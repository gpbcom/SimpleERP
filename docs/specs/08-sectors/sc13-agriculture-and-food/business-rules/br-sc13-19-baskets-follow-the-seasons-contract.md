🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🌾 [SC13 Agriculture and food](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC13-19 Baskets follow the season's contract

# 📏 BR-SC13-19 Baskets follow the season's contract

**Status:** 🔄 waiting for the owner

## Statement

A week's baskets are the baskets of the contracts that are Active and not in absence for that week, and the instalments
of a contract add up exactly to the price of the season. A member declares an absence or a swap before the cut-off of
the pick-up, and not after.

## Why

Baskets packed for absent members are wasted and a price that does not match the instalments creates disputes. The owner
asked for basket subscriptions ([D557](../../../06-decisions/sectors/d557-benchmark-gaps-sc13-agriculture-and-food.md)).
(Proposed) The France-pack rule is written later.

## Examples

| Case | Result |
|---|---|
| 24 weeks at 15.00 EUR | 360.00 EUR over the instalments |
| Absence declared before the cut-off | no basket for that week |
| Absence declared after the cut-off | refused, the basket is packed |
| Member joining at week 9 | the price covers weeks 9 to 24 only |
| Contract Pending | no basket planned |

## Applies to

- [UC-SC13-24](../use-cases/06-vineyards-contractors-and-cooperatives/uc-sc13-24-sell-basket-subscriptions.md)
- [E-SC13-20 Basket subscription](../data/e-sc13-20-basket-subscription.md)
- [E-F6-07](../../../02-functional/f06-customers-and-sales/data/e-f06-07-subscription-contract.md)

## Exceptions

None.

## Configurable

The cut-off time, the pick-up points and the sizes, by the farmer.

## Open questions

None.

---

⬅️ [BR-SC13-18 Rebates follow the members' deliveries](br-sc13-18-rebates-follow-the-members-deliveries.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC13-20 Fellings follow the management plan](br-sc13-20-fellings-follow-the-management-plan.md)
