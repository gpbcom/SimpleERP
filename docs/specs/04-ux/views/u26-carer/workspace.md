🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🤝 [Carer: app shell and home](README.md) › 🧰 U26 Carer: workspace

# 🧰 U26 Carer: workspace

**Status:** ✅ specified

## Purpose

The views [U26 Carer](../../../01-users/personas/u26-carer.md) works with, embedded on their [home screen](README.md)
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
| [S-F1-L06 Roles](../../../02-functional/f01-administration/screens/00-lists/s-f01-l06-roles.md) | Administration | Mine: copied from | UC-F9-33 |
| [S-F2-L20 Offline form settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l20-offline-form-settings.md) | No-code configuration | Mine: roles | UC-F2-22 |
| [S-F2-L25 Request types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l25-request-types.md) | No-code configuration | Open: Draft, Published | UC-F9-33 |
| [S-F2-L28 Offline change queues](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l28-offline-change-queues.md) | No-code configuration | All | UC-F2-22 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F9-L01 Employee records](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l01-employee-records.md) | HR and projects | Mine: manager | UC-F9-33 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F9-L09 Time-off requests](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l09-time-off-requests.md) | HR and projects | Open: ToApprove, Approved, Refused | UC-F9-35 |
| [S-F9-L12 Certifications](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l12-certifications.md) | HR and projects | Mine: employee | UC-F9-33 |
| [S-F9-L16 Shifts](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l16-shifts.md) | HR and projects | Mine: role | UC-F9-30, UC-F9-37 |
| [S-F9-L26 Rounds](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l26-rounds.md) | HR and projects | Mine: person | UC-F9-30, UC-F9-33, UC-F9-35, UC-SC04-06 and more |
| [S-F9-L28 Assignment proposals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l28-assignment-proposals.md) | HR and projects | Mine: chosen | UC-F9-33, UC-F9-35 |
| [S-F9-L29 Degrees](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l29-degrees.md) | HR and projects | Mine: employee | UC-F9-33 |
| [S-F9-L30 Qualification types](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l30-qualification-types.md) | HR and projects | Open: Active | UC-F9-33 |
| [S-F9-L32 Live positions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l32-live-positions.md) | HR and projects | Mine: employee | UC-F9-37 |
| [S-F16-L12 Work requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l12-work-requests.md) | Customer support agents | Mine: confirmed by | UC-F9-33, UC-F9-35 |
| [S-T13-L02 Routes](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l02-routes.md) | Maps and geodata | All | UC-F9-30, UC-F9-33 |
| [S-SC04-L04 Visits](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l04-visits.md) | Home care | Mine: carer | UC-SC04-06, UC-SC04-04, UC-SC04-15 |
| [S-SC04-L06 Care log entries](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l06-care-log-entries.md) | Home care | All | UC-SC04-05 |
| [S-SC04-L07 Care incidents](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l07-care-incidents.md) | Home care | All | UC-SC04-05 |
| [S-SC04-L14 Residents](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l14-residents.md) | Home care | All | UC-SC04-16 |
| [S-SC04-L17 Childcare contracts](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l17-childcare-contracts.md) | Home care | All | UC-SC04-19 |
| [S-SC04-L18 Care acts](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l18-care-acts.md) | Home care | All | UC-SC04-20 |

## Navigation

Each view also sits in its capability's menu (D495):
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customer support agents](../../../02-functional/f16-customer-support-agents/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Home care](../../../08-sectors/sc04-home-care/screens/00-lists/README.md),
[Maps and geodata](../../../03-technical/t13-maps-and-geodata/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U26 | desktop | ![Workspace, U26, light](mockups/workspace-desktop-light.png) | ![Workspace, U26, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U26 | phone | ![Workspace, U26, light](mockups/workspace-phone-light.png) | ![Workspace, U26, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
