🏠 [Specs](../../README.md) › 🏷️ [Sectors](../README.md) › 🏭 SC05 Manufacturing

# 🏭 SC05 Manufacturing

**Status:** ✅ specified

Interviewed on 2026-11-11 after F12 (D115): D329 to D331.

## Summary

What a manufacturer adds on top of F12: setups for discrete, batch and process production, recipes, make to order and
engineer to order, customer parts, packaging and labels, and the quality system of ISO 9001
([D329](../../06-decisions/sectors/d329-manufacturing-sector-coverage.md)).

## Profile

Manufacturers and food processors of 5 to 1 000 people, often ISO 9001 certified or preparing it.

## Personas

[U27 Quality manager](../../01-users/personas/u27-quality-manager.md),
[U21 Production planner](../../01-users/personas/u21-production-planner.md),
[U20 Production operator](../../01-users/personas/u20-production-operator.md),
[U15 Warehouse operator](../../01-users/personas/u15-warehouse-operator.md),
[U04 Purchasing](../../01-users/personas/u04-purchasing.md), [U03 Sales](../../01-users/personas/u03-sales.md),
[U06 HR](../../01-users/personas/u06-hr.md), [U07 Administrator](../../01-users/personas/u07-administrator.md),
[U13 Owner](../../01-users/personas/u13-owner.md).

## Capabilities used

- [F1 Administration](../../02-functional/f01-administration/README.md): users, roles and sites: the plants and the
  warehouse.
- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md): the sector pack's record types,
  approval chains for documents,
  [UC-F2-29](../../02-functional/f02-no-code-configuration/use-cases/11-rights-translations-and-approvals/uc-f02-29-set-up-an-approval-chain.md),
  offline scans.
- [F3 Assistant](../../02-functional/f03-assistant/README.md): questions on quality
  ([UC-SC05-15](use-cases/04-quality-system/uc-sc05-15-ask-the-assistant-about-quality.md)).
- [F4 Meetings](../../02-functional/f04-meetings/README.md): the management review recorded as a meeting.
- [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md): configurator quotes,
  [UC-F6-14](../../02-functional/f06-customers-and-sales/use-cases/05-benchmark-additions/uc-f06-14-configure-products-in-a-quote.md),
  and complaints.
- [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md): suppliers and their performance,
  lots, customer parts.
- [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md): training of operators.
- [F12 Manufacturing (plugin)](../../02-functional/f12-manufacturing/README.md): production, quality, calibration,
  qualifications and the shared recipes and batches,
  [UC-F12-31](../../02-functional/f12-manufacturing/use-cases/09-recipes-and-batches/uc-f12-31-define-a-recipe-and-produce-in-batches.md).
- [F14 Plugin store](../../02-functional/f14-plugin-store/README.md): the sector pack is installed and updated from the
  plugin store,
  [UC-F14-02](../../02-functional/f14-plugin-store/use-cases/01-find-and-install/uc-f14-02-install-a-plugin-or-sector-pack.md).
- Shared capabilities of [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md) this sector uses:
  [UC-F12-31 Define a recipe and produce in batches](../../02-functional/f12-manufacturing/use-cases/09-recipes-and-batches/uc-f12-31-define-a-recipe-and-produce-in-batches.md).

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

- [Manufacturing](../../01-users/example-companies/manufacturing.md)

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

⬅️ [Home care](../sc04-home-care/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Restaurant and hospitality](../sc06-hospitality/README.md)
