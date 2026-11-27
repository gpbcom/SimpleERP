🏠 [Specs](../../README.md) › 🎯 [Vision](../README.md) › 🛣️ [Roadmap and options](README.md) › 📦 What V1 holds

# 📦 What V1 holds

**Status:** ✅ specified

Everything V1 holds, counted from the specifications tree, with the step of the [adopted roadmap](roadmap.md) each part
sits in. It is the common ground of the [roadmap options](options/README.md): every option places each line of these
tables in one of its steps, and none leaves one out
([D3](../../06-decisions/foundations/d03-every-area-in-the-first-version.md),
[D380](../../06-decisions/vision/d380-every-capability-first-confirmed.md),
[D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)).

The use cases are the measure of size the options compare: a step's share is its use cases over the 1221 use cases of
the 25 capabilities and 20 sectors. Technical capabilities hold requirements, not use cases, and are compared by what
they serve.

## Totals

| Part | Count | Detail |
|---|---|---|
| Functional capabilities | 25 | 780 use cases, 675 business rules, 651 entities, 1396 screens |
| Technical capabilities | 13 | 104 requirements, plus 24 technical challenges |
| Sectors | 20 | 441 use cases, 390 business rules, 366 entities, 800 screens |
| Non-functional requirements | 20 | one page each |
| Technical design chapters | 25 | in seven themes of docs/technical |
| France country pack | 262 | rules in 26 themes |
| Personas | 56 | each with its views and journeys |
| Mock-up images | 49216 | every flow step, per persona, device and theme |

The dated pilot ([D451](../../06-decisions/vision/d451-dated-pilot-before-the-release.md)) runs F1 to F9: 293 use cases,
24 % of V1, on top of the whole platform.

## Gaps of the adopted roadmap

The adopted roadmap was written on 2026-11-12. Five points of it no longer matched the specifications; the owner
settled them on 2026-11-27 by adopting option A in twelve phases ([D569](../../06-decisions/vision/d569-roadmap-option-a-in-twelve-phases.md)):

- [T13 Maps and geodata](../../03-technical/t13-maps-and-geodata/README.md) (2026-11-13) has no step. It is part of the
  platform, so it belongs in step 2 ([D16](../../06-decisions/foundations/d16-platform-first.md)): it is built in P2.
- SC17 to SC20 (step 36n, 2026-11-14) have no step: [SC17](../../08-sectors/sc17-beauty-and-wellness/README.md),
  [SC18](../../08-sectors/sc18-sports-and-fitness/README.md),
  [SC19](../../08-sectors/sc19-trades-and-home-services/README.md),
  [SC20](../../08-sectors/sc20-public-bodies/README.md). They belong in step 9 with the other sectors: they are built in P10.
- The pilot ([D451](../../06-decisions/vision/d451-dated-pilot-before-the-release.md)) runs F1 to F9 once step 6 is
  built, but [F5](../../02-functional/f05-social-media/README.md) sits in step 8: either F5 moves before the pilot, or
  the pilot runs without it. Option A keeps F5 in step 8 (P9), so the pilot runs without it, and the phase calendar
  supersedes D451's date (D569).
- The [data migration](../../../technical/data/data-migration.md) chapter is not linked to any step, though the pilot
  company has to import its data first (D379, working in one day). It is built before the pilot, with the platform.
- The text of the adopted roadmap said T1 to T12 and 16 sectors; it now says T1 to T13 and 20 sectors.

## Functional capabilities

| Capability | Use cases | Rules | Entities | Flows | Screens | Technical capabilities used | Adopted step |
|---|---|---|---|---|---|---|---|
| [F1 Administration](../../02-functional/f01-administration/README.md) | 27 | 36 | 26 | 15 | 56 | [T1](../../03-technical/t01-companies-and-data-isolation/README.md), [T2](../../03-technical/t02-identity-and-access/README.md), [T3](../../03-technical/t03-audit-trail/README.md), [T6](../../03-technical/t06-mcp-and-a2a-gateway/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T10](../../03-technical/t10-translations-and-notifications/README.md) | 2 |
| [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md) | 35 | 32 | 34 | 13 | 69 | [T2](../../03-technical/t02-identity-and-access/README.md), [T3](../../03-technical/t03-audit-trail/README.md), [T4](../../03-technical/t04-plugin-runtime/README.md), [T5](../../03-technical/t05-api-and-webhooks/README.md) | 2 |
| [F3 Assistant](../../02-functional/f03-assistant/README.md) | 24 | 47 | 27 | 13 | 54 | [T2](../../03-technical/t02-identity-and-access/README.md), [T3](../../03-technical/t03-audit-trail/README.md), [T6](../../03-technical/t06-mcp-and-a2a-gateway/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T8](../../03-technical/t08-rag-platform/README.md) | 2 |
| [F4 Meetings](../../02-functional/f04-meetings/README.md) | 31 | 36 | 29 | 14 | 56 | [T2](../../03-technical/t02-identity-and-access/README.md), [T3](../../03-technical/t03-audit-trail/README.md), [T6](../../03-technical/t06-mcp-and-a2a-gateway/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T8](../../03-technical/t08-rag-platform/README.md) | 2 |
| [F5 Social media and marketing](../../02-functional/f05-social-media/README.md) | 28 | 23 | 25 | 10 | 53 | [T5](../../03-technical/t05-api-and-webhooks/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 8 |
| [F6 Customers and sales](../../02-functional/f06-customers-and-sales/README.md) | 31 | 23 | 27 | 10 | 55 | [T2](../../03-technical/t02-identity-and-access/README.md), [T3](../../03-technical/t03-audit-trail/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 3 |
| [F7 Purchasing and stock](../../02-functional/f07-purchasing-and-stock/README.md) | 30 | 24 | 27 | 10 | 57 | [T3](../../03-technical/t03-audit-trail/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 4 |
| [F8 Accounting](../../02-functional/f08-accounting/README.md) | 40 | 32 | 43 | 12 | 81 | [T3](../../03-technical/t03-audit-trail/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 5 |
| [F9 HR and projects](../../02-functional/f09-hr-and-projects/README.md) | 47 | 46 | 52 | 15 | 96 | [T2](../../03-technical/t02-identity-and-access/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 6 |
| [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md) | 32 | 26 | 24 | 12 | 55 | [T3](../../03-technical/t03-audit-trail/README.md), [T11](../../03-technical/t11-legal-corpora/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 7 |
| [F11 Online shop (plugin)](../../02-functional/f11-online-shop/README.md) | 33 | 28 | 27 | 11 | 59 | [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T11](../../03-technical/t11-legal-corpora/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 7 |
| [F12 Manufacturing (plugin)](../../02-functional/f12-manufacturing/README.md) | 35 | 30 | 33 | 14 | 67 | [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T11](../../03-technical/t11-legal-corpora/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 7 |
| [F13 Payroll (plugin)](../../02-functional/f13-payroll/README.md) | 38 | 28 | 31 | 10 | 62 | [T11](../../03-technical/t11-legal-corpora/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 7 |
| [F14 Plugin store](../../02-functional/f14-plugin-store/README.md) | 32 | 27 | 25 | 8 | 55 | [T4](../../03-technical/t04-plugin-runtime/README.md), [T11](../../03-technical/t11-legal-corpora/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 7 |
| [F15 Legal assistant](../../02-functional/f15-legal-assistant/README.md) | 20 | 24 | 21 | 7 | 39 | [T2](../../03-technical/t02-identity-and-access/README.md), [T3](../../03-technical/t03-audit-trail/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T8](../../03-technical/t08-rag-platform/README.md), [T11](../../03-technical/t11-legal-corpora/README.md) | 6 |
| [F16 Customer support agents](../../02-functional/f16-customer-support-agents/README.md) | 23 | 19 | 17 | 7 | 37 | [T3](../../03-technical/t03-audit-trail/README.md), [T6](../../03-technical/t06-mcp-and-a2a-gateway/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T8](../../03-technical/t08-rag-platform/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 3 |
| [F17 Competitive analysis](../../02-functional/f17-competitive-analysis/README.md) | 29 | 20 | 24 | 8 | 52 | [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T8](../../03-technical/t08-rag-platform/README.md), [T11](../../03-technical/t11-legal-corpora/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 8 |
| [F18 Hosted websites and domains (hosted edition)](../../02-functional/f18-hosted-websites-and-domains/README.md) | 31 | 25 | 23 | 7 | 54 | [T5](../../03-technical/t05-api-and-webhooks/README.md), [T9](../../03-technical/t09-install-backups-and-updates/README.md), [T10](../../03-technical/t10-translations-and-notifications/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 10 |
| [F19 Feature factory (hosted edition)](../../02-functional/f19-feature-factory/README.md) | 30 | 23 | 19 | 7 | 48 | [T4](../../03-technical/t04-plugin-runtime/README.md), [T5](../../03-technical/t05-api-and-webhooks/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T9](../../03-technical/t09-install-backups-and-updates/README.md) | 10 |
| [F20 Hosted support assistant (hosted edition)](../../02-functional/f20-hosted-support-assistant/README.md) | 32 | 23 | 21 | 8 | 53 | [T3](../../03-technical/t03-audit-trail/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T8](../../03-technical/t08-rag-platform/README.md), [T9](../../03-technical/t09-install-backups-and-updates/README.md) | 10 |
| [F21 Onboarding and module activation](../../02-functional/f21-onboarding-and-modules/README.md) | 29 | 20 | 21 | 6 | 48 | [T1](../../03-technical/t01-companies-and-data-isolation/README.md), [T4](../../03-technical/t04-plugin-runtime/README.md), [T10](../../03-technical/t10-translations-and-notifications/README.md), [T11](../../03-technical/t11-legal-corpora/README.md) | 2 |
| [F22 Unified platform cost management](../../02-functional/f22-unified-cost-management/README.md) | 30 | 21 | 21 | 8 | 51 | [T3](../../03-technical/t03-audit-trail/README.md), [T4](../../03-technical/t04-plugin-runtime/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 2 |
| [F23 What-if simulation and impact](../../02-functional/f23-what-if-simulation/README.md) | 34 | 21 | 17 | 8 | 45 | [T1](../../03-technical/t01-companies-and-data-isolation/README.md), [T6](../../03-technical/t06-mcp-and-a2a-gateway/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T11](../../03-technical/t11-legal-corpora/README.md) | 8 |
| [F24 Integrations hub](../../02-functional/f24-integrations-hub/README.md) | 31 | 20 | 19 | 8 | 48 | [T2](../../03-technical/t02-identity-and-access/README.md), [T6](../../03-technical/t06-mcp-and-a2a-gateway/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T12](../../03-technical/t12-connectors-and-scrapers/README.md) | 2 |
| [F25 DevOps agents (hosted edition)](../../02-functional/f25-devops-agents/README.md) | 28 | 21 | 18 | 7 | 46 | [T3](../../03-technical/t03-audit-trail/README.md), [T6](../../03-technical/t06-mcp-and-a2a-gateway/README.md), [T7](../../03-technical/t07-ai-providers-and-models/README.md), [T9](../../03-technical/t09-install-backups-and-updates/README.md) | 1 |

## Technical capabilities

| Capability | Requirements | Entities | Screens | Used by | Adopted step |
|---|---|---|---|---|---|
| [T1 Companies and data isolation](../../03-technical/t01-companies-and-data-isolation/README.md) | 8 | 4 | 8 | [F1](../../02-functional/f01-administration/README.md), [F21](../../02-functional/f21-onboarding-and-modules/README.md), [F23](../../02-functional/f23-what-if-simulation/README.md) | 2 |
| [T2 Identity and access engine](../../03-technical/t02-identity-and-access/README.md) | 7 | 4 | 8 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F15](../../02-functional/f15-legal-assistant/README.md), [F24](../../02-functional/f24-integrations-hub/README.md) | 2 |
| [T3 Audit trail](../../03-technical/t03-audit-trail/README.md) | 6 | 3 | 6 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../02-functional/f08-accounting/README.md), [F10](../../02-functional/f10-point-of-sale/README.md), [F15](../../02-functional/f15-legal-assistant/README.md), [F16](../../02-functional/f16-customer-support-agents/README.md), [F20](../../02-functional/f20-hosted-support-assistant/README.md), [F22](../../02-functional/f22-unified-cost-management/README.md), [F25](../../02-functional/f25-devops-agents/README.md) | 2 |
| [T4 Plugin runtime](../../03-technical/t04-plugin-runtime/README.md) | 8 | 4 | 8 | [F2](../../02-functional/f02-no-code-configuration/README.md), [F14](../../02-functional/f14-plugin-store/README.md), [F19](../../02-functional/f19-feature-factory/README.md), [F21](../../02-functional/f21-onboarding-and-modules/README.md), [F22](../../02-functional/f22-unified-cost-management/README.md) | 2 |
| [T5 API and webhooks](../../03-technical/t05-api-and-webhooks/README.md) | 7 | 4 | 8 | [F2](../../02-functional/f02-no-code-configuration/README.md), [F5](../../02-functional/f05-social-media/README.md), [F18](../../02-functional/f18-hosted-websites-and-domains/README.md), [F19](../../02-functional/f19-feature-factory/README.md) | 2 |
| [T6 MCP and A2A gateway](../../03-technical/t06-mcp-and-a2a-gateway/README.md) | 7 | 4 | 8 | [F1](../../02-functional/f01-administration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F16](../../02-functional/f16-customer-support-agents/README.md), [F23](../../02-functional/f23-what-if-simulation/README.md), [F24](../../02-functional/f24-integrations-hub/README.md), [F25](../../02-functional/f25-devops-agents/README.md) | 2 |
| [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md) | 8 | 4 | 8 | [F1](../../02-functional/f01-administration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F5](../../02-functional/f05-social-media/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F11](../../02-functional/f11-online-shop/README.md), [F12](../../02-functional/f12-manufacturing/README.md), [F15](../../02-functional/f15-legal-assistant/README.md), [F16](../../02-functional/f16-customer-support-agents/README.md), [F17](../../02-functional/f17-competitive-analysis/README.md), [F19](../../02-functional/f19-feature-factory/README.md), [F20](../../02-functional/f20-hosted-support-assistant/README.md), [F22](../../02-functional/f22-unified-cost-management/README.md), [F23](../../02-functional/f23-what-if-simulation/README.md), [F24](../../02-functional/f24-integrations-hub/README.md), [F25](../../02-functional/f25-devops-agents/README.md) | 2 |
| [T8 RAG platform (Milvus)](../../03-technical/t08-rag-platform/README.md) | 6 | 3 | 6 | [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F15](../../02-functional/f15-legal-assistant/README.md), [F16](../../02-functional/f16-customer-support-agents/README.md), [F17](../../02-functional/f17-competitive-analysis/README.md), [F20](../../02-functional/f20-hosted-support-assistant/README.md) | 2 |
| [T9 Install, backups and updates](../../03-technical/t09-install-backups-and-updates/README.md) | 8 | 4 | 8 | [F18](../../02-functional/f18-hosted-websites-and-domains/README.md), [F19](../../02-functional/f19-feature-factory/README.md), [F20](../../02-functional/f20-hosted-support-assistant/README.md), [F25](../../02-functional/f25-devops-agents/README.md) | 2 |
| [T10 Translations and notifications](../../03-technical/t10-translations-and-notifications/README.md) | 6 | 3 | 6 | [F1](../../02-functional/f01-administration/README.md), [F18](../../02-functional/f18-hosted-websites-and-domains/README.md), [F21](../../02-functional/f21-onboarding-and-modules/README.md) | 2 |
| [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md) | 6 | 4 | 8 | [F10](../../02-functional/f10-point-of-sale/README.md), [F11](../../02-functional/f11-online-shop/README.md), [F12](../../02-functional/f12-manufacturing/README.md), [F13](../../02-functional/f13-payroll/README.md), [F14](../../02-functional/f14-plugin-store/README.md), [F15](../../02-functional/f15-legal-assistant/README.md), [F17](../../02-functional/f17-competitive-analysis/README.md), [F21](../../02-functional/f21-onboarding-and-modules/README.md), [F23](../../02-functional/f23-what-if-simulation/README.md) | 2 |
| [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) | 19 | 7 | 14 | [F5](../../02-functional/f05-social-media/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F10](../../02-functional/f10-point-of-sale/README.md), [F11](../../02-functional/f11-online-shop/README.md), [F12](../../02-functional/f12-manufacturing/README.md), [F13](../../02-functional/f13-payroll/README.md), [F14](../../02-functional/f14-plugin-store/README.md), [F16](../../02-functional/f16-customer-support-agents/README.md), [F17](../../02-functional/f17-competitive-analysis/README.md), [F18](../../02-functional/f18-hosted-websites-and-domains/README.md), [F22](../../02-functional/f22-unified-cost-management/README.md), [F24](../../02-functional/f24-integrations-hub/README.md) | 2 |
| [T13 Maps and geodata](../../03-technical/t13-maps-and-geodata/README.md) | 8 | 4 | 5 | the whole suite (planning, maps, places) | 2 (D16, D569) |

## Technical challenges

The 24 hard problems of [03-technical/challenges](../../03-technical/challenges/README.md), with the capabilities that
cannot pass their acceptance criteria until each is solved, and the earliest adopted step that needs it.

| Challenge | Needed by | Earliest step |
|---|---|---|
| [TC-01 Isolation of companies at every layer](../../03-technical/challenges/tc-01-isolation-at-every-layer.md) | T1 | 2 |
| [TC-02 Modules switched on in one click, and a plugin-first core](../../03-technical/challenges/tc-02-modules-and-plugins-at-runtime.md) | T4, F21 | 2 |
| [TC-03 No-code configuration against schema and upgrades](../../03-technical/challenges/tc-03-no-code-configuration-and-schema.md) | F2 | 2 |
| [TC-04 The country pack as a versioned rule engine](../../03-technical/challenges/tc-04-country-pack-rule-engine.md) | T11, F6, F8 | 2 |
| [TC-05 Records that must never change, and those that must be erased](../../03-technical/challenges/tc-05-inalterable-and-certified-records.md) | T3, F8, F10 | 2 |
| [TC-06 Offline devices and synchronisation](../../03-technical/challenges/tc-06-offline-devices-and-sync.md) | F7, F9, F10 | 3 to 7 |
| [TC-07 The AI assistant can do everything, within the user's rights](../../03-technical/challenges/tc-07-ai-everywhere-within-rights.md) | F3 | 2 |
| [TC-08 Search and RAG that respect rights and erasure](../../03-technical/challenges/tc-08-permission-aware-search.md) | T8, F3, F15 | 2 |
| [TC-09 Local AI without a graphics card](../../03-technical/challenges/tc-09-local-ai-without-a-graphics-card.md) | T7 | 2 |
| [TC-10 Capturing meetings on outside platforms](../../03-technical/challenges/tc-10-meeting-capture.md) | F4 | 2 |
| [TC-11 Connectors, scrapers and the outside world](../../03-technical/challenges/tc-11-connectors-and-generated-scrapers.md) | T12, F5, F17 | 2 |
| [TC-12 Code written by an AI, running in production](../../03-technical/challenges/tc-12-generated-code-in-production.md) | F19, F25 | 1 |
| [TC-13 Hosted operations helped by an AI](../../03-technical/challenges/tc-13-operations-run-by-an-ai.md) | F20, F25 | 1 |
| [TC-14 Planning and calculation engines](../../03-technical/challenges/tc-14-planning-and-calculation-engines.md) | T13, F9, F12, F13 | 2 |
| [TC-15 Large lists, reports and dashboards](../../03-technical/challenges/tc-15-large-data-reports-and-lists.md) | F8, F22, every list view | 2 |
| [TC-16 Files, media and archives](../../03-technical/challenges/tc-16-files-media-and-archives.md) | T9, F8 | 2 |
| [TC-17 Security and compliance profiles](../../03-technical/challenges/tc-17-security-and-compliance-profiles.md) | T2 | 1 |
| [TC-18 Install, upgrade and migrate without a consultant](../../03-technical/challenges/tc-18-install-upgrade-and-migrate.md) | T9, F21 | 2 |
| [TC-19 Languages, currencies and countries](../../03-technical/challenges/tc-19-languages-currencies-and-countries.md) | T10, T11 | 2 |
| [TC-20 Testing a very wide product](../../03-technical/challenges/tc-20-testing-a-very-wide-product.md) | F25, every step | 1 |
| [TC-21 Metering every paid call, and stopping on a budget](../../03-technical/challenges/tc-21-metering-every-paid-call.md) | T7, F22 | 2 |
| [TC-22 Simulating the whole company on copies](../../03-technical/challenges/tc-22-simulation-on-copies.md) | F23 | 8 |
| [TC-23 Many connectors, connected in few steps, kept working](../../03-technical/challenges/tc-23-many-connectors-few-steps.md) | T12, F24 | 2 |
| [TC-24 Agents that read production and write code](../../03-technical/challenges/tc-24-agents-on-code-and-production.md) | F25 | 1 |

## Sectors

Every sector pack installs through the plugin store (F14) and no-code configuration (F2). The wave is the group of
sectors that become possible once the same capabilities are built (option D and option F use it): wave 1 needs only the
business areas, payroll and the store, wave 2 also needs the point of sale, the online shop or hosted websites, wave 3
also needs manufacturing.

| Sector | Use cases | Rules | Entities | Screens | Capabilities used | Wave | Adopted step |
|---|---|---|---|---|---|---|---|
| [SC01 Construction](../../08-sectors/sc01-construction/README.md) | 19 | 19 | 18 | 37 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F13](../../02-functional/f13-payroll/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 1 | 9 |
| [SC02 Retail](../../08-sectors/sc02-retail/README.md) | 19 | 19 | 16 | 35 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F10](../../02-functional/f10-point-of-sale/README.md), [F11](../../02-functional/f11-online-shop/README.md), [F13](../../02-functional/f13-payroll/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 2 | 9 |
| [SC03 Services](../../08-sectors/sc03-services/README.md) | 19 | 19 | 20 | 39 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F5](../../02-functional/f05-social-media/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F13](../../02-functional/f13-payroll/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 1 | 9 |
| [SC04 Home care](../../08-sectors/sc04-home-care/README.md) | 20 | 20 | 18 | 37 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F5](../../02-functional/f05-social-media/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F13](../../02-functional/f13-payroll/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 1 | 9 |
| [SC05 Manufacturing](../../08-sectors/sc05-manufacturing/README.md) | 19 | 19 | 18 | 37 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F12](../../02-functional/f12-manufacturing/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 3 | 9 |
| [SC06 Restaurant and hospitality](../../08-sectors/sc06-hospitality/README.md) | 21 | 21 | 18 | 38 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F10](../../02-functional/f10-point-of-sale/README.md), [F12](../../02-functional/f12-manufacturing/README.md), [F13](../../02-functional/f13-payroll/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 3 | 9 |
| [SC07 Transport and logistics](../../08-sectors/sc07-transport/README.md) | 24 | 19 | 21 | 45 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F13](../../02-functional/f13-payroll/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 1 | 9 |
| [SC08 Non-profit association](../../08-sectors/sc08-non-profit/README.md) | 24 | 19 | 19 | 41 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F5](../../02-functional/f05-social-media/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F8](../../02-functional/f08-accounting/README.md), [F10](../../02-functional/f10-point-of-sale/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 2 | 9 |
| [SC09 Health practices](../../08-sectors/sc09-health-practices/README.md) | 26 | 21 | 19 | 45 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../02-functional/f08-accounting/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 1 | 9 |
| [SC10 Real estate](../../08-sectors/sc10-real-estate/README.md) | 24 | 19 | 20 | 44 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F8](../../02-functional/f08-accounting/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 1 | 9 |
| [SC11 Professional firms](../../08-sectors/sc11-professional-firms/README.md) | 24 | 19 | 19 | 43 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F14](../../02-functional/f14-plugin-store/README.md), [F15](../../02-functional/f15-legal-assistant/README.md) | 1 | 9 |
| [SC12 Education and training](../../08-sectors/sc12-education-and-training/README.md) | 24 | 19 | 23 | 46 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F5](../../02-functional/f05-social-media/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F11](../../02-functional/f11-online-shop/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 2 | 9 |
| [SC13 Agriculture and food](../../08-sectors/sc13-agriculture-and-food/README.md) | 25 | 20 | 21 | 46 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F10](../../02-functional/f10-point-of-sale/README.md), [F12](../../02-functional/f12-manufacturing/README.md), [F13](../../02-functional/f13-payroll/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 3 | 9 |
| [SC14 IT and software](../../08-sectors/sc14-it-and-software/README.md) | 25 | 19 | 20 | 44 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F13](../../02-functional/f13-payroll/README.md), [F14](../../02-functional/f14-plugin-store/README.md), [F16](../../02-functional/f16-customer-support-agents/README.md), [F24](../../02-functional/f24-integrations-hub/README.md) | 1 | 9 |
| [SC15 Wholesale and distribution](../../08-sectors/sc15-wholesale-and-distribution/README.md) | 24 | 19 | 17 | 40 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F11](../../02-functional/f11-online-shop/README.md), [F13](../../02-functional/f13-payroll/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 2 | 9 |
| [SC16 Events and culture](../../08-sectors/sc16-events-and-culture/README.md) | 24 | 19 | 22 | 46 | [F1](../../02-functional/f01-administration/README.md), [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F5](../../02-functional/f05-social-media/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F10](../../02-functional/f10-point-of-sale/README.md), [F13](../../02-functional/f13-payroll/README.md), [F14](../../02-functional/f14-plugin-store/README.md) | 2 | 9 |
| [SC17 Beauty and wellness](../../08-sectors/sc17-beauty-and-wellness/README.md) | 20 | 20 | 13 | 33 | [F4](../../02-functional/f04-meetings/README.md), [F5](../../02-functional/f05-social-media/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F10](../../02-functional/f10-point-of-sale/README.md), [F11](../../02-functional/f11-online-shop/README.md), [F13](../../02-functional/f13-payroll/README.md) | 2 | 9 (D569) |
| [SC18 Sports and fitness](../../08-sectors/sc18-sports-and-fitness/README.md) | 20 | 20 | 16 | 36 | [F4](../../02-functional/f04-meetings/README.md), [F5](../../02-functional/f05-social-media/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F10](../../02-functional/f10-point-of-sale/README.md), [F13](../../02-functional/f13-payroll/README.md) | 2 | 9 (D569) |
| [SC19 Trades and home services](../../08-sectors/sc19-trades-and-home-services/README.md) | 20 | 20 | 13 | 33 | [F2](../../02-functional/f02-no-code-configuration/README.md), [F4](../../02-functional/f04-meetings/README.md), [F6](../../02-functional/f06-customers-and-sales/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F13](../../02-functional/f13-payroll/README.md) | 1 | 9 (D569) |
| [SC20 Public bodies](../../08-sectors/sc20-public-bodies/README.md) | 20 | 20 | 15 | 35 | [F2](../../02-functional/f02-no-code-configuration/README.md), [F3](../../02-functional/f03-assistant/README.md), [F4](../../02-functional/f04-meetings/README.md), [F7](../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../02-functional/f08-accounting/README.md), [F9](../../02-functional/f09-hr-and-projects/README.md), [F11](../../02-functional/f11-online-shop/README.md), [F13](../../02-functional/f13-payroll/README.md), [F18](../../02-functional/f18-hosted-websites-and-domains/README.md) | 2 | 9 (D569) |

## Non-functional requirements

The earliest adopted step that must meet each requirement.

| Requirement | Earliest step |
|---|---|
| [Accessibility](../../05-non-functional/accessibility.md) | 2 |
| [AI governance](../../05-non-functional/ai-governance.md) | 1 |
| [Availability](../../05-non-functional/availability.md) | 2 |
| [Backups](../../05-non-functional/backups.md) | 2 |
| [Data isolation](../../05-non-functional/data-isolation.md) | 2 |
| [Data retention](../../05-non-functional/data-retention.md) | 2 |
| [E-invoicing platforms](../../05-non-functional/e-invoicing-platforms.md) | 5 |
| [Installation](../../05-non-functional/installation.md) | 2 |
| [Legal advice limits](../../05-non-functional/legal-advice-limits.md) | 6 |
| [Legal rules in France](../../05-non-functional/legal-france.md) | 3 to 6 |
| [Localisation](../../05-non-functional/localisation.md) | 2 |
| [Meeting assistant benchmark](../../05-non-functional/meeting-assistant-benchmark.md) | 2 |
| [Meeting recording](../../05-non-functional/meeting-recording.md) | 2 |
| [Observability](../../05-non-functional/observability.md) | 1 and 2 |
| [Performance](../../05-non-functional/performance.md) | 2 |
| [Privacy and GDPR](../../05-non-functional/privacy-gdpr.md) | 2 |
| [Scalability](../../05-non-functional/scalability.md) | 2 |
| [Sector technical standards](../../05-non-functional/sector-technical-standards.md) | 9 |
| [Security](../../05-non-functional/security.md) | 1 |
| [Updates](../../05-non-functional/updates.md) | 2 |

## Technical design chapters

The chapters of [docs/technical](../../../technical/README.md) the adopted roadmap links to each step; their target
designs are built when that step starts.

| Chapter | Theme | Adopted step |
|---|---|---|
| [development process](../../../technical/delivery/development-process.md) | delivery | 1 |
| [ci cd and stages](../../../technical/delivery/ci-cd-and-stages.md) | delivery | 1 |
| [tests and traceability](../../../technical/delivery/tests-and-traceability.md) | delivery | 1 |
| [repository layout](../../../technical/architecture/repository-layout.md) | architecture | 1 |
| [infrastructure](../../../technical/infrastructure/infrastructure.md) | infrastructure | 1 |
| [devops](../../../technical/operations/devops.md) | operations | 1 |
| [ai operations](../../../technical/operations/ai-operations.md) | operations | 1 |
| [supply chain and licences](../../../technical/security/supply-chain-and-licences.md) | security | 1 |
| [security](../../../technical/security/security.md) | security | 1 and 2 |
| [architecture](../../../technical/architecture/architecture.md) | architecture | 2 |
| [backend](../../../technical/architecture/backend.md) | architecture | 2 |
| [frontend](../../../technical/architecture/frontend.md) | architecture | 2 |
| [configuration](../../../technical/architecture/configuration.md) | architecture | 2 |
| [api](../../../technical/interfaces/api.md) | interfaces | 2 |
| [mcp](../../../technical/interfaces/mcp.md) | interfaces | 2 |
| [a2a](../../../technical/interfaces/a2a.md) | interfaces | 2 |
| [plugin sdk](../../../technical/interfaces/plugin-sdk.md) | interfaces | 2 |
| [data model](../../../technical/data/data-model.md) | data | 2 |
| [storage](../../../technical/data/storage.md) | data | 2 |
| [observability](../../../technical/operations/observability.md) | operations | 2 |
| [operations](../../../technical/operations/operations.md) | operations | 2 |
| [performance and capacity](../../../technical/infrastructure/performance-and-capacity.md) | infrastructure | 2 |
| [deployment](../../../technical/infrastructure/deployment.md) | infrastructure | 2 |
| [release and versioning](../../../technical/delivery/release-and-versioning.md) | delivery | 2 |
| [data migration](../../../technical/data/data-migration.md) | data | none: needed before the pilot imports its data (D451, D379) |

## France country pack

Every legal rule comes from the pack ([D8](../../06-decisions/foundations/d08-france-first.md), France first); a
capability passes its acceptance criteria only with the rules of its themes. The sector themes come with their sector
packs.

| Theme | Rules | Needed by |
|---|---|---|
| [Accounting](../../10-country-packs/france/accounting/README.md) | 13 | F8 |
| [Agriculture](../../10-country-packs/france/agriculture/README.md) | 6 | its sector pack |
| [AI and recording](../../10-country-packs/france/ai-and-recording/README.md) | 5 | F3, F4 |
| [Company identity](../../10-country-packs/france/company/README.md) | 6 | F1 |
| [Construction](../../10-country-packs/france/construction/README.md) | 9 | its sector pack |
| [Consumer](../../10-country-packs/france/consumer/README.md) | 19 | F6, F11 |
| [Data protection](../../10-country-packs/france/data-protection/README.md) | 14 | F1, T3 |
| [Digital](../../10-country-packs/france/digital/README.md) | 10 | F5, F11, F18 |
| [Education](../../10-country-packs/france/education/README.md) | 9 | its sector pack |
| [Environment](../../10-country-packs/france/environment/README.md) | 4 | F7, F12 |
| [Events](../../10-country-packs/france/events/README.md) | 6 | its sector pack |
| [Health practice](../../10-country-packs/france/health-practice/README.md) | 12 | its sector pack |
| [Home care](../../10-country-packs/france/home-care/README.md) | 6 | its sector pack |
| [Hospitality](../../10-country-packs/france/hospitality/README.md) | 4 | its sector pack |
| [Invoicing](../../10-country-packs/france/invoicing/README.md) | 13 | F6, F8 |
| [Labour](../../10-country-packs/france/labour/README.md) | 31 | F9, F15 |
| [Non-profit](../../10-country-packs/france/non-profit/README.md) | 5 | its sector pack |
| [Payments](../../10-country-packs/france/payments/README.md) | 4 | F6, F8 |
| [Payroll](../../10-country-packs/france/payroll/README.md) | 7 | F13 |
| [Point of sale](../../10-country-packs/france/point-of-sale/README.md) | 10 | F10 |
| [Products and traceability](../../10-country-packs/france/products/README.md) | 7 | F7 |
| [Professional firms](../../10-country-packs/france/professional-firms/README.md) | 11 | its sector pack |
| [Real estate](../../10-country-packs/france/real-estate/README.md) | 13 | its sector pack |
| [Tax and VAT](../../10-country-packs/france/tax-and-vat/README.md) | 18 | F6, F8 |
| [Trade](../../10-country-packs/france/trade/README.md) | 10 | F7, F15 |
| [Transport](../../10-country-packs/france/transport/README.md) | 10 | its sector pack |

## UX

The [design system, visual identity, views and mock-ups](../../04-ux/README.md) apply to every screen: the design system
and the views of the personas are built in step 2, each capability's screens with the capability.

---

⬅️ [Roadmap](roadmap.md) · ⬆️ [Up](README.md) · ➡️ [Roadmap options](options/README.md)
