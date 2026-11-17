🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 📦 SC15 Wholesale and distribution

# 📦 SC15 Wholesale and distribution

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D359 to D361.

## Summary

What wholesalers and distributors add to F6 and F7: price agreements and rebates, the yearly agreement with retailers,
EDI, rep and portal orders, back-orders and drop-shipping, waves, pallets and returns, supplier funds, imports and EU
statistics, reps' visits, margins and credit limits
([D359](../../06-decisions/sectors/d359-wholesale-sector-coverage.md)).

## Profile

Wholesalers and distributors of food, building, industrial and consumer goods, with reps on the road, retail customers
on EDI and imports.

## Personas

[U42 Sales representative](../../01-users/personas/u42-sales-representative.md),
[U03 Sales](../../01-users/personas/u03-sales.md), [U04 Purchasing](../../01-users/personas/u04-purchasing.md),
[U15 Warehouse operator](../../01-users/personas/u15-warehouse-operator.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U09 Customer](../../01-users/personas/u09-customer.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users, reps' tablets, B2B portal accounts.
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types
  and offline scans,
  [UC-F2-22](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions on the road
  ([UC-SC15-20](use-cases/05-sales-force-and-performance/uc-sc15-20-ask-the-assistant.md)).
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): price agreements, offline orders on
  the road,
  [UC-F6-21](../../02-functional/f06-customers-and-sales/use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-21-take-orders-offline-on-the-road.md),
  credit limits and the shared targets and commissions,
  [UC-F6-25](../../02-functional/f06-customers-and-sales/use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-25-set-sales-targets-and-pay-commissions.md).
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md): buying, warehouse waves, returns,
  landed costs, supplier performance.
- [F8 Accounting](../../02-functional/f08-accounting/README.md): rebates, EU statistics and VAT.
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): reps' routes on the shared rounds optimiser,
  [UC-F9-30](../../02-functional/f09-hr-and-projects/use-cases/11-capacity-rounds-and-partners/uc-f09-30-plan-rounds-and-optimise-routes.md).
- [F11 Online shop (plugin)](../../02-functional/f11-online-shop/README.md): the B2B portal and catalogue,
  [UC-F11-11](../../02-functional/f11-online-shop/use-cases/04-special-sales/uc-f11-11-sell-b2b-online.md).
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md): reps' commissions as pay inputs,
  [UC-F13-03](../../02-functional/f13-payroll/use-cases/02-monthly-pay-run/uc-f13-03-collect-pay-inputs-from-f9.md).
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F6-25 Set sales targets and pay commissions](../../02-functional/f06-customers-and-sales/use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-25-set-sales-targets-and-pay-commissions.md),
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
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (EDI with retailers)

Also: offline sales representatives (REQ-T05-07).

## Example company

- [Wholesale and distribution](../../01-users/example-companies/wholesale-and-distribution.md)

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

⬅️ [IT and software](../sc14-it-and-software/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Events and culture](../sc16-events-and-culture/README.md)
