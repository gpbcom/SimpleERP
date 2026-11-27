🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🔮 F23 What-if simulation and impact

# 🔮 F23 What-if simulation and impact

**Status:** ✅ specified

Build step: 8. Growth and insight (Proposed).

## Summary

Answering "what happens if one or several of these elements change?": scenarios on a copy of the company's data, run
through the ERP's own rules, showing the impact on every area against the baseline forecast, with ranges, sensitivity,
comparison and counter-measures, built and explained by the AI assistant in plain words; nothing changes the live
company until a person applies an action ([D401](../../06-decisions/f23-what-if-simulation/d401-what-if-coverage.md),
[D402](../../06-decisions/f23-what-if-simulation/d402-impact-through-the-real-rules.md),
[D403](../../06-decisions/f23-what-if-simulation/d403-forecast-ranges-and-assistant.md)).

## Scope

- **Build:** the baseline, scenarios, changes to any element, ranges.
- **Run:** on a copy, with the real rules, from screens or the AI assistant.
- **Impact:** sales and margin, cash, statements, stock and purchases, production and capacity, staff and payroll, legal
  thresholds and taxes, platform costs.
- **Decide:** sensitivity, comparison, counter-measures, sharing.
- **Act and watch:** proposals approved by people, warnings when a real change hits the forecast.
- **Goals, financing and accuracy:** goal seeking, break-even, financing options and a bank pack, forecast accuracy and
  recalibration, sector drivers; budgets stay in F8 (UC-F8-19), scenarios in F23 (D480).

## Personas

[U13 Owner](../../01-users/personas/u13-owner.md), [U05 Accounting](../../01-users/personas/u05-accounting.md),
[U02 Manager](../../01-users/personas/u02-manager.md), [U31 Treasurer](../../01-users/personas/u31-treasurer.md),
[U21 Production planner](../../01-users/personas/u21-production-planner.md),
[U06 HR](../../01-users/personas/u06-hr.md), [U03 Sales](../../01-users/personas/u03-sales.md),
[U04 Purchasing](../../01-users/personas/u04-purchasing.md),
[U08 External accountant](../../01-users/personas/u08-external-accountant.md).

## Out of scope

- Applying changes to the live company: each capability's own approvals.
- Decisions about named people (BR-F23-12).

## Technical capabilities used

- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)
- [T1 Companies and data isolation](../../03-technical/t01-companies-and-data-isolation/README.md) (copies)
- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md) (the country pack's values by date)
- [T6 MCP and A2A gateway](../../03-technical/t06-mcp-and-a2a-gateway/README.md) (the AI assistant's tools)

## Build step

Step 8, Growth and insight, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)) (Proposed): in V1, like everything the
specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | 🔄 |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [Unified platform cost management](../f22-unified-cost-management/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Integrations hub](../f24-integrations-hub/README.md)
