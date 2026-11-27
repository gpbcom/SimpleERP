🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
📋 [Medical secretary: app shell and home](README.md) › 🧰 U33 Medical secretary: workspace

# 🧰 U33 Medical secretary: workspace

**Status:** ✅ specified

## Purpose

The views [U33 Medical secretary](../../../01-users/personas/u33-medical-secretary.md) works with, embedded on their
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
| [S-F2-L05 Record types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l05-record-types.md) | No-code configuration | Open: Draft, Live | UC-F2-18 |
| [S-F2-L17 Bookable resource settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l17-bookable-resource-settings.md) | No-code configuration | Open: Draft, Published | UC-F2-18, UC-F2-19, UC-SC09-12 |
| [S-F2-L18 Resource bookings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l18-resource-bookings.md) | No-code configuration | Open: Requested, Confirmed, NoShow | UC-F2-19, UC-SC09-01 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L01 Meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l01-meetings.md) | Meetings | Open: Planned, Live, WaitingForReview | UC-F4-25 |
| [S-F4-L08 Key moments](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l08-key-moments.md) | Meetings | All | D519, VC-10 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | UC-F4-25 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F6-L14 Funder agreements](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l14-funder-agreements.md) | Customers and sales | Open: Active | UC-SC09-07 |
| [S-F7-L06 Items](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l06-items.md) | Purchasing and stock | All | UC-SC09-23 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-SC09-L01 Appointments](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l01-appointments.md) | Health practices | Open: Booked, Confirmed, NoShow | UC-SC09-01, UC-SC09-02, UC-SC09-20, UC-SC09-12 |
| [S-SC09-L02 Patients](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l02-patients.md) | Health practices | All | UC-SC09-03 |
| [S-SC09-L03 Clinical record entries](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l03-clinical-record-entries.md) | Health practices | Mine: author | UC-SC09-20, UC-SC09-10 |
| [S-SC09-L05 Care sheets](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l05-care-sheets.md) | Health practices | Open: Signed, Sent | UC-SC09-06, UC-SC09-07 |
| [S-SC09-L06 Insurer returns](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l06-insurer-returns.md) | Health practices | All | UC-SC09-07 |
| [S-SC09-L07 Patient invoices](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l07-patient-invoices.md) | Health practices | All | UC-SC09-08 |
| [S-SC09-L08 Health exchanges](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l08-health-exchanges.md) | Health practices | All | UC-SC09-10 |
| [S-SC09-L09 Consulting rooms](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l09-consulting-rooms.md) | Health practices | All | UC-SC09-12 |
| [S-SC09-L11 Sterilisation cycles](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l11-sterilisation-cycles.md) | Health practices | All | UC-SC09-14 |
| [S-SC09-L16 Animals](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l16-animals.md) | Health practices | All | UC-SC09-23 |
| [S-SC09-L18 Centre activities](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l18-centre-activities.md) | Health practices | All | UC-SC09-25 |
| [S-SC09-L19 Funding indicators](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l19-aci-indicators.md) | Health practices | All | UC-SC09-26 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Health practices](../../../08-sectors/sc09-health-practices/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U33 | desktop | ![Workspace, U33, light](mockups/workspace-desktop-light.png) | ![Workspace, U33, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U33 | phone | ![Workspace, U33, light](mockups/workspace-phone-light.png) | ![Workspace, U33, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
