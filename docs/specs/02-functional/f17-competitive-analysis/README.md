🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🔭 F17 Competitive analysis

# 🔭 F17 Competitive analysis

**Status:** ✅ specified

Build step: 8. Growth and insight.

## Summary

Following the customers' own competitors from every lawful public and paid source: profiles, products and prices,
hiring, tenders, intellectual property, reviews, news and deals, compared side by side, turned into sourced SWOT, battle
cards and win-loss analysis, with alerts and digests
([D382](../../06-decisions/f17-competitive-analysis/d382-competitive-analysis-coverage.md),
[D383](../../06-decisions/f17-competitive-analysis/d383-competitive-sources-lawful.md)).

## Scope

- **Follow:** the competitor list, profiles from registers and filings, paid data providers.
- **Signals:** products and prices, job offers, tenders won, patents and trademarks, reviews, news, social media,
  funding and legal events.
- **Analyse:** side-by-side comparison, SWOT and positioning, market shares, battle cards, win and loss from F6 deals.
- **Share:** alerts, digests, restricted access, the AI assistant.
- **Opportunities and money:** tender watch, data costs against F22 budgets, price-index suggestions to F6 with
  approval, battle cards fed by F4's call topics, share of voice and index reports (D474).

## Personas

[U13 Owner](../../01-users/personas/u13-owner.md), [U12 Marketing](../../01-users/personas/u12-marketing.md),
[U03 Sales](../../01-users/personas/u03-sales.md), [U02 Manager](../../01-users/personas/u02-manager.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md).

## Out of scope

- SimpleERP's own benchmark of competing ERPs: the vision's [benchmark](../../00-vision/benchmark/benchmark.md).
- Following individual people.
- Building the connectors and scrapers: T12.

## Technical capabilities used

- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (sources, providers)
- [T8 RAG platform (Milvus)](../../03-technical/t08-rag-platform/README.md) (facts and citations)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md)
- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md) (the country pack)

## Build step

Step 8, Growth and insight, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the
specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | ✅ |
| 📏 |  | [Business rules](business-rules/README.md) | ✅ |
| 🗃️ |  | [Data](data/README.md) | ✅ |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | ✅ |

---

⬅️ [Customer support agents](../f16-customer-support-agents/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Hosted websites and domains (hosted edition)](../f18-hosted-websites-and-domains/README.md)
