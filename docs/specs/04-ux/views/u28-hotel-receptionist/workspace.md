🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🛎️ [Hotel receptionist: app shell and home](README.md) › 🧰 U28 Hotel receptionist: workspace

# 🧰 U28 Hotel receptionist: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U28 Hotel receptionist](../../../01-users/personas/u28-hotel-receptionist.md) works with, embedded on their
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
| [S-F2-L05 Record types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l05-record-types.md) | No-code configuration | Needs attention | UC-F2-18 |
| [S-F2-L17 Bookable resource settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l17-bookable-resource-settings.md) | No-code configuration | Needs attention | UC-F2-18, UC-F2-19, UC-SC06-07 |
| [S-F2-L18 Resource bookings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l18-resource-bookings.md) | No-code configuration | Open: Requested, Confirmed, NoShow | UC-F2-19, UC-SC06-08 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Needs attention | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | All | flow charts (VR-3) |
| [S-F6-L01 Customer records](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l01-customer-records.md) | Customers and sales | All | UC-SC06-21 |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Needs attention | D519, VC-14 |
| [S-F6-L04 Orders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l04-orders.md) | Customers and sales | Open: Open, InProgress | UC-SC06-18 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-SC06-L02 Menu dishes](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l02-menu-dishes.md) | Restaurant and hospitality | All | UC-SC06-15 |
| [S-SC06-L06 Hotel rooms](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l06-hotel-rooms.md) | Restaurant and hospitality | All | UC-SC06-07, UC-SC06-10 |
| [S-SC06-L07 Rate plans](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l07-rate-plans.md) | Restaurant and hospitality | All | UC-SC06-07 |
| [S-SC06-L08 Room reservations](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l08-room-reservations.md) | Restaurant and hospitality | Open: Booked, Arrived, Departed | UC-SC06-08, UC-SC06-15, UC-SC06-09 |
| [S-SC06-L09 Folios](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l09-folios.md) | Restaurant and hospitality | Needs attention | UC-SC06-09, UC-SC06-11 |
| [S-SC06-L10 Housekeeping tasks](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l10-housekeeping-tasks.md) | Restaurant and hospitality | All | UC-SC06-10 |
| [S-SC06-L11 Tourist tax lines](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l11-tourist-tax-lines.md) | Restaurant and hospitality | All | UC-SC06-12 |
| [S-SC06-L13 Pitches](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l13-pitches.md) | Restaurant and hospitality | All | UC-SC06-16 |
| [S-SC06-L15 Group bookings](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l15-group-bookings.md) | Restaurant and hospitality | All | UC-SC06-18 |
| [S-SC06-L16 Price rules](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l16-price-rules.md) | Restaurant and hospitality | All | UC-SC06-19 |
| [S-SC06-L18 Guest profiles](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l18-guest-profiles.md) | Restaurant and hospitality | All | UC-SC06-21 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Restaurant and hospitality](../../../08-sectors/sc06-hospitality/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U28 | desktop | ![Workspace, U28, light](mockups/workspace-desktop-light.png) | ![Workspace, U28, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U28 | phone | ![Workspace, U28, light](mockups/workspace-phone-light.png) | ![Workspace, U28, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
