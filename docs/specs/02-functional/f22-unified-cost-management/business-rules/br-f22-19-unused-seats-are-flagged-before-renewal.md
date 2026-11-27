🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F22-19 Unused seats are flagged before renewal

# 📏 BR-F22-19 Unused seats are flagged before renewal

**Status:** ✅ specified

## Statement

A subscription with seats paid above seats used is flagged to the administrator at least 30 days before its notice date,
once per renewal, with the number of unused seats and what they cost per year.

## Why

The saving exists only if the company can still act: after the notice date the renewal is due. The owner asked for light
subscription management
([D541](../../../06-decisions/f22-unified-cost-management/d541-benchmark-gaps-f22-unified-cost-management.md)).

## Examples

| Case | Result |
|---|---|
| 20 seats paid, 14 used, notice date in 40 days | flagged: 6 seats, 864 EUR a year |
| 20 seats paid, 20 used | not flagged |
| Notice date in 10 days and the flag not yet raised | flagged at once, marked late |
| Seats used declared by hand 4 months ago | flagged with the note that the figure is old |
| A flag dismissed by the administrator | not raised again for this renewal |

## Applies to

- [UC-F22-28](../use-cases/08-credits-saas-and-carbon/uc-f22-28-manage-saas-subscriptions.md)
- [E-F22-20 SaaS subscription](../data/e-f22-20-saas-subscription.md)
- [E-F22-06 Cost budget](../data/e-f22-06-cost-budget.md)

## Exceptions

A subscription marked as fixed price with no seats is never flagged.

## Configurable

The number of days before the notice date (30 by default), by the administrator.

## Open questions

None.

---

⬅️ [BR-F22-18 Automatic top-ups stay within the budget](br-f22-18-automatic-top-ups-stay-within-the-budget.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F22-20 Carbon figures carry their method and source](br-f22-20-carbon-figures-carry-their-method-and-source.md)
