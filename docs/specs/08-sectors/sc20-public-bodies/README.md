🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🏛️ SC20 Public bodies

# 🏛️ SC20 Public bodies

**Status:** ✅ specified

Interviewed on 2026-11-14 as a new sector: D564 (the owner's answers of 2026-11-14: G17 and the sector interview G197
and G198).

## Summary

What communes, groups of communes and their public establishments add: public accounting under the M57 framework with
the split between authorising officer and public accountant, public procurement, a citizen services portal, grades and
statutory pay, and the four areas the owner added (council meetings and deliberations, the civil registry, planning
permits, the register of public assets). ([D564](../../06-decisions/sectors/d564-benchmark-gaps-sc20-public-bodies.md))

## Profile

Local bodies: communes, groups of communes, and their public establishments such as social action centres and tourist
offices. The accounting framework is M57, with the heritage of M14 for assets carried over (D564). State bodies, regions
and hospitals are out of scope.

## Personas

[U54 Public finance officer](../../01-users/personas/u54-public-finance-officer.md),
[U55 Elected official](../../01-users/personas/u55-elected-official.md),
[U56 Citizen](../../01-users/personas/u56-citizen.md), [U06 HR](../../01-users/personas/u06-hr.md), [U45 Payroll
officer](../../01-users/personas/u45-payroll-officer.md),
[U16 Office worker](../../01-users/personas/u16-office-worker.md).

## Capabilities used

- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): request types, approval chains
  and the portal,
  [UC-F2-20](../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md).
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions on the budget
  ([UC-SC20-16](use-cases/04-public-hr-and-pay/uc-sc20-16-ask-the-assistant-about-the-budget.md)).
- [F4 Meetings](../../02-functional/f04-meetings/README.md): council meetings and their minutes.
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md): orders, calls for tenders and
  suppliers,
  [UC-F7-14](../../02-functional/f07-purchasing-and-stock/use-cases/06-benchmark-additions/uc-f07-14-run-a-call-for-tenders-and-rate-suppliers.md).
- [F8 Accounting](../../02-functional/f08-accounting/README.md): the books, fixed assets and budgets,
  [UC-F8-08](../../02-functional/f08-accounting/use-cases/04-tax-assets-and-analytics/uc-f08-08-manage-fixed-assets-and-deferrals.md).
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): employee records and contracts.
- [F11 Online shop](../../02-functional/f11-online-shop/README.md): online payment,
  [UC-F11-06](../../02-functional/f11-online-shop/use-cases/02-shop-and-check-out/uc-f11-06-pay-online.md).
- [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md): payslips and the social declaration,
  [UC-F13-10](../../02-functional/f13-payroll/use-cases/03-declarations-and-payments/uc-f13-10-file-the-monthly-social-declaration-and-handle-returns.md).
- [F18 Hosted websites and domains](../../02-functional/f18-hosted-websites-and-domains/README.md): the council's
  website where decisions are posted.

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

- [UC-SC20-01](use-cases/01-public-accounting/uc-sc20-01-prepare-and-vote-the-budget.md)
- [UC-SC20-02 Commit expenditure](use-cases/01-public-accounting/uc-sc20-02-commit-expenditure.md)
- [UC-SC20-03](use-cases/01-public-accounting/uc-sc20-03-issue-payment-orders-and-revenue-titles.md)
- [UC-SC20-04](use-cases/01-public-accounting/uc-sc20-04-exchange-with-the-public-treasury.md)
- [UC-SC20-05](use-cases/02-public-procurement/uc-sc20-05-prepare-a-tender-file.md)
- [UC-SC20-06](use-cases/02-public-procurement/uc-sc20-06-publish-the-tender.md)
- [UC-SC20-07](use-cases/02-public-procurement/uc-sc20-07-analyse-bids-and-award.md)
- [UC-SC20-08](use-cases/02-public-procurement/uc-sc20-08-follow-the-public-contract.md)
- [UC-SC20-09](use-cases/03-citizen-services/uc-sc20-09-receive-a-citizens-request.md)
- [UC-SC20-10](use-cases/03-citizen-services/uc-sc20-10-book-halls-and-equipment.md)
- [UC-SC20-11](use-cases/03-citizen-services/uc-sc20-11-take-online-payments.md)
- [UC-SC20-12](use-cases/03-citizen-services/uc-sc20-12-publish-council-decisions.md)
- [UC-SC20-13](use-cases/04-public-hr-and-pay/uc-sc20-13-manage-grades-and-steps.md)
- [UC-SC20-14](use-cases/04-public-hr-and-pay/uc-sc20-14-compute-statutory-pay.md)
- [UC-SC20-15](use-cases/04-public-hr-and-pay/uc-sc20-15-declare-public-sector-contributions.md)
- [UC-SC20-16](use-cases/04-public-hr-and-pay/uc-sc20-16-ask-the-assistant-about-the-budget.md)
- [UC-SC20-17](use-cases/05-council-registry-permits-and-assets/uc-sc20-17-run-council-meetings-and-deliberations.md)
- [UC-SC20-18](use-cases/05-council-registry-permits-and-assets/uc-sc20-18-keep-the-civil-registry.md)
- [UC-SC20-19](use-cases/05-council-registry-permits-and-assets/uc-sc20-19-instruct-planning-permits.md)
- [UC-SC20-20](use-cases/05-council-registry-permits-and-assets/uc-sc20-20-keep-the-public-assets-register.md)

## Contents

|  | ID | Page | Status |
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

⬅️ [Trades and home services](../sc19-trades-and-home-services/README.md) · ⬆️ [Up](../README.md)
