🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F22-15 Self-hosted compute has a cost

# 📏 BR-F22-15 Self-hosted compute has a cost

**Status:** 🔄 waiting for the owner

## Statement

The machines running local models (D440) are costed per hour from their purchase price spread over their life and the
electricity they use; this cost is allocated to the features that used them, like any provider.

## Why

Local models are not free (D479); the owner compares them with paid providers.

## Examples

| Case | Result |
|---|---|
| Server 6 000.00 EUR over 36 months, 400 W at 0.25 EUR per kWh | passes: 0.33 EUR per hour (Proposed) computed |
| Feature using 60 % of the GPU hours | passes: 60 % of the cost |
| Machine with no purchase price | passes: electricity only, flagged |

## Applies to

- [UC-F22-22 Count the cost of self-hosted compute](../use-cases/01-see-and-set-up/uc-f22-22-count-the-cost-of-self-hosted-compute.md)
- [UC-F22-01 See all platform costs in one place](../use-cases/01-see-and-set-up/uc-f22-01-see-all-platform-costs-in-one-place.md)
- [UC-F22-14 Allocate costs to accounts and projects](../use-cases/04-accounting/uc-f22-14-allocate-costs-to-accounts-and-projects.md)
- [UC-F22-17 Follow the hosting's own platform costs](../use-cases/05-billing/uc-f22-17-follow-the-hosting-s-own-platform-costs.md)

## Exceptions

Machines shared with other uses are counted for their share only.

## Configurable

Purchase price, life, power and electricity price per machine.

## Open questions

None.

---

⬅️ [BR-F22-14 Foreign prices converted at the day's rate](br-f22-14-foreign-prices-converted-at-the-days-rate.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F22-16](br-f22-16-recommendations-show-their-saving-and-never-act-alone.md)
