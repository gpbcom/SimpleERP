🏠 [Specs](../../README.md) › 🎯 [Vision](../README.md) › 💡 [Product](README.md) › 🧭 Positioning

# 🧭 Positioning

**Status:** ✅ specified

## Existing ERPs

Odoo, ERPNext and Dolibarr can already be self-hosted.

## What makes simple-ERP different

simple-ERP differs on five points:

- **Simpler to use:** a small company sets it up and learns it without a consultant.
- **Modern and API-first:** micro-services, a documented API, modern front ends and containers.
- **Truly open:** AGPL-3.0, with no paid edition holding back features. Only the publisher's hosting services are closed
  ([D388](../../06-decisions/vision/d388-hosted-edition-open-core.md)). Every ERP feature stays open and self-hostable;
  the hosted edition adds closed services that run the hosting: websites and domains, the feature factory, the support
  assistant and the DevOps agents (F18, F19, F20 and F25); country-pack updates are free for everyone
  ([D447](../../06-decisions/vision/d447-country-pack-updates-free-hosted-only-named.md)).
- **AI-native:** see [AI](../../02-functional/README.md#ai).
- **A product of its own:** support, hosting, installation and sector packs can be sold around it.

Two more differences came with ticket GH-2: the legal assistant
([D28](../../06-decisions/foundations/d28-legal-assistant.md)) and the social media module. See
[D29](../../06-decisions/foundations/d29-social-media-module.md).

Five more came on 2026-11-12:

- 🔭 **Competitive analysis** of the customer's own competitors, from every lawful source
  ([F17](../../02-functional/f17-competitive-analysis/README.md));
- 🌐 **A website and domain generated** from the ERP's data, tested before it goes live
  ([F18](../../02-functional/f18-hosted-websites-and-domains/README.md));
- 🏭 **A feature factory:** a chatbot that builds a missing feature as a plugin, which other hosted customers can use,
  its author earning half of its price ([F19](../../02-functional/f19-feature-factory/README.md));
- 🛟 **A support assistant** that talks to non-technical people and fixes with an engineer's yes
  ([F20](../../02-functional/f20-hosted-support-assistant/README.md));
- 🧭 **Set up by a non-technical person,** step by step, each module in one click
  ([F21](../../02-functional/f21-onboarding-and-modules/README.md)).

Then four more:

- 💸 **Every paid usage in one place,** AI, connectors, scraping and subscriptions, with budgets that warn then stop
  ([F22](../../02-functional/f22-unified-cost-management/README.md));
- 🔮 **What if?** Any change simulated on a copy of the company, its impact on every area shown, also from the AI
  assistant ([F23](../../02-functional/f23-what-if-simulation/README.md));
- 🔌 **Connected to the European office suites** openDesk and La Suite numérique, and to 50 ATS and CRM by default, each
  in a few steps ([F24](../../02-functional/f24-integrations-hub/README.md));
- 🤖 **Customers' requests handled by DevOps agents,** from report to pull request, maintainers approving
  ([F25](../../02-functional/f25-devops-agents/README.md)).

## The stance

🛡️ Sovereign, 🤖 AI-native and 🧩 one fully integrated suite that replaces them all
([D373](../../06-decisions/vision/d373-sovereign-ai-native-suite.md)): the ERP, the meeting assistant, the support
agents, the social media tool and the legal service, in one product, on the company's servers by default, outside only
where an administrator chooses a provider
([D440](../../06-decisions/vision/d440-local-by-default-outside-by-choice.md)).

## Against each kind of contender

| Contender | What it does | simple-ERP's answer |
|---|---|---|
| 🎙️ AI meeting assistants | Transcripts and summaries pushed to a CRM, in the vendor's cloud | Meetings land on the ERP's own records, with models on the company's servers by default (F4, D440) |
| 🎧 AI support-agent platforms | Agents log in to back offices and follow fixed procedures, paid per ticket | Agents act through the ERP's own API and permissions, and through connectors or browser automation for outside tools (F16, T12) |
| 🏢 Classic ERPs | Broad suites, integrator, per-user and per-app prices, AI paid in credits | Set up in a day, flat price per company, AI included when self-hosted |
| 🧠 AI-native ERPs | Agents at the core, SaaS only, finance first, quote prices, seldom French | The same agents across every area, self-hosted, France first, AGPL |
| 🏠 Sector software | Deep in one sector (home care, retail…), little AI or API | 16 sector packs on one platform, with its AI and API |

The company's own data is never scraped, and goes to a third party only where an administrator chose a provider for a
feature, under that provider's processing terms; customers' data never goes into GitHub
([D440](../../06-decisions/vision/d440-local-by-default-outside-by-choice.md)). The full comparison is the
[⚖️ Benchmark](../benchmark/benchmark.md).

---

⬅️ [Objectives](objectives.md) · ⬆️ [Up](README.md) · ➡️ [Success criteria](success-criteria.md)
