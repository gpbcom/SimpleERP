🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🍽️ [Waiter: app shell and home](README.md) › 🧰 U18 Waiter: workspace

# 🧰 U18 Waiter: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U18 Waiter](../../../01-users/personas/u18-waiter.md) works with, embedded on their [home screen](README.md)
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
| [S-F6-L01 Customer records](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l01-customer-records.md) | Customers and sales | All | UC-SC06-21 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F10-L01 Point of sales](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l01-point-of-sales.md) | Point of sale (plugin) | All | UC-F10-16 |
| [S-F10-L02 Till sessions](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l02-till-sessions.md) | Point of sale (plugin) | Open: Open, Closing, Posted | UC-F10-20 |
| [S-F10-L03 Point of sale orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l03-point-of-sale-orders.md) | Point of sale (plugin) | Mine: customer | UC-F10-03, UC-F10-09, UC-F10-11, UC-F10-20 |
| [S-F10-L04 Till payments](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l04-till-payments.md) | Point of sale (plugin) | All | UC-F10-03, UC-F10-11, UC-F10-21 |
| [S-F10-L11 Floor and tables](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l11-floor-and-tables.md) | Point of sale (plugin) | All | UC-F10-09 |
| [S-F10-L12 Table bookings](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l12-table-bookings.md) | Point of sale (plugin) | All | UC-F10-09 |
| [S-F10-L16 Age checks](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l16-age-checks.md) | Point of sale (plugin) | All | UC-F10-22 |
| [S-SC06-L05 Staff benefits](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l05-staff-benefits.md) | Restaurant and hospitality | All | UC-SC06-05 |
| [S-SC06-L09 Folios](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l09-folios.md) | Restaurant and hospitality | All | UC-SC06-11 |
| [S-SC06-L12 Meal voucher payments](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l12-meal-voucher-payments.md) | Restaurant and hospitality | All | UC-SC06-13 |
| [S-SC06-L18 Guest profiles](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l18-guest-profiles.md) | Restaurant and hospitality | All | UC-SC06-21 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Restaurant and hospitality](../../../08-sectors/sc06-hospitality/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U18 | desktop | ![Workspace, U18, light](mockups/workspace-desktop-light.png) | ![Workspace, U18, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U18 | phone | ![Workspace, U18, light](mockups/workspace-phone-light.png) | ![Workspace, U18, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
