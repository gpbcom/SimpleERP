🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🙋 [Volunteer: app shell and home](README.md) › 🧰 U32 Volunteer: workspace

# 🧰 U32 Volunteer: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U32 Volunteer](../../../01-users/personas/u32-volunteer.md) works with, embedded on their
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
| [S-F5-L07 Registration events](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l07-registration-events.md) | Social media and marketing | Open: Draft, Planned, Published | UC-SC08-12 |
| [S-F5-L12 Event tickets](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l12-event-tickets.md) | Social media and marketing | Mine: holder | UC-SC08-12 |
| [S-F8-L20 Volunteer contributions](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l20-volunteer-contributions.md) | Accounting | All | UC-SC08-11 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-SC08-L10 Missions](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l10-missions.md) | Non-profit association | All | UC-SC08-10 |
| [S-SC08-L11 Volunteer hours](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l11-volunteer-hours.md) | Non-profit association | All | UC-SC08-11 |
| [S-SC08-L12 Association events](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l12-association-events.md) | Non-profit association | Open: Planned | UC-SC08-12 |
| [S-SC08-L13 Temporary bars](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l13-temporary-bars.md) | Non-profit association | Mine: authorisation | UC-SC08-13 |
| [S-SC16-L10 Staffing posts](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l10-staffing-posts.md) | Events and culture | All | UC-SC16-09 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Events and culture](../../../08-sectors/sc16-events-and-culture/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Non-profit association](../../../08-sectors/sc08-non-profit/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U32 | desktop | ![Workspace, U32, light](mockups/workspace-desktop-light.png) | ![Workspace, U32, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U32 | phone | ![Workspace, U32, light](mockups/workspace-phone-light.png) | ![Workspace, U32, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
