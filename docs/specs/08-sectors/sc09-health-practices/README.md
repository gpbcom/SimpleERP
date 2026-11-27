🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🩺 SC09 Health practices

# 🩺 SC09 Health practices

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D341 to D343.

## Summary

Full practice software for doctors, dentists, physiotherapists, nurses and health centres: appointments, patient files,
the clinical record, prescriptions, electronic billing to health insurance, third-party payment, fees, the national
health record, results, teleconsultation, the practice's organisation, accounts and certifications
([D341](../../06-decisions/sectors/d341-health-practices-sector-coverage.md)).

## Profile

Private practices and health centres of 1 to 50 practitioners, with secretaries; health data on certified hosting.

## Personas

[U33 Medical secretary](../../01-users/personas/u33-medical-secretary.md),
[U13 Owner](../../01-users/personas/u13-owner.md), [U09 Customer](../../01-users/personas/u09-customer.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md),
[U11 IT provider administrator](../../01-users/personas/u11-provider-admin.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users with secrecy roles, practitioners and
  secretaries, patient portal accounts.
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types
  and the shared booking engine for appointments, rooms and equipment,
  [UC-F2-18](../../02-functional/f02-no-code-configuration/use-cases/08-views-and-bookings/uc-f02-18-make-a-record-type-bookable.md).
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions on the practice, clinical content only with
  local models ([UC-SC09-20](use-cases/01-appointments/uc-sc09-20-ask-the-assistant-about-the-practice.md)).
- [F4 Meetings](../../02-functional/f04-meetings/README.md): teleconsultation through the shared client video meetings,
  [UC-F4-25](../../02-functional/f04-meetings/use-cases/12-rooms-and-client-video/uc-f04-25-hold-a-client-video-meeting.md).
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): patient invoices and the shared
  multi-payer invoicing for insurers' shares,
  [UC-F6-20](../../02-functional/f06-customers-and-sales/use-cases/07-special-invoicing/uc-f06-20-invoice-several-payers-with-funders-and-caps.md).
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md): consumables.
- [F8 Accounting](../../02-functional/f08-accounting/README.md): practice accounts, shared costs, retrocessions.
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack and its certified modules are
  installed and updated from the plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F2-18 Make a record type bookable](../../02-functional/f02-no-code-configuration/use-cases/08-views-and-bookings/uc-f02-18-make-a-record-type-bookable.md),
  [UC-F4-25 Hold a client video meeting](../../02-functional/f04-meetings/use-cases/12-rooms-and-client-video/uc-f04-25-hold-a-client-video-meeting.md),
  [UC-F6-20 Invoice several payers with funders and caps](../../02-functional/f06-customers-and-sales/use-cases/07-special-invoicing/uc-f06-20-invoice-several-payers-with-funders-and-caps.md).

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
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (health insurance and secure
  messaging)

Also: HDS hosting (CR-FR-055).

## Example company

- [Health practices](../../01-users/example-companies/health-practices.md)

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

⬅️ [Non-profit association](../sc08-non-profit/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Real estate](../sc10-real-estate/README.md)
