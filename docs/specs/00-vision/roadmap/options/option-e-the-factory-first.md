🏠 [Specs](../../../README.md) › 🎯 [Vision](../../README.md) › 🛣️ [Roadmap and options](../README.md) ›
🔀 [Roadmap options](README.md) › 🏭 Option E: the factory first

# 🏭 Option E: the factory first

**Status:** 🔄 waiting for the owner

## Principle

The DevOps agents are joined early by the feature factory and the plugin store, used by the publisher itself first: the
business areas, the plugins and above all the 20 sector packs are then produced as factory work (generated, reviewed,
tested plugins and configuration) rather than written one by one.

## Steps

| Step | Holds | Starts after | Use cases (share of V1) | Notes |
|---|---|---|---|---|
| 1. DevOps agents | [F25](../../../02-functional/f25-devops-agents/README.md) | none | 28 (2 %) |  |
| 2. Platform | [T1](../../../03-technical/t01-companies-and-data-isolation/README.md), [T2](../../../03-technical/t02-identity-and-access/README.md), [T3](../../../03-technical/t03-audit-trail/README.md), [T4](../../../03-technical/t04-plugin-runtime/README.md), [T5](../../../03-technical/t05-api-and-webhooks/README.md), [T6](../../../03-technical/t06-mcp-and-a2a-gateway/README.md), [T7](../../../03-technical/t07-ai-providers-and-models/README.md), [T8](../../../03-technical/t08-rag-platform/README.md), [T9](../../../03-technical/t09-install-backups-and-updates/README.md), [T10](../../../03-technical/t10-translations-and-notifications/README.md), [T11](../../../03-technical/t11-legal-corpora/README.md), [T12](../../../03-technical/t12-connectors-and-scrapers/README.md), [T13](../../../03-technical/t13-maps-and-geodata/README.md), [F1](../../../02-functional/f01-administration/README.md), [F2](../../../02-functional/f02-no-code-configuration/README.md), [F3](../../../02-functional/f03-assistant/README.md), [F4](../../../02-functional/f04-meetings/README.md), [F21](../../../02-functional/f21-onboarding-and-modules/README.md), [F22](../../../02-functional/f22-unified-cost-management/README.md) | 1 | 176 (14 %) |  |
| 3. The factory | [F14](../../../02-functional/f14-plugin-store/README.md), [F19](../../../02-functional/f19-feature-factory/README.md) | 2 | 62 (5 %) | used by the publisher first (D388) |
| 4. Business areas | [F6](../../../02-functional/f06-customers-and-sales/README.md), [F7](../../../02-functional/f07-purchasing-and-stock/README.md), [F8](../../../02-functional/f08-accounting/README.md), [F9](../../../02-functional/f09-hr-and-projects/README.md), [F5](../../../02-functional/f05-social-media/README.md) | 3 | 176 (14 %) | D4 order; pilot |
| 5. Plugins and support | [F10](../../../02-functional/f10-point-of-sale/README.md), [F11](../../../02-functional/f11-online-shop/README.md), [F12](../../../02-functional/f12-manufacturing/README.md), [F13](../../../02-functional/f13-payroll/README.md), [F15](../../../02-functional/f15-legal-assistant/README.md), [F16](../../../02-functional/f16-customer-support-agents/README.md), [F24](../../../02-functional/f24-integrations-hub/README.md) | 4 | 212 (17 %) | D15 |
| 6. Sectors | [SC01](../../../08-sectors/sc01-construction/README.md), [SC02](../../../08-sectors/sc02-retail/README.md), [SC03](../../../08-sectors/sc03-services/README.md), [SC04](../../../08-sectors/sc04-home-care/README.md), [SC05](../../../08-sectors/sc05-manufacturing/README.md), [SC06](../../../08-sectors/sc06-hospitality/README.md), [SC07](../../../08-sectors/sc07-transport/README.md), [SC08](../../../08-sectors/sc08-non-profit/README.md), [SC09](../../../08-sectors/sc09-health-practices/README.md), [SC10](../../../08-sectors/sc10-real-estate/README.md), [SC11](../../../08-sectors/sc11-professional-firms/README.md), [SC12](../../../08-sectors/sc12-education-and-training/README.md), [SC13](../../../08-sectors/sc13-agriculture-and-food/README.md), [SC14](../../../08-sectors/sc14-it-and-software/README.md), [SC15](../../../08-sectors/sc15-wholesale-and-distribution/README.md), [SC16](../../../08-sectors/sc16-events-and-culture/README.md), [SC17](../../../08-sectors/sc17-beauty-and-wellness/README.md), [SC18](../../../08-sectors/sc18-sports-and-fitness/README.md), [SC19](../../../08-sectors/sc19-trades-and-home-services/README.md), [SC20](../../../08-sectors/sc20-public-bodies/README.md) | 5 | 441 (36 %) | all in parallel, as factory work |
| 7. Insight and hosted services | [F17](../../../02-functional/f17-competitive-analysis/README.md), [F23](../../../02-functional/f23-what-if-simulation/README.md), [F18](../../../02-functional/f18-hosted-websites-and-domains/README.md), [F20](../../../02-functional/f20-hosted-support-assistant/README.md) | 4 | 126 (10 %) |  |

Every step also builds the technical design chapters, technical challenges, non-functional requirements and country-pack
themes its capabilities need, as listed in [What V1 holds](../inventory.md).

## Dependency graph

```mermaid
flowchart LR
  S1[1. DevOps agents] --> S2[2. Platform]
  S2 --> S3[3. Factory: F14, F19]
  S3 --> S4[4. Business areas]
  S4 --> P{{Pilot D451}}
  S4 --> S5[5. Plugins and support]
  S5 --> S6[6. Sectors, in parallel]
  S4 --> S7[7. Insight and hosted]
  S6 --> R((V1 release))
  S7 --> R
```

## The dated pilot

The pilot starts after step 4, so the factory is on its critical path: if the factory falls short, the pilot slips.

## Decisions

| Decision | In this option | How |
|---|---|---|
| [D3](../../../06-decisions/foundations/d03-every-area-in-the-first-version.md) | ✅ kept |  |
| [D4](../../../06-decisions/foundations/d04-business-build-order.md) | ✅ kept |  |
| [D15](../../../06-decisions/foundations/d15-industry-areas-as-plugins.md) | ✅ kept |  |
| [D16](../../../06-decisions/foundations/d16-platform-first.md) | ✅ kept |  |
| [D380](../../../06-decisions/vision/d380-every-capability-first-confirmed.md) | ✅ kept |  |
| [D451](../../../06-decisions/vision/d451-dated-pilot-before-the-release.md) | ⚠️ bent | the factory sits before the pilot |
| [D483](../../../06-decisions/vision/d483-roadmap-devops-agents-first.md) | ✅ kept | F14 and F19 (Proposed placements) move to step 3 |

## Strengths

- The most leverage: the sectors alone hold a large share of V1's use cases, and the factory makes them in parallel.
- The factory is tried on its hardest customer, the publisher, before customers pay for it.

## Risks

- The factory is built before the domain it generates is proven.
- Generated code in production (TC-12) is on the critical path of the pilot.
- It puts the most work on the maintainer's review of generated pull requests.

---

⬅️ [Option D: sector waves](option-d-sector-waves.md) · ⬆️ [Up](README.md) ·
➡️ [Option F: the pilot spine, with tracks and waves](option-f-pilot-spine-tracks-and-waves.md)
