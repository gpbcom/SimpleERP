🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🛠️ [SimpleERP maintainer: app shell and home](README.md) › 🧰 U47 SimpleERP maintainer: workspace

# 🧰 U47 SimpleERP maintainer: workspace

**Status:** ✅ specified

## Purpose

The views [U47 SimpleERP maintainer](../../../01-users/personas/u47-simpleerp-maintainer.md) works with, embedded on
their [home screen](README.md)
([D484](../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D493](../../../06-decisions/ux/d493-persona-workspaces-from-the-use-cases.md),
[D495](../../../06-decisions/ux/d495-views-listed-under-each-capabilitys-menu.md)): the list of each record type their
use cases and flow charts work on, with the owner's review of 2026-11-13
([D519](../../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)). Each view opens on the
persona's default saved view. The default is the view's "Mine" for a persona who works on their own records,
"Needs attention" for one who oversees others' (managers, the owner, HR, the administrators and the planner roles), else
"Open", else "All".

## Embedded views

| View | Capability | Default saved view | Why |
|---|---|---|---|
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F24-L01 Connectors](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l01-connectors.md) | Integrations hub | All | UC-F24-18 |
| [S-F24-L10 Connector incidents](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l10-connector-incidents.md) | Integrations hub | All | UC-F24-16 |
| [S-F24-L11 Connector categories](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l11-connector-categories.md) | Integrations hub | Open: Active | UC-F24-27 |
| [S-F24-L12 Integration icons](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l12-integration-icons.md) | Integrations hub | Open: Proposed, Approved, Replaced | UC-F24-27 |
| [S-F24-L15 Connector catalogue reviews](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l15-connector-catalogue-reviews.md) | Integrations hub | All | UC-F24-18 |
| [S-F25-L01 Bug or feature requests](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l01-bug-or-feature-requests.md) | DevOps agents (hosted edition) | All | UC-F25-16 |
| [S-F25-L02 USER features](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l02-user-features.md) | DevOps agents (hosted edition) | All | UC-F25-03, UC-F25-04 |
| [S-F25-L03 USER tickets](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l03-user-tickets.md) | DevOps agents (hosted edition) | All | UC-F25-03, UC-F25-21, UC-F25-07 |
| [S-F25-L04 Study notes](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l04-study-notes.md) | DevOps agents (hosted edition) | All | UC-F25-05 |
| [S-F25-L05 Agent pull requests](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l05-agent-pull-requests.md) | DevOps agents (hosted edition) | All | UC-F25-06, UC-F25-23, UC-F25-10, UC-F25-13 |
| [S-F25-L06 Agent tickets](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l06-agent-tickets.md) | DevOps agents (hosted edition) | All | UC-F25-07, UC-F25-11, UC-F25-12 |
| [S-F25-L07 Reproductions](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l07-reproductions.md) | DevOps agents (hosted edition) | All | UC-F25-08, UC-F25-09 |
| [S-F25-L08 Approvals](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l08-approvals.md) | DevOps agents (hosted edition) | All | UC-F25-12, UC-F25-13, UC-F25-19 |
| [S-F25-L10 Agent runs](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l10-agent-runs.md) | DevOps agents (hosted edition) | All | UC-F25-17, UC-F25-18, UC-F25-19 |
| [S-F25-L11 Triages](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l11-triages.md) | DevOps agents (hosted edition) | Open: Triaged, Acknowledged, Late | UC-F25-03, UC-F25-21 |
| [S-F25-L12 Vulnerability cases](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l12-vulnerability-cases.md) | DevOps agents (hosted edition) | Open: Reported, Confirmed, Fixed | UC-F25-22 |
| [S-F25-L13 Spec check reports](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l13-spec-check-reports.md) | DevOps agents (hosted edition) | All | UC-F25-06, UC-F25-23, UC-F25-19 |
| [S-F25-L14 Votes](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l14-votes.md) | DevOps agents (hosted edition) | Open: Counted | UC-F25-12 |
| [S-F25-L15 SPECS features](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l15-specs-features.md) | DevOps agents (hosted edition) | All | UC-F25-07 |
| [S-F25-L16 Roadmap items](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l16-roadmap-items.md) | DevOps agents (hosted edition) | All | UC-F25-25 |
| [S-F25-L18 Report credits](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l18-report-credits.md) | DevOps agents (hosted edition) | All | UC-F25-27 |
| [S-F25-L19 Work contracts](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l19-work-contracts.md) | DevOps agents (hosted edition) | All | UC-F25-29, UC-F25-30, UC-F25-31, UC-F25-32 and more |
| [S-F25-L20 Agent roles](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l20-agent-roles.md) | DevOps agents (hosted edition) | All | UC-F25-29, UC-F25-31, UC-F25-32, UC-F25-33 and more |
| [S-F25-L21 Worker handoffs](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l21-worker-handoffs.md) | DevOps agents (hosted edition) | All | UC-F25-32, UC-F25-33, UC-F25-35 |
| [S-F25-L22 Verifications](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l22-verifications.md) | DevOps agents (hosted edition) | All | UC-F25-34, UC-F25-35, UC-F25-36 |
| [S-F25-L23 Run checkpoints](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l23-run-checkpoints.md) | DevOps agents (hosted edition) | All | UC-F25-36 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[DevOps agents (hosted edition)](../../../02-functional/f25-devops-agents/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Integrations hub](../../../02-functional/f24-integrations-hub/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U47 | desktop | ![Workspace, U47, light](mockups/workspace-desktop-light.png) | ![Workspace, U47, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U47 | phone | ![Workspace, U47, light](mockups/workspace-phone-light.png) | ![Workspace, U47, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
