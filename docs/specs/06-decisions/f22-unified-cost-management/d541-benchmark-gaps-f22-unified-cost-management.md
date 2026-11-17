🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
💸 [Decisions: F22 Unified platform cost management](README.md) › 📜 D541 Benchmark gaps of F22 Unified cost management

# 📜 D541 Benchmark gaps of F22 Unified cost management

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found four cost
features that F22 did not cover: prepaid credit packs, a light register of software subscriptions, the carbon of compute
and routing of AI tasks to cheaper models. F22 already meters, budgets, forecasts and allocates the platform's costs;
these extend what is bought, what is tracked, what is reported and how the AI spend is cut. The subscription register
moves the line "the company's other software subscriptions" out of F22's out-of-scope list.

## Options

- G111 Prepaid credit packs: prepaid packs that top up inside the budget, or units billed one by one only.
- G112 SaaS subscriptions: a light register with seats and renewal dates, or no tracking of other tools.
- G113 Carbon of compute: carbon figures that carry their method and source, or no carbon figure.
- G114 Model routing savings: routing that respects a quality bar, or one cheapest model for every task.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F22 gets four use cases in one new flow, FL-F22-08, each with its screen and its rule, and three entities with their
lists; the carbon of compute has no entity of its own, since its figures are computed from the metered calls and the
machines. All at full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G111 | Prepaid credit packs | UC-F22-27: packs whose automatic top-up never goes beyond the budget | "Prepaid credit packs" |
| G112 | SaaS subscriptions | UC-F22-28: a register that flags unused seats before the notice date | "SaaS subscriptions" |
| G113 | Carbon of compute | UC-F22-29: carbon figures with their method, factor source and year | "Carbon of compute" |
| G114 | Model routing savings | UC-F22-30: routing rules that never go below a task's quality bar | "Model routing savings" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F22 Unified cost
management").

## Consequences

- G111 Prepaid credit packs:
  [UC-F22-27](../../02-functional/f22-unified-cost-management/use-cases/08-credits-saas-and-carbon/uc-f22-27-buy-prepaid-credit-packs.md),
  [S-F22-27](../../02-functional/f22-unified-cost-management/screens/08-credits-saas-and-carbon/s-f22-27-credit-packs.md)
  and
  [BR-F22-18](../../02-functional/f22-unified-cost-management/business-rules/br-f22-18-automatic-top-ups-stay-within-the-budget.md),
  with [E-F22-19](../../02-functional/f22-unified-cost-management/data/e-f22-19-credit-pack.md) Credit pack and its list
  [S-F22-L19](../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l19-credit-packs.md).
- G112 SaaS subscriptions:
  [UC-F22-28](../../02-functional/f22-unified-cost-management/use-cases/08-credits-saas-and-carbon/uc-f22-28-manage-saas-subscriptions.md),
  [S-F22-28](../../02-functional/f22-unified-cost-management/screens/08-credits-saas-and-carbon/s-f22-28-saas-subscriptions.md)
  and
  [BR-F22-19](../../02-functional/f22-unified-cost-management/business-rules/br-f22-19-unused-seats-are-flagged-before-renewal.md),
  with [E-F22-20](../../02-functional/f22-unified-cost-management/data/e-f22-20-saas-subscription.md) SaaS subscription
  and its list
  [S-F22-L20](../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l20-saas-subscriptions.md).
- G113 Carbon of compute:
  [UC-F22-29](../../02-functional/f22-unified-cost-management/use-cases/08-credits-saas-and-carbon/uc-f22-29-measure-the-carbon-of-compute.md),
  [S-F22-29](../../02-functional/f22-unified-cost-management/screens/08-credits-saas-and-carbon/s-f22-29-compute-carbon.md)
  and
  [BR-F22-20](../../02-functional/f22-unified-cost-management/business-rules/br-f22-20-carbon-figures-carry-their-method-and-source.md).
- G114 Model routing savings:
  [UC-F22-30](../../02-functional/f22-unified-cost-management/use-cases/08-credits-saas-and-carbon/uc-f22-30-route-ai-tasks-to-save-costs.md),
  [S-F22-30](../../02-functional/f22-unified-cost-management/screens/08-credits-saas-and-carbon/s-f22-30-model-routing.md)
  and
  [BR-F22-21](../../02-functional/f22-unified-cost-management/business-rules/br-f22-21-routing-never-goes-below-a-tasks-quality-bar.md),
  with [E-F22-21](../../02-functional/f22-unified-cost-management/data/e-f22-21-routing-rule.md) Routing rule and its
  list [S-F22-L21](../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l21-routing-rules.md).
- Drawn in [FL-F22-08](../../02-functional/f22-unified-cost-management/flows/fl-f22-08-credits-saas-and-carbon.md)
  Credits, SaaS subscriptions, carbon and routing.

## Related

- [FL-F22-08](../../02-functional/f22-unified-cost-management/flows/fl-f22-08-credits-saas-and-carbon.md)
- [D397 Unified platform cost management coverage](d397-cost-management-coverage.md)
- [D398 Budgets warn, then stop](d398-budgets-warn-then-stop.md)
- [D399 Hosted usage: quota, then per unit](d399-hosted-usage-billing.md)
- [D479](d479-f22-gaps-and-improvements.md)

---

⬅️ [D540](../f21-onboarding-and-modules/d540-benchmark-gaps-f21-onboarding-and-modules.md) · ⬆️ [Up](README.md) ·
➡️ [D542](../f23-what-if-simulation/d542-benchmark-gaps-f23-what-if-simulation.md)
