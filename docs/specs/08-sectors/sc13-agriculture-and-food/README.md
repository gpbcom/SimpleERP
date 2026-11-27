🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🌾 SC13 Agriculture and food

# 🌾 SC13 Agriculture and food

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D353 to D355.

## Summary

What farms and food processors add: plots and crops, treatment and fertilisation registers, harvests and lots, herds and
veterinary treatments, CAP aid, machinery, seasonal workers, direct sales, cooperatives, organic records; recipes and
batches, traceability, HACCP, labels, shelf life and recalls; costs and reports
([D353](../../06-decisions/sectors/d353-agriculture-sector-coverage.md)).

## Profile

Farms of every size, wine estates, farm shops and small food processors, often working offline in the field.

## Personas

[U40 Farmer](../../01-users/personas/u40-farmer.md), [U14 Field worker](../../01-users/personas/u14-field-worker.md),
[U21 Production planner](../../01-users/personas/u21-production-planner.md),
[U20 Production operator](../../01-users/personas/u20-production-operator.md),
[U27 Quality manager](../../01-users/personas/u27-quality-manager.md),
[U15 Warehouse operator](../../01-users/personas/u15-warehouse-operator.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U09 Customer](../../01-users/personas/u09-customer.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users, seasonal workers' accounts, the farm and
  the processing site.
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types,
  the map view, and the shared offline phone forms,
  [UC-F2-22](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions and dictation
  ([UC-SC13-20](use-cases/03-farm-business/uc-sc13-20-ask-the-assistant.md)).
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): basket subscriptions and customers.
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md): lots, stock, traceability.
- [F8 Accounting](../../02-functional/f08-accounting/README.md): CAP aid on the shared grant accounting,
  [UC-F8-22](../../02-functional/f08-accounting/use-cases/07-client-money-grants-and-non-profits/uc-f08-22-account-for-a-grant.md),
  margins, cooperative payments.
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): seasonal hiring.
- [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md): direct sales at the farm and markets.
- [F12 Manufacturing (plugin)](../../02-functional/f12-manufacturing/README.md): processing on the shared recipes and
  batches,
  [UC-F12-31](../../02-functional/f12-manufacturing/use-cases/09-recipes-and-batches/uc-f12-31-define-a-recipe-and-produce-in-batches.md),
  machine maintenance.
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md): seasonal and farm workers' pay under the MSA,
  [UC-F13-25](../../02-functional/f13-payroll/use-cases/07-schemes-and-special-contracts/uc-f13-25-pay-farm-workers-under-the-msa.md).
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F2-22 Fill a form offline on the phone](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  [UC-F8-22 Account for a grant](../../02-functional/f08-accounting/use-cases/07-client-money-grants-and-non-profits/uc-f08-22-account-for-a-grant.md),
  [UC-F12-31 Define a recipe and produce in batches](../../02-functional/f12-manufacturing/use-cases/09-recipes-and-batches/uc-f12-31-define-a-recipe-and-produce-in-batches.md).

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

## Example company

- [Agriculture and food](../../01-users/example-companies/agriculture-and-food.md)

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

⬅️ [Education and training](../sc12-education-and-training/README.md) · ⬆️ [Up](../README.md) ·
➡️ [IT and software](../sc14-it-and-software/README.md)
