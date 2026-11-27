🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🏘️ SC10 Real estate

# 🏘️ SC10 Real estate

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D344 to D346.

## Summary

What estate agencies, property managers and co-ownership managers add: mandates, listings, viewings, offers, client
funds, fees; lettings, rents, indexation, deposits, charges, landlord statements, diagnostics and unpaid rents;
assemblies, budgets, calls, works fund and co-owners' accounts
([D344](../../06-decisions/sectors/d344-real-estate-sector-coverage.md)).

## Profile

Estate agencies, property managers and co-ownership managers, from one agent to networks, with client funds under a
guarantee.

## Personas

[U34 Property manager](../../01-users/personas/u34-property-manager.md),
[U35 Real-estate agent](../../01-users/personas/u35-real-estate-agent.md),
[U09 Customer](../../01-users/personas/u09-customer.md), [U05 Accounting](../../01-users/personas/u05-accounting.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users, agencies as sites, portal accounts for
  landlords, tenants and co-owners,
  [UC-F1-19](../../02-functional/f01-administration/use-cases/12-portal-accounts-and-integrations/uc-f01-19-manage-portal-accounts.md).
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types,
  the shared portals,
  [UC-F2-20](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md),
  e-signature, offline inventories.
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions on the portfolio
  ([UC-SC10-20](use-cases/06-portal-and-assistant/uc-sc10-20-ask-the-assistant-about-the-portfolio.md)).
- [F4 Meetings](../../02-functional/f04-meetings/README.md): viewings booked,
  [UC-F4-18](../../02-functional/f04-meetings/use-cases/10-benchmark-additions/uc-f04-18-let-customers-book-appointments.md),
  and assemblies recorded.
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): fees, rent calls, payments and
  instalment plans.
- [F8 Accounting](../../02-functional/f08-accounting/README.md): the shared third-party client money,
  [UC-F8-21](../../02-functional/f08-accounting/use-cases/07-client-money-grants-and-non-profits/uc-f08-21-keep-third-party-client-money.md),
  and co-ownership books.
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F2-20 Expose a record type on a portal](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md),
  [UC-F8-21 Keep third-party client money](../../02-functional/f08-accounting/use-cases/07-client-money-grants-and-non-profits/uc-f08-21-keep-third-party-client-money.md).

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

- [Real estate](../../01-users/example-companies/real-estate.md)

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

⬅️ [Health practices](../sc09-health-practices/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Professional firms](../sc11-professional-firms/README.md)
