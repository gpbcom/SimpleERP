🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🚛 SC07 Transport and logistics

# 🚛 SC07 Transport and logistics

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D335 to D337.

## Summary

What hauliers and logistics companies add: orders, trips and routes, fleet and drivers, consignment notes, the driver's
phone, proofs of delivery, tachograph and driving times, dangerous goods, fuel and tolls, maintenance, chartering,
billing with surcharges, warehouse logistics for clients, the client portal, CO2 information, margins and cabotage
([D335](../../06-decisions/sectors/d335-transport-sector-coverage.md)).

## Profile

Road hauliers, couriers, removal companies and logistics providers, from 1 truck to large fleets, drivers on the road
and often offline.

## Personas

[U29 Dispatcher](../../01-users/personas/u29-dispatcher.md), [U30 Driver](../../01-users/personas/u30-driver.md),
[U15 Warehouse operator](../../01-users/personas/u15-warehouse-operator.md),
[U03 Sales](../../01-users/personas/u03-sales.md), [U04 Purchasing](../../01-users/personas/u04-purchasing.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U06 HR](../../01-users/personas/u06-hr.md),
[U13 Owner](../../01-users/personas/u13-owner.md), [U09 Customer](../../01-users/personas/u09-customer.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users, depots as sites, client portal accounts.
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types
  and the shared offline phone forms for drivers,
  [UC-F2-22](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions on the fleet
  ([UC-SC07-20](use-cases/01-orders-and-planning/uc-sc07-20-ask-the-assistant-about-the-fleet.md)).
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): quotes, orders, invoices and the
  client portal,
  [UC-F6-11](../../02-functional/f06-customers-and-sales/use-cases/02-quote-to-order/uc-f06-11-use-the-customer-portal.md).
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md): the warehouse for clients, parts
  and fuel.
- [F8 Accounting](../../02-functional/f08-accounting/README.md): fuel and toll posting, margins, the sustainability
  figures.
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): drivers' documents and training, the fleet,
  [UC-F9-12](../../02-functional/f09-hr-and-projects/use-cases/05-workplace-services/uc-f09-12-manage-the-fleet.md), the
  shared rounds optimiser,
  [UC-F9-30](../../02-functional/f09-hr-and-projects/use-cases/11-capacity-rounds-and-partners/uc-f09-30-plan-rounds-and-optimise-routes.md).
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md): drivers' hours, nights away and allowances as pay
  inputs,
  [UC-F13-03](../../02-functional/f13-payroll/use-cases/02-monthly-pay-run/uc-f13-03-collect-pay-inputs-from-f9.md).
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F2-22 Fill a form offline on the phone](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  [UC-F9-30 Plan rounds and optimise routes](../../02-functional/f09-hr-and-projects/use-cases/11-capacity-rounds-and-partners/uc-f09-30-plan-rounds-and-optimise-routes.md).

## Technical capabilities used

- [T1 Companies and data isolation](../../03-technical/t01-companies-and-data-isolation/README.md)
- [T2 Identity and access](../../03-technical/t02-identity-and-access/README.md)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)
- [T4 Plugin runtime](../../03-technical/t04-plugin-runtime/README.md) (the sector pack)
- [T5 API and webhooks](../../03-technical/t05-api-and-webhooks/README.md)
- [T6 MCP and A2A gateway](../../03-technical/t06-mcp-and-a2a-gateway/README.md)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md) (the AI assistant)
- [T8 RAG platform](../../03-technical/t08-rag-platform/README.md)
- [T9 Install, backups and updates](../../03-technical/t09-install-backups-and-updates/README.md)
- [T10 Translations and notifications](../../03-technical/t10-translations-and-notifications/README.md)
- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md) (the country pack's rules)
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (carriers, telematics)

Also: offline drivers' phones (REQ-T05-07); planning (REQ-T04-08).

## Example company

- [Transport and logistics](../../01-users/example-companies/transport.md)

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | 🔄 |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🎁 |  | [Sector pack](sector-pack.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [Restaurant and hospitality](../sc06-hospitality/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Non-profit association](../sc08-non-profit/README.md)
