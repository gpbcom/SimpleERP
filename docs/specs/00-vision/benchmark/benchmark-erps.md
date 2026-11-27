🏠 [Specs](../../README.md) › 🎯 [Vision](../README.md) › 📊 [Benchmark](README.md) › 🏢 Benchmark: ERPs and home care

# 🏢 Benchmark: ERPs and home care

**Status:** ✅ specified

## Scope

Erps and home care against SimpleERP, read on 2026-11-11. Summary in the [⚖️ Benchmark](benchmark.md).

## How to read

📐 specified for SimpleERP's first version, not built yet · ✅ in the standard offer · 💰 paid add-on, higher plan or
partner module · 🟡 partial, limited, beta or announced · ❌ no, or out of the product's scope · 🔍 not found in public
sources · ℹ️ context only · ⬜ not specified yet

## Matrix

### 🏛️ Product and business

| ID | Criterion | SimpleERP | Odoo | ERPNext | Dolibarr | Ximi |
|---|---|---|---|---|---|---|
| A01 | Category and scope | 📐 Full ERP suite + meetings, social media, support agents, legal assistant, 16 sectors | ✅ All-in-one business suite, ~50 official apps (claim) | ✅ Open-source ERP (accounting, stock, manufacturing, CRM) on Frappe framework | ✅ Modular open-source ERP & CRM for SMEs, freelancers, associations | ✅ Vertical ERP for home services: SAP, SAAD, SSIAD, SPASAD, senior residences |
| A02 | Licence | 📐 AGPL-3.0, core and plugins, no paid edition | 🟡 Open core: Community LGPLv3; Enterprise under a proprietary licence | ✅ ERPNext GPL-3.0, "no paywalls"; Frappe framework MIT; Helpdesk AGPL-3.0 | ✅ GPL-3.0, fully open source | ❌ Proprietary SaaS |
| A03 | Self-hosting possible | 📐 Fully self-hosted, AI included; no graphics card needed | ✅ Community self-hosted; Enterprise on-premise only on Custom plan 💰 | ✅ Free self-hosting with official install scripts | ✅ On-premise, VPS, Docker, Windows/Mac/Linux packages | ❌ Cloud-only offer (100% web, hosted in France) |
| A04 | Managed cloud offer; where data is hosted | 📐 Managed hosting in the EU only (publisher); IT providers host too | ✅ Odoo Online; region choice (Europe…); backups replicated Europe+Canada, not restrictable | ✅ Frappe Cloud (AWS/OCI); Frankfurt (EU), London, Zurich listed | 💰 Partner DoliCloud, "hosted in Europe" | ✅ SaaS hosted in France on HDS-certified hosting |
| A05 | Pricing model | 📐 Flat fee per company + metered AI when the publisher hosts the AI | ✅ Per user/month: Standard €19.90 promo (€24.90/€31.10 list), Custom €35.90 promo | ✅ No per-user fee; Frappe Cloud from $5/site/month, dedicated from $125 | ✅ Software free; DoliCloud Basic €14/user/month, Premium from €45/month | 🟡 Quote-based; one listing says from €49/month (unverified) |
| A06 | Free plan or free edition | 📐 Free: the whole product self-hosted | ✅ One App Free (one app, unlimited users) plus free Community | ✅ Self-hosted is free; Frappe Cloud has 14-day trial only | ✅ Software entirely free; DoliCloud 30-day free trial | ❌ No free offer (review site) |
| A07 | Target company size | 📐 1 to 250+ employees, no size limit | ✅ Small to large; 28M users, 8,000+ staff (claim) | ✅ SMBs (<50-user Success Packs) to enterprises via partners; 30,000+ companies | ✅ SMEs, large companies, freelancers, associations (claim) | ✅ All sizes, 1,200+ structures; judged oversized for micro-structures (review) |
| A08 | Countries / localisations supported; France specifically | 📐 France first; other countries as country packs (law corpus + rules) | ✅ 103 fiscal localisations; full France package (l10n_fr) | 🟡 Regional features; France: FEC + chained log via community app | ✅ France well covered: PCG chart data, FEC/FEC2 exports in core | 🟡 France only, built around French home-care rules |
| A09 | UI languages | 📐 French and English at launch, open to more | 🔍 Language count not found in pages read | 🔍 Language count not found in pages read | 🟡 Website in 25 languages; UI count not stated | 🟡 French only ("100% français") |
| A10 | One platform hosting many client companies | 📐 One platform for many client companies (IT providers, accounting firms) | 🟡 Multi-company per database (Custom 💰); accounting-firm directory; no multi-tenant console | ✅ Bench multi-site; Frappe Cloud dashboard "manage multiple tenants" | 💰 Multi-entity via external Multicompany module | 🟡 Agency networks and franchises supported; not multi-client hosting |
| A11 | Typical setup | 📐 Self-serve guided setup with a sector pack; working in one day, no consultant | 🟡 Self-serve online or 21,000+ partners; implementation time not stated | 🟡 Self-implement free or 200+ partners; Frappe does no implementation | 🟡 Self-install, DoliCloud self-serve or partners; time not stated | 🟡 Vendor onboarding and training; "start needs a real project" (review) |
| A12 | Security certifications | 📐 Deployable under SecNumCloud, SOC 2, HDS (health); ISO 27001 controls | 🟡 Only CSA STAR Level 1 stated; no ISO 27001/SOC 2/HDS found | ✅ ISO 27001:2022, ISO 9001, SOC 2 Type II (2024–25); no HDS | 🔍 No certification stated (project or DoliCloud) | ✅ ISO 27001, 27018, 20000-1, HDS (AFNOR); Ségur-referenced |
| A13 | Company | Publisher to be set up; France | ✅ Odoo SA, Belgium HQ; 8,000+ employees; 21,000+ partners | ✅ Frappe, backed by Zerodha/Rainmatter; 82 team members listed | ✅ Dolibarr association (since 2009); community plus partner firms | ✅ Xelya, Saint-Cloud FR, founded 2005, ~240 staff, >€30M revenue (claim) |

### 🧱 Platform

| ID | Criterion | SimpleERP | Odoo | ERPNext | Dolibarr | Ximi |
|---|---|---|---|---|---|---|
| B01 | Data isolation per company | 📐 One database per company | ✅ Dedicated database per customer on Odoo Online | ✅ Dedicated database per site, even on shared hosting | 🟡 One database per instance; Multicompany entities share one database | 🔍 Not stated |
| B02 | SSO | 📐 SSO (SAML, OIDC), two-factor | 🟡 2FA; OAuth (Google, Microsoft, Facebook), LDAP; SAML not documented | 🟡 LDAP, OAuth tokens; SAML/MFA not confirmed in pages read | 🟡 OpenID Connect login with user auto-creation (v21/v24); MFA not found | 🔍 Not stated |
| B03 | Roles and fine-grained permissions | 📐 Roles and record rules | ✅ Groups, four role types, per-app access levels (Comm.) | ✅ Role permissions, record-level user permissions, field levels, data masking (v16) | 🔍 Not documented in pages read | 🟡 Access rights restrict data to authorised users |
| B04 | Audit trail of every change | 📐 Audit trail of every change | 🟡 Chatter tracking; Odoo 20 logs group changes; no full audit log found | 🔍 No audit trail described in pages read | 🟡 BlockedLog unalterable log of invoices/payments; not a full change log | 🟡 Care transmissions traced and non-editable; general audit not stated |
| B05 | Public API | 📐 Documented REST API and webhooks | ✅ JSON-2/XML-RPC API (Custom plan 💰 on Online); webhooks via automation rules | ✅ REST CRUD API with token/OAuth; webhooks not confirmed in pages read | ✅ REST API, Webhook and Zapier modules in core | 🟡 API mode only for DSN exchange with Net-Entreprises; no public API |
| B06 | MCP server and/or A2A protocol | 📐 MCP server and A2A agent, both ways | 💰 Odoo 20: "Connect to your database via MCP"; client and server (third-party report) | 🟡 No official MCP; third-party Frappe Assistant Core on marketplace | 🟡 v24.0: "Experimental MCP server and AI Assistant" in core | 🔍 Not found |
| B07 | App store / marketplace / plugins | 📐 Plugin store (F14, AGPL plugins) | ✅ App store; 50,000+ community apps (claim) | ✅ Frappe Cloud Marketplace; size not stated | ✅ DoliStore official marketplace; size not stated | 🔍 No app store found |
| B08 | Integrations / connectors catalogue | 📐 Connector catalogue + connector/scraper factory | 🟡 Native connectors (Amazon Ent., payments, IoT Ent.); no total count | ✅ Shopify, WooCommerce, Amazon, Stripe, Plaid, Twilio and more; no count | 🟡 Zapier, Stripe, webhooks, email collector in core; no count | 🟡 Microsoft 365, Paybox, BH Technologies, CPAM, Chorus Pro |
| B09 | Version upgrades | 📐 Backups and updates built in | ✅ Version upgrades included (Ent.); Online: 14 backups, 3 data centres | ✅ Frappe Cloud manages upgrades and backups; self-hosters do their own | 🟡 Self-managed upgrades; DoliCloud hosting; backups not stated | ✅ SaaS; regulatory and agreement updates applied automatically |
| B10 | Mobile apps; offline mode | 📐 Phone app for the AI assistant, meetings, carers, POS; offline tills and tablets | 💰 Android/iOS apps Ent.-only; Odoo 20 offline record editing | 🟡 Mobile-friendly web UI; no native app stated | 🔍 Native mobile app not found in pages read | ✅ Ximi Mobile and Ximi Family (iOS/Android); offline per Appvizer only |
| B11 | Data import / migration from other tools | 📐 Import from other tools (step 19m migration, UC-F21-09) | 🟡 Import tool; FEC import for France; no named migrators found | ✅ Data Import tool with role-based Import permission | ✅ Import/export module in core | 🔍 Migration offer not stated |
| B12 | Customisation without code | 📐 Fields, statuses, forms, record types, templates, visual workflows, sandbox | 💰 Studio (Ent., Custom plan): fields, forms, automation rules, reports | ✅ Customize Form, custom fields, multi-level approval workflows | 🟡 Extra fields; low-code Module Builder (developer-oriented) | 🟡 Custom evaluation forms and survey questions |
| B13 | Build apps or workflows from plain language | 📐 Record types, workflows, apps and agents drafted from plain language | 🟡 Web pages generated from a prompt; no plain-language app building | 🔍 Forum says Frappe Builder "powered by AI"; unverified | 🔍 Not found | 🔍 Not found |

### 🤖 AI

| ID | Criterion | SimpleERP | Odoo | ERPNext | Dolibarr | Ximi |
|---|---|---|---|---|---|---|
| C01 | AI assistant chatting over the company's own data | 📐 Assistant on every screen, answers with sources, within permissions | 💰 AI agents read own records; Ask AI search (AI app, Ent.) | 🟡 Not native; external assistants via third-party MCP app | 🟡 Experimental v24 assistant with tools over third parties, invoices, products | 🔍 No AI assistant found |
| C02 | AI agents that perform write actions | 📐 Acts after confirmation; AI agents always-on, scheduled, on demand | 💰 Odoo 20 agents create/update records; scheduled or automated triggers | 🟡 Only through third-party MCP tools (invoices, stock) | 🟡 v24 MCP tools incl. object CRUD and invoices (experimental) | 🟡 Plizi computes replacement plans submitted for approval |
| C03 | Agent governance | 📐 Confirmation, thresholds, risk tiers, audit agent, preview of affected records | 🟡 Permission-request buttons, confirmation at tool-call limit, chat review | ❌ No native agents | 🟡 Confirmation level, per-context tool allow-lists, AI log viewer and retention | 🟡 Plizi plans need approval before applying |
| C04 | AI models used; option to run models locally / self-hosted / bring your own key | 📐 Local open models by default; external provider per feature with own key | 🟡 ChatGPT, Gemini; own key optional Online, required on-prem; Odoo 20 credits | 🟡 No native model; bring any MCP assistant | ✅ BYOK: OpenAI, Mistral, Anthropic, Gemini, Groq, DeepSeek, custom OpenAI-compatible URL | 🔍 Not stated |
| C05 | RAG / search over company documents | 📐 RAG platform on Milvus over records, files, meetings, knowledge base, law | 💰 Agent sources: PDFs, links, Documents, Knowledge (indexed) | ❌ No native AI features listed | 🔍 Not found | 🔍 Not found |
| C06 | AI document capture | 📐 AI reading of supplier bills and documents | 💰 Vendor-bill and expense OCR (Ent.), IAP credits | ❌ No native OCR listed | 🟡 Mistral OCR model configurable for "docparsing"; scope unclear | 🟡 Supplier invoices "read automatically" (paper or electronic) |
| C07 | AI pricing | 📐 Included when self-hosted; metered when the publisher hosts | 💰 Odoo 20: "All AI features now need credits" (IAP) | ❌ No native AI | ✅ Module included; pay your own provider API | 🔍 Not stated |
| C08 | AI acting on OUTSIDE systems | 📐 Outside systems through API, MCP/A2A, browser automation and scrapers, static or agentic | 🟡 Odoo 20 MCP client (third-party report); no RPA or scraping | ❌ No native agent | 🔍 Not found (its MCP server exposes Dolibarr to outside agents) | 🔍 Not found |

### 🧩 Functional

| ID | Criterion | SimpleERP | Odoo | ERPNext | Dolibarr | Ximi |
|---|---|---|---|---|---|---|
| D01 | Administration | 📐 Company, sites, users, roles, connections, AI settings, multi-company | ✅ Users, companies, settings; multi-company on Custom plan 💰 | ✅ Multi-company, users, roles | 🟡 Users and settings core; multi-company via external module 💰 | ✅ Multi-entity, agency networks, franchises |
| D02 | Documents workspace, e-signature, spreadsheets / dashboards on ERP data | 📐 Documents workspace, e-signature, live spreadsheets and dashboards | 💰 Documents, Spreadsheet, Sign all Ent.-only | 🟡 Insights dashboards; no e-signature or document workspace found | 🟡 Online signature links; document storage; no spreadsheet found | 🟡 Document management (GED), dashboards; e-signature in CRM |
| D03 | Meetings | 📐 Bot for Teams, Meet, Zoom, Webex, Jitsi, BigBlueButton; transcripts, summaries | 🟡 Discuss call recording and summaries; no bot joining Zoom/Meet/Teams | ❌ Out of scope | ❌ Out of scope | ❌ Out of scope |
| D04 | Meetings | 📐 Decisions and tasks linked to records; in-person and phone recording, softphone | 💰 VoIP app Ent.; meeting notes into CRM not found | 🟡 Telephony via Twilio/Exotel; no meeting capture | ❌ Out of scope | 🟡 Telephony: client file pops up on incoming call |
| D05 | Calendar, appointment booking, team chat | 📐 Two-way calendars, appointment booking, team chat, call routing | ✅ Calendar, Discuss chat (Comm.); Appointments Ent. 💰 | 🟡 Raven team chat; booking not found | ✅ Agenda and BookCal booking module in core; no team chat found | 🟡 Planning, secure messaging, Outlook task sync; no booking |
| D06 | Social media | 📐 11 networks, approval, calendar, automatic mode, inbox, statistics | 💰 Social Marketing Ent.; Odoo 20 replies to Messenger/Instagram DMs | 🔍 Not found | 🔍 Not found | ❌ Out of scope |
| D07 | Marketing | 📐 Email and SMS campaigns, journeys, events, surveys | ✅ Email, SMS, Events, Surveys (Comm.); Marketing Automation Ent. 💰 | 🟡 CRM newsletters; no automation journeys found | ✅ Emailing, surveys, event organisation modules; no journeys | 🟡 Satisfaction surveys by mass email only |
| D08 | CRM | 📐 Leads, pipeline, scoring, assignment, enrichment, dedup | ✅ CRM leads and pipeline (Comm.); AI agent creates leads | ✅ Leads, opportunities, territories; separate Frappe CRM app | ✅ Prospects, opportunities, proposals | ✅ CRM: quotes, contracts, e-signature, exchange tracking |
| D09 | Sales | 📐 Quotes, options, configurator, click or e-signature acceptance, customer portal | ✅ Sales (Comm.); e-signature via Sign (Ent.) | ✅ Quotations, sales orders, pricing rules, customer portal | ✅ Proposals, orders, contracts, online proposal signature | ✅ Quote to planned intervention; extranet portal with online payment |
| D10 | Invoicing, payments, subscriptions / recurring billing, rental | 📐 Invoices, payments, dunning, subscriptions, usage billing, rental | ✅ Invoicing, payments (Comm.); Subscriptions, Rental Ent. 💰 | ✅ Invoicing, payments (Stripe, GoCardless…) | ✅ Billing, payments, Stripe, contracts/subscriptions | ✅ Invoices from planning, SEPA, card (Paybox), recurring interventions |
| D11 | Purchasing | 📐 Requests, approvals, orders, supplier portal, tenders and supplier rating | ✅ Purchase app (Comm.) | ✅ Material requests, POs, approvals, supplier scorecards | ✅ Purchasing and supplier orders in core | 🟡 Purchases with automatic supplier-invoice reading |
| D12 | Inventory and warehouse | 📐 Multi-warehouse, routes, barcode, lots and serials, 3PL, repairs | ✅ Inventory (Comm.); Barcode Ent. 💰; 3PL industry package | ✅ Multi-warehouse, serial/batch tracking, stock ledger | ✅ Products, stocks, shipments in core | ❌ Out of scope |
| D13 | Accounting core | 📐 Ledger, payables, receivables, bank aggregators, AI matching, VAT, assets | 💰 Full Accounting (bank reconciliation, assets…) Ent.-only; Invoicing in Comm. | ✅ GL, AP/AR, fixed assets, multi-currency; Plaid bank sync | ✅ Double-entry accounting, bank reconciliation, assets module | 🟡 Automatic entries, balance sheet, FEC; bank reconciliation not stated |
| D14 | Accounting advanced | 📐 Multi-currency, consolidation with eliminations, IFRS 15, continuous close, FP&A, spend cards | 💰 Consolidation, budgets, analytic (Ent.); IFRS 15 / FP&A not checked | 🟡 Consolidated trial balance, IFRS report templates (v16); no FP&A found | 🔍 Not found | 🟡 Analytic split by entity/activity; no consolidation found |
| D15 | France accounting | 📐 PCG, FEC, French VAT returns from the France pack | 💰 l10n_fr chart, FEC, VAT report (reports app Ent.) | 🟡 FEC via community "ERPNext France" app (paid listing); PCG/VAT not found | ✅ French chart data and FEC/FEC2 export in core | 🟡 FEC export; PCG/VAT return not stated |
| D16 | France e-invoicing reform 2026 | 📐 Factur-X/UBL/CII; connected to an approved platform (choice in Q13) | ✅ Registered PA (Apr 2026); receives Factur-X/UBL/CII, sends UBL; no per-invoice fee | 🔍 No PA connector or Factur-X support found | 🟡 Not a PA; community PA connector module; Factur-X module; partner PAs | ✅ Xelya on DGFiP PA list; included in licence; Chorus Pro |
| D17 | HR | 📐 Employees, French duties, recruitment, leave, attendance, appraisals, expenses | ✅ Employees, leave, recruitment (Comm.); appraisals, expense OCR Ent. 💰 | ✅ Frappe HR: employees, attendance, payroll | ✅ Employees, leave, expenses, timesheets, recruitment modules | 🟡 Contracts, DPAE, recruitment, training; leave/appraisals not stated |
| D18 | Projects and planning | 📐 Projects, timesheets, shifts, field service, rounds with travel times | ✅ Project/Timesheet (Comm.); Planning, Field Service Ent. 💰 | ✅ Projects, tasks, timesheets; shift/field scheduling not found | ✅ Projects/tasks, interventions; no route planning found | ✅ Intervention planning, skills matching, road travel times (Plizi) |
| D19 | Point of sale | 📐 Shop, restaurant, kiosk, offline, terminals, scales; certified before French sale | 🟡 POS (Comm.); l10n_fr_pos_cert inalterability module; NF525 certificate not found | 🟡 Multi-store POS; chained log via France app; NF525 not found | 🟡 TakePOS + BlockedLog inalterability; NF525 certificate not found | ❌ Out of scope |
| D20 | Website builder and online shop | 📐 Website builder and online shop, B2B, marketplaces via connectors | ✅ Website, eCommerce, blog (Comm.) | 🟡 Frappe Builder websites; e-commerce through Shopify/WooCommerce | ✅ CMS/website module in core | ❌ Out of scope (client extranet only) |
| D21 | Manufacturing | 📐 BOM, MRP, work orders, quality, maintenance, PLM, OEE | ✅ MRP (Comm.); PLM, Quality, Shopfloor Ent. 💰 | ✅ Multi-level BOM, MRP, work orders, quality, subcontracting | ✅ MRP, BOM, workstations in core | ❌ Out of scope |
| D22 | Payroll | 📐 Payroll plugin (France, DSN, F13) | 🟡 French payroll accounting module only; DSN via third-party $239 module | 🔍 No French payroll/DSN found | 🔍 No French payroll/DSN found | ✅ Payroll with DSN, PAS, BAD/SAP/FEHAP agreements, particulier-employeur |
| D23 | Helpdesk | 📐 Own customer service and outside helpdesks, every channel, knowledge base | 💰 Helpdesk Ent.; Odoo 20 AI similar-ticket answer suggestions | ✅ Frappe Helpdesk: email, telephony, knowledge base, SLA, portal | ✅ Ticket and knowledge-management modules, email collector | 🟡 Request/complaint tracking with assignment; no helpdesk |
| D24 | AI support agents answering customers and resolving tickets in back offices | 📐 AI agents resolving requests end to end, intents automated once proven accurate | 💰 AI agent on Live Chat (generates leads); no back-office resolution | ❌ No AI support agent found | 🟡 v24 AI tools in ticket reply editor; no autonomous agent | ❌ Out of scope |
| D25 | Legal | 📐 Legal assistant on country law and sector standards, proactive warnings | ❌ None found | ❌ None found | ❌ None found | ❌ Out of scope |
| D26 | Sector editions offered | 📐 16 sector packs (SC01 to SC16) | ✅ ~100 industry packages (law firm, 3PL, cleaning…); no home care | ✅ Manufacturing, retail, education, healthcare, non-profit, services | 🔍 No sector editions found | ✅ Editions per structure (firm, association, network, franchise) and activity |

### 🏠 Home care

| ID | Criterion | SimpleERP | Odoo | ERPNext | Dolibarr | Ximi |
|---|---|---|---|---|---|---|
| E01 | Care-worker scheduling and replacements | 📐 Rounds, replacements, carers' skills | 🟡 Generic Planning/Field Service (Ent.); no care-worker module | ❌ No home-care module found | ❌ No home-care module found | ✅ Matching engine plus Plizi multi-day replacement optimisation |
| E02 | Mobile time-and-attendance at the beneficiary's home | 📐 Carer's phone with check-in and check-out | 🟡 Field Service mobile only (Ent.); no télégestion | ❌ No home-care module found | ❌ No home-care module found | ✅ Geolocated/NFC/QR mobile clock-in, toll-free landline, Domiphone departmental |
| E03 | Beneficiary file | 📐 Care recipients, care plans, care log, incidents, family access | ❌ No beneficiary or care-plan module in apps or industries | ❌ No home-care module found | ❌ No home-care module found | ✅ Care file, PAP, traced transmissions, liaison notebook (option) |
| E04 | Billing to funders | 📐 Billing to recipients and funders, tax-credit certificate, immediate advance | ❌ No APA/PCH/CESU billing found | ❌ No home-care module found | ❌ No home-care module found | ✅ APA/PCH multi-funder billing, caps, CPAM, Chorus Pro; CESU scanning |
| E05 | Compliance with sector rules | 📐 Quality and the France pack's home-care rules | ❌ No SAAD/SSIAD compliance features found | ❌ No home-care module found | ❌ No home-care module found | 🟡 Ségur, ARS/ANAP indicators, quality evaluations; rate setting not stated |

---

⬅️ [Benchmark](benchmark.md) · ⬆️ [Up](README.md) · ➡️ [Benchmark: AI tools](benchmark-ai-tools.md)
