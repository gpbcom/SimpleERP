🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🏗️ SC01 Construction

# 🏗️ SC01 Construction

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D316 to D319.

## Summary

What a construction company adds to SimpleERP: sites, quotes by lots, site planning, time and materials per site, the
site diary, progress bills with retention, subcontracting, equipment, works declarations, acceptance and warranties,
site margins, for private and public customers ([D316](../../06-decisions/sectors/d316-construction-sector-coverage.md),
[D318](../../06-decisions/sectors/d318-construction-customers.md)).

## Profile

Building and renovation companies and trades, 1 to 500 people, several sites at once, crews on the move and often
offline, subcontractors, private customers, companies and public buyers.

## Personas

[U22 Site manager](../../01-users/personas/u22-site-manager.md),
[U14 Field worker](../../01-users/personas/u14-field-worker.md), [U03 Sales](../../01-users/personas/u03-sales.md),
[U04 Purchasing](../../01-users/personas/u04-purchasing.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U09 Customer](../../01-users/personas/u09-customer.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): the users, roles and sites of the company, the
  crews' phone accounts.
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types,
  and the shared offline phone forms,
  [UC-F2-22](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  for time and the diary, the booking engine,
  [UC-F2-19](../../02-functional/f02-no-code-configuration/use-cases/08-views-and-bookings/uc-f02-19-book-a-resource.md),
  for equipment, and e-signature.
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions and actions on a site
  ([UC-SC01-15](use-cases/03-run-the-site/uc-sc01-15-ask-the-assistant-about-a-site.md)).
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): quotes, progress invoices with
  retention,
  [UC-F6-06](../../02-functional/f06-customers-and-sales/use-cases/03-invoice-and-get-paid/uc-f06-06-invoice-deposits-progress-and-final.md),
  Chorus Pro,
  [UC-F6-19](../../02-functional/f06-customers-and-sales/use-cases/07-special-invoicing/uc-f06-19-invoice-a-public-buyer-through-chorus-pro.md),
  the customer portal.
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md): purchases and rentals per site, the
  vans' stock.
- [F8 Accounting](../../02-functional/f08-accounting/README.md): reverse charge, posting, site profitability,
  [UC-F8-20](../../02-functional/f08-accounting/use-cases/06-benchmark-additions/uc-f08-20-analyse-profitability.md).
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): crews, shifts, timesheets, subcontractors on
  projects,
  [UC-F9-32](../../02-functional/f09-hr-and-projects/use-cases/11-capacity-rounds-and-partners/uc-f09-32-work-with-subcontractors-and-freelancers-on-projects.md),
  the construction card.
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md): pay inputs from site hours and the construction
  agreements,
  [UC-F13-33](../../02-functional/f13-payroll/use-cases/09-collective-agreements-by-family/uc-f13-33-apply-the-construction-agreements.md).
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F2-22 Fill a form offline on the phone](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

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
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (Chorus Pro,
  works-near-networks declarations)

Also: offline site devices (REQ-T05-07).

## Example company

- [Construction](../../01-users/example-companies/construction.md)

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

⬆️ [Up](../README.md) · ➡️ [Retail](../sc02-retail/README.md)
