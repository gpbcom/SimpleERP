🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🗂️ [Care coordinator: app shell and home](README.md) › 🧰 U25 Care coordinator: workspace

# 🧰 U25 Care coordinator: workspace

**Status:** ✅ specified

## Purpose

The views [U25 Care coordinator](../../../01-users/personas/u25-care-coordinator.md) works with, embedded on their
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
| [S-F1-L06 Roles](../../../02-functional/f01-administration/screens/00-lists/s-f01-l06-roles.md) | Administration | All | UC-F9-33, UC-F9-36 |
| [S-F2-L04 List views](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l04-list-views.md) | No-code configuration | Needs attention | UC-F9-36 |
| [S-F2-L25 Request types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l25-request-types.md) | No-code configuration | Needs attention | UC-F9-33, UC-F9-34, UC-F16-16 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Needs attention | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | All | flow charts (VR-3) |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Needs attention | D519, VC-14 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Needs attention | UC-F6-20 |
| [S-F6-L14 Funder agreements](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l14-funder-agreements.md) | Customers and sales | Needs attention | UC-F6-20, UC-SC04-01, UC-SC04-08 |
| [S-F8-L18 Grants](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l18-grants.md) | Accounting | Open: Granted, Received | UC-SC04-14 |
| [S-F9-L01 Employee records](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l01-employee-records.md) | HR and projects | All | UC-F9-33 |
| [S-F9-L02 Contracts](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l02-contracts.md) | HR and projects | Open: Draft, Running | UC-SC04-18 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-F9-L09 Time-off requests](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l09-time-off-requests.md) | HR and projects | Open: ToApprove, Approved, Refused | UC-F9-35 |
| [S-F9-L10 Attendances](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l10-attendances.md) | HR and projects | All | UC-F9-36 |
| [S-F9-L12 Certifications](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l12-certifications.md) | HR and projects | Needs attention | UC-F9-33 |
| [S-F9-L16 Shifts](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l16-shifts.md) | HR and projects | Needs attention | UC-F9-30 |
| [S-F9-L26 Rounds](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l26-rounds.md) | HR and projects | Needs attention | UC-F9-30, UC-F9-33, UC-F9-34, UC-F9-35 and more |
| [S-F9-L28 Assignment proposals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l28-assignment-proposals.md) | HR and projects | Needs attention | UC-F9-33, UC-F9-34, UC-F9-35 |
| [S-F9-L29 Degrees](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l29-degrees.md) | HR and projects | Needs attention | UC-F9-33 |
| [S-F9-L30 Qualification types](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l30-qualification-types.md) | HR and projects | Open: Active | UC-F9-33 |
| [S-F9-L32 Live positions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l32-live-positions.md) | HR and projects | All | UC-F9-36 |
| [S-F9-L33 Automatic scheduling settings](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l33-automatic-scheduling-settings.md) | HR and projects | All | UC-F9-34 |
| [S-F13-L02 Employee pay profiles](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l02-employee-pay-profiles.md) | Payroll (plugin) | Mine: employee | UC-SC04-18 |
| [S-F16-L01 Customer requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l01-customer-requests.md) | Customer support agents | Needs attention | UC-F16-16 |
| [S-F16-L12 Work requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l12-work-requests.md) | Customer support agents | Needs attention | UC-F9-33, UC-F9-34, UC-F9-35, UC-F9-36 and more |
| [S-T13-L01 Geocoded places](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l01-geocoded-places.md) | Maps and geodata | All | UC-F9-36, UC-F16-16 |
| [S-T13-L02 Routes](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l02-routes.md) | Maps and geodata | All | UC-F9-30, UC-F9-33, UC-F9-36 |
| [S-T13-L03 Map layers](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l03-map-layers.md) | Maps and geodata | Needs attention | UC-F9-36 |
| [S-SC04-L01 Care recipients](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l01-care-recipients.md) | Home care | All | UC-SC04-01, UC-SC04-07 |
| [S-SC04-L02 Care fundings](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l02-care-fundings.md) | Home care | All | UC-SC04-01 |
| [S-SC04-L03 Care plans](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l03-care-plans.md) | Home care | All | UC-SC04-02 |
| [S-SC04-L04 Visits](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l04-visits.md) | Home care | Open: Planned, Missed | UC-SC04-03, UC-SC04-06, UC-SC04-15 |
| [S-SC04-L06 Care log entries](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l06-care-log-entries.md) | Home care | All | UC-SC04-05, UC-SC04-07 |
| [S-SC04-L07 Care incidents](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l07-care-incidents.md) | Home care | All | UC-SC04-05 |
| [S-SC04-L08 Care invoices](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l08-care-invoices.md) | Home care | All | UC-SC04-08 |
| [S-SC04-L10 Complaints](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l10-complaints.md) | Home care | Needs attention | UC-SC04-12 |
| [S-SC04-L11 Carer qualifications](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l11-carer-qualifications.md) | Home care | All | UC-SC04-13 |
| [S-SC04-L12 Activity reports](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l12-activity-reports.md) | Home care | All | UC-SC04-14 |
| [S-SC04-L14 Residents](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l14-residents.md) | Home care | All | UC-SC04-16 |
| [S-SC04-L15 CESU vouchers](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l15-cesu-vouchers.md) | Home care | All | UC-SC04-17 |
| [S-SC04-L16 Mandates](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l16-mandates.md) | Home care | All | UC-SC04-18 |
| [S-SC04-L17 Childcare contracts](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l17-childcare-contracts.md) | Home care | All | UC-SC04-19 |
| [S-SC04-L18 Care acts](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l18-care-acts.md) | Home care | All | UC-SC04-20 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customer support agents](../../../02-functional/f16-customer-support-agents/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Home care](../../../08-sectors/sc04-home-care/screens/00-lists/README.md),
[Maps and geodata](../../../03-technical/t13-maps-and-geodata/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U25 | desktop | ![Workspace, U25, light](mockups/workspace-desktop-light.png) | ![Workspace, U25, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U25 | phone | ![Workspace, U25, light](mockups/workspace-phone-light.png) | ![Workspace, U25, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
