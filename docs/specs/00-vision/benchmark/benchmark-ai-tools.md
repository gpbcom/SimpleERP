🏠 [Specs](../../README.md) › 🎯 [Vision](../README.md) › 📊 [Benchmark](README.md) › 🤖 Benchmark: AI tools

# 🤖 Benchmark: AI tools

**Status:** ✅ specified

## Scope

Ai meeting and support tools against simple-ERP, read on 2026-11-11. Summary in the [⚖️ Benchmark](benchmark.md).

## How to read

📐 specified for simple-ERP's first version, not built yet · ✅ in the standard offer · 💰 paid add-on, higher plan or
partner module · 🟡 partial, limited, beta or announced · ❌ no, or out of the product's scope · 🔍 not found in public
sources · ℹ️ context only · ⬜ not specified yet

## Matrix

### 🏛️ Product and business

| ID | Criterion | simple-ERP | Noota | Nebesta |
|---|---|---|---|---|
| A01 | Category and scope | 📐 Full ERP suite + meetings, social media, support agents, legal assistant, 16 sectors | ✅ AI assistant for meetings, calls and email, syncing to CRM/ATS | ✅ Managed AI agents resolving level 2+ support tickets end-to-end (claim) |
| A02 | Licence | 📐 AGPL-3.0, core and plugins, no paid edition | ❌ Proprietary SaaS | ❌ Proprietary managed service |
| A03 | Self-hosting possible | 📐 Fully self-hosted, AI included; no graphics card needed | ❌ SaaS only (standard EU or sovereign France environment) | ❌ Managed service only |
| A04 | Managed cloud offer; where data is hosted | 📐 Managed hosting in the EU only (publisher); IT providers host too | ✅ GCP EU (BE/NL) default; sovereign France option (Scaleway/Bleu, SecNumCloud) | 🟡 "EU data residency" claimed; hosting provider/location not named |
| A05 | Pricing model | 📐 Flat fee per company + metered AI when the publisher hosts the AI | ✅ Per user/month (annual/monthly): Pro €19/€29, Business €39/€49, Enterprise custom | ✅ Outcome-based, per resolved ticket; ~€1/ticket per v2 site FAQ (claim) |
| A06 | Free plan or free edition | 📐 Free: the whole product self-hosted | ✅ Free plan: 10 AI credits/user, 1-month storage, bot-only | 🔍 No free plan or trial stated |
| A07 | Target company size | 📐 1 to 250+ employees, no size limit | 🟡 Individuals to enterprises; Enterprise plan for 50+ seats | 🟡 Support teams in insurance, SaaS, car rental, e-commerce; size not stated |
| A08 | Countries / localisations supported; France specifically | 📐 France first; other countries as country packs (law corpus + rules) | 🟡 French vendor; phone calls in 32 countries; transcription locales not stated | 🟡 French customers shown; countries not stated |
| A09 | UI languages | 📐 French and English at launch, open to more | 🟡 Site in EN/FR/ES/DE/IT/NL; transcription languages not stated | 🔍 Not stated |
| A10 | One platform hosting many client companies | 📐 One platform for many client companies (IT providers, accounting firms) | ❌ Out of scope (workspaces only) | ❌ Out of scope (per-customer deployments) |
| A11 | Typical setup | 📐 Self-serve guided setup with a sector pack; working in one day, no consultant | ✅ Self-serve; dedicated onboarding on Enterprise | ✅ Vendor-deployed in ~4 weeks after shadow mode (claim) |
| A12 | Security certifications | 📐 Deployable under SecNumCloud, SOC 2, HDS (health); ISO 27001 controls | ✅ ISO 27001 (Jul 2026), SOC 2 Type II, GDPR; HDS only via providers | 🟡 SOC 2 Type II claimed (other site: "in progress"); ISO 27001-aligned; GDPR |
| A13 | Company | Publisher to be set up; France | ✅ Paris, founded 2020; €3M raised 2025 (Blast Club, Sharpstone, Bpifrance) | ✅ NEBESTA SAS Paris; Kima, Serena, Motier, Freestyle; ex-Ankorstore/Doctolib founders |

### 🧱 Platform

| ID | Criterion | simple-ERP | Noota | Nebesta |
|---|---|---|---|---|
| B01 | Data isolation per company | 📐 One database per company | 🟡 Per-workspace hosting choice; workspaces private by default | ✅ Per-tenant isolation (claim) |
| B02 | SSO | 📐 SSO (SAML, OIDC), two-factor | 💰 SSO (Azure AD, SAML) + provisioning on Enterprise only | 🔍 Not stated |
| B03 | Roles and fine-grained permissions | 📐 Roles and record rules | ✅ Role-based access; meetings private by default | 🔍 Not stated |
| B04 | Audit trail of every change | 📐 Audit trail of every change | 🔍 Audit logs not mentioned | ✅ Full audit trail of AI actions and reasoning, SIEM export (claim) |
| B05 | Public API | 📐 Documented REST API and webhooks | 💰 API & webhooks from Business plan | 🟡 Custom REST/webhook channel listed; no public API docs |
| B06 | MCP server and/or A2A protocol | 📐 MCP server and A2A agent, both ways | ✅ Remote MCP server, read-only, 6 tools; plan tier contradictory | 🔍 Not found |
| B07 | App store / marketplace / plugins | 📐 Plugin store (F14, AGPL plugins) | ❌ No marketplace; integrations directory only | ❌ Out of scope |
| B08 | Integrations / connectors catalogue | 📐 Connector catalogue + connector/scraper factory | ✅ 53 listed (homepage says 46) incl. Odoo, HubSpot, Salesforce | ✅ Zendesk, Intercom, HubSpot, Salesforce, Front, Freshdesk, Slack |
| B09 | Version upgrades | 📐 Backups and updates built in | ✅ Vendor-managed SaaS; customer-set retention, deletion within 24 h | ✅ Vendor-managed; new SOP versions replay-tested before release (claim) |
| B10 | Mobile apps; offline mode | 📐 Phone app for the AI assistant, meetings, carers, POS; offline tills and tablets | ✅ iOS/Android apps; offline not stated | 🔍 Not stated |
| B11 | Data import / migration from other tools | 📐 Import from other tools (step 19m migration, UC-F21-09) | ❌ Out of scope | ❌ Out of scope |
| B12 | Customisation without code | 📐 Fields, statuses, forms, record types, templates, visual workflows, sandbox | 🟡 Custom templates, vocabulary, company rules (Business) | 🟡 Per-intent SOPs, configured with the vendor |
| B13 | Build apps or workflows from plain language | 📐 Record types, workflows, apps and agents drafted from plain language | 🟡 Noota builds automations from a description, reviewed before go-live | 🟡 SOPs auto-updated from reviewed conversations (claim) |

### 🤖 AI

| ID | Criterion | simple-ERP | Noota | Nebesta |
|---|---|---|---|---|
| C01 | AI assistant chatting over the company's own data | 📐 Assistant on every screen, answers with sources, within permissions | ✅ Ask Noota: sourced answers over meetings, emails, uploads | ❌ Customer-facing agent; no internal chat assistant stated |
| C02 | AI agents that perform write actions | 📐 Acts after confirmation; AI agents always-on, scheduled, on demand | 💰 Automations write notes, tasks, deal stage to CRM (Business) | ✅ Executes refunds, cancellations, billing disputes in back offices (claim) |
| C03 | Agent governance | 📐 Confirmation, thresholds, risk tiers, audit agent, preview of affected records | 🟡 Review before activation; dry runs promised early 2027; no per-record approval | ✅ Shadow mode, per-intent rollout, per-ticket scoring, human fallback |
| C04 | AI models used; option to run models locally / self-hosted / bring your own key | 📐 Local open models by default; external provider per feature with own key | 🟡 Claude/Gemini/Mistral via Vertex; sovereign: Mistral + open-weight in France; no BYOK | 🔍 Models not named; "fine-tuned AI judge" |
| C05 | RAG / search over company documents | 📐 RAG platform on Milvus over records, files, meetings, knowledge base, law | ✅ Searches meetings, emails, Word/PDF uploads with citations | 🟡 "RAG" mentioned, no detail |
| C06 | AI document capture | 📐 AI reading of supplier bills and documents | ❌ Out of scope | 🔍 Not stated |
| C07 | AI pricing | 📐 Included when self-hosted; metered when the publisher hosts | 🟡 AI credits: Free 10, Pro 100, Business unlimited | ✅ Included in per-resolved-ticket price (claim) |
| C08 | AI acting on OUTSIDE systems | 📐 Outside systems through API, MCP/A2A, browser automation and scrapers, static or agentic | ✅ Writes to HubSpot, Salesforce, Pipedrive, ATS through native API integrations | ✅ Login/password access to back offices, "no API", deterministic SOPs (claim) |

### 🧩 Functional

| ID | Criterion | simple-ERP | Noota | Nebesta |
|---|---|---|---|---|
| D01 | Administration | 📐 Company, sites, users, roles, connections, AI settings, multi-company | 🟡 Workspaces, admin controls, groups (Business) | ❌ Out of scope |
| D02 | Documents workspace, e-signature, spreadsheets / dashboards on ERP data | 📐 Documents workspace, e-signature, live spreadsheets and dashboards | 🟡 Team dashboards only | ❌ Out of scope |
| D03 | Meetings | 📐 Bot for Teams, Meet, Zoom, Webex, Jitsi, BigBlueButton; transcripts, summaries | ✅ Bot or bot-less on Zoom, Meet, Teams, Webex; transcripts, summaries | ❌ Out of scope |
| D04 | Meetings | 📐 Decisions and tasks linked to records; in-person and phone recording, softphone | ✅ CRM/ATS sync, in-person mobile recording, VoIP calls (Business) | ❌ Out of scope |
| D05 | Calendar, appointment booking, team chat | 📐 Two-way calendars, appointment booking, team chat, call routing | 🟡 Calendar integrations; no booking or chat | ❌ Out of scope |
| D06 | Social media | 📐 11 networks, approval, calendar, automatic mode, inbox, statistics | ❌ Out of scope (LinkedIn integration only) | ❌ Out of scope |
| D07 | Marketing | 📐 Email and SMS campaigns, journeys, events, surveys | ❌ Out of scope | ❌ Out of scope |
| D08 | CRM | 📐 Leads, pipeline, scoring, assignment, enrichment, dedup | 🟡 CRM enrichment; Sales Agent "soon" | ❌ Out of scope |
| D09 | Sales | 📐 Quotes, options, configurator, click or e-signature acceptance, customer portal | ❌ Out of scope | ❌ Out of scope |
| D10 | Invoicing, payments, subscriptions / recurring billing, rental | 📐 Invoices, payments, dunning, subscriptions, usage billing, rental | ❌ Out of scope | ❌ Out of scope |
| D11 | Purchasing | 📐 Requests, approvals, orders, supplier portal, tenders and supplier rating | ❌ Out of scope | ❌ Out of scope |
| D12 | Inventory and warehouse | 📐 Multi-warehouse, routes, barcode, lots and serials, 3PL, repairs | ❌ Out of scope | ❌ Out of scope |
| D13 | Accounting core | 📐 Ledger, payables, receivables, bank aggregators, AI matching, VAT, assets | ❌ Out of scope | ❌ Out of scope |
| D14 | Accounting advanced | 📐 Multi-currency, consolidation with eliminations, IFRS 15, continuous close, FP&A, spend cards | ❌ Out of scope | ❌ Out of scope |
| D15 | France accounting | 📐 PCG, FEC, French VAT returns from the France pack | ❌ Out of scope | ❌ Out of scope |
| D16 | France e-invoicing reform 2026 | 📐 Factur-X/UBL/CII; connected to an approved platform (choice in Q13) | ❌ Out of scope | ❌ Out of scope |
| D17 | HR | 📐 Employees, French duties, recruitment, leave, attendance, appraisals, expenses | 💰 Recruitment Agent add-on €99–139/user/month; no core HR | ❌ Out of scope |
| D18 | Projects and planning | 📐 Projects, timesheets, shifts, field service, rounds with travel times | ❌ Out of scope | ❌ Out of scope |
| D19 | Point of sale | 📐 Shop, restaurant, kiosk, offline, terminals, scales; certified before French sale | ❌ Out of scope | ❌ Out of scope |
| D20 | Website builder and online shop | 📐 Website builder and online shop, B2B, marketplaces via connectors | ❌ Out of scope | ❌ Out of scope |
| D21 | Manufacturing | 📐 BOM, MRP, work orders, quality, maintenance, PLM, OEE | ❌ Out of scope | ❌ Out of scope |
| D22 | Payroll | 📐 Payroll plugin (France, DSN, F13) | ❌ Out of scope | ❌ Out of scope |
| D23 | Helpdesk | 📐 Own customer service and outside helpdesks, every channel, knowledge base | ❌ Out of scope (Zendesk sync only) | 🟡 Works inside existing helpdesks; not a helpdesk itself |
| D24 | AI support agents answering customers and resolving tickets in back offices | 📐 AI agents resolving requests end to end, intents automated once proven accurate | ❌ Out of scope | ✅ Core product: resolves tickets in back offices, 99% accuracy (claim) |
| D25 | Legal | 📐 Legal assistant on country law and sector standards, proactive warnings | ❌ Out of scope | ❌ Out of scope |
| D26 | Sector editions offered | 📐 16 sector packs (SC01 to SC16) | ❌ None; sales and recruiting focus | 🟡 Intents for insurance, SaaS, car rental, e-commerce, hotels, delivery |

### 🏠 Home care

| ID | Criterion | simple-ERP | Noota | Nebesta |
|---|---|---|---|---|
| E01 | Care-worker scheduling and replacements | 📐 Rounds, replacements, carers' skills | ❌ Out of scope | ❌ Out of scope |
| E02 | Mobile time-and-attendance at the beneficiary's home | 📐 Carer's phone with check-in and check-out | ❌ Out of scope | ❌ Out of scope |
| E03 | Beneficiary file | 📐 Care recipients, care plans, care log, incidents, family access | ❌ Out of scope | ❌ Out of scope |
| E04 | Billing to funders | 📐 Billing to recipients and funders, tax-credit certificate, immediate advance | ❌ Out of scope | ❌ Out of scope |
| E05 | Compliance with sector rules | 📐 Quality and the France pack's home-care rules | ❌ Out of scope | ❌ Out of scope |

---

⬅️ [Benchmark: ERPs and home care](benchmark-erps.md) · ⬆️ [Up](README.md) ·
➡️ [Benchmark: AI-native ERPs](benchmark-ai-native-erps.md)
