🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F22-18 Automatic top-ups stay within the budget

# 📏 BR-F22-18 Automatic top-ups stay within the budget

**Status:** 🔄 waiting for the owner

## Statement

An automatic top-up buys a pack only when the price fits in the budget left at the pack's level for the period, and
never more packs than the monthly maximum set for it; when it does not fit, nothing is bought and the owner is told.

## Why

A top-up is spending: letting it run past the budget would defeat the warn-then-stop rule of
[BR-F22-06](br-f22-06-stop-at-budget-legal-duties-kept.md). The owner asked for prepaid credit packs
([D541](../../../06-decisions/f22-unified-cost-management/d541-benchmark-gaps-f22-unified-cost-management.md)).

## Examples

| Case | Result |
|---|---|
| Budget left 120 EUR, pack 40 EUR | the top-up is bought |
| Budget left 20 EUR, pack 40 EUR | nothing is bought, the owner is told |
| Two packs already bought this month, maximum two | no third pack |
| A manual purchase by the administrator above the budget | refused until the budget is raised ([UC-F22-09](../use-cases/02-budgets-and-stops/uc-f22-09-raise-a-budget-or-approve-a-run.md)) |
| A pack with units left at expiry | the units are lost, as the terms shown at purchase say |

## Applies to

- [UC-F22-27](../use-cases/08-credits-saas-and-carbon/uc-f22-27-buy-prepaid-credit-packs.md)
- [E-F22-19 Credit pack](../data/e-f22-19-credit-pack.md)
- [BR-F22-06 Stop at the budget, legal duties kept](br-f22-06-stop-at-budget-legal-duties-kept.md)
- [E-F22-06 Cost budget](../data/e-f22-06-cost-budget.md)

## Exceptions

None: a purchase a legal duty needs does not exist, since packs only prepay usage.

## Configurable

The owner's approval amount, the threshold and the monthly maximum of each pack.

## Open questions

None.

---

⬅️ [BR-F22-17 Re-billing rules per client](br-f22-17-re-billing-rules-per-client.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F22-19 Unused seats are flagged before renewal](br-f22-19-unused-seats-are-flagged-before-renewal.md)
