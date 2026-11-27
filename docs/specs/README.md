# 🏠 SimpleERP specifications

**Status:** 🔄 being written, from the owner's interview (ticket GH-2)

## Vision

**SimpleERP is one open, sovereign tool that runs the whole company, and its AI does the work.**

SimpleERP is an open-source ERP for small and medium companies, whatever their field. It is fully self-hosted,
extendable, and AI-native. Read the whole vision in [🎯 Vision](00-vision/README.md).

| | Section | What it holds |
|---|---|---|
| 🎯 | [Vision](00-vision/README.md) | What SimpleERP is, the problem, objectives, positioning, licence, roadmap, glossary |
| 👤 | [Users](01-users/README.md) | The personas, the ready-made roles, the example companies |
| 🧩 | [Functional capabilities](02-functional/README.md) | What users do: F1 to F25, each with its use cases, flows, rules, data and screens |
| ⚙️ | [Technical capabilities](03-technical/README.md) | What the platform provides: T1 to T13, each with its requirements and interfaces |
| 🎨 | [UX](04-ux/README.md) | Principles, visual identity, design system, views and journeys per persona |
| 📏 | [Non-functional requirements](05-non-functional/README.md) | Performance, security, privacy, backups, accessibility, legal rules |
| 📜 | [Decisions](06-decisions/README.md) | Every decision taken, one file each |
| ❓ | [Questions](07-questions/README.md) | Every open or answered question, one file each |
| 🏷️ | [Sectors](08-sectors/README.md) | The 16 company types: what each adds, and its sector pack |
| ⏳ | [Waiting for the owner](09-waiting/README.md) | Pages waiting for the owner's confirmation, and the open questions |
| 🌍 | [Country packs](10-country-packs/README.md) | Each country's law and the legal rules SimpleERP enforces there |
| 🧱 | [Templates](_templates/README.md) | The shape of each kind of page |

## Status board

Updated after every interview round. Build steps ([roadmap](00-vision/roadmap/roadmap.md), D483): 1 DevOps agents, 2
platform, 3 customers and sales, 4 purchasing and stock, 5 accounting, 6 HR, projects and the legal assistant, 7
plugins and the store, 8 growth and insight, 9 sectors, 10 hosted services. Everything is in V1.

### Users and UX

| | Item | Status |
|---|---|---|
| 👥 | [Personas](01-users/personas/README.md) | ✅ |
| 🏢 | [Example companies](01-users/example-companies/README.md) | ✅ |
| 🎨 | [Visual identity](04-ux/visual-identity/README.md) | ✅ |
| 📐 | [Design system](04-ux/design-system/README.md) | ✅ |
| 🪟 | [Views and journeys](04-ux/views/README.md) | ✅ |

### Functional capabilities

| | ID | Capability | Build step | Status |
|---|---|---|---|---|
| 🛡️ | F1 | [Administration](02-functional/f01-administration/README.md) | 2 | ✅ |
| 🔧 | F2 | [No-code configuration](02-functional/f02-no-code-configuration/README.md) | 2 | ✅ |
| 🤖 | F3 | [Assistant](02-functional/f03-assistant/README.md) | 2 | ✅ |
| 🎙️ | F4 | [Meetings](02-functional/f04-meetings/README.md) | 2 | ✅ |
| 📣 | F5 | [Social media and marketing](02-functional/f05-social-media/README.md) | 8 | ✅ |
| 🛒 | F6 | [Customers and sales](02-functional/f06-customers-and-sales/README.md) | 3 | ✅ |
| 📦 | F7 | [Purchasing and stock](02-functional/f07-purchasing-and-stock/README.md) | 4 | ✅ |
| 📒 | F8 | [Accounting](02-functional/f08-accounting/README.md) | 5 | ✅ |
| 👥 | F9 | [HR and projects](02-functional/f09-hr-and-projects/README.md) | 6 | ✅ |
| 🏪 | F10 | [Point of sale (plugin)](02-functional/f10-point-of-sale/README.md) | 7 | ✅ |
| 🛍️ | F11 | [Online shop (plugin)](02-functional/f11-online-shop/README.md) | 7 | ✅ |
| 🏭 | F12 | [Manufacturing (plugin)](02-functional/f12-manufacturing/README.md) | 7 | ✅ |
| 💶 | F13 | [Payroll (plugin)](02-functional/f13-payroll/README.md) | 7 | ✅ |
| 🧰 | F14 | [Plugin store](02-functional/f14-plugin-store/README.md) | 7 | ✅ |
| ⚖️ | F15 | [Legal assistant](02-functional/f15-legal-assistant/README.md) | 6 | ✅ |
| 🎧 | F16 | [Customer support agents](02-functional/f16-customer-support-agents/README.md) | 3 | ✅ |
| 🔭 | F17 | [Competitive analysis](02-functional/f17-competitive-analysis/README.md) | 8 | ✅ |
| 🌐 | F18 | [Hosted websites and domains (hosted edition)](02-functional/f18-hosted-websites-and-domains/README.md) | 10 | ✅ |
| 🏭 | F19 | [Feature factory (hosted edition)](02-functional/f19-feature-factory/README.md) | 10 | ✅ |
| 🛟 | F20 | [Hosted support assistant (hosted edition)](02-functional/f20-hosted-support-assistant/README.md) | 10 | ✅ |
| 🧭 | F21 | [Onboarding and module activation](02-functional/f21-onboarding-and-modules/README.md) | 2 | ✅ |
| 💸 | F22 | [Unified platform cost management](02-functional/f22-unified-cost-management/README.md) | 2 | ✅ |
| 🔮 | F23 | [What-if simulation and impact](02-functional/f23-what-if-simulation/README.md) | 8 | ✅ |
| 🔌 | F24 | [Integrations hub](02-functional/f24-integrations-hub/README.md) | 2 | ✅ |
| 🤖 | F25 | [DevOps agents (hosted edition)](02-functional/f25-devops-agents/README.md) | 1 | ✅ |

### Sectors

Interviewed after F12 (D115).

| | ID | Sector | Status |
|---|---|---|---|
| 🏗️ | SC01 | [Construction](08-sectors/sc01-construction/README.md) | ✅ |
| 🛍️ | SC02 | [Retail](08-sectors/sc02-retail/README.md) | ✅ |
| 💼 | SC03 | [Services](08-sectors/sc03-services/README.md) | ✅ |
| 🏠 | SC04 | [Home care](08-sectors/sc04-home-care/README.md) | ✅ |
| 🏭 | SC05 | [Manufacturing](08-sectors/sc05-manufacturing/README.md) | ✅ |
| 🍽️ | SC06 | [Restaurant and hospitality](08-sectors/sc06-hospitality/README.md) | ✅ |
| 🚛 | SC07 | [Transport and logistics](08-sectors/sc07-transport/README.md) | ✅ |
| 🤲 | SC08 | [Non-profit association](08-sectors/sc08-non-profit/README.md) | ✅ |
| 🩺 | SC09 | [Health practices](08-sectors/sc09-health-practices/README.md) | ✅ |
| 🏘️ | SC10 | [Real estate](08-sectors/sc10-real-estate/README.md) | ✅ |
| ⚖️ | SC11 | [Professional firms](08-sectors/sc11-professional-firms/README.md) | ✅ |
| 🎓 | SC12 | [Education and training](08-sectors/sc12-education-and-training/README.md) | ✅ |
| 🌾 | SC13 | [Agriculture and food](08-sectors/sc13-agriculture-and-food/README.md) | ✅ |
| 💻 | SC14 | [IT and software](08-sectors/sc14-it-and-software/README.md) | ✅ |
| 📦 | SC15 | [Wholesale and distribution](08-sectors/sc15-wholesale-and-distribution/README.md) | ✅ |
| 🎭 | SC16 | [Events and culture](08-sectors/sc16-events-and-culture/README.md) | ✅ |

### Technical capabilities

| | ID | Capability | Status |
|---|---|---|---|
| 🏢 | T1 | [Companies and data isolation](03-technical/t01-companies-and-data-isolation/README.md) | ✅ |
| 🔐 | T2 | [Identity and access engine](03-technical/t02-identity-and-access/README.md) | ✅ |
| 🧾 | T3 | [Audit trail](03-technical/t03-audit-trail/README.md) | ✅ |
| 🔌 | T4 | [Plugin runtime](03-technical/t04-plugin-runtime/README.md) | ✅ |
| 🔗 | T5 | [API and webhooks](03-technical/t05-api-and-webhooks/README.md) | ✅ |
| 🛰️ | T6 | [MCP and A2A gateway](03-technical/t06-mcp-and-a2a-gateway/README.md) | ✅ |
| 🧠 | T7 | [AI providers and models](03-technical/t07-ai-providers-and-models/README.md) | ✅ |
| 📚 | T8 | [RAG platform (Milvus)](03-technical/t08-rag-platform/README.md) | ✅ |
| 🚀 | T9 | [Install, backups and updates](03-technical/t09-install-backups-and-updates/README.md) | ✅ |
| 🌐 | T10 | [Translations and notifications](03-technical/t10-translations-and-notifications/README.md) | ✅ |
| 🏛️ | T11 | [Legal corpora](03-technical/t11-legal-corpora/README.md) | ✅ |
| 🕸️ | T12 | [Connectors and scrapers](03-technical/t12-connectors-and-scrapers/README.md) | ✅ |
| 🗺️ | T13 | [Maps and geodata](03-technical/t13-maps-and-geodata/README.md) | 🔄 |

## Waiting for the owner

1638 pages hold items waiting for the owner's confirmation, and the open questions: see
[Waiting for the owner](09-waiting/README.md).

## How to read

- **Start here,** then follow the tiles. Every page starts with a breadcrumb (🏠 › section › page) and ends with
  ⬅️ previous · ⬆️ up · ➡️ next links.
- **Functional or technical:** a functional capability (F) is something a user does; a technical capability (T) is
  something the platform provides to the functional ones.
- **One file per item:** each use case, flow, business rule, entity, screen, journey, component, requirement,
  decision and question has its own page, its own ID, and links to the items it relates to.
- **Templates:** each kind of page has the shape of its template in [🧱 Templates](_templates/README.md).
- **Diagrams** are Mermaid blocks. They render on GitHub, and in VS Code with a Mermaid preview extension.
- **Nothing is invented:** what the owner has not answered is a question in [❓ Questions](07-questions/README.md),
  and what Claude proposes is marked "(Proposed)" until the owner confirms it.
- **IDs never change** and are never reused: U01 personas, UC-F6-01 use cases, BR-F6-01 rules, E-F6-01 entities, S-F6-01
  screens, FL-F6-01 flows, J-U03-01 journeys, REQ-T2-01 requirements, C-01 components, D1 decisions, Q1 questions.

## Icon legend

| Icon | Meaning |
|---|---|
| ✅ | Specified: confirmed by the owner |
| 🔄 | Being interviewed, or waiting for the owner's confirmation of its "(Proposed)" items (listed in [Waiting for the owner](09-waiting/README.md)) |
| ⬜ | To specify |
| ❓ | Open question (legend) |
| 🚫 | Out of scope, or withdrawn |
| 🎯 👤 🧩 ⚙️ 🎨 📏 📜 | Vision, users, functional, technical, UX, non-functional, decisions |
| 📝 🔀 📏 🗃️ 🖥️ 🧭 📌 | Use case, flow, business rule, entity, screen, journey, requirement |

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 🧱 |  | [Templates](_templates/README.md) | ⬜ |
| 🎯 |  | [Vision](00-vision/README.md) | ✅ |
| 👤 |  | [Users](01-users/README.md) | ✅ |
| 🧩 |  | [Functional capabilities](02-functional/README.md) | ✅ |
| ⚙️ |  | [Technical capabilities](03-technical/README.md) | 🔄 |
| 🎨 |  | [UX](04-ux/README.md) | ✅ |
| 📏 |  | [Non-functional requirements](05-non-functional/README.md) | ⬜ |
| 📜 |  | [Decisions](06-decisions/README.md) | ✅ |
| ❓ |  | [Questions](07-questions/README.md) | ✅ |
| 🏷️ |  | [Sectors](08-sectors/README.md) | ✅ |
| ⏳ |  | [Waiting for the owner](09-waiting/README.md) | 🔄 |
| 🌍 |  | [Country packs](10-country-packs/README.md) | ✅ |
