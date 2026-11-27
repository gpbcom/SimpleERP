🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🏠 SC04 Home care

# 🏠 SC04 Home care

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D326 to D328.

## Summary

What a home-care provider adds: care recipients and funding, care plans, rounds with travel times, the carer's phone
with check-in and check-out, the care log and incidents, replacements, family access, billing to recipients and funders,
the yearly tax-credit certificate, the immediate advance, quality and carers' skills
([D326](../../06-decisions/sectors/d326-home-care-sector-coverage.md)).

## Profile

Home-help and home-care services for elderly, disabled and fragile people and families: associations and companies of 5
to 1 000 carers, many visits a day, funders and families involved.

## Personas

[U25 Care coordinator](../../01-users/personas/u25-care-coordinator.md),
[U26 Carer](../../01-users/personas/u26-carer.md), [U09 Customer](../../01-users/personas/u09-customer.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U06 HR](../../01-users/personas/u06-hr.md),
[U13 Owner](../../01-users/personas/u13-owner.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users, agencies as sites, and portal accounts
  for families,
  [UC-F1-19](../../02-functional/f01-administration/use-cases/12-portal-accounts-and-integrations/uc-f01-19-manage-portal-accounts.md).
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types,
  the shared portals,
  [UC-F2-20](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md),
  and offline phone forms,
  [UC-F2-22](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions on the rounds
  ([UC-SC04-15](use-cases/03-visit/uc-sc04-15-ask-the-assistant-about-the-rounds.md)).
- [F5 Social media and marketing](../../02-functional/f05-social-media/README.md): satisfaction surveys.
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): recipients, invoices and the shared
  multi-payer invoicing with funders and caps,
  [UC-F6-20](../../02-functional/f06-customers-and-sales/use-cases/07-special-invoicing/uc-f06-20-invoice-several-payers-with-funders-and-caps.md).
- [F8 Accounting](../../02-functional/f08-accounting/README.md): funders' receivables, the immediate advance's payments
  and grants,
  [UC-F8-22](../../02-functional/f08-accounting/use-cases/07-client-money-grants-and-non-profits/uc-f08-22-account-for-a-grant.md).
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): schedules, absences, skills, training and the
  shared rounds optimiser,
  [UC-F9-30](../../02-functional/f09-hr-and-projects/use-cases/11-capacity-rounds-and-partners/uc-f09-30-plan-rounds-and-optimise-routes.md).
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md): pay inputs: visit hours, travel time, splits,
  mileage, under the home-help agreement,
  [UC-F13-31](../../02-functional/f13-payroll/use-cases/09-collective-agreements-by-family/uc-f13-31-apply-the-home-help-agreement.md).
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F2-20 Expose a record type on a portal](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md),
  [UC-F2-22 Fill a form offline on the phone](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  [UC-F6-20 Invoice several payers with funders and caps](../../02-functional/f06-customers-and-sales/use-cases/07-special-invoicing/uc-f06-20-invoice-several-payers-with-funders-and-caps.md),
  [UC-F8-22 Account for a grant](../../02-functional/f08-accounting/use-cases/07-client-money-grants-and-non-profits/uc-f08-22-account-for-a-grant.md),
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
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (funders' and URSSAF portals)

Also: offline carers' phones (REQ-T05-07); planning (REQ-T04-08).

## Example company

- [Home care](../../01-users/example-companies/home-care.md)

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

⬅️ [Services](../sc03-services/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Manufacturing](../sc05-manufacturing/README.md)
