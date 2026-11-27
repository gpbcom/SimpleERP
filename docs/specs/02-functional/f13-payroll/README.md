🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 💶 F13 Payroll (plugin)

# 💶 F13 Payroll (plugin)

**Status:** ✅ specified

Build step: 7. Plugins and the plugin store.

## Summary

Paying employees: payroll set-up, pay inputs from F9, gross to net with collective-agreement rules and withholding tax,
the pay-run check, clarified payslips, payments, the monthly social declaration, corrections, contributions, accounting
entries, sick leave, end of contract, simulations, benefits, yearly reports and rate updates, covering everything the
benchmark offers ([D365](../../06-decisions/f13-payroll/d365-payroll-coverage.md)).

## Scope

- **Set-up:** establishments, contribution accounts, collective agreements, employees' pay.
- **Pay run:** inputs, gross to net, agreement rules, withholding, anomalies, approval, payslips.
- **Declarations and payments:** transfers, the monthly social declaration, contributions, accounting, corrections.
- **Events:** sick leave, end of contract, simulations, benefits.
- **Rules:** rates and ceilings from the country pack, dated by period; yearly reports.
- **Schemes and special contracts:** health and provident schemes, apprentices, interns, officers, intermittent
  performers, farm workers under the MSA (D470).
- **Deductions and savings:** garnishments, advances, profit-sharing and employee savings, paid-leave pay valuation
  (D470).
- **Agreement families:** hotels and restaurants, home help, Syntec, construction; payroll cost by site, project and
  axis (D470).

## Personas

[U45 Payroll officer](../../01-users/personas/u45-payroll-officer.md), [U06 HR](../../01-users/personas/u06-hr.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U01 Employee](../../01-users/personas/u01-employee.md),
[U13 Owner](../../01-users/personas/u13-owner.md), [U07 Administrator](../../01-users/personas/u07-administrator.md),
[U40 Farmer](../../01-users/personas/u40-farmer.md) (farm workers under the MSA),
[U43 Event producer](../../01-users/personas/u43-event-producer.md) (intermittent performers).

## Out of scope

- Contracts, time and leave themselves: F9 (F13 reads them).
- Accounting itself: F8.

## Technical capabilities used

- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md) (the country pack's rates and rules)
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (declaration filing, banks)

## Build step

Step 7, Plugins and the plugin store, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the specifications hold.

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

⬅️ [Manufacturing (plugin)](../f12-manufacturing/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Plugin store](../f14-plugin-store/README.md)
