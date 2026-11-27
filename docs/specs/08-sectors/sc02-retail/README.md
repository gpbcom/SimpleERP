🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🛍️ SC02 Retail

# 🛍️ SC02 Retail

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D320 to D322.

## Summary

What a retail company adds to F10 Point of sale and F11 Online shop: several stores, assortments, size and colour grids
and seasons, replenishment and transfers, labels, sales periods, counts, selling and returning across channels,
clienteling, targets, schedules, unsold goods and store performance
([D320](../../06-decisions/sectors/d320-retail-sector-coverage.md)).

## Profile

Fashion, home, sports, food and specialist retail, from one shop to chains and franchises, often with an online shop.

## Personas

[U23 Store manager](../../01-users/personas/u23-store-manager.md),
[U17 Cashier](../../01-users/personas/u17-cashier.md),
[U15 Warehouse operator](../../01-users/personas/u15-warehouse-operator.md),
[U12 Marketing](../../01-users/personas/u12-marketing.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U09 Customer](../../01-users/personas/u09-customer.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): the users, roles and sites: one site per store
  and the warehouse.
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types
  and offline scans on the phone,
  [UC-F2-22](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions and actions on a store
  ([UC-SC02-15](use-cases/05-unsold-goods-and-performance/uc-sc02-15-ask-the-assistant-about-a-store.md)).
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): targets and commissions per store and
  staff,
  [UC-F6-25](../../02-functional/f06-customers-and-sales/use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-25-set-sales-targets-and-pay-commissions.md).
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md): stock, replenishment, transfers,
  counts, unsold goods.
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): staff schedules and Sunday rules,
  [UC-F9-15](../../02-functional/f09-hr-and-projects/use-cases/06-plan-and-deliver-work/uc-f09-15-plan-shifts.md).
- [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md): tills, receipts, returns, clienteling,
  store performance.
- [F11 Online shop (plugin)](../../02-functional/f11-online-shop/README.md): online orders, click & collect, ship from
  store.
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md): commissions and Sunday extra pay sent as pay
  inputs,
  [UC-F13-03](../../02-functional/f13-payroll/use-cases/02-monthly-pay-run/uc-f13-03-collect-pay-inputs-from-f9.md).
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F6-25 Set sales targets and pay commissions](../../02-functional/f06-customers-and-sales/use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-25-set-sales-targets-and-pay-commissions.md).

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
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (sales channels)

Also: offline tills (REQ-T05-07).

## Example company

- [Retail](../../01-users/example-companies/retail.md)

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | ✅ |
| 📏 |  | [Business rules](business-rules/README.md) | ✅ |
| 🗃️ |  | [Data](data/README.md) | ✅ |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🎁 |  | [Sector pack](sector-pack.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | ✅ |

---

⬅️ [Construction](../sc01-construction/README.md) · ⬆️ [Up](../README.md) · ➡️ [Services](../sc03-services/README.md)
