🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) ›
💸 TC-21 Metering every paid call, and stopping on a budget

# 💸 TC-21 Metering every paid call, and stopping on a budget

**Status:** ✅ listed for the technical interviews

## Challenge

Record the cost of every paid call (AI, connectors, data providers, scraping) where it is made, check the budgets before
each call, stop new paid calls at a budget without ever blocking a legal duty, and bill the hosted quota and its units.

## Raised by

- [F22 Unified platform cost management](../../02-functional/f22-unified-cost-management/README.md)
- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [F16 Customer support agents](../../02-functional/f16-customer-support-agents/README.md)
- [F17 Competitive analysis](../../02-functional/f17-competitive-analysis/README.md)
- [F19 Feature factory (hosted edition)](../../02-functional/f19-feature-factory/README.md)
- [T7 AI providers and models](../t07-ai-providers-and-models/README.md)
- [T12 Connectors and scrapers](../t12-connectors-and-scrapers/README.md)

## Why it is hard

- Paid calls are made in many services, by people, workflows and agents running on their own.
- The budget check sits on the path of every call: it must be fast and still exact when calls run in parallel.
- Prices change; a past cost must not.
- A stop must never cut an e-invoice or a payroll declaration.

## Already decided

- [D397](../../06-decisions/f22-unified-cost-management/d397-cost-management-coverage.md) Unified platform cost
  management coverage
- [D398](../../06-decisions/f22-unified-cost-management/d398-budgets-warn-then-stop.md) Budgets warn, then stop
- [D399](../../06-decisions/f22-unified-cost-management/d399-hosted-usage-billing.md) Hosted usage: quota, then per unit

## Options to weigh

- One metering library or gateway that every paid call goes through, against metering in each service.
- Budget counters reserved before a call and settled after it.
- Usage events into the reporting store, matched later with providers' invoices.

## Settled in

- 19a Architecture and scalability ([chapter](../../../technical/architecture/architecture.md))
- 19b Performance and capacity ([chapter](../../../technical/infrastructure/performance-and-capacity.md))
- 19i AI operations ([chapter](../../../technical/operations/ai-operations.md))
- 19d API design and contracts ([chapter](../../../technical/interfaces/api.md))
- Then the technical capabilities: [T7 AI providers and models](../t07-ai-providers-and-models/README.md),
  [T12 Connectors and scrapers](../t12-connectors-and-scrapers/README.md).

## Questions for the interview

- Must the budget check hold exactly under parallel calls, or may it overrun by one call?
- Which calls count as legal duties, and who lists them per country?

---

⬅️ [TC-20 Testing a very wide product](tc-20-testing-a-very-wide-product.md) · ⬆️ [Up](README.md) ·
➡️ [TC-22 Simulating the whole company on copies](tc-22-simulation-on-copies.md)
