🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › ⚖️ SC11 Professional firms

# ⚖️ SC11 Professional firms

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D347 to D349.

## Summary

What law, accounting, architecture and engineering firms add: client intake with identity and conflict checks,
engagements and fees, matters, time, trust accounts, deadlines, documents, the portal, accountants' portfolios and
filings, architects' phases, anti-money-laundering, walls and the firm's management
([D347](../../06-decisions/sectors/d347-professional-firms-sector-coverage.md)).

## Profile

Firms of 1 to 500 professionals and assistants, bound by professional secrecy and anti-money-laundering duties.

## Personas

[U36 Professional](../../01-users/personas/u36-professional.md),
[U37 Professional's assistant](../../01-users/personas/u37-assistant.md),
[U09 Customer](../../01-users/personas/u09-customer.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U13 Owner](../../01-users/personas/u13-owner.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users with walls, partners and assistants,
  client portal accounts.
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types,
  the shared portals,
  [UC-F2-20](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md),
  documents and e-signature.
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions within walls
  ([UC-SC11-20](use-cases/02-matters-and-documents/uc-sc11-20-ask-the-assistant-about-a-matter.md)).
- [F4 Meetings](../../02-functional/f04-meetings/README.md): client video meetings through the shared capability,
  [UC-F4-25](../../02-functional/f04-meetings/use-cases/12-rooms-and-client-video/uc-f04-25-hold-a-client-video-meeting.md).
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): fee bills, phases and the shared
  targets for partners,
  [UC-F6-25](../../02-functional/f06-customers-and-sales/use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-25-set-sales-targets-and-pay-commissions.md).
- [F8 Accounting](../../02-functional/f08-accounting/README.md): the shared third-party client money for trust accounts,
  [UC-F8-21](../../02-functional/f08-accounting/use-cases/07-client-money-grants-and-non-profits/uc-f08-21-keep-third-party-client-money.md),
  filings.
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): continuing training.
- [F15 Legal assistant](../../02-functional/f15-legal-assistant/README.md): the legal assistant for lawyers' research.
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F4-25 Hold a client video meeting](../../02-functional/f04-meetings/use-cases/12-rooms-and-client-video/uc-f04-25-hold-a-client-video-meeting.md),
  [UC-F6-25 Set sales targets and pay commissions](../../02-functional/f06-customers-and-sales/use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-25-set-sales-targets-and-pay-commissions.md),
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

- [Professional firms](../../01-users/example-companies/professional-firms.md)

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

⬅️ [Real estate](../sc10-real-estate/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Education and training](../sc12-education-and-training/README.md)
