🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🧑‍💼 [Manager: app shell and home](README.md) › 🧰 U02 Manager: workspace

# 🧰 U02 Manager: workspace

**Status:** ✅ specified

## Purpose

The views [U02 Manager](../../../01-users/personas/u02-manager.md) works with, embedded on their
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
| [S-F1-L02 Company sites](../../../02-functional/f01-administration/screens/00-lists/s-f01-l02-company-sites.md) | Administration | Needs attention | UC-F1-02, UC-F1-15 |
| [S-F1-L03 Users](../../../02-functional/f01-administration/screens/00-lists/s-f01-l03-users.md) | Administration | All | UC-F1-15, UC-F1-16, UC-F1-17, UC-F1-18 |
| [S-F1-L06 Roles](../../../02-functional/f01-administration/screens/00-lists/s-f01-l06-roles.md) | Administration | All | UC-F1-15, UC-F1-18, UC-F9-36 |
| [S-F1-L13 Approval delegations](../../../02-functional/f01-administration/screens/00-lists/s-f01-l13-approval-delegations.md) | Administration | Open: Planned, Active | UC-F1-16, UC-F1-17 |
| [S-F1-L16 Access review campaigns](../../../02-functional/f01-administration/screens/00-lists/s-f01-l16-access-review-campaigns.md) | Administration | Needs attention | UC-F1-18 |
| [S-F2-L01 Custom fields](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l01-custom-fields.md) | No-code configuration | Needs attention | UC-F2-01 |
| [S-F2-L04 List views](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l04-list-views.md) | No-code configuration | Needs attention | UC-F2-17, UC-F9-36 |
| [S-F2-L12 Spreadsheets](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l12-spreadsheets.md) | No-code configuration | All | UC-F2-12 |
| [S-F2-L15 Sandboxes](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l15-sandboxes.md) | No-code configuration | All | UC-F2-15, UC-F2-16 |
| [S-F2-L16 Visual views](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l16-visual-views.md) | No-code configuration | Needs attention | UC-F2-17 |
| [S-F2-L18 Resource bookings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l18-resource-bookings.md) | No-code configuration | Open: Requested, Confirmed, NoShow | UC-F4-21 |
| [S-F2-L24 Approval chains](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l24-approval-chains.md) | No-code configuration | Needs attention | UC-F2-29 |
| [S-F2-L25 Request types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l25-request-types.md) | No-code configuration | Needs attention | UC-F9-34, UC-F16-16 |
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Open: Private, Shared | UC-F3-01, UC-F3-08, UC-F15-01 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-01, UC-F3-02, UC-F3-04 |
| [S-F3-L04 Assistant change batches](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l04-assistant-change-batches.md) | Assistant | Open: Proposed | UC-F3-03 |
| [S-F3-L07 Personal connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l07-personal-connections.md) | Assistant | Needs attention | UC-F3-06 |
| [S-F3-L12 Conversation folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l12-conversation-folders.md) | Assistant | All | UC-F3-08 |
| [S-F3-L14 Answer feedbacks](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l14-answer-feedbacks.md) | Assistant | All | UC-F3-01 |
| [S-F3-L15 Agents](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l15-agents.md) | Assistant | Open: Paused | UC-F3-10 |
| [S-F3-L16 AI fields](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l16-ai-fields.md) | Assistant | All | UC-F3-12 |
| [S-F3-L20 Memory items](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l20-memory-items.md) | Assistant | All | UC-F3-17 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | UC-F3-03, UC-F3-04, UC-F3-06 |
| [S-F3-L26 Briefings](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l26-briefings.md) | Assistant | Needs attention | UC-F3-23 |
| [S-F4-L01 Meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l01-meetings.md) | Meetings | Needs attention | UC-F4-01, UC-F4-02, UC-F4-05, UC-F4-07 and more |
| [S-F4-L02 Transcripts](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l02-transcripts.md) | Meetings | All | UC-F4-01, UC-F4-02 |
| [S-F4-L03 Summary templates](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l03-summary-templates.md) | Meetings | Needs attention | UC-F4-05 |
| [S-F4-L04 Action items](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l04-action-items.md) | Meetings | Needs attention | UC-F4-05, UC-F4-27 |
| [S-F4-L06 Scorecards](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l06-scorecards.md) | Meetings | All | UC-F4-12 |
| [S-F4-L07 Evaluation grids](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l07-evaluation-grids.md) | Meetings | All | UC-F4-13 |
| [S-F4-L08 Key moments](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l08-key-moments.md) | Meetings | All | D519, VC-10 |
| [S-F4-L09 Scheduled digests](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l09-scheduled-digests.md) | Meetings | All | UC-F4-15 |
| [S-F4-L10 Chat channels](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l10-chat-channels.md) | Meetings | All | UC-F4-17 |
| [S-F4-L13 Call topics](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l13-call-topics.md) | Meetings | All | UC-F4-20 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Needs attention | D519, VC-11 |
| [S-F4-L17 Meeting summaries](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l17-meeting-summaries.md) | Meetings | All | UC-F4-05, UC-F4-07 |
| [S-F4-L18 Recording notices](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l18-recording-notices.md) | Meetings | All | UC-F4-01 |
| [S-F4-L19 Follow-up emails](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l19-follow-up-emails.md) | Meetings | All | UC-F4-05 |
| [S-F4-L20 Human review requests](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l20-human-review-requests.md) | Meetings | All | UC-F4-12 |
| [S-F4-L21 Interview debriefs](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l21-interview-debriefs.md) | Meetings | All | UC-F4-13 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L24 Meeting prep briefs](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l24-meeting-prep-briefs.md) | Meetings | All | UC-F4-09 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | All | UC-F4-09 |
| [S-F5-L01 Posts](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l01-posts.md) | Social media and marketing | Needs attention | UC-F5-02, UC-F5-04 |
| [S-F6-L01 Customer records](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l01-customer-records.md) | Customers and sales | All | UC-F6-17 |
| [S-F6-L02 Opportunities](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l02-opportunities.md) | Customers and sales | All | UC-F6-02 |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Needs attention | D519, VC-14 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Needs attention | UC-F6-26 |
| [S-F6-L08 Sales price lists](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l08-sales-price-lists.md) | Customers and sales | All | UC-F6-12 |
| [S-F6-L11 Timeline entries](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l11-timeline-entries.md) | Customers and sales | All | UC-F6-17 |
| [S-F6-L18 Commission plan and targets](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l18-commission-plan-and-targets.md) | Customers and sales | Needs attention | UC-F6-25, UC-F6-26 |
| [S-F6-L19 Commission lines](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l19-commission-lines.md) | Customers and sales | Open: Approved | UC-F6-25 |
| [S-F6-L20 Leads](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l20-leads.md) | Customers and sales | All | UC-F6-13 |
| [S-F7-L02 Purchase requests](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l02-purchase-requests.md) | Purchasing and stock | Needs attention | UC-F7-01, UC-F7-20 |
| [S-F7-L03 Purchase orders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l03-purchase-orders.md) | Purchasing and stock | Needs attention | UC-F7-01 |
| [S-F7-L04 Transfers](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l04-transfers.md) | Purchasing and stock | Open: Sent, Received, Reserved | UC-F7-08 |
| [S-F7-L06 Items](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l06-items.md) | Purchasing and stock | All | UC-F7-21, UC-F7-11 |
| [S-F7-L07 Locations](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l07-locations.md) | Purchasing and stock | All | UC-F7-13, UC-F7-07 |
| [S-F7-L08 Routes](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l08-routes.md) | Purchasing and stock | All | UC-F7-13 |
| [S-F7-L09 Reordering rules](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l09-reordering-rules.md) | Purchasing and stock | All | UC-F7-13, UC-F7-21 |
| [S-F7-L10 Lot or serials](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l10-lot-or-serials.md) | Purchasing and stock | All | UC-F7-08 |
| [S-F7-L11 Stock counts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l11-stock-counts.md) | Purchasing and stock | All | UC-F7-07, UC-F7-11 |
| [S-F7-L17 Approved catalogues](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l17-approved-catalogues.md) | Purchasing and stock | Open: Active | UC-F7-20 |
| [S-F7-L21 Demand forecasts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l21-demand-forecasts.md) | Purchasing and stock | All | UC-F7-21 |
| [S-F8-L08 Accounting budgets](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l08-accounting-budgets.md) | Accounting | All | UC-F8-09 |
| [S-F8-L09 Expense claims](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l09-expense-claims.md) | Accounting | Needs attention | UC-F8-12 |
| [S-F8-L16 Budget plans](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l16-budget-plans.md) | Accounting | All | UC-F8-19 |
| [S-F8-L30 Analytic plans](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l30-analytic-plans.md) | Accounting | All | UC-F8-09 |
| [S-F8-L43 Trips](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l43-trips.md) | Accounting | Needs attention | UC-F8-39 |
| [S-F9-L01 Employee records](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l01-employee-records.md) | HR and projects | All | UC-F9-02, UC-F9-21, UC-F9-26, UC-F9-38 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | UC-F3-08 |
| [S-F9-L04 Activity plans](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l04-activity-plans.md) | HR and projects | All | UC-F9-02 |
| [S-F9-L05 HR duties](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l05-hr-duties.md) | HR and projects | Needs attention | UC-F9-21 |
| [S-F9-L07 Applicants](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l07-applicants.md) | HR and projects | All | UC-F9-06 |
| [S-F9-L08 Time-off allocations](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l08-time-off-allocations.md) | HR and projects | All | UC-F9-09 |
| [S-F9-L09 Time-off requests](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l09-time-off-requests.md) | HR and projects | Open: ToApprove, Approved, Refused | UC-F9-09 |
| [S-F9-L10 Attendances](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l10-attendances.md) | HR and projects | All | UC-F9-10, UC-F9-36 |
| [S-F9-L11 Appraisals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l11-appraisals.md) | HR and projects | All | UC-F9-11 |
| [S-F9-L12 Certifications](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l12-certifications.md) | HR and projects | Needs attention | UC-F9-11, UC-F9-25, UC-F9-38 |
| [S-F9-L14 Approval requests](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l14-approval-requests.md) | HR and projects | All | UC-F9-13 |
| [S-F9-L16 Shifts](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l16-shifts.md) | HR and projects | Needs attention | UC-F9-15 |
| [S-F9-L17 Timesheet lines](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l17-timesheet-lines.md) | HR and projects | Needs attention | UC-F9-16 |
| [S-F9-L18 Project and tasks](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l18-project-and-tasks.md) | HR and projects | Open: New, Planned, Active | UC-F9-17, UC-F9-18, UC-F9-29, UC-F9-32 |
| [S-F9-L22 Training sessions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l22-training-sessions.md) | HR and projects | Open: Planned, Held | UC-F9-25 |
| [S-F9-L23 Work accidents](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l23-work-accidents.md) | HR and projects | Open: Active | UC-F9-26 |
| [S-F9-L25 Resource allocations](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l25-resource-allocations.md) | HR and projects | Open: Planned | UC-F9-29 |
| [S-F9-L26 Rounds](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l26-rounds.md) | HR and projects | Needs attention | UC-F9-34, UC-F9-36 |
| [S-F9-L27 Subcontractor assignments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l27-subcontractor-assignments.md) | HR and projects | Open: Proposed, Active | UC-F9-32 |
| [S-F9-L28 Assignment proposals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l28-assignment-proposals.md) | HR and projects | Needs attention | UC-F9-34 |
| [S-F9-L29 Degrees](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l29-degrees.md) | HR and projects | Needs attention | UC-F9-38 |
| [S-F9-L30 Qualification types](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l30-qualification-types.md) | HR and projects | Open: Active | UC-F9-38 |
| [S-F9-L31 Attribute readings](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l31-attribute-readings.md) | HR and projects | Needs attention | UC-F9-38 |
| [S-F9-L32 Live positions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l32-live-positions.md) | HR and projects | All | UC-F9-36 |
| [S-F9-L33 Automatic scheduling settings](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l33-automatic-scheduling-settings.md) | HR and projects | All | UC-F9-34 |
| [S-F9-L34 Attendance kiosks](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l34-attendance-kiosks.md) | HR and projects | All | UC-F9-10 |
| [S-F9-L35 Employee badges](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l35-employee-badges.md) | HR and projects | All | UC-F9-10 |
| [S-F9-L37 Field worksheets](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l37-field-worksheets.md) | HR and projects | All | UC-F9-18 |
| [S-F9-L39 Lunch orders](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l39-lunch-orders.md) | HR and projects | All | UC-F9-13 |
| [S-F9-L48 Work location days](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l48-work-location-days.md) | HR and projects | Needs attention | UC-F9-43 |
| [S-F9-L50 Succession plans](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l50-succession-plans.md) | HR and projects | Needs attention | UC-F9-45 |
| [S-F10-L01 Point of sales](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l01-point-of-sales.md) | Point of sale (plugin) | All | UC-F10-01, UC-F10-16, UC-F10-15 |
| [S-F10-L02 Till sessions](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l02-till-sessions.md) | Point of sale (plugin) | Needs attention | UC-F10-01, UC-F10-20, UC-F10-28 |
| [S-F10-L03 Point of sale orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l03-point-of-sale-orders.md) | Point of sale (plugin) | Needs attention | UC-F10-04, UC-F10-09, UC-F10-20, UC-F10-28 |
| [S-F10-L04 Till payments](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l04-till-payments.md) | Point of sale (plugin) | All | UC-F10-04 |
| [S-F10-L05 Receipts](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l05-receipts.md) | Point of sale (plugin) | All | UC-F10-04 |
| [S-F10-L06 Closures](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l06-closures.md) | Point of sale (plugin) | All | UC-F10-01, UC-F10-18 |
| [S-F10-L07 Till archives](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l07-till-archives.md) | Point of sale (plugin) | All | UC-F10-18 |
| [S-F10-L08 Price promotions](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l08-price-promotions.md) | Point of sale (plugin) | All | UC-F10-06 |
| [S-F10-L09 Combos](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l09-combos.md) | Point of sale (plugin) | All | UC-F10-06 |
| [S-F10-L11 Floor and tables](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l11-floor-and-tables.md) | Point of sale (plugin) | All | UC-F10-09, UC-F10-15 |
| [S-F10-L12 Table bookings](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l12-table-bookings.md) | Point of sale (plugin) | All | UC-F10-09 |
| [S-F10-L14 Point of sale devices](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l14-point-of-sale-devices.md) | Point of sale (plugin) | All | UC-F10-15 |
| [S-F10-L15 Till event logs](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l15-till-event-logs.md) | Point of sale (plugin) | All | UC-F10-01, UC-F10-18 |
| [S-F12-L01 Bill of materials](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l01-bill-of-materials.md) | Manufacturing (plugin) | Needs attention | UC-F12-10 |
| [S-F12-L04 Manufacturing orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l04-manufacturing-orders.md) | Manufacturing (plugin) | Needs attention | UC-F12-04 |
| [S-F12-L05 Work orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l05-work-orders.md) | Manufacturing (plugin) | Needs attention | UC-F12-04, UC-F12-23 |
| [S-F12-L09 Equipments](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l09-equipments.md) | Manufacturing (plugin) | All | UC-F12-17 |
| [S-F12-L11 Engineering changes](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l11-engineering-changes.md) | Manufacturing (plugin) | All | UC-F12-10 |
| [S-F12-L18 Schedule slots](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l18-schedule-slots.md) | Manufacturing (plugin) | Open: Planned, Published | UC-F12-23 |
| [S-F12-L26 Risk assessments](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l26-risk-assessments.md) | Manufacturing (plugin) | All | UC-F12-17 |
| [S-F12-L27 Safety registers](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l27-safety-registers.md) | Manufacturing (plugin) | All | UC-F12-17 |
| [S-F15-L01 Law packs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l01-law-packs.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L02 Legal warnings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l02-legal-warnings.md) | Legal assistant | All | UC-F15-01, UC-F15-02 |
| [S-F15-L03 Document checks](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l03-document-checks.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L04 Standard register entries](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l04-standard-register-entries.md) | Legal assistant | Needs attention | UC-F15-01 |
| [S-F15-L10 Lawyer hand-offs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l10-lawyer-hand-offs.md) | Legal assistant | Needs attention | UC-F15-01 |
| [S-F15-L11 Warning triggers](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l11-warning-triggers.md) | Legal assistant | All | UC-F15-02 |
| [S-F16-L01 Customer requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l01-customer-requests.md) | Customer support agents | Needs attention | UC-F16-04, UC-F16-07, UC-F16-08, UC-F16-09 and more |
| [S-F16-L02 Intents](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l02-intents.md) | Customer support agents | All | UC-F16-02, UC-F16-03, UC-F16-14, UC-F16-05 |
| [S-F16-L03 Resolution reviews](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l03-resolution-reviews.md) | Customer support agents | All | UC-F16-04, UC-F16-05 |
| [S-F16-L05 Service-level policies](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l05-service-level-policies.md) | Customer support agents | Open: Active, Changed | UC-F16-05, UC-F16-07 |
| [S-F16-L06 Queues](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l06-queues.md) | Customer support agents | Needs attention | UC-F16-08 |
| [S-F16-L07 Macros](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l07-macros.md) | Customer support agents | Open: Active | UC-F16-08 |
| [S-F16-L08 Satisfaction ratings](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l08-satisfaction-ratings.md) | Customer support agents | Needs attention | UC-F16-04, UC-F16-05, UC-F16-09 |
| [S-F16-L09 Help-centre articles](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l09-help-centre-articles.md) | Customer support agents | Needs attention | UC-F16-10 |
| [S-F16-L10 Intent candidates](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l10-intent-candidates.md) | Customer support agents | All | UC-F16-14 |
| [S-F16-L11 Fraud signals](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l11-fraud-signals.md) | Customer support agents | All | UC-F16-15 |
| [S-F16-L12 Work requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l12-work-requests.md) | Customer support agents | Needs attention | UC-F9-34, UC-F9-36, UC-F16-16 |
| [S-F17-L11 Battle cards](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l11-battle-cards.md) | Competitive analysis | All | UC-F17-24 |
| [S-F17-L12 Win-loss records](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l12-win-loss-records.md) | Competitive analysis | All | UC-F17-14 |
| [S-F17-L20 Call topic signals](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l20-call-topic-signals.md) | Competitive analysis | All | UC-F17-24 |
| [S-F22-L02 Metered call records](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l02-metered-call-records.md) | Unified platform cost management | All | UC-F22-20, UC-F22-03 |
| [S-F22-L06 Cost budgets](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l06-cost-budgets.md) | Unified platform cost management | All | UC-F22-20, UC-F22-06 |
| [S-F22-L09 Allocation rules](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l09-allocation-rules.md) | Unified platform cost management | All | UC-F22-03 |
| [S-F22-L10 Run estimates](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l10-run-estimates.md) | Unified platform cost management | Open: Running | UC-F22-10 |
| [S-F23-L02 Scenarios](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l02-scenarios.md) | What-if simulation and impact | All | UC-F23-02, UC-F23-20 |
| [S-F23-L03 Scenario changes](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l03-scenario-changes.md) | What-if simulation and impact | All | UC-F23-03, UC-F23-25 |
| [S-F23-L04 Simulation runs](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l04-simulation-runs.md) | What-if simulation and impact | All | UC-F23-20 |
| [S-F23-L05 Impact results](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l05-impact-results.md) | What-if simulation and impact | All | UC-F23-20 |
| [S-F23-L07 Counter-measures](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l07-counter-measures.md) | What-if simulation and impact | All | UC-F23-16 |
| [S-F23-L14 Sector drivers](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l14-sector-drivers.md) | What-if simulation and impact | All | UC-F23-03, UC-F23-25 |
| [S-F23-L15 Budget contributions](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l15-budget-contributions.md) | What-if simulation and impact | Needs attention | UC-F23-31 |
| [S-F24-L03 Suite components](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l03-suite-components.md) | Integrations hub | All | UC-F24-07, UC-F24-08 |
| [S-T13-L01 Geocoded places](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l01-geocoded-places.md) | Maps and geodata | All | UC-F9-36, UC-F16-16 |
| [S-T13-L02 Routes](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l02-routes.md) | Maps and geodata | All | UC-F9-36 |
| [S-T13-L03 Map layers](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l03-map-layers.md) | Maps and geodata | Needs attention | UC-F9-36 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Competitive analysis](../../../02-functional/f17-competitive-analysis/screens/00-lists/README.md),
[Customer support agents](../../../02-functional/f16-customer-support-agents/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Integrations hub](../../../02-functional/f24-integrations-hub/screens/00-lists/README.md),
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Maps and geodata](../../../03-technical/t13-maps-and-geodata/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md),
[Unified platform cost management](../../../02-functional/f22-unified-cost-management/screens/00-lists/README.md),
[What-if simulation and impact](../../../02-functional/f23-what-if-simulation/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U02 | desktop | ![Workspace, U02, light](mockups/workspace-desktop-light.png) | ![Workspace, U02, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U02 | phone | ![Workspace, U02, light](mockups/workspace-phone-light.png) | ![Workspace, U02, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
