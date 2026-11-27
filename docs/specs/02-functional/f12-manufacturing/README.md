🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🏭 F12 Manufacturing (plugin)

# 🏭 F12 Manufacturing (plugin)

**Status:** ✅ specified

Build step: 7. Plugins and the plugin store.

## Summary

Making products: bills of materials and routings, planning, manufacturing orders, the shop-floor tablet, lots and
serials, quality, maintenance, subcontracting, engineering changes, unbuild and repair, costs, machine data and OEE,
product compliance, safety registers and waste, covering everything the benchmark offers
([D312](../../06-decisions/f12-manufacturing/d312-manufacturing-coverage.md),
[D314](../../06-decisions/f12-manufacturing/d314-machines-through-connectors.md)).

## Scope

- **Products:** bills of materials, kits, by-products, variants, versions; work centres and routings; engineering
  changes (PLM).
- **Planning:** master plan, material requirements, capacity, proposals, picking for production.
- **Making:** manufacturing and work orders, the shop-floor tablet, consumption, lots and serials, unbuild, rework and
  repair.
- **Quality and maintenance:** control points, non-conformities, preventive, corrective and legal checks.
- **Subcontracting and costs:** components at the subcontractor, standard and actual costs, variances to accounting.
- **Machines:** signals through T12 connectors, stops, OEE (D314).
- **Compliance:** product compliance files, the risk assessment, the safety register, the waste register, classified
  installations.
- **Gaps and improvements round ([D469](../../06-decisions/f12-manufacturing/d469-f12-gaps-and-improvements.md),
  2026-11-12):** recipes and batch production (shared capability,
  [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md)), calibration of measuring equipment, operator
  qualifications per work centre, finite-capacity scheduling, FMEA and statistical process control, energy per
  operation, the digital product passport, the shop-floor tablet's loading and offline states, month-end
  work-in-progress valuation, versioned work instructions with operator acknowledgement, and deeper flows.

## Personas

[U21 Production planner](../../01-users/personas/u21-production-planner.md),
[U20 Production operator](../../01-users/personas/u20-production-operator.md),
[U15 Warehouse operator](../../01-users/personas/u15-warehouse-operator.md),
[U04 Purchasing](../../01-users/personas/u04-purchasing.md), [U02 Manager](../../01-users/personas/u02-manager.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md),
[U27 Quality manager](../../01-users/personas/u27-quality-manager.md),
[U06 Human resources](../../01-users/personas/u06-hr.md), [U09 Customer](../../01-users/personas/u09-customer.md),
[U19 Kitchen staff](../../01-users/personas/u19-kitchen-staff.md), [U40 Farmer](../../01-users/personas/u40-farmer.md).

## Out of scope

- Stock moves and purchases themselves: F7 (F12 creates them).
- Sales and delivery dates: F6.
- People's time and shifts: F9.
- Accounting entries: F8 (F12 sends them).

## Technical capabilities used

- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (machines, sensors, scales,
  printers)
- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md) (the country pack)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md) (assistant at the machine)

## Build step

Step 7, Plugins and the plugin store, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | ✅ |
| 📏 |  | [Business rules](business-rules/README.md) | ✅ |
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

⬅️ [Online shop (plugin)](../f11-online-shop/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Payroll (plugin)](../f13-payroll/README.md)
