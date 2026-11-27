🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🧳 [Sales representative: app shell and home](README.md) › 🧰 U42 Sales representative: workspace

# 🧰 U42 Sales representative: workspace

**Status:** ✅ specified

## Purpose

The views [U42 Sales representative](../../../01-users/personas/u42-sales-representative.md) works with, embedded on
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
| [S-F2-L20 Offline form settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l20-offline-form-settings.md) | No-code configuration | Mine: roles | UC-F6-21 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F6-L04 Orders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l04-orders.md) | Customers and sales | Open: Open, InProgress | UC-F6-21 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-SC15-21, UC-SC15-22 |
| [S-F6-L06 Customer payments](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l06-customer-payments.md) | Customers and sales | All | UC-SC15-22 |
| [S-F6-L18 Commission plan and targets](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l18-commission-plan-and-targets.md) | Customers and sales | Open: Draft, Active | UC-F6-25, UC-SC15-14 |
| [S-F6-L19 Commission lines](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l19-commission-lines.md) | Customers and sales | Mine: rep | UC-F6-25 |
| [S-F7-L11 Stock counts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l11-stock-counts.md) | Purchasing and stock | All | UC-SC15-22 |
| [S-F7-L25 Packaging deposits](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l25-packaging-deposits.md) | Purchasing and stock | All | UC-SC15-21 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F9-L16 Shifts](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l16-shifts.md) | HR and projects | Mine: role | UC-F9-30 |
| [S-F9-L26 Rounds](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l26-rounds.md) | HR and projects | Mine: person | UC-F9-30, UC-SC15-14 |
| [S-T13-L02 Routes](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l02-routes.md) | Maps and geodata | All | UC-F9-30 |
| [S-SC15-L01 Price agreements](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l01-price-agreements.md) | Wholesale and distribution | Open: Active | UC-SC15-01, UC-SC15-20 |
| [S-SC15-L04 Sales orders](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l04-sales-orders.md) | Wholesale and distribution | All | UC-SC15-05, UC-SC15-20 |
| [S-SC15-L11 Visit reports](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l11-visit-reports.md) | Wholesale and distribution | All | UC-SC15-14 |
| [S-SC15-L15 Bar loans](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l15-bar-loans.md) | Wholesale and distribution | All | UC-SC15-21 |
| [S-SC15-L16 Van stocks](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l16-van-stocks.md) | Wholesale and distribution | All | UC-SC15-22 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Maps and geodata](../../../03-technical/t13-maps-and-geodata/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Wholesale and distribution](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U42 | desktop | ![Workspace, U42, light](mockups/workspace-desktop-light.png) | ![Workspace, U42, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U42 | phone | ![Workspace, U42, light](mockups/workspace-phone-light.png) | ![Workspace, U42, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
