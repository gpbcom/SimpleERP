🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 💻 SC14 IT and software

# 💻 SC14 IT and software

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D356 to D358.

## Summary

What software publishers, SaaS companies and IT services add: subscriptions, usage and revenue, licences and renewals,
service levels, managed services, sprints and release notes, features followed in the development tool, customer health,
processor agreements, bills of materials and vulnerabilities, incident reporting, data export and switching, EU VAT,
dunning, the portal and SaaS metrics ([D356](../../06-decisions/sectors/d356-it-and-software-sector-coverage.md)).

## Profile

Software publishers, SaaS companies, IT service and managed-service providers, from start-ups to large firms, selling
across the EU.

## Personas

[U41 Customer success manager](../../01-users/personas/u41-customer-success-manager.md),
[U16 Office worker](../../01-users/personas/u16-office-worker.md),
[U24 Engagement manager](../../01-users/personas/u24-engagement-manager.md),
[U03 Sales](../../01-users/personas/u03-sales.md), [U05 Accounting](../../01-users/personas/u05-accounting.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U09 Customer](../../01-users/personas/u09-customer.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users, customer portal accounts, API tokens,
  [UC-F1-20](../../02-functional/f01-administration/use-cases/12-portal-accounts-and-integrations/uc-f01-20-create-and-revoke-api-tokens-and-service-accounts.md).
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types,
  partner portals,
  [UC-F2-20](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md),
  e-signature.
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions on customers
  ([UC-SC14-20](use-cases/06-portal-and-metrics/uc-sc14-20-ask-the-assistant.md)).
- [F4 Meetings](../../02-functional/f04-meetings/README.md): business reviews by video,
  [UC-F4-25](../../02-functional/f04-meetings/use-cases/12-rooms-and-client-video/uc-f04-25-hold-a-client-video-meeting.md).
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): subscriptions, usage billing and the
  shared commissions for partners,
  [UC-F6-25](../../02-functional/f06-customers-and-sales/use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-25-set-sales-targets-and-pay-commissions.md).
- [F8 Accounting](../../02-functional/f08-accounting/README.md): revenue recognition, EU VAT.
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): projects, sprints and time.
- [F16 Customer support agents](../../02-functional/f16-customer-support-agents/README.md): support tickets and service
  levels.
- [F24 Integrations hub](../../02-functional/f24-integrations-hub/README.md): the development tool and monitoring
  connectors.
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md): sales commissions sent as pay inputs,
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

## Example company

- [IT and software](../../01-users/example-companies/it-and-software.md)

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

⬅️ [Agriculture and food](../sc13-agriculture-and-food/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Wholesale and distribution](../sc15-wholesale-and-distribution/README.md)
