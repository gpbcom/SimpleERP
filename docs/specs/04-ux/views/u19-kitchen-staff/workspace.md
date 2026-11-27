🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
👩‍🍳 [Kitchen staff: app shell and home](README.md) › 🧰 U19 Kitchen staff: workspace

# 🧰 U19 Kitchen staff: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U19 Kitchen staff](../../../01-users/personas/u19-kitchen-staff.md) works with, embedded on their
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
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Open: Draft, ToApprove, Sent | UC-SC06-17 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F10-L01 Point of sales](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l01-point-of-sales.md) | Point of sale (plugin) | All | UC-F10-16 |
| [S-F10-L03 Point of sale orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l03-point-of-sale-orders.md) | Point of sale (plugin) | Mine: customer | UC-F10-10, UC-F10-17 |
| [S-F10-L13 Preparation tickets](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l13-preparation-tickets.md) | Point of sale (plugin) | All | UC-F10-10 |
| [S-F10-L22 Takeaway orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l22-takeaway-orders.md) | Point of sale (plugin) | Mine: customer | UC-F10-29 |
| [S-F12-L04 Manufacturing orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l04-manufacturing-orders.md) | Manufacturing (plugin) | Open: Draft, Confirmed, InProgress | UC-F12-31 |
| [S-F12-L25 Recipes](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l25-recipes.md) | Manufacturing (plugin) | All | UC-F12-31, UC-SC06-01 |
| [S-SC06-L02 Menu dishes](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l02-menu-dishes.md) | Restaurant and hospitality | All | UC-SC06-01 |
| [S-SC06-L03 Hygiene records](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l03-hygiene-records.md) | Restaurant and hospitality | All | UC-SC06-03 |
| [S-SC06-L04 Waste records](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l04-waste-records.md) | Restaurant and hospitality | All | UC-SC06-04 |
| [S-SC06-L14 Catering orders](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l14-catering-orders.md) | Restaurant and hospitality | All | UC-SC06-17 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Restaurant and hospitality](../../../08-sectors/sc06-hospitality/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U19 | desktop | ![Workspace, U19, light](mockups/workspace-desktop-light.png) | ![Workspace, U19, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U19 | phone | ![Workspace, U19, light](mockups/workspace-phone-light.png) | ![Workspace, U19, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
