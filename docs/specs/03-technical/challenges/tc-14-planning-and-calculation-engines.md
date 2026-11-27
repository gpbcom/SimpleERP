🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🧮 TC-14 Planning and calculation engines

# 🧮 TC-14 Planning and calculation engines

**Status:** ✅ listed for the technical interviews

## Challenge

Plan rounds, crews, production, deliveries and staff with an optimiser, and compute payroll, taxes and surcharges
exactly, with values from the country pack.

## Raised by

- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md)
- [F12 Manufacturing (plugin)](../../02-functional/f12-manufacturing/README.md)
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md)
- [SC04 Home care](../../08-sectors/sc04-home-care/README.md)
- [SC07 Transport and logistics](../../08-sectors/sc07-transport/README.md)

## Why it is hard

- Optimisation problems grow fast with the number of people, places and time slots.
- Payroll must be exact to the cent and explainable, with rules that change each year.
- Long computations must not block screens.

## Already decided

- [D293](../../06-decisions/country-packs/d293-capabilities-take-legal-rules-from-the-pack.md) Capabilities take legal
  rules from the country pack

## Options to weigh

- A constraint solver as a separate worker, with time limits and a best-so-far answer.
- Payroll as a versioned calculation with test cases per country-pack version.
- Background jobs with progress and a Stop button.

## Settled in

- 19a Architecture and scalability ([chapter](../../../technical/architecture/architecture.md))
- 19b Performance and capacity ([chapter](../../../technical/infrastructure/performance-and-capacity.md))
- Then the technical capabilities: [T4 Plugin runtime](../t04-plugin-runtime/README.md) (REQ-T04-08),
  [T11 Legal corpora](../t11-legal-corpora/README.md) (calculations per pack version, REQ-T11-06); T9 was named here
  before the review of 2026-11-12.

## Questions for the interview

- What size of plan must answer within a minute?
- Is a third-party payroll engine acceptable, or must it be in SimpleERP?

---

⬅️ [TC-13 Hosted operations helped by an AI](tc-13-operations-run-by-an-ai.md) · ⬆️ [Up](README.md) ·
➡️ [TC-15 Large lists, reports and dashboards](tc-15-large-data-reports-and-lists.md)
