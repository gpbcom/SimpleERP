🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
✅ [Quality manager: app shell and home](README.md) › 🧰 U27 Quality manager: workspace

# 🧰 U27 Quality manager: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U27 Quality manager](../../../01-users/personas/u27-quality-manager.md) works with, embedded on their
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
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F6-L27 Warranties](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l27-warranties.md) | Customers and sales | All | UC-SC05-17 |
| [S-F7-L01 Supplier records](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l01-supplier-records.md) | Purchasing and stock | All | UC-F7-19 |
| [S-F7-L07 Locations](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l07-locations.md) | Purchasing and stock | All | UC-F7-23 |
| [S-F7-L10 Lot or serials](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l10-lot-or-serials.md) | Purchasing and stock | All | UC-SC05-17, UC-SC15-24 |
| [S-F7-L16 Supplier scores](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l16-supplier-scores.md) | Purchasing and stock | All | UC-F7-19 |
| [S-F7-L19 Safety data sheets](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l19-safety-data-sheets.md) | Purchasing and stock | All | UC-F7-23 |
| [S-F7-L22 Delivery notes](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l22-delivery-notes.md) | Purchasing and stock | All | UC-SC15-24 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F9-L24 Risk assessment lines](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l24-risk-assessment-lines.md) | HR and projects | All | UC-F9-27 |
| [S-F12-L07 Quality control points](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l07-quality-control-points.md) | Manufacturing (plugin) | All | UC-F12-25 |
| [S-F12-L09 Equipments](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l09-equipments.md) | Manufacturing (plugin) | All | UC-F12-21 |
| [S-F12-L10 Maintenance requests](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l10-maintenance-requests.md) | Manufacturing (plugin) | All | UC-F12-35 |
| [S-F12-L14 Product compliance files](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l14-product-compliance-files.md) | Manufacturing (plugin) | All | UC-F12-30 |
| [S-F12-L16 Calibrations](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l16-calibrations.md) | Manufacturing (plugin) | All | UC-F12-21, UC-SC05-12 |
| [S-F12-L17 Qualification requirements](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l17-qualification-requirements.md) | Manufacturing (plugin) | All | UC-SC05-13 |
| [S-F12-L19 FMEA lines](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l19-fmea-lines.md) | Manufacturing (plugin) | Open: Open | UC-F12-24 |
| [S-F12-L20 Control charts](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l20-control-charts.md) | Manufacturing (plugin) | All | UC-F12-25 |
| [S-F12-L24 Product passports](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l24-product-passports.md) | Manufacturing (plugin) | All | UC-F12-30 |
| [S-F12-L30 CAD documents](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l30-cad-documents.md) | Manufacturing (plugin) | Mine: reviewer | UC-F12-32 |
| [S-F12-L33 Tools](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l33-tools.md) | Manufacturing (plugin) | Mine: work centre | UC-F12-35 |
| [S-SC05-L04 Engineered designs](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l04-engineered-designs.md) | Manufacturing | All | UC-SC05-04 |
| [S-SC05-L07 Controlled documents](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l07-controlled-documents.md) | Manufacturing | Open: Draft, Approved | UC-SC05-07, UC-SC05-15 |
| [S-SC05-L08 Audits](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l08-audits.md) | Manufacturing | Open: Open | UC-SC05-08 |
| [S-SC05-L09 Quality actions](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l09-quality-actions.md) | Manufacturing | Open: Open, Effective | UC-SC05-08, UC-SC05-09, UC-SC05-15 |
| [S-SC05-L10 Supplier ratings](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l10-supplier-ratings.md) | Manufacturing | Mine: supplier | UC-SC05-10 |
| [S-SC05-L11 8D reports](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l11-8d-reports.md) | Manufacturing | All | UC-SC05-11 |
| [S-SC05-L12 Instruments](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l12-instruments.md) | Manufacturing | All | UC-SC05-12 |
| [S-SC05-L13 Operation qualifications](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l13-operation-qualifications.md) | Manufacturing | All | UC-SC05-13 |
| [S-SC05-L14 Management reviews](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l14-management-reviews.md) | Manufacturing | All | UC-SC05-14 |
| [S-SC05-L16 Graded units](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l16-graded-units.md) | Manufacturing | All | UC-SC05-17 |
| [S-SC13-L04 Lots](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l04-lots.md) | Agriculture and food | Open: Blocked, Refused | UC-SC13-14, UC-SC13-17 |
| [S-SC13-L11 Organic records](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l11-organic-records.md) | Agriculture and food | All | UC-SC13-12 |
| [S-SC13-L12 Batches](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l12-batches.md) | Agriculture and food | All | UC-SC13-14 |
| [S-SC13-L13 Hygiene readings](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l13-hygiene-readings.md) | Agriculture and food | All | UC-SC13-15 |
| [S-SC13-L14 Product labels](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l14-product-labels.md) | Agriculture and food | All | UC-SC13-16 |
| [S-SC13-L15 Recalls](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l15-recalls.md) | Agriculture and food | All | UC-SC13-17 |
| [S-SC15-L17 Device lots](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l17-device-lots.md) | Wholesale and distribution | All | UC-SC15-24 |

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
| Workspace, U27 | desktop | ![Workspace, U27, light](mockups/workspace-desktop-light.png) | ![Workspace, U27, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U27 | phone | ![Workspace, U27, light](mockups/workspace-phone-light.png) | ![Workspace, U27, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
