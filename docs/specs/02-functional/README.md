🏠 [Specs](../README.md) › 🧩 Functional capabilities

# 🧩 Functional capabilities

**Status:** ✅ specified

What users do. One folder per capability.

## Business areas

Every area below is in the first version, built on the platform described in [Capabilities](#build-order). The
first four are built in this order, each one using the previous ones:

1. **Customers and sales:** customers and contacts, quotes, orders, invoices, payments received.
2. **Purchasing and stock:** suppliers, purchase orders, receipts, stock levels and movements.
3. **Accounting:** ledger, VAT, bank reconciliation, accounting exports.
4. **HR and projects:** employees, time off, timesheets, projects and their profitability.

Also in the first version, built last as plugins: **point of sale**, an **online shop**, **manufacturing** and
**payroll**.

## Extension

- **No-code configuration:** a business user adds custom fields, statuses, forms, document templates and simple
  workflows from the screens, without a developer.
- **Plugins:** developers write installable modules (entities, screens, business rules) against a stable API, without
  changing the core.
- **API and webhooks:** a documented REST API and webhooks for other tools, such as an online shop, a bank or BI.
- **Sector packs:** ready-made sets of configuration and plugins that adapt the ERP to one field, such as
  construction, retail, services or home care.
- **MCP and A2A, both ways:** the ERP calls external MCP servers and A2A agents (GitHub, Crunchbase…) set up by an
  administrator, and it is itself an MCP server and an A2A agent, so that external assistants can query it and act on
  it within the user's permissions.

## AI

- **Assistant:** a chatbot that answers questions from the knowledge held in the ERP, within the user's permissions.
- **Meetings:** transcripts and summaries of Google Meet, Microsoft Teams and Zoom meetings, with summaries each user
  can customise to their needs. A meeting comes in two ways:
  - imported from the transcript or recording the platform already made, through the user's linked account;
  - recorded by a self-hosted bot that joins the meeting as a participant.
- **Where the AI runs:** local open models by default, so that no data leaves the server. An administrator may switch
  a feature to an external provider (such as Claude, OpenAI or Mistral) with their own key.

## Build order

See the [roadmap](../00-vision/roadmap/roadmap.md) for the build steps of every capability.

**Plugins prove the platform:** X1 to X4 are built only on the public plugin API, like a third party would. Whatever
they need that the API lacks is added to the API, never reached around it. X1 to X4 are now F10 to F13. See
[D26](../06-decisions/foundations/d26-technical-and-functional-capabilities.md).

## Dependency graph

⬜ To be specified.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 🛡️ | F1 | [Administration](f01-administration/README.md) | ✅ |
| 🔧 | F2 | [No-code configuration](f02-no-code-configuration/README.md) | ✅ |
| 🤖 | F3 | [Assistant](f03-assistant/README.md) | ✅ |
| 🎙️ | F4 | [Meetings](f04-meetings/README.md) | ✅ |
| 📣 | F5 | [Social media](f05-social-media/README.md) | ✅ |
| 🛒 | F6 | [Customers and sales](f06-customers-and-sales/README.md) | ✅ |
| 📦 | F7 | [Purchasing and stock](f07-purchasing-and-stock/README.md) | ✅ |
| 📒 | F8 | [Accounting](f08-accounting/README.md) | ✅ |
| 👥 | F9 | [HR and projects](f09-hr-and-projects/README.md) | ✅ |
| 🏪 | F10 | [Point of sale (plugin)](f10-point-of-sale/README.md) | ✅ |
| 🛍️ | F11 | [Online shop (plugin)](f11-online-shop/README.md) | ✅ |
| 🏭 | F12 | [Manufacturing (plugin)](f12-manufacturing/README.md) | ✅ |
| 💶 | F13 | [Payroll (plugin)](f13-payroll/README.md) | ✅ |
| 🧰 | F14 | [Plugin store](f14-plugin-store/README.md) | ✅ |
| ⚖️ | F15 | [Legal assistant](f15-legal-assistant/README.md) | ✅ |
| 🎧 | F16 | [Customer support agents](f16-customer-support-agents/README.md) | 🔄 |
| 🔭 | F17 | [Competitive analysis](f17-competitive-analysis/README.md) | ✅ |
| 🌐 | F18 | [Hosted websites and domains (hosted edition)](f18-hosted-websites-and-domains/README.md) | ✅ |
| 🏭 | F19 | [Feature factory (hosted edition)](f19-feature-factory/README.md) | ✅ |
| 🛟 | F20 | [Hosted support assistant (hosted edition)](f20-hosted-support-assistant/README.md) | ✅ |
| 🧭 | F21 | [Onboarding and module activation](f21-onboarding-and-modules/README.md) | ✅ |
| 💸 | F22 | [Unified platform cost management](f22-unified-cost-management/README.md) | ✅ |
| 🔮 | F23 | [What-if simulation and impact](f23-what-if-simulation/README.md) | ✅ |
| 🔌 | F24 | [Integrations hub](f24-integrations-hub/README.md) | ✅ |
| 🤖 | F25 | [DevOps agents (hosted edition)](f25-devops-agents/README.md) | ✅ |

After F21: the [technical challenges](../03-technical/challenges/README.md) these capabilities bring to the platform.

---

⬅️ [Users](../01-users/README.md) · ⬆️ [Up](../README.md) · ➡️ [Technical capabilities](../03-technical/README.md)
