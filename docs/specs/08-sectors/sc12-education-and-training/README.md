🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🎓 SC12 Education and training

# 🎓 SC12 Education and training

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D350 to D352.

## Summary

What training providers and private schools add: catalogue and sessions, enrolments, agreements and funding,
invitations, attendance, e-learning, certificates, satisfaction, billing, trainers, the quality file, the yearly report;
school enrolment, classes, timetables, grades, absences and fees
([D350](../../06-decisions/sectors/d350-education-sector-coverage.md)).

## Profile

Training providers of 1 to 500 trainers, company academies and private schools.

## Personas

[U38 Training coordinator](../../01-users/personas/u38-training-coordinator.md),
[U39 Trainer](../../01-users/personas/u39-trainer.md), [U09 Customer](../../01-users/personas/u09-customer.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U13 Owner](../../01-users/personas/u13-owner.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users, trainers, portal accounts for learners
  and parents,
  [UC-F1-19](../../02-functional/f01-administration/use-cases/12-portal-accounts-and-integrations/uc-f01-19-manage-portal-accounts.md).
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types,
  the shared booking engine for rooms,
  [UC-F2-18](../../02-functional/f02-no-code-configuration/use-cases/08-views-and-bookings/uc-f02-18-make-a-record-type-bookable.md),
  portals for learners and parents,
  [UC-F2-20](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md),
  offline attendance.
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions on sessions
  ([UC-SC12-20](use-cases/03-deliver-and-assess/uc-sc12-20-ask-the-assistant.md)).
- [F4 Meetings](../../02-functional/f04-meetings/README.md): remote sessions by video.
- [F5 Social media and marketing](../../02-functional/f05-social-media/README.md): satisfaction surveys.
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): quotes, agreements and the shared
  multi-payer invoicing for funders,
  [UC-F6-20](../../02-functional/f06-customers-and-sales/use-cases/07-special-invoicing/uc-f06-20-invoice-several-payers-with-funders-and-caps.md).
- [F8 Accounting](../../02-functional/f08-accounting/README.md): school grants on the shared grant accounting,
  [UC-F8-22](../../02-functional/f08-accounting/use-cases/07-client-money-grants-and-non-profits/uc-f08-22-account-for-a-grant.md).
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): trainers and freelance trainers.
- [F11 Online shop (plugin)](../../02-functional/f11-online-shop/README.md): the catalogue on the website.
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F2-18 Make a record type bookable](../../02-functional/f02-no-code-configuration/use-cases/08-views-and-bookings/uc-f02-18-make-a-record-type-bookable.md),
  [UC-F2-20 Expose a record type on a portal](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md),
  [UC-F6-20 Invoice several payers with funders and caps](../../02-functional/f06-customers-and-sales/use-cases/07-special-invoicing/uc-f06-20-invoice-several-payers-with-funders-and-caps.md),
  [UC-F8-22 Account for a grant](../../02-functional/f08-accounting/use-cases/07-client-money-grants-and-non-profits/uc-f08-22-account-for-a-grant.md).

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

- [Education and training](../../01-users/example-companies/education-and-training.md)

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

⬅️ [Professional firms](../sc11-professional-firms/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Agriculture and food](../sc13-agriculture-and-food/README.md)
