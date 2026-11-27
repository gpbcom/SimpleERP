🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 📦 F7 Purchasing and stock

# 📦 F7 Purchasing and stock

**Status:** ✅ specified

Build step: 4. Purchasing and stock.

## Summary

Buying, receiving, storing, replenishing, shipping, counting, tracing and valuing stock, with a supplier portal and rich
stock optimisation ([D266](../../06-decisions/f07-purchasing-and-stock/d266-purchasing-and-stock-scope.md) to
[D273](../../06-decisions/f07-purchasing-and-stock/d273-other-stock-features.md)).

## Scope

- **Purchasing:** requests, approval by amount and budget, orders, blanket orders, receipts, supplier invoices matched
  three ways.
- **Replenishment:** reordering rules, AI forecast, lead times, forecasted stock, the replenishment report,
  make-to-order, dropshipping, cross-docking.
- **Warehouse:** several warehouses and locations, routes in 1 to 3 steps, putaway and capacities, removal and
  reservation strategies, batch, cluster and wave picking, barcode.
- **Traceability:** lots, serials, expiry dates, recalls.
- **Valuation and counts:** costing methods, landed costs, cycle counts, stock analytics (aging, dead stock, turnover,
  ABC).
- **Other:** carriers, returns and scrap, consignment, kits, subcontracting, packages, units, variants, quality checks.
- **Supplier portal** (D17).
- **Benchmark additions (D305):** calls for tenders and supplier rating, trade between group companies, third-party
  warehouses and sales channels, repairs.
- **Gaps and improvements round ([D464](../../06-decisions/f07-purchasing-and-stock/d464-f07-gaps-and-improvements.md),
  2026-11-12):** supplier contracts and price agreements with rebates and renewal notice, supplier performance, approved
  catalogues and punch-out for employees' requests, explicit safety stock and min/max per item, packaging
  eco-contributions (EPR), dangerous goods with their safety data sheets, purchase carbon (scope 3), deeper receive and
  replenish flows, and the scanner screens' loading and offline states.

## Personas

[U04 Purchasing](../../01-users/personas/u04-purchasing.md),
[U15 Warehouse operator](../../01-users/personas/u15-warehouse-operator.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U02 Manager](../../01-users/personas/u02-manager.md),
[U13 Owner](../../01-users/personas/u13-owner.md), [U10 Supplier](../../01-users/personas/u10-supplier.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md),
[U01 Employee](../../01-users/personas/u01-employee.md), [U09 Customer](../../01-users/personas/u09-customer.md),
[U27 Quality manager](../../01-users/personas/u27-quality-manager.md).

## Out of scope

- Manufacturing orders and bills of materials: F12.
- Accounting entries: F8.
- The online shop's front: F11.

## Technical capabilities used

- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (carriers, supplier portals,
  e-invoicing)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md) (forecast, invoice reading)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)

## Build step

Step 4, Purchasing and stock, of the [roadmap](../../00-vision/roadmap/roadmap.md)
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

⬅️ [Customers and sales](../f06-customers-and-sales/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Accounting](../f08-accounting/README.md)
