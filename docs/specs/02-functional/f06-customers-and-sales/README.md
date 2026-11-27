🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🛒 F6 Customers and sales

# 🛒 F6 Customers and sales

**Status:** ✅ specified

Build step: 3. Customers and sales.

## Summary

The whole sales cycle, from the first contact to the last payment, and a portal where customers do everything themselves
([D251](../../06-decisions/f06-customers-and-sales/d251-sales-cycle.md) to
[D254](../../06-decisions/f06-customers-and-sales/d254-quote-acceptance.md)).

## Scope

- **Leads and pipeline:** contacts, companies, leads, opportunities by stage, activities, forecasts.
- **Quotes and orders:** products and services, price lists, discounts, options, versions; acceptance by click or
  e-signature; orders and work follow-up.
- **Invoices and payments:** invoices, deposits, credit notes, payments, reminders and dunning; e-invoicing formats
  (D118) and the platform of Q13.
- **Subscriptions:** recurring contracts, billing, renewals, price indexation.
- **Portal:** accept, sign, pay, download, follow, send requests, update details (D17, D252).
- **Payments:** through providers the company picks, no card number in SimpleERP (D253).
- **Benchmark additions (D304):** lead scoring, assignment and enrichment; product configurator; rental; usage,
  commitment and milestone billing.
- **Gaps and improvements round ([D463](../../06-decisions/f06-customers-and-sales/d463-f06-gaps-and-improvements.md),
  2026-11-12):** account hierarchy with its activity timeline and emails, credit limits and credit hold, public buyers
  through Chorus Pro, multi-payer invoicing with funders and caps and commissions and targets (shared capabilities,
  [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md)), offline order taking on the road, pro-forma
  invoices and statements of account, instalment plans and disputed invoices, sales and margin reports, and more and
  deeper flows.

## Personas

[U03 Sales](../../01-users/personas/u03-sales.md), [U02 Manager](../../01-users/personas/u02-manager.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md),
[U16 Office worker](../../01-users/personas/u16-office-worker.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U09 Customer](../../01-users/personas/u09-customer.md),
[U15 Warehouse operator](../../01-users/personas/u15-warehouse-operator.md),
[U41 Customer success manager](../../01-users/personas/u41-customer-success-manager.md),
[U25 Care coordinator](../../01-users/personas/u25-care-coordinator.md),
[U38 Training coordinator](../../01-users/personas/u38-training-coordinator.md),
[U42 Sales representative](../../01-users/personas/u42-sales-representative.md),
[U23 Store manager](../../01-users/personas/u23-store-manager.md).

## Out of scope

- Accounting entries: F8 (F6 hands invoices and payments over).
- Support requests' resolution: F16.
- The online shop: F11.

## Technical capabilities used

- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (payments, e-signature,
  e-invoicing)
- [T2 Identity and access](../../03-technical/t02-identity-and-access/README.md) (portal)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)

## Build step

Step 3, Customers and sales, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | 🔄 |
| 🔀 |  | [Flows](flows/README.md) | 🔄 |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | 🔄 |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [Social media](../f05-social-media/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Purchasing and stock](../f07-purchasing-and-stock/README.md)
