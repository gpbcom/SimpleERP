# Capabilities

SimpleERP is meant for start-ups and small companies that need one place to manage their business data. This chapter
lists its business capabilities and where each one stands.

## Built

None yet. The repository holds the project's skeleton and its command line entry point, which only greets the user.

## Specified, not built yet

Every capability below is specified in [docs/specs/](../specs/README.md) (ticket GH-2): its use cases per persona,
flows, business rules, data, screens with images for each persona and device, permissions, notifications, reports,
AI, API, MCP and A2A exposure, and the French rules it applies from the country pack. The build step is the one of the
[roadmap](../specs/00-vision/roadmap/roadmap.md): everything is in V1, the DevOps agents first (D483).

| Capability | Specification | Build step |
|---|---|---|
| F1 Administration | [docs/specs/02-functional/f01-administration/](../specs/02-functional/f01-administration/README.md) | 2 |
| F2 No-code configuration | [docs/specs/02-functional/f02-no-code-configuration/](../specs/02-functional/f02-no-code-configuration/README.md) | 2 |
| F3 Assistant | [docs/specs/02-functional/f03-assistant/](../specs/02-functional/f03-assistant/README.md) | 2 |
| F4 Meetings | [docs/specs/02-functional/f04-meetings/](../specs/02-functional/f04-meetings/README.md) | 2 |
| F5 Social media and marketing | [docs/specs/02-functional/f05-social-media/](../specs/02-functional/f05-social-media/README.md) | 8 |
| F6 Customers and sales | [docs/specs/02-functional/f06-customers-and-sales/](../specs/02-functional/f06-customers-and-sales/README.md) | 3 |
| F7 Purchasing and stock | [docs/specs/02-functional/f07-purchasing-and-stock/](../specs/02-functional/f07-purchasing-and-stock/README.md) | 4 |
| F8 Accounting | [docs/specs/02-functional/f08-accounting/](../specs/02-functional/f08-accounting/README.md) | 5 |
| F9 HR and projects | [docs/specs/02-functional/f09-hr-and-projects/](../specs/02-functional/f09-hr-and-projects/README.md) | 6 |
| F10 Point of sale (plugin) | [docs/specs/02-functional/f10-point-of-sale/](../specs/02-functional/f10-point-of-sale/README.md) | 7 |
| F11 Online shop (plugin) | [docs/specs/02-functional/f11-online-shop/](../specs/02-functional/f11-online-shop/README.md) | 7 |
| F12 Manufacturing (plugin) | [docs/specs/02-functional/f12-manufacturing/](../specs/02-functional/f12-manufacturing/README.md) | 7 |
| F13 Payroll (plugin) | [docs/specs/02-functional/f13-payroll/](../specs/02-functional/f13-payroll/README.md) | 7 |
| F14 Plugin store | [docs/specs/02-functional/f14-plugin-store/](../specs/02-functional/f14-plugin-store/README.md) | 7 |
| F15 Legal assistant | [docs/specs/02-functional/f15-legal-assistant/](../specs/02-functional/f15-legal-assistant/README.md) | 6 |
| F16 Customer support agents | [docs/specs/02-functional/f16-customer-support-agents/](../specs/02-functional/f16-customer-support-agents/README.md) | 3 |
| F17 Competitive analysis | [docs/specs/02-functional/f17-competitive-analysis/](../specs/02-functional/f17-competitive-analysis/README.md) | 8 |
| F18 Hosted websites and domains (hosted edition) | [docs/specs/02-functional/f18-hosted-websites-and-domains/](../specs/02-functional/f18-hosted-websites-and-domains/README.md) | 10 |
| F19 Feature factory (hosted edition) | [docs/specs/02-functional/f19-feature-factory/](../specs/02-functional/f19-feature-factory/README.md) | 10 |
| F20 Hosted support assistant (hosted edition) | [docs/specs/02-functional/f20-hosted-support-assistant/](../specs/02-functional/f20-hosted-support-assistant/README.md) | 10 |
| F21 Onboarding and module activation | [docs/specs/02-functional/f21-onboarding-and-modules/](../specs/02-functional/f21-onboarding-and-modules/README.md) | 2 |
| F22 Unified platform cost management | [docs/specs/02-functional/f22-unified-cost-management/](../specs/02-functional/f22-unified-cost-management/README.md) | 2 |
| F23 What-if simulation and impact | [docs/specs/02-functional/f23-what-if-simulation/](../specs/02-functional/f23-what-if-simulation/README.md) | 8 |
| F24 Integrations hub | [docs/specs/02-functional/f24-integrations-hub/](../specs/02-functional/f24-integrations-hub/README.md) | 2 |
| F25 DevOps agents (hosted edition) | [docs/specs/02-functional/f25-devops-agents/](../specs/02-functional/f25-devops-agents/README.md) | 1 |

## Sectors

Each kind of company has its own interview and folder: the record types, rules, documents, regulation, screens and
sector pack it adds to the capabilities above.

| Sector | Specification |
|---|---|
| SC01 Construction | [docs/specs/08-sectors/sc01-construction/](../specs/08-sectors/sc01-construction/README.md) |
| SC02 Retail | [docs/specs/08-sectors/sc02-retail/](../specs/08-sectors/sc02-retail/README.md) |
| SC03 Services | [docs/specs/08-sectors/sc03-services/](../specs/08-sectors/sc03-services/README.md) |
| SC04 Home care | [docs/specs/08-sectors/sc04-home-care/](../specs/08-sectors/sc04-home-care/README.md) |
| SC05 Manufacturing | [docs/specs/08-sectors/sc05-manufacturing/](../specs/08-sectors/sc05-manufacturing/README.md) |
| SC06 Restaurant and hospitality | [docs/specs/08-sectors/sc06-hospitality/](../specs/08-sectors/sc06-hospitality/README.md) |
| SC07 Transport and logistics | [docs/specs/08-sectors/sc07-transport/](../specs/08-sectors/sc07-transport/README.md) |
| SC08 Non-profit association | [docs/specs/08-sectors/sc08-non-profit/](../specs/08-sectors/sc08-non-profit/README.md) |
| SC09 Health practices | [docs/specs/08-sectors/sc09-health-practices/](../specs/08-sectors/sc09-health-practices/README.md) |
| SC10 Real estate | [docs/specs/08-sectors/sc10-real-estate/](../specs/08-sectors/sc10-real-estate/README.md) |
| SC11 Professional firms | [docs/specs/08-sectors/sc11-professional-firms/](../specs/08-sectors/sc11-professional-firms/README.md) |
| SC12 Education and training | [docs/specs/08-sectors/sc12-education-and-training/](../specs/08-sectors/sc12-education-and-training/README.md) |
| SC13 Agriculture and food | [docs/specs/08-sectors/sc13-agriculture-and-food/](../specs/08-sectors/sc13-agriculture-and-food/README.md) |
| SC14 IT and software | [docs/specs/08-sectors/sc14-it-and-software/](../specs/08-sectors/sc14-it-and-software/README.md) |
| SC15 Wholesale and distribution | [docs/specs/08-sectors/sc15-wholesale-and-distribution/](../specs/08-sectors/sc15-wholesale-and-distribution/README.md) |
| SC16 Events and culture | [docs/specs/08-sectors/sc16-events-and-culture/](../specs/08-sectors/sc16-events-and-culture/README.md) |
| SC17 Beauty and wellness | [docs/specs/08-sectors/sc17-beauty-and-wellness/](../specs/08-sectors/sc17-beauty-and-wellness/README.md) |
| SC18 Sports and fitness | [docs/specs/08-sectors/sc18-sports-and-fitness/](../specs/08-sectors/sc18-sports-and-fitness/README.md) |
| SC19 Trades and home services | [docs/specs/08-sectors/sc19-trades-and-home-services/](../specs/08-sectors/sc19-trades-and-home-services/README.md) |
| SC20 Public bodies | [docs/specs/08-sectors/sc20-public-bodies/](../specs/08-sectors/sc20-public-bodies/README.md) |

Each capability gets its own chapter here when its first ticket is handed over (written by the ticket's `doc-writer` agent): what users can do, who,
where, the business rules, and the flow.

Last reviewed: 2026-11-17 (GH-2)
