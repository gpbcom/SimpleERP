🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🔮 TC-22 Simulating the whole company on copies

# 🔮 TC-22 Simulating the whole company on copies

**Status:** ✅ listed for the technical interviews

## Challenge

Run what-if scenarios on a copy or overlay of a company's data through the ERP's own rules (sales, stock, planning,
payroll, accounting), with ranges drawn hundreds of times, and keep the figures exact and private.

## Raised by

- [F23 What-if simulation and impact](../../02-functional/f23-what-if-simulation/README.md)
- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [F8 Accounting](../../02-functional/f08-accounting/README.md)
- [F12 Manufacturing (plugin)](../../02-functional/f12-manufacturing/README.md)
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md)
- [F22 Unified platform cost management](../../02-functional/f22-unified-cost-management/README.md)

## Why it is hard

- The real rules were written to change live data, not to run a thousand times on a copy.
- A copy of a large company is heavy; an overlay must never leak into the live data.
- Ranges multiply computing time; the AI assistant must not invent figures the simulation did not compute.
- Each reader may see only some figures.

## Already decided

- [D293](../../06-decisions/country-packs/d293-capabilities-take-legal-rules-from-the-pack.md) Capabilities take legal
  rules from the country pack
- [D401](../../06-decisions/f23-what-if-simulation/d401-what-if-coverage.md) What-if simulation coverage
- [D402](../../06-decisions/f23-what-if-simulation/d402-impact-through-the-real-rules.md) Impact through the ERP's own
  rules
- [D403](../../06-decisions/f23-what-if-simulation/d403-forecast-ranges-and-assistant.md) Baseline, ranges, and the
  AI assistant

## Options to weigh

- Rules as pure functions that run on live data and on a scenario overlay alike.
- Copy-on-write snapshots, or scenario overlays in the same database.
- Monte Carlo runs as background jobs on workers, with a time budget and partial results.

## Settled in

- 19a Architecture and scalability ([chapter](../../../technical/architecture/architecture.md))
- 19b Performance and capacity ([chapter](../../../technical/infrastructure/performance-and-capacity.md))
- 19c Storage ([chapter](../../../technical/data/storage.md))
- 19i AI operations ([chapter](../../../technical/operations/ai-operations.md))
- Then the technical capabilities: [T1 Companies and data isolation](../t01-companies-and-data-isolation/README.md),
  [T7 AI providers and models](../t07-ai-providers-and-models/README.md).

## Questions for the interview

- How long may a scenario run before it moves to the background?
- Must scenarios survive upgrades of the rules, or be re-run?

---

⬅️ [TC-21 Metering every paid call, and stopping on a budget](tc-21-metering-every-paid-call.md) · ⬆️ [Up](README.md) ·
➡️ [TC-23 Many connectors, connected in few steps, kept working](tc-23-many-connectors-few-steps.md)
