🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 💸 F22 Unified platform cost management

# 💸 F22 Unified platform cost management

**Status:** ✅ specified

Build step: 2. Platform.

## Summary

Every paid usage of the platform in one place (AI, paid connectors and data providers, scraping, subscriptions,
feature-factory features, the hosting): metered where it happens, budgeted with warnings and a stop that never blocks a
legal duty, estimated before large runs, forecast, allocated and matched with suppliers' invoices; in the hosted
edition, an included quota then units at a published price list
([D397](../../06-decisions/f22-unified-cost-management/d397-cost-management-coverage.md),
[D398](../../06-decisions/f22-unified-cost-management/d398-budgets-warn-then-stop.md),
[D399](../../06-decisions/f22-unified-cost-management/d399-hosted-usage-billing.md)).

## Scope

- **See:** all costs, per module, feature, provider, department, project or client; the AI assistant.
- **Set up:** providers and prices, own keys or the hosted quota.
- **Control:** budgets, warnings, the stop, approvals, estimates, live cost with a Stop button, anomalies.
- **Account:** allocation, invoice matching, forecasts, reports.
- **Bill:** the hosted quota and units, IT providers' re-billing, the hosting's own costs.
- **Currencies, compute and savings:** foreign-currency prices, self-hosted compute cost, savings recommendations, more
  KPIs, re-billing rules and client statements for IT providers (D479).

## Personas

[U13 Owner](../../01-users/personas/u13-owner.md), [U05 Accounting](../../01-users/personas/u05-accounting.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md),
[U02 Manager](../../01-users/personas/u02-manager.md),
[U11 IT provider administrator](../../01-users/personas/u11-provider-admin.md),
[U48 Hosting engineer](../../01-users/personas/u48-hosting-engineer.md).

## Out of scope

- Paying the company's other software subscriptions: F8 purchases and payments. Finding and following them is in
  scope since D541 ([UC-F22-28](use-cases/08-credits-saas-and-carbon/uc-f22-28-manage-saas-subscriptions.md)).
- Paying providers: F8 purchases and payments.

## Technical capabilities used

- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md) (AI metering)
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (connector and scraping
  metering)
- [T4 Plugin runtime](../../03-technical/t04-plugin-runtime/README.md) (subscriptions)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)

## Build step

Step 2, Platform, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | ✅ |
| 📏 |  | [Business rules](business-rules/README.md) | ✅ |
| 🗃️ |  | [Data](data/README.md) | ✅ |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | ✅ |

---

⬅️ [Onboarding and module activation](../f21-onboarding-and-modules/README.md) · ⬆️ [Up](../README.md) ·
➡️ [What-if simulation and impact](../f23-what-if-simulation/README.md)
