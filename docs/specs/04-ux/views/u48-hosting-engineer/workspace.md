🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🧑‍🔧 [Hosting engineer: app shell and home](README.md) › 🧰 U48 Hosting engineer: workspace

# 🧰 U48 Hosting engineer: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U48 Hosting engineer](../../../01-users/personas/u48-hosting-engineer.md) works with, embedded on their
[home screen](README.md)
([D484](../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D493](../../../06-decisions/ux/d493-persona-workspaces-from-the-use-cases.md),
[D495](../../../06-decisions/ux/d495-views-listed-under-each-capabilitys-menu.md)): the list of each record type their
use cases and flow charts work on, with the owner's review of 2026-11-13
([D519](../../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)). Each view opens on the
persona's default saved view. (Proposed) The default is the view's "Mine" for a persona who works on their own records,
"Needs attention" for one who oversees others' (managers, the owner, HR, the administrators and the planner roles), else
"Open", else "All".

## Embedded views

| View | Capability | Default saved view | Why |
|---|---|---|---|
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-F18-L07 Domains](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l07-domains.md) | Hosted websites and domains (hosted edition) | All | UC-F18-20 |
| [S-F18-L08 DNS records](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l08-dns-records.md) | Hosted websites and domains (hosted edition) | All | UC-F18-11 |
| [S-F18-L09 TLS certificates](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l09-tls-certificates.md) | Hosted websites and domains (hosted edition) | All | UC-F18-11, UC-F18-20 |
| [S-F18-L10 Publication check reports](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l10-publication-check-reports.md) | Hosted websites and domains (hosted edition) | All | UC-F18-14 |
| [S-F18-L12 Uptime events](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l12-uptime-events.md) | Hosted websites and domains (hosted edition) | All | UC-F18-20 |
| [S-F18-L19 Site backups](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l19-site-backups.md) | Hosted websites and domains (hosted edition) | Needs attention | UC-F18-27 |
| [S-F19-L04 Generated plugin versions](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l04-generated-plugin-versions.md) | Feature factory (hosted edition) | All | UC-F19-04, UC-F19-06, UC-F19-17, UC-F19-13 |
| [S-F19-L05 Feature check reports](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l05-feature-check-reports.md) | Feature factory (hosted edition) | All | UC-F19-05, UC-F19-06, UC-F19-17 |
| [S-F19-L07 Feature promotions](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l07-feature-promotions.md) | Feature factory (hosted edition) | All | UC-F19-13, UC-F19-14 |
| [S-F19-L10 Feature withdrawals](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l10-feature-withdrawals.md) | Feature factory (hosted edition) | All | UC-F19-18 |
| [S-F19-L11 Delivery commitments](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l11-delivery-commitments.md) | Feature factory (hosted edition) | Needs attention | UC-F19-21 |
| [S-F19-L14 Security and privacy reviews](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l14-security-and-privacy-reviews.md) | Feature factory (hosted edition) | Needs attention | UC-F19-06, UC-F19-24 |
| [S-F20-L01 Support requests](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l01-support-requests.md) | Hosted support assistant (hosted edition) | All | UC-F20-08 |
| [S-F20-L03 Screenshots](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l03-screenshots.md) | Hosted support assistant (hosted edition) | All | UC-F20-18 |
| [S-F20-L04 Diagnosis](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l04-diagnosis.md) | Hosted support assistant (hosted edition) | All | UC-F20-04, UC-F20-07 |
| [S-F20-L05 Cluster readings](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l05-cluster-readings.md) | Hosted support assistant (hosted edition) | All | UC-F20-04 |
| [S-F20-L06 Fix proposals](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l06-fix-proposals.md) | Hosted support assistant (hosted edition) | All | UC-F20-06, UC-F20-07, UC-F20-13, UC-F20-11 |
| [S-F20-L07 Service incidents](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l07-service-incidents.md) | Hosted support assistant (hosted edition) | All | UC-F20-08, UC-F20-10, UC-F20-11, UC-F20-15 and more |
| [S-F20-L08 Restores](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l08-restores.md) | Hosted support assistant (hosted edition) | All | UC-F20-13 |
| [S-F20-L09 Breach records](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l09-breach-records.md) | Hosted support assistant (hosted edition) | All | UC-F20-15 |
| [S-F20-L10 Ratings](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l10-ratings.md) | Hosted support assistant (hosted edition) | All | UC-F20-16 |
| [S-F20-L11 Assistant policies](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l11-assistant-policies.md) | Hosted support assistant (hosted edition) | All | UC-F20-17, UC-F20-18 |
| [S-F20-L13 Maintenance notices](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l13-maintenance-notices.md) | Hosted support assistant (hosted edition) | Open: Planned, Running, Overrun | UC-F20-21 |
| [S-F20-L15 Incident reports](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l15-incident-reports.md) | Hosted support assistant (hosted edition) | Needs attention | UC-F20-10, UC-F20-23 |
| [S-F20-L17 NIS2 fact sheets](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l17-nis2-fact-sheets.md) | Hosted support assistant (hosted edition) | Needs attention | UC-F20-15, UC-F20-26 |
| [S-F20-L19 Engineer calls](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l19-engineer-calls.md) | Hosted support assistant (hosted edition) | Needs attention | UC-F20-29, UC-F20-30 |
| [S-F20-L20 Access grants](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l20-access-grants.md) | Hosted support assistant (hosted edition) | Needs attention | UC-F20-30 |
| [S-F21-L13 Onboarding figures](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l13-onboarding-figures.md) | Onboarding and module activation | All | UC-F21-20 |
| [S-F22-L02 Metered call records](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l02-metered-call-records.md) | Unified platform cost management | All | UC-F22-22, UC-F22-18, UC-F22-17 |
| [S-F22-L07 Cost alerts](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l07-cost-alerts.md) | Unified platform cost management | All | UC-F22-18 |
| [S-F22-L12 Invoice matches](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l12-invoice-matches.md) | Unified platform cost management | All | UC-F22-17 |
| [S-F22-L15 Compute machines](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l15-compute-machines.md) | Unified platform cost management | Open: InService | UC-F22-22, UC-F22-17 |
| [S-F25-L07 Reproductions](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l07-reproductions.md) | DevOps agents (hosted edition) | All | UC-F25-08 |
| [S-F25-L10 Agent runs](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l10-agent-runs.md) | DevOps agents (hosted edition) | All | UC-F25-17, UC-F25-18 |
| [S-F25-L12 Vulnerability cases](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l12-vulnerability-cases.md) | DevOps agents (hosted edition) | Open: Reported, Confirmed, Fixed | UC-F25-22 |
| [S-F25-L20 Agent roles](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l20-agent-roles.md) | DevOps agents (hosted edition) | Needs attention | UC-F25-31 |
| [S-F25-L23 Run checkpoints](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l23-run-checkpoints.md) | DevOps agents (hosted edition) | Needs attention | UC-F25-37 |
| [S-T04-L03 Plugin installations](../../../03-technical/t04-plugin-runtime/screens/00-lists/s-t04-l03-plugin-installations.md) | Plugin runtime | All | admin list (D494) |
| [S-T07-L04 Evaluation results](../../../03-technical/t07-ai-providers-and-models/screens/00-lists/s-t07-l04-evaluation-results.md) | AI providers and models | All | admin list (D494) |
| [S-T08-L03 Index jobs](../../../03-technical/t08-rag-platform/screens/00-lists/s-t08-l03-index-jobs.md) | RAG platform (Milvus) | All | admin list (D494) |
| [S-T09-L01 Server installations](../../../03-technical/t09-install-backups-and-updates/screens/00-lists/s-t09-l01-server-installations.md) | Install, backups and updates | All | admin list (D494) |
| [S-T09-L02 Restore points](../../../03-technical/t09-install-backups-and-updates/screens/00-lists/s-t09-l02-restore-points.md) | Install, backups and updates | All | admin list (D494) |
| [S-T09-L03 Upgrade runs](../../../03-technical/t09-install-backups-and-updates/screens/00-lists/s-t09-l03-upgrade-runs.md) | Install, backups and updates | All | admin list (D494) |
| [S-T09-L04 Namespace access grants](../../../03-technical/t09-install-backups-and-updates/screens/00-lists/s-t09-l04-namespace-access-grants.md) | Install, backups and updates | All | admin list (D494) |
| [S-T12-L04 Connector runs](../../../03-technical/t12-connectors-and-scrapers/screens/00-lists/s-t12-l04-connector-runs.md) | Connectors and scrapers | All | admin list (D494) |

## Navigation

Each view also sits in its capability's menu (D495):
[AI providers and models](../../../03-technical/t07-ai-providers-and-models/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Connectors and scrapers](../../../03-technical/t12-connectors-and-scrapers/screens/00-lists/README.md),
[DevOps agents (hosted edition)](../../../02-functional/f25-devops-agents/screens/00-lists/README.md),
[Feature factory (hosted edition)](../../../02-functional/f19-feature-factory/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Hosted support assistant (hosted edition)](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/README.md),
[Hosted websites and domains (hosted edition)](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/README.md),
[Install, backups and updates](../../../03-technical/t09-install-backups-and-updates/screens/00-lists/README.md),
[Onboarding and module activation](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/README.md),
[Plugin runtime](../../../03-technical/t04-plugin-runtime/screens/00-lists/README.md),
[RAG platform (Milvus)](../../../03-technical/t08-rag-platform/screens/00-lists/README.md),
[Unified platform cost management](../../../02-functional/f22-unified-cost-management/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U48 | desktop | ![Workspace, U48, light](mockups/workspace-desktop-light.png) | ![Workspace, U48, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U48 | phone | ![Workspace, U48, light](mockups/workspace-phone-light.png) | ![Workspace, U48, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
