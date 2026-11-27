🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F19-23 Maintenance covers upgrades within the plan

# 📏 BR-F19-23 Maintenance covers upgrades within the plan

**Status:** ✅ specified

## Statement

A maintenance plan covers the adaptation of the feature to every SimpleERP upgrade released while the plan is active
and the security fixes of the feature, and nothing else: a new function is a change that is ordered and priced apart.

## Why

Without a clear limit a plan turns into unlimited free development, and without a plan a feature paid once breaks at the
next upgrade. The owner asked for a maintenance plan
([D538](../../../06-decisions/f19-feature-factory/d538-benchmark-gaps-f19-feature-factory.md)).

## Examples

| Case | Result |
|---|---|
| A new version 2.4 breaks the feature | adapted before the customer's upgrade, no extra charge |
| A security fix found in the feature | applied and signed, no extra charge |
| A new column on the feature's report | a change, ordered apart |
| A feature on the monthly feature price | no plan needed: upkeep is included |
| A cancellation on the 10th | the plan runs to the end of the month |

## Applies to

- [UC-F19-30](../use-cases/07-catalogue-and-co-funding/uc-f19-30-subscribe-to-a-feature-maintenance-plan.md)
- [E-F19-19 Feature maintenance plan](../data/e-f19-19-feature-maintenance-plan.md)
- [E-F19-04 Generated plugin version](../data/e-f19-04-generated-plugin-version.md)
- [E-F19-03 Feature subscription](../data/e-f19-03-feature-subscription.md)

## Exceptions

None.

## Configurable

The monthly price and what the plan covers, by the SimpleERP team in the price catalogue.

## Open questions

None.

---

⬅️ [BR-F19-22](br-f19-22-pledges-are-charged-only-when-the-goal-is-met.md) · ⬆️ [Up](README.md)
