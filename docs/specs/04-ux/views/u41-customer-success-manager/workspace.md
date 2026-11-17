🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🚀 [Customer success manager: app shell and home](README.md) › 🧰 U41 Customer success manager: workspace

# 🧰 U41 Customer success manager: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U41 Customer success manager](../../../01-users/personas/u41-customer-success-manager.md) works with,
embedded on their [home screen](README.md)
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
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F6-L01 Customer records](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l01-customer-records.md) | Customers and sales | All | UC-F6-17 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-F16-22, UC-SC14-23 |
| [S-F6-L07 Subscription contracts](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l07-subscription-contracts.md) | Customers and sales | All | UC-SC14-23 |
| [S-F6-L11 Timeline entries](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l11-timeline-entries.md) | Customers and sales | All | UC-F6-17 |
| [S-F7-L05 Supplier invoices](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l05-supplier-invoices.md) | Purchasing and stock | All | UC-SC14-23 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F16-L16 Support contracts](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l16-support-contracts.md) | Customer support agents | All | UC-F16-22 |
| [S-SC14-L01 Software subscriptions](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l01-software-subscriptions.md) | IT and software | Open: Trial, Active | UC-SC14-10, UC-SC14-18 |
| [S-SC14-L04 Software licences](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l04-software-licences.md) | IT and software | All | UC-SC14-04 |
| [S-SC14-L05 Service levels](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l05-service-levels.md) | IT and software | All | UC-SC14-05 |
| [S-SC14-L06 Managed assets](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l06-managed-assets.md) | IT and software | All | UC-SC14-06 |
| [S-SC14-L08 Software release notes](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l08-software-release-notes.md) | IT and software | All | UC-SC14-08, UC-SC14-21 |
| [S-SC14-L09 Health scores](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l09-health-scores.md) | IT and software | All | UC-SC14-09, UC-SC14-10, UC-SC14-18, UC-SC14-20 |
| [S-SC14-L16 Tracked features](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l16-tracked-features.md) | IT and software | All | UC-SC14-21, UC-SC14-20 |
| [S-SC14-L18 Licence subscriptions](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l18-licence-subscriptions.md) | IT and software | All | UC-SC14-23 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customer support agents](../../../02-functional/f16-customer-support-agents/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[IT and software](../../../08-sectors/sc14-it-and-software/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U41 | desktop | ![Workspace, U41, light](mockups/workspace-desktop-light.png) | ![Workspace, U41, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U41 | phone | ![Workspace, U41, light](mockups/workspace-phone-light.png) | ![Workspace, U41, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
