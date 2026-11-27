🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🦺 [Field worker: app shell and home](README.md) › 🧰 U14 Field worker: workspace

# 🧰 U14 Field worker: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U14 Field worker](../../../01-users/personas/u14-field-worker.md) works with, embedded on their
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
| [S-F1-L06 Roles](../../../02-functional/f01-administration/screens/00-lists/s-f01-l06-roles.md) | Administration | Mine: copied from | UC-F9-33 |
| [S-F2-L14 Signature requests](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l14-signature-requests.md) | No-code configuration | Open: Sent, Signed, Refused | UC-SC19-20 |
| [S-F2-L20 Offline form settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l20-offline-form-settings.md) | No-code configuration | Mine: roles | UC-F2-22 |
| [S-F2-L25 Request types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l25-request-types.md) | No-code configuration | Open: Draft, Published | UC-F9-33 |
| [S-F2-L28 Offline change queues](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l28-offline-change-queues.md) | No-code configuration | All | UC-F2-22 |
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Mine: owner | UC-F3-01, UC-F3-08, UC-F3-09, UC-F15-01 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-01, UC-F3-02, UC-F3-04 |
| [S-F3-L04 Assistant change batches](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l04-assistant-change-batches.md) | Assistant | Mine: user | UC-F3-03 |
| [S-F3-L07 Personal connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l07-personal-connections.md) | Assistant | Mine: user | UC-F3-06 |
| [S-F3-L12 Conversation folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l12-conversation-folders.md) | Assistant | Mine: owner | UC-F3-08 |
| [S-F3-L13 Queued questions](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l13-queued-questions.md) | Assistant | All | UC-F3-09 |
| [S-F3-L14 Answer feedbacks](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l14-answer-feedbacks.md) | Assistant | All | UC-F3-01 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | UC-F3-03, UC-F3-04, UC-F3-06 |
| [S-F4-L01 Meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l01-meetings.md) | Meetings | Open: Planned, Live, WaitingForReview | UC-F4-03, UC-F4-05, UC-F4-16 |
| [S-F4-L02 Transcripts](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l02-transcripts.md) | Meetings | All | UC-F4-03 |
| [S-F4-L03 Summary templates](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l03-summary-templates.md) | Meetings | All | UC-F4-05 |
| [S-F4-L04 Action items](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l04-action-items.md) | Meetings | Open: Open | UC-F4-05 |
| [S-F4-L08 Key moments](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l08-key-moments.md) | Meetings | All | D519, VC-10 |
| [S-F4-L11 Appointment types](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l11-appointment-types.md) | Meetings | All | UC-F4-18 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L17 Meeting summaries](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l17-meeting-summaries.md) | Meetings | All | UC-F4-05 |
| [S-F4-L19 Follow-up emails](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l19-follow-up-emails.md) | Meetings | All | UC-F4-05 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Open: Draft, ToApprove, Sent | UC-SC19-13, UC-SC19-20 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-SC14-22, UC-SC19-08 |
| [S-F7-L10 Lot or serials](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l10-lot-or-serials.md) | Purchasing and stock | All | UC-SC14-22 |
| [S-F7-L11 Stock counts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l11-stock-counts.md) | Purchasing and stock | All | UC-SC19-19 |
| [S-F9-L01 Employee records](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l01-employee-records.md) | HR and projects | Mine: manager | UC-F9-04, UC-F9-26, UC-F9-33 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | UC-F3-08 |
| [S-F9-L10 Attendances](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l10-attendances.md) | HR and projects | Mine: employee | UC-F9-10 |
| [S-F9-L12 Certifications](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l12-certifications.md) | HR and projects | Mine: employee | UC-F9-33 |
| [S-F9-L16 Shifts](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l16-shifts.md) | HR and projects | Mine: role | UC-F9-15 |
| [S-F9-L17 Timesheet lines](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l17-timesheet-lines.md) | HR and projects | Mine: employee | UC-F9-16 |
| [S-F9-L18 Project and tasks](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l18-project-and-tasks.md) | HR and projects | Open: New, Planned, Active | UC-F9-18 |
| [S-F9-L23 Work accidents](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l23-work-accidents.md) | HR and projects | Mine: employee | UC-F9-26 |
| [S-F9-L26 Rounds](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l26-rounds.md) | HR and projects | Mine: person | UC-F9-33 |
| [S-F9-L28 Assignment proposals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l28-assignment-proposals.md) | HR and projects | Mine: chosen | UC-F9-33 |
| [S-F9-L29 Degrees](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l29-degrees.md) | HR and projects | Mine: employee | UC-F9-33 |
| [S-F9-L30 Qualification types](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l30-qualification-types.md) | HR and projects | Open: Active | UC-F9-33 |
| [S-F9-L34 Attendance kiosks](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l34-attendance-kiosks.md) | HR and projects | All | UC-F9-10 |
| [S-F9-L35 Employee badges](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l35-employee-badges.md) | HR and projects | All | UC-F9-10 |
| [S-F9-L37 Field worksheets](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l37-field-worksheets.md) | HR and projects | All | UC-F9-18 |
| [S-F10-L02 Till sessions](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l02-till-sessions.md) | Point of sale (plugin) | Open: Open, Closing, Posted | UC-F10-14 |
| [S-F10-L03 Point of sale orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l03-point-of-sale-orders.md) | Point of sale (plugin) | Mine: customer | UC-F10-14 |
| [S-F10-L04 Till payments](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l04-till-payments.md) | Point of sale (plugin) | All | UC-F10-14 |
| [S-F13-L03 Pay inputs](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l03-pay-inputs.md) | Payroll (plugin) | Mine: employee | UC-SC19-17 |
| [S-F15-L01 Law packs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l01-law-packs.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L02 Legal warnings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l02-legal-warnings.md) | Legal assistant | Mine: shown to | UC-F15-01 |
| [S-F15-L03 Document checks](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l03-document-checks.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L04 Standard register entries](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l04-standard-register-entries.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L10 Lawyer hand-offs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l10-lawyer-hand-offs.md) | Legal assistant | All | UC-F15-01 |
| [S-F16-L12 Work requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l12-work-requests.md) | Customer support agents | Mine: confirmed by | UC-F9-33 |
| [S-T13-L02 Routes](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l02-routes.md) | Maps and geodata | All | UC-F9-33 |
| [S-SC01-L01 Construction sites](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l01-construction-sites.md) | Construction | Open: Planned, Running, Accepted | UC-SC01-15 |
| [S-SC01-L04 Site time and material entries](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l04-site-time-and-material-entries.md) | Construction | All | UC-SC01-04 |
| [S-SC01-L05 Site diary entries](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l05-site-diary-entries.md) | Construction | All | UC-SC01-05, UC-SC01-15 |
| [S-SC03-L17 Assignment contracts](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l17-assignment-contracts.md) | Services | All | UC-SC03-16 |
| [S-SC13-L03 Field operations](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l03-field-operations.md) | Agriculture and food | All | UC-SC13-02 |
| [S-SC13-L08 Seasonal contracts](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l08-seasonal-contracts.md) | Agriculture and food | All | UC-SC13-09 |
| [S-SC14-L17 Leased devices](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l17-leased-devices.md) | IT and software | All | UC-SC14-22 |
| [S-SC19-L02 Planned visits](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l02-planned-visits.md) | Trades and home services | All | UC-SC19-03 |
| [S-SC19-L03 Check-up certificates](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l03-check-up-certificates.md) | Trades and home services | All | UC-SC19-03 |
| [S-SC19-L04 Interventions](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l04-interventions.md) | Trades and home services | All | UC-SC19-06, UC-SC19-08, UC-SC19-17 |
| [S-SC19-L05 Site reports](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l05-site-reports.md) | Trades and home services | All | UC-SC19-06, UC-SC19-07, UC-SC19-08 |
| [S-SC19-L07 Installations](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l07-installations.md) | Trades and home services | All | UC-SC19-13, UC-SC19-16 |
| [S-SC19-L10 Regulated records](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l10-regulated-records.md) | Trades and home services | All | UC-SC19-16 |
| [S-SC19-L11 On-call rotas](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l11-on-call-rotas.md) | Trades and home services | All | UC-SC19-17 |
| [S-SC19-L13 Van stocks](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l13-van-stocks.md) | Trades and home services | All | UC-SC19-07, UC-SC19-19 |

## Navigation

Each view also sits in its capability's menu (D495):
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Agriculture and food](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Construction](../../../08-sectors/sc01-construction/screens/00-lists/README.md),
[Customer support agents](../../../02-functional/f16-customer-support-agents/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[IT and software](../../../08-sectors/sc14-it-and-software/screens/00-lists/README.md),
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md),
[Maps and geodata](../../../03-technical/t13-maps-and-geodata/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Services](../../../08-sectors/sc03-services/screens/00-lists/README.md),
[Trades and home services](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U14 | desktop | ![Workspace, U14, light](mockups/workspace-desktop-light.png) | ![Workspace, U14, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U14 | phone | ![Workspace, U14, light](mockups/workspace-phone-light.png) | ![Workspace, U14, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
