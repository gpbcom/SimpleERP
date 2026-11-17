🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🤲 SC08 Non-profit association

# 🤲 SC08 Non-profit association

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D338 to D340.

## Summary

What an association adds: members and dues, the assembly and the board, donations, campaigns, tax receipts, regular
donors, grants and reports, volunteers, events and bars, association accounts and their publication, bequests,
communication and members' rights ([D338](../../06-decisions/sectors/d338-non-profit-sector-coverage.md)).

## Profile

Associations and foundations, from small clubs run by volunteers to large charities with employees, grants and thousands
of donors.

## Personas

[U31 Treasurer](../../01-users/personas/u31-treasurer.md), [U32 Volunteer](../../01-users/personas/u32-volunteer.md),
[U13 Owner](../../01-users/personas/u13-owner.md), [U12 Marketing](../../01-users/personas/u12-marketing.md),
[U09 Customer](../../01-users/personas/u09-customer.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users, volunteers and portal accounts for
  members,
  [UC-F1-19](../../02-functional/f01-administration/use-cases/12-portal-accounts-and-integrations/uc-f01-19-manage-portal-accounts.md).
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types,
  portals for members and volunteers,
  [UC-F2-20](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md),
  e-signature.
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions on the association
  ([UC-SC08-20](use-cases/02-donations-and-receipts/uc-sc08-20-ask-the-assistant-about-the-association.md)).
- [F4 Meetings](../../02-functional/f04-meetings/README.md): assemblies and board meetings recorded,
  [UC-F4-03](../../02-functional/f04-meetings/use-cases/02-record-in-person-or-by-phone/uc-f04-03-record-an-in-person-meeting.md).
- [F5 Social media and marketing](../../02-functional/f05-social-media/README.md): campaigns, newsletters and the shared
  events and ticketing,
  [UC-F5-17](../../02-functional/f05-social-media/use-cases/07-events-and-ticketing/uc-f05-17-set-up-ticketing-for-an-event.md).
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): members, donors, the portal and the
  shared multi-payer billing for co-funded projects,
  [UC-F6-20](../../02-functional/f06-customers-and-sales/use-cases/07-special-invoicing/uc-f06-20-invoice-several-payers-with-funders-and-caps.md).
- [F8 Accounting](../../02-functional/f08-accounting/README.md): non-profit accounts,
  [UC-F8-23](../../02-functional/f08-accounting/use-cases/07-client-money-grants-and-non-profits/uc-f08-23-keep-non-profit-accounts.md),
  dedicated funds and grants,
  [UC-F8-22](../../02-functional/f08-accounting/use-cases/07-client-money-grants-and-non-profits/uc-f08-22-account-for-a-grant.md).
- [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md): the till of temporary bars.
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F5-17 Set up ticketing for an event](../../02-functional/f05-social-media/use-cases/07-events-and-ticketing/uc-f05-17-set-up-ticketing-for-an-event.md),
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

- [Non-profit association](../../01-users/example-companies/non-profit.md)

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

⬅️ [Transport and logistics](../sc07-transport/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Health practices](../sc09-health-practices/README.md)
