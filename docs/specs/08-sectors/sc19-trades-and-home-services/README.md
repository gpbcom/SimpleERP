🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🔧 SC19 Trades and home services

# 🔧 SC19 Trades and home services

**Status:** ✅ specified

Interviewed on 2026-11-14 as a new sector: D563 (the owner's answers of 2026-11-14: G16 and the sector interview G195
and G196).

## Summary

What plumbers, heating and air-conditioning engineers, electricians, solar installers, locksmiths, handymen, cleaners
and gardeners add: maintenance contracts with their legal yearly check-ups, interventions dispatched and reported on the
phone, the home-services tax credit with its certificate and immediate advance, installations with grants and labels,
and the four areas the owner added (emergency on-call, builders' warranties, stock in each van, quotes made on site and
signed on the phone). ([D563](../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md))

## Profile

Small and medium trades companies that work in customers' homes: plumbing, heating and air conditioning, electricity,
solar, locksmiths, handymen, cleaning and gardening, from one van to a fleet. Each trade is an option of the sector
pack, so a company switches on only the trades it practises (D563).

## Personas

[U13 Owner](../../01-users/personas/u13-owner.md), [U29 Dispatcher](../../01-users/personas/u29-dispatcher.md),
[U14 Field worker](../../01-users/personas/u14-field-worker.md),
[U22 Site manager](../../01-users/personas/u22-site-manager.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md),
[U04 Purchasing and stock](../../01-users/personas/u04-purchasing.md),
[U09 Customer](../../01-users/personas/u09-customer.md).

## Capabilities used

- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): e-signature of quotes and
  reports,
  [UC-F2-14](../../02-functional/f02-no-code-configuration/use-cases/07-benchmark-additions/uc-f02-14-send-documents-for-e-signature.md).
- [F4 Meetings](../../02-functional/f04-meetings/README.md): appointments the customer books online,
  [UC-F4-18](../../02-functional/f04-meetings/use-cases/10-benchmark-additions/uc-f04-18-let-customers-book-appointments.md).
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): quotes, orders, invoices and
  subscription contracts.
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md): parts, lots, locations and reloads.
- [F8 Accounting](../../02-functional/f08-accounting/README.md): invoices, deposits and the tax-credit advance.
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): field service, rounds, qualifications and
  shifts,
  [UC-F9-18](../../02-functional/f09-hr-and-projects/use-cases/06-plan-and-deliver-work/uc-f09-18-run-field-service.md).
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md): on-call allowances as pay inputs.

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

## Use cases

- [UC-SC19-01](use-cases/01-maintenance-contracts/uc-sc19-01-sell-a-maintenance-contract.md)
- [UC-SC19-02](use-cases/01-maintenance-contracts/uc-sc19-02-generate-recurring-visits.md)
- [UC-SC19-03](use-cases/01-maintenance-contracts/uc-sc19-03-record-legal-check-ups.md)
- [UC-SC19-04](use-cases/01-maintenance-contracts/uc-sc19-04-renew-and-index-contracts.md)
- [UC-SC19-05](use-cases/02-on-site-intervention/uc-sc19-05-dispatch-an-intervention.md)
- [UC-SC19-06](use-cases/02-on-site-intervention/uc-sc19-06-report-on-site-with-photos.md)
- [UC-SC19-07](use-cases/02-on-site-intervention/uc-sc19-07-record-parts-used.md)
- [UC-SC19-08](use-cases/02-on-site-intervention/uc-sc19-08-sign-and-invoice-on-the-spot.md)
- [UC-SC19-09](use-cases/03-home-services-tax-credit/uc-sc19-09-sell-cleaning-and-gardening-to-households.md)
- [UC-SC19-10](use-cases/03-home-services-tax-credit/uc-sc19-10-plan-recurring-household-visits.md)
- [UC-SC19-11](use-cases/03-home-services-tax-credit/uc-sc19-11-issue-the-tax-credit-certificate.md)
- [UC-SC19-12](use-cases/03-home-services-tax-credit/uc-sc19-12-use-the-immediate-advance.md)
- [UC-SC19-13](use-cases/04-installations-and-labels/uc-sc19-13-run-an-installation-project.md)
- [UC-SC19-14](use-cases/04-installations-and-labels/uc-sc19-14-file-grants-and-certificates.md)
- [UC-SC19-15](use-cases/04-installations-and-labels/uc-sc19-15-keep-the-rge-label-evidence.md)
- [UC-SC19-16](use-cases/04-installations-and-labels/uc-sc19-16-keep-refrigerant-and-grid-connection-records.md)
- [UC-SC19-17](use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-17-run-the-emergency-on-call-service.md)
- [UC-SC19-18](use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-18-keep-builders-warranties-and-certificates.md)
- [UC-SC19-19](use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-19-keep-stock-in-each-van.md)
- [UC-SC19-20](use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-20-quote-on-site-and-sign-on-the-phone.md)

## Contents

|  | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | 🔄 |
| 🔀 |  | [Flows](flows/README.md) | 🔄 |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | 🔄 |
| 🎁 |  | [Sector pack](sector-pack.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [Sports and fitness](../sc18-sports-and-fitness/README.md) · ⬆️ [Up](../README.md)
