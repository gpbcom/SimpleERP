🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
👷 [Site manager: app shell and home](README.md) › 🧰 U22 Site manager: workspace

# 🧰 U22 Site manager: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U22 Site manager](../../../01-users/personas/u22-site-manager.md) works with, embedded on their
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
| [S-F2-L03 Form layouts](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l03-form-layouts.md) | No-code configuration | Needs attention | UC-F2-21 |
| [S-F2-L04 List views](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l04-list-views.md) | No-code configuration | Needs attention | UC-F2-17 |
| [S-F2-L16 Visual views](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l16-visual-views.md) | No-code configuration | Needs attention | UC-F2-17 |
| [S-F2-L20 Offline form settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l20-offline-form-settings.md) | No-code configuration | Needs attention | UC-F2-21, UC-F2-22 |
| [S-F2-L28 Offline change queues](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l28-offline-change-queues.md) | No-code configuration | All | UC-F2-22 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Needs attention | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | All | flow charts (VR-3) |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Needs attention | D519, VC-14 |
| [S-F8-L18 Grants](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l18-grants.md) | Accounting | Open: Granted, Received | UC-SC19-14 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-SC01-L01 Construction sites](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l01-construction-sites.md) | Construction | Open: Planned, Running, Accepted | UC-SC01-01, UC-SC01-15, UC-SC01-14 |
| [S-SC01-L02 Quote lots](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l02-quote-lots.md) | Construction | All | UC-SC01-01, UC-SC01-02 |
| [S-SC01-L03 Site phases](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l03-site-phases.md) | Construction | All | UC-SC01-03 |
| [S-SC01-L04 Site time and material entries](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l04-site-time-and-material-entries.md) | Construction | All | UC-SC01-04 |
| [S-SC01-L05 Site diary entries](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l05-site-diary-entries.md) | Construction | All | UC-SC01-05, UC-SC01-15 |
| [S-SC01-L06 Progress bills](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l06-progress-bills.md) | Construction | Needs attention | UC-SC01-06, UC-SC01-14 |
| [S-SC01-L07 Subcontracts](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l07-subcontracts.md) | Construction | All | UC-SC01-07 |
| [S-SC01-L08 Equipment assignments](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l08-equipment-assignments.md) | Construction | All | UC-SC01-03, UC-SC01-08 |
| [S-SC01-L09 Works declarations](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l09-works-declarations.md) | Construction | All | UC-SC01-09 |
| [S-SC01-L10 Acceptance records](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l10-acceptance-records.md) | Construction | All | UC-SC01-10, UC-SC01-11 |
| [S-SC01-L11 Warranties](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l11-warranties.md) | Construction | All | UC-SC01-10, UC-SC01-11 |
| [S-SC01-L13 As-built files](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l13-as-built-files.md) | Construction | All | UC-SC01-11 |
| [S-SC01-L14 Site safety documents](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l14-site-safety-documents.md) | Construction | All | UC-SC01-09 |
| [S-SC01-L15 Revision formulas](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l15-revision-formulas.md) | Construction | All | UC-SC01-16 |
| [S-SC01-L17 BIM imports](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l17-bim-imports.md) | Construction | All | UC-SC01-18 |
| [S-SC01-L18 Grant files](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l18-grant-files.md) | Construction | All | UC-SC01-19, UC-SC19-14 |
| [S-SC19-L07 Installations](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l07-installations.md) | Trades and home services | All | UC-SC19-13, UC-SC19-14 |
| [S-SC19-L08 Grant files](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l08-grant-files.md) | Trades and home services | All | UC-SC19-13, UC-SC19-14 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Construction](../../../08-sectors/sc01-construction/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Trades and home services](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U22 | desktop | ![Workspace, U22, light](mockups/workspace-desktop-light.png) | ![Workspace, U22, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U22 | phone | ![Workspace, U22, light](mockups/workspace-phone-light.png) | ![Workspace, U22, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
