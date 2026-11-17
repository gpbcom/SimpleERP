🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🎭 SC16 Events and culture

# 🎭 SC16 Events and culture

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D362 to D364.

## Summary

What event organisers, venues and cultural places add: events and budgets, venues, artists and riders, performers'
declarations, ticketing and access, the box office, accreditations, shifts, sponsors and exhibitors, bars and
merchandise, safety, copyright, the ticket tax, memberships, refunds, reports and attendee messages
([D362](../../06-decisions/sectors/d362-events-sector-coverage.md)).

## Profile

Event organisers, venues, theatres, festivals and museums, from one-off events to full seasons, with volunteers and
intermittent performers.

## Personas

[U43 Event producer](../../01-users/personas/u43-event-producer.md),
[U44 Box-office agent](../../01-users/personas/u44-box-office-agent.md),
[U32 Volunteer](../../01-users/personas/u32-volunteer.md), [U17 Cashier](../../01-users/personas/u17-cashier.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U09 Customer](../../01-users/personas/u09-customer.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users, volunteers and portal accounts.
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types,
  the shared booking engine for rooms, stands and timed entries,
  [UC-F2-18](../../02-functional/f02-no-code-configuration/use-cases/08-views-and-bookings/uc-f02-18-make-a-record-type-bookable.md),
  volunteer portals.
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions on the event
  ([UC-SC16-20](use-cases/05-declarations-and-reports/uc-sc16-20-ask-the-assistant.md)).
- [F5 Social media and marketing](../../02-functional/f05-social-media/README.md): the shared events and ticketing
  model,
  [UC-F5-17](../../02-functional/f05-social-media/use-cases/07-events-and-ticketing/uc-f05-17-set-up-ticketing-for-an-event.md),
  [UC-F5-18](../../02-functional/f05-social-media/use-cases/07-events-and-ticketing/uc-f05-18-sell-at-the-box-office-and-scan-tickets.md),
  attendee messages, surveys.
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): sponsor and exhibitor invoices,
  refunds.
- [F8 Accounting](../../02-functional/f08-accounting/README.md): event budgets and declarations.
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): staff and volunteer shifts.
- [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md): box office, bars and merchandise tills.
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md): intermittent performers' pay,
  [UC-F13-24](../../02-functional/f13-payroll/use-cases/07-schemes-and-special-contracts/uc-f13-24-pay-intermittent-performers.md).
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F2-18 Make a record type bookable](../../02-functional/f02-no-code-configuration/use-cases/08-views-and-bookings/uc-f02-18-make-a-record-type-bookable.md),
  [UC-F5-17 Set up ticketing for an event](../../02-functional/f05-social-media/use-cases/07-events-and-ticketing/uc-f05-17-set-up-ticketing-for-an-event.md).

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

- [Events and culture](../../01-users/example-companies/events-and-culture.md)

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

⬅️ [Wholesale and distribution](../sc15-wholesale-and-distribution/README.md) · ⬆️ [Up](../README.md)
