🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🗺️ [Dispatcher: app shell and home](README.md) › 🧰 U29 Dispatcher: workspace

# 🧰 U29 Dispatcher: workspace

**Status:** ✅ specified

## Purpose

The views [U29 Dispatcher](../../../01-users/personas/u29-dispatcher.md) works with, embedded on their
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
| [S-F9-L01 Employee records](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l01-employee-records.md) | HR and projects | All | UC-F9-33 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-F9-L09 Time-off requests](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l09-time-off-requests.md) | HR and projects | Open: ToApprove, Approved, Refused | UC-F9-35 |
| [S-F9-L10 Attendances](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l10-attendances.md) | HR and projects | All | UC-F9-36 |
| [S-F9-L12 Certifications](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l12-certifications.md) | HR and projects | Needs attention | UC-F9-33 |
| [S-F9-L16 Shifts](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l16-shifts.md) | HR and projects | Needs attention | UC-F9-30 |
| [S-F9-L17 Timesheet lines](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l17-timesheet-lines.md) | HR and projects | Mine: employee | UC-SC19-10 |
| [S-F9-L26 Rounds](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l26-rounds.md) | HR and projects | Needs attention | UC-F9-30, UC-F9-33, UC-F9-34, UC-F9-35 and more |
| [S-F9-L28 Assignment proposals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l28-assignment-proposals.md) | HR and projects | Needs attention | UC-F9-33, UC-F9-34, UC-F9-35 |
| [S-F9-L29 Degrees](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l29-degrees.md) | HR and projects | Needs attention | UC-F9-33 |
| [S-F9-L30 Qualification types](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l30-qualification-types.md) | HR and projects | Open: Active | UC-F9-33 |
| [S-F9-L32 Live positions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l32-live-positions.md) | HR and projects | All | UC-F9-36 |
| [S-F9-L33 Automatic scheduling settings](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l33-automatic-scheduling-settings.md) | HR and projects | All | UC-F9-34 |
| [S-F9-L37 Field worksheets](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l37-field-worksheets.md) | HR and projects | All | UC-SC19-05 |
| [S-F13-L03 Pay inputs](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l03-pay-inputs.md) | Payroll (plugin) | Mine: employee | UC-SC19-17 |
| [S-F16-L01 Customer requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l01-customer-requests.md) | Customer support agents | Needs attention | UC-F16-16 |
| [S-F16-L12 Work requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l12-work-requests.md) | Customer support agents | Needs attention | UC-F9-33, UC-F9-34, UC-F9-35, UC-F9-36 and more |
| [S-T13-L01 Geocoded places](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l01-geocoded-places.md) | Maps and geodata | All | UC-F9-36, UC-F16-16 |
| [S-T13-L02 Routes](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l02-routes.md) | Maps and geodata | All | UC-F9-30, UC-F9-33, UC-F9-36 |
| [S-T13-L03 Map layers](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l03-map-layers.md) | Maps and geodata | Needs attention | UC-F9-36 |
| [S-SC07-L01 Transport orders](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l01-transport-orders.md) | Transport and logistics | All | UC-SC07-01 |
| [S-SC07-L02 Trips](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l02-trips.md) | Transport and logistics | All | UC-SC07-02, UC-SC07-20, UC-SC07-19, UC-SC07-18 |
| [S-SC07-L03 Fleet vehicles](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l03-fleet-vehicles.md) | Transport and logistics | Needs attention | UC-SC07-03, UC-SC07-11 |
| [S-SC07-L04 Driver documents](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l04-driver-documents.md) | Transport and logistics | All | UC-SC07-04 |
| [S-SC07-L05 Consignment notes](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l05-consignment-notes.md) | Transport and logistics | All | UC-SC07-05, UC-SC07-16 |
| [S-SC07-L06 Stops](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l06-stops.md) | Transport and logistics | Needs attention | UC-SC07-20, UC-SC07-07, UC-SC07-16 |
| [S-SC07-L07 Transport incidents](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l07-transport-incidents.md) | Transport and logistics | All | UC-SC07-07 |
| [S-SC07-L08 Tachograph files](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l08-tachograph-files.md) | Transport and logistics | All | UC-SC07-08 |
| [S-SC07-L09 Dangerous goods declarations](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l09-dangerous-goods-declarations.md) | Transport and logistics | All | UC-SC07-09 |
| [S-SC07-L10 Fuel and toll lines](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l10-fuel-and-toll-lines.md) | Transport and logistics | All | UC-SC07-10 |
| [S-SC07-L11 Vehicle repairs](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l11-vehicle-repairs.md) | Transport and logistics | All | UC-SC07-11 |
| [S-SC07-L12 Charters](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l12-charters.md) | Transport and logistics | Needs attention | UC-SC07-12 |
| [S-SC07-L13 Transport invoice lines](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l13-transport-invoice-lines.md) | Transport and logistics | All | UC-SC07-13, UC-SC07-17, UC-SC07-18 |
| [S-SC07-L14 Client stocks](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l14-client-stocks.md) | Transport and logistics | All | UC-SC07-14 |
| [S-SC07-L15 Cabotage operations](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l15-cabotage-operations.md) | Transport and logistics | All | UC-SC07-19 |
| [S-SC07-L16 Proof of deliveries](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l16-proof-of-deliveries.md) | Transport and logistics | All | UC-SC07-07 |
| [S-SC07-L17 Transport CO2 statements](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l17-transport-co2-statements.md) | Transport and logistics | All | UC-SC07-17 |
| [S-SC07-L18 Passenger trips](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l18-passenger-trips.md) | Transport and logistics | All | UC-SC07-21 |
| [S-SC07-L19 Removals](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l19-removals.md) | Transport and logistics | All | UC-SC07-22 |
| [S-SC07-L20 Parcels](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l20-parcels.md) | Transport and logistics | All | UC-SC07-23 |
| [S-SC07-L21 Shipment files](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l21-shipment-files.md) | Transport and logistics | All | UC-SC07-24 |
| [S-SC19-L02 Planned visits](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l02-planned-visits.md) | Trades and home services | All | UC-SC19-02 |
| [S-SC19-L04 Interventions](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l04-interventions.md) | Trades and home services | All | UC-SC19-05, UC-SC19-17 |
| [S-SC19-L11 On-call rotas](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l11-on-call-rotas.md) | Trades and home services | All | UC-SC19-17 |

## Navigation

Each view also sits in its capability's menu (D495):
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customer support agents](../../../02-functional/f16-customer-support-agents/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Maps and geodata](../../../03-technical/t13-maps-and-geodata/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md),
[Trades and home services](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/README.md),
[Transport and logistics](../../../08-sectors/sc07-transport/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U29 | desktop | ![Workspace, U29, light](mockups/workspace-desktop-light.png) | ![Workspace, U29, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U29 | phone | ![Workspace, U29, light](mockups/workspace-phone-light.png) | ![Workspace, U29, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
