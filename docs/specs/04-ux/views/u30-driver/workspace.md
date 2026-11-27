🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🚚 [Driver: app shell and home](README.md) › 🧰 U30 Driver: workspace

# 🧰 U30 Driver: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U30 Driver](../../../01-users/personas/u30-driver.md) works with, embedded on their [home screen](README.md)
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
| [S-F1-L06 Roles](../../../02-functional/f01-administration/screens/00-lists/s-f01-l06-roles.md) | Administration | Mine: copied from | UC-F9-33 |
| [S-F2-L20 Offline form settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l20-offline-form-settings.md) | No-code configuration | Mine: roles | UC-F2-22 |
| [S-F2-L25 Request types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l25-request-types.md) | No-code configuration | Open: Draft, Published | UC-F9-33 |
| [S-F2-L28 Offline change queues](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l28-offline-change-queues.md) | No-code configuration | All | UC-F2-22 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-SC13-22 |
| [S-F9-L01 Employee records](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l01-employee-records.md) | HR and projects | Mine: manager | UC-F9-33 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F9-L09 Time-off requests](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l09-time-off-requests.md) | HR and projects | Open: ToApprove, Approved, Refused | UC-F9-35 |
| [S-F9-L12 Certifications](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l12-certifications.md) | HR and projects | Mine: employee | UC-F9-33 |
| [S-F9-L16 Shifts](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l16-shifts.md) | HR and projects | Mine: role | UC-F9-30, UC-F9-37 |
| [S-F9-L26 Rounds](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l26-rounds.md) | HR and projects | Mine: person | UC-F9-30, UC-F9-33, UC-F9-35 |
| [S-F9-L28 Assignment proposals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l28-assignment-proposals.md) | HR and projects | Mine: chosen | UC-F9-33, UC-F9-35 |
| [S-F9-L29 Degrees](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l29-degrees.md) | HR and projects | Mine: employee | UC-F9-33 |
| [S-F9-L30 Qualification types](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l30-qualification-types.md) | HR and projects | Open: Active | UC-F9-33 |
| [S-F9-L32 Live positions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l32-live-positions.md) | HR and projects | Mine: employee | UC-F9-37 |
| [S-F16-L12 Work requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l12-work-requests.md) | Customer support agents | Mine: confirmed by | UC-F9-33, UC-F9-35 |
| [S-T13-L02 Routes](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l02-routes.md) | Maps and geodata | All | UC-F9-30, UC-F9-33 |
| [S-SC07-L02 Trips](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l02-trips.md) | Transport and logistics | Mine: driver | UC-SC07-20 |
| [S-SC07-L05 Consignment notes](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l05-consignment-notes.md) | Transport and logistics | All | UC-SC07-05 |
| [S-SC07-L06 Stops](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l06-stops.md) | Transport and logistics | Open: New, Open | UC-SC07-20, UC-SC07-06, UC-SC07-07 |
| [S-SC07-L07 Transport incidents](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l07-transport-incidents.md) | Transport and logistics | All | UC-SC07-07 |
| [S-SC07-L09 Dangerous goods declarations](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l09-dangerous-goods-declarations.md) | Transport and logistics | All | UC-SC07-09 |
| [S-SC07-L13 Transport invoice lines](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l13-transport-invoice-lines.md) | Transport and logistics | All | UC-SC07-21 |
| [S-SC07-L16 Proof of deliveries](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l16-proof-of-deliveries.md) | Transport and logistics | All | UC-SC07-07 |
| [S-SC07-L18 Passenger trips](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l18-passenger-trips.md) | Transport and logistics | All | UC-SC07-21 |
| [S-SC07-L20 Parcels](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l20-parcels.md) | Transport and logistics | All | UC-SC07-23 |
| [S-SC13-L07 Machines](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l07-machines.md) | Agriculture and food | All | UC-SC13-22 |
| [S-SC13-L18 Field jobs](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l18-field-jobs.md) | Agriculture and food | All | UC-SC13-22 |

## Navigation

Each view also sits in its capability's menu (D495):
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Agriculture and food](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customer support agents](../../../02-functional/f16-customer-support-agents/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Maps and geodata](../../../03-technical/t13-maps-and-geodata/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Transport and logistics](../../../08-sectors/sc07-transport/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U30 | desktop | ![Workspace, U30, light](mockups/workspace-desktop-light.png) | ![Workspace, U30, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U30 | phone | ![Workspace, U30, light](mockups/workspace-phone-light.png) | ![Workspace, U30, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
