🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🗓️ [Production planner: app shell and home](README.md) › 🧰 U21 Production planner: workspace

# 🧰 U21 Production planner: workspace

**Status:** ✅ specified

## Purpose

The views [U21 Production planner](../../../01-users/personas/u21-production-planner.md) works with, embedded on their
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
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Needs attention | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | All | flow charts (VR-3) |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Needs attention | D519, VC-14 |
| [S-F7-L02 Purchase requests](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l02-purchase-requests.md) | Purchasing and stock | All | UC-F12-33 |
| [S-F7-L04 Transfers](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l04-transfers.md) | Purchasing and stock | Open: Sent, Received, Reserved | UC-F12-33 |
| [S-F7-L07 Locations](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l07-locations.md) | Purchasing and stock | All | UC-SC05-19 |
| [S-F7-L10 Lot or serials](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l10-lot-or-serials.md) | Purchasing and stock | All | UC-SC05-16, UC-SC05-19 |
| [S-F7-L21 Demand forecasts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l21-demand-forecasts.md) | Purchasing and stock | All | UC-F12-03 |
| [S-F8-L06 Tax returns](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l06-tax-returns.md) | Accounting | Open: Prepared, Validated, Filed | UC-SC05-16 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-F9-L12 Certifications](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l12-certifications.md) | HR and projects | Needs attention | UC-F12-22 |
| [S-F12-L01 Bill of materials](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l01-bill-of-materials.md) | Manufacturing (plugin) | Needs attention | UC-F12-01, UC-F12-10 |
| [S-F12-L02 Work centres](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l02-work-centres.md) | Manufacturing (plugin) | All | UC-F12-02, UC-F12-12, UC-F12-14 |
| [S-F12-L03 Routing operations](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l03-routing-operations.md) | Manufacturing (plugin) | All | UC-F12-02, UC-F12-28 |
| [S-F12-L04 Manufacturing orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l04-manufacturing-orders.md) | Manufacturing (plugin) | Needs attention | UC-F12-03, UC-F12-04, UC-F12-11, UC-F12-09 and more |
| [S-F12-L05 Work orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l05-work-orders.md) | Manufacturing (plugin) | Needs attention | UC-F12-04, UC-F12-20, UC-F12-23, UC-F12-26 |
| [S-F12-L06 Component consumptions](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l06-component-consumptions.md) | Manufacturing (plugin) | All | UC-F12-26 |
| [S-F12-L07 Quality control points](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l07-quality-control-points.md) | Manufacturing (plugin) | All | UC-F12-07, UC-F12-25 |
| [S-F12-L08 Non-conformities](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l08-non-conformities.md) | Manufacturing (plugin) | Needs attention | UC-F12-07 |
| [S-F12-L09 Equipments](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l09-equipments.md) | Manufacturing (plugin) | All | UC-F12-08, UC-F12-17, UC-F12-21 |
| [S-F12-L10 Maintenance requests](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l10-maintenance-requests.md) | Manufacturing (plugin) | All | UC-F12-08 |
| [S-F12-L11 Engineering changes](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l11-engineering-changes.md) | Manufacturing (plugin) | All | UC-F12-10 |
| [S-F12-L12 Master plan lines](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l12-master-plan-lines.md) | Manufacturing (plugin) | All | UC-F12-03 |
| [S-F12-L13 Machine signals](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l13-machine-signals.md) | Manufacturing (plugin) | All | UC-F12-13, UC-F12-14, UC-F12-19, UC-F12-29 |
| [S-F12-L14 Product compliance files](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l14-product-compliance-files.md) | Manufacturing (plugin) | All | UC-F12-16, UC-F12-30 |
| [S-F12-L15 Waste register lines](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l15-waste-register-lines.md) | Manufacturing (plugin) | All | UC-F12-18 |
| [S-F12-L16 Calibrations](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l16-calibrations.md) | Manufacturing (plugin) | Needs attention | UC-F12-21 |
| [S-F12-L17 Qualification requirements](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l17-qualification-requirements.md) | Manufacturing (plugin) | All | UC-F12-22 |
| [S-F12-L18 Schedule slots](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l18-schedule-slots.md) | Manufacturing (plugin) | Open: Planned, Published | UC-F12-23 |
| [S-F12-L19 FMEA lines](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l19-fmea-lines.md) | Manufacturing (plugin) | Needs attention | UC-F12-24 |
| [S-F12-L20 Control charts](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l20-control-charts.md) | Manufacturing (plugin) | All | UC-F12-25 |
| [S-F12-L21 Work-in-progress valuations](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l21-work-in-progress-valuations.md) | Manufacturing (plugin) | All | UC-F12-27 |
| [S-F12-L22 Work instruction versions](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l22-work-instruction-versions.md) | Manufacturing (plugin) | Needs attention | UC-F12-28 |
| [S-F12-L23 Energy readings](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l23-energy-readings.md) | Manufacturing (plugin) | All | UC-F12-29 |
| [S-F12-L24 Product passports](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l24-product-passports.md) | Manufacturing (plugin) | Needs attention | UC-F12-30 |
| [S-F12-L25 Recipes](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l25-recipes.md) | Manufacturing (plugin) | Needs attention | UC-F12-31, UC-SC05-02, UC-SC13-13 |
| [S-F12-L26 Risk assessments](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l26-risk-assessments.md) | Manufacturing (plugin) | All | UC-F12-17 |
| [S-F12-L27 Safety registers](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l27-safety-registers.md) | Manufacturing (plugin) | All | UC-F12-17 |
| [S-F12-L29 Unbuild orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l29-unbuild-orders.md) | Manufacturing (plugin) | All | UC-F12-11 |
| [S-F12-L30 CAD documents](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l30-cad-documents.md) | Manufacturing (plugin) | Mine: reviewer | UC-F12-32 |
| [S-F12-L31 Kanban cards](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l31-kanban-cards.md) | Manufacturing (plugin) | Mine: station | UC-F12-33 |
| [S-F12-L32 MPS lines](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l32-mps-lines.md) | Manufacturing (plugin) | Mine: planner | UC-F12-34 |
| [S-F23-L05 Impact results](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l05-impact-results.md) | What-if simulation and impact | All | UC-F23-10 |
| [S-SC05-L01 Production setups](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l01-production-setups.md) | Manufacturing | All | UC-SC05-01 |
| [S-SC05-L02 Batch recipes](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l02-batch-recipes.md) | Manufacturing | All | UC-SC05-02 |
| [S-SC05-L03 Configuration rules](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l03-configuration-rules.md) | Manufacturing | All | UC-SC05-03 |
| [S-SC05-L04 Engineered designs](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l04-engineered-designs.md) | Manufacturing | All | UC-SC05-04 |
| [S-SC05-L05 Customer-supplied parts](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l05-customer-supplied-parts.md) | Manufacturing | All | UC-SC05-05 |
| [S-SC05-L07 Controlled documents](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l07-controlled-documents.md) | Manufacturing | Needs attention | UC-SC05-15 |
| [S-SC05-L09 Quality actions](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l09-quality-actions.md) | Manufacturing | Needs attention | UC-SC05-09, UC-SC05-15 |
| [S-SC05-L15 Bonded stocks](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l15-bonded-stocks.md) | Manufacturing | All | UC-SC05-16 |
| [S-SC05-L18 Remnants](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l18-remnants.md) | Manufacturing | All | UC-SC05-19 |
| [S-SC13-L04 Lots](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l04-lots.md) | Agriculture and food | Needs attention | UC-SC13-13 |
| [S-SC13-L12 Batches](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l12-batches.md) | Agriculture and food | All | UC-SC13-13 |
| [S-SC13-L14 Product labels](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l14-product-labels.md) | Agriculture and food | All | UC-SC13-16 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Agriculture and food](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Manufacturing](../../../08-sectors/sc05-manufacturing/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[What-if simulation and impact](../../../02-functional/f23-what-if-simulation/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U21 | desktop | ![Workspace, U21, light](mockups/workspace-desktop-light.png) | ![Workspace, U21, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U21 | phone | ![Workspace, U21, light](mockups/workspace-phone-light.png) | ![Workspace, U21, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
