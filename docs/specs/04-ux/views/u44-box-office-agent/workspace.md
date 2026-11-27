🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🎟️ [Box-office agent: app shell and home](README.md) › 🧰 U44 Box-office agent: workspace

# 🧰 U44 Box-office agent: workspace

**Status:** ✅ specified

## Purpose

The views [U44 Box-office agent](../../../01-users/personas/u44-box-office-agent.md) works with, embedded on their
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
| [S-F5-L11 Ticket type and seat maps](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l11-ticket-type-and-seat-maps.md) | Social media and marketing | Open: Draft | UC-F5-18 |
| [S-F5-L12 Event tickets](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l12-event-tickets.md) | Social media and marketing | Mine: holder | UC-F5-18, UC-SC16-05 |
| [S-F8-L06 Tax returns](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l06-tax-returns.md) | Accounting | Open: Prepared, Validated, Filed | UC-SC16-22 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F10-L16 Age checks](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l16-age-checks.md) | Point of sale (plugin) | All | UC-F10-22 |
| [S-SC16-L01 Shows](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l01-shows.md) | Events and culture | Open: OnSale, Approved, Held | UC-SC16-20 |
| [S-SC16-L07 Ticket orders](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l07-ticket-orders.md) | Events and culture | Open: Refunded, Exchanged | UC-SC16-05, UC-SC16-17 |
| [S-SC16-L08 Admission tickets](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l08-admission-tickets.md) | Events and culture | Open: Sent | UC-SC16-05, UC-SC16-06, UC-SC16-07 |
| [S-SC16-L09 Accreditations](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l09-accreditations.md) | Events and culture | All | UC-SC16-08 |
| [S-SC16-L10 Staffing posts](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l10-staffing-posts.md) | Events and culture | All | UC-SC16-20 |
| [S-SC16-L16 Memberships](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l16-memberships.md) | Events and culture | All | UC-SC16-16 |
| [S-SC16-L18 Ticket refunds](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l18-ticket-refunds.md) | Events and culture | All | UC-SC16-17 |
| [S-SC16-L19 Cashless accounts](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l19-cashless-accounts.md) | Events and culture | All | UC-SC16-21 |
| [S-SC16-L20 Screenings](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l20-screenings.md) | Events and culture | All | UC-SC16-22 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Events and culture](../../../08-sectors/sc16-events-and-culture/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U44 | desktop | ![Workspace, U44, light](mockups/workspace-desktop-light.png) | ![Workspace, U44, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U44 | phone | ![Workspace, U44, light](mockups/workspace-phone-light.png) | ![Workspace, U44, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
