🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🏭 [Decisions: F19 Feature factory (hosted edition)](README.md) › 📜 D538 Benchmark gaps of F19 Feature factory

# 📜 D538 Benchmark gaps of F19 Feature factory

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found four gaps in
the feature factory: no sight of similar features before ordering, no fixed-price small changes, no way to share the
cost of a feature, and no plan to keep a feature paid once working across upgrades. F19 already quotes, generates, signs
and promotes features at 300 EUR a month; these add choice before and care after.

## Options

- G99 See similar features: similar features shown before any quote, or the quote straight from the request.
- G100 Fixed-price catalogue: a fixed-price catalogue of small changes, or every change quoted.
- G101 Co-funded features: co-funded features charged only when the goal is met, or each feature paid by its requester
  alone.
- G102 Feature maintenance plan: a monthly maintenance plan for features paid once, or upkeep only on the monthly
  feature price.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F19 gets four use cases in one new flow, FL-F19-07, each with its screen and its rule, and three entities with their
lists; the similar-features view has no entity of its own, since it reads the stores and records its choice in the
request's audit trail. The monthly feature price of D390 is unchanged. All at full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G99 | See similar features | UC-F19-27: similar features shown before any quote | "See similar features" |
| G100 | Fixed-price catalogue | UC-F19-28: fixed-price changes that keep their price | "Fixed-price catalogue" |
| G101 | Co-funded features | UC-F19-29: pledges charged only when the goal is met | "Co-funded features" |
| G102 | Feature maintenance plan | UC-F19-30: a maintenance plan that covers upgrades within the plan | "Feature maintenance plan" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F19 Feature factory").

## Consequences

- G99 See similar features:
  [UC-F19-27](../../02-functional/f19-feature-factory/use-cases/07-catalogue-and-co-funding/uc-f19-27-see-similar-features-before-ordering.md),
  [S-F19-26](../../02-functional/f19-feature-factory/screens/07-catalogue-and-co-funding/s-f19-26-similar-features.md)
  and
  [BR-F19-20](../../02-functional/f19-feature-factory/business-rules/br-f19-20-similar-features-are-shown-before-any-quote.md).
- G100 Fixed-price catalogue:
  [UC-F19-28](../../02-functional/f19-feature-factory/use-cases/07-catalogue-and-co-funding/uc-f19-28-order-a-fixed-price-change.md),
  [S-F19-27](../../02-functional/f19-feature-factory/screens/07-catalogue-and-co-funding/s-f19-27-fixed-price-catalogue.md)
  and
  [BR-F19-21](../../02-functional/f19-feature-factory/business-rules/br-f19-21-fixed-price-changes-keep-their-price.md),
  with [E-F19-17](../../02-functional/f19-feature-factory/data/e-f19-17-catalogue-change.md) Catalogue change and its
  list [S-F19-L17](../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l17-catalogue-changes.md).
- G101 Co-funded features:
  [UC-F19-29](../../02-functional/f19-feature-factory/use-cases/07-catalogue-and-co-funding/uc-f19-29-co-fund-a-feature.md),
  [S-F19-28](../../02-functional/f19-feature-factory/screens/07-catalogue-and-co-funding/s-f19-28-co-funding.md) and
  [BR-F19-22](../../02-functional/f19-feature-factory/business-rules/br-f19-22-pledges-are-charged-only-when-the-goal-is-met.md),
  with [E-F19-18](../../02-functional/f19-feature-factory/data/e-f19-18-funding-pledge.md) Funding pledge and its list
  [S-F19-L18](../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l18-funding-pledges.md).
- G102 Feature maintenance plan:
  [UC-F19-30](../../02-functional/f19-feature-factory/use-cases/07-catalogue-and-co-funding/uc-f19-30-subscribe-to-a-feature-maintenance-plan.md),
  [S-F19-29](../../02-functional/f19-feature-factory/screens/07-catalogue-and-co-funding/s-f19-29-maintenance-plan.md)
  and
  [BR-F19-23](../../02-functional/f19-feature-factory/business-rules/br-f19-23-maintenance-covers-upgrades-within-the-plan.md),
  with [E-F19-19](../../02-functional/f19-feature-factory/data/e-f19-19-feature-maintenance-plan.md) Maintenance plan
  and its list
  [S-F19-L19](../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l19-feature-maintenance-plans.md).
- Drawn in [FL-F19-07](../../02-functional/f19-feature-factory/flows/fl-f19-07-catalogue-and-co-funding.md) Similar
  features, catalogue, co-funding and maintenance.

## Related

- [FL-F19-07](../../02-functional/f19-feature-factory/flows/fl-f19-07-catalogue-and-co-funding.md)
- [D389 Generated features are plugins](d389-generated-features-are-plugins.md)
- [D390 Feature price and promotion credit](d390-feature-price-and-promotion-credit.md)
- [D476](d476-f19-gaps-and-improvements.md)
- [BR-F19-09](../../02-functional/f19-feature-factory/business-rules/br-f19-09-price-excludes-vat.md)
- [BR-F19-16](../../02-functional/f19-feature-factory/business-rules/br-f19-16-nothing-charged-without-an-accepted-feature.md)

---

⬅️ [D537](../f18-hosted-websites-and-domains/d537-benchmark-gaps-f18-hosted-websites-and-domains.md) ·
⬆️ [Up](README.md) · ➡️ [D539](../f20-hosted-support-assistant/d539-benchmark-gaps-f20-hosted-support-assistant.md)
