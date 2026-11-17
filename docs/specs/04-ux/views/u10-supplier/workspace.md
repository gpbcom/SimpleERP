🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🚚 [Supplier: app shell and home](README.md) › 🧰 U10 Supplier: workspace

# 🧰 U10 Supplier: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U10 Supplier](../../../01-users/personas/u10-supplier.md) works with, embedded on their
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
| [S-F1-L17 Portal accounts](../../../02-functional/f01-administration/screens/00-lists/s-f01-l17-portal-accounts.md) | Administration | All | UC-F1-19 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F7-L01 Supplier records](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l01-supplier-records.md) | Purchasing and stock | All | UC-F7-12 |
| [S-F7-L03 Purchase orders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l03-purchase-orders.md) | Purchasing and stock | All | UC-F7-12 |
| [S-F7-L13 Call for tenders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l13-call-for-tenders.md) | Purchasing and stock | All | UC-F7-14 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F9-L18 Project and tasks](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l18-project-and-tasks.md) | HR and projects | Open: New, Planned, Active | UC-F9-32 |
| [S-F9-L27 Subcontractor assignments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l27-subcontractor-assignments.md) | HR and projects | Open: Proposed, Active | UC-F9-32 |

## Navigation

Each view also sits in its capability's menu (D495):
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U10 | desktop | ![Workspace, U10, light](mockups/workspace-desktop-light.png) | ![Workspace, U10, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U10 | phone | ![Workspace, U10, light](mockups/workspace-phone-light.png) | ![Workspace, U10, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
