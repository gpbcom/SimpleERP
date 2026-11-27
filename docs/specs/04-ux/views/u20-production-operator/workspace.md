🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🧑‍🏭 [Production operator: app shell and home](README.md) › 🧰 U20 Production operator: workspace

# 🧰 U20 Production operator: workspace

**Status:** ✅ specified

## Purpose

The views [U20 Production operator](../../../01-users/personas/u20-production-operator.md) works with, embedded on their
[home screen](README.md)
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
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F6-L27 Warranties](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l27-warranties.md) | Customers and sales | All | UC-SC05-17 |
| [S-F7-L02 Purchase requests](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l02-purchase-requests.md) | Purchasing and stock | All | UC-F12-33 |
| [S-F7-L04 Transfers](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l04-transfers.md) | Purchasing and stock | Open: Sent, Received, Reserved | UC-F12-33 |
| [S-F7-L07 Locations](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l07-locations.md) | Purchasing and stock | All | UC-SC05-19 |
| [S-F7-L10 Lot or serials](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l10-lot-or-serials.md) | Purchasing and stock | All | UC-SC05-17, UC-SC05-19 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F9-L12 Certifications](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l12-certifications.md) | HR and projects | Mine: employee | UC-F12-22 |
| [S-F12-L03 Routing operations](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l03-routing-operations.md) | Manufacturing (plugin) | All | UC-F12-28 |
| [S-F12-L04 Manufacturing orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l04-manufacturing-orders.md) | Manufacturing (plugin) | Open: Draft, Confirmed, InProgress | UC-F12-11, UC-F12-20, UC-F12-31 |
| [S-F12-L05 Work orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l05-work-orders.md) | Manufacturing (plugin) | Open: New, Late | UC-F12-05, UC-F12-20, UC-F12-26 |
| [S-F12-L06 Component consumptions](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l06-component-consumptions.md) | Manufacturing (plugin) | All | UC-F12-06, UC-F12-26 |
| [S-F12-L07 Quality control points](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l07-quality-control-points.md) | Manufacturing (plugin) | All | UC-F12-07, UC-F12-25 |
| [S-F12-L08 Non-conformities](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l08-non-conformities.md) | Manufacturing (plugin) | Open: Open, InProgress | UC-F12-07 |
| [S-F12-L09 Equipments](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l09-equipments.md) | Manufacturing (plugin) | All | UC-F12-08 |
| [S-F12-L10 Maintenance requests](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l10-maintenance-requests.md) | Manufacturing (plugin) | All | UC-F12-08 |
| [S-F12-L17 Qualification requirements](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l17-qualification-requirements.md) | Manufacturing (plugin) | All | UC-F12-22, UC-SC05-13 |
| [S-F12-L20 Control charts](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l20-control-charts.md) | Manufacturing (plugin) | All | UC-F12-25 |
| [S-F12-L22 Work instruction versions](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l22-work-instruction-versions.md) | Manufacturing (plugin) | All | UC-F12-28 |
| [S-F12-L25 Recipes](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l25-recipes.md) | Manufacturing (plugin) | All | UC-F12-31, UC-SC05-02, UC-SC13-13 |
| [S-F12-L28 Shop-floor terminals](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l28-shop-floor-terminals.md) | Manufacturing (plugin) | All | UC-F12-05 |
| [S-F12-L29 Unbuild orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l29-unbuild-orders.md) | Manufacturing (plugin) | All | UC-F12-11 |
| [S-F12-L31 Kanban cards](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l31-kanban-cards.md) | Manufacturing (plugin) | Mine: station | UC-F12-33 |
| [S-F12-L33 Tools](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l33-tools.md) | Manufacturing (plugin) | Mine: work centre | UC-F12-35 |
| [S-SC05-L02 Batch recipes](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l02-batch-recipes.md) | Manufacturing | All | UC-SC05-02 |
| [S-SC05-L06 Label templates](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l06-label-templates.md) | Manufacturing | All | UC-SC05-06 |
| [S-SC05-L07 Controlled documents](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l07-controlled-documents.md) | Manufacturing | Open: Draft, Approved | UC-SC05-07 |
| [S-SC05-L13 Operation qualifications](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l13-operation-qualifications.md) | Manufacturing | All | UC-SC05-13 |
| [S-SC05-L16 Graded units](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l16-graded-units.md) | Manufacturing | All | UC-SC05-17 |
| [S-SC05-L18 Remnants](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l18-remnants.md) | Manufacturing | All | UC-SC05-19 |
| [S-SC13-L04 Lots](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l04-lots.md) | Agriculture and food | Open: Blocked, Refused | UC-SC13-13 |
| [S-SC13-L12 Batches](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l12-batches.md) | Agriculture and food | All | UC-SC13-13 |
| [S-SC13-L13 Hygiene readings](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l13-hygiene-readings.md) | Agriculture and food | All | UC-SC13-15 |
| [S-SC15-L14 Pallets](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l14-pallets.md) | Wholesale and distribution | All | UC-SC05-06 |

## Navigation

Each view also sits in its capability's menu (D495):
[Agriculture and food](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Manufacturing](../../../08-sectors/sc05-manufacturing/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Wholesale and distribution](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U20 | desktop | ![Workspace, U20, light](mockups/workspace-desktop-light.png) | ![Workspace, U20, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U20 | phone | ![Workspace, U20, light](mockups/workspace-phone-light.png) | ![Workspace, U20, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
