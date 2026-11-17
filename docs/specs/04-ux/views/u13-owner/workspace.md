🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
👑 [Owner: app shell and home](README.md) › 🧰 U13 Owner: workspace

# 🧰 U13 Owner: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U13 Owner](../../../01-users/personas/u13-owner.md) works with, embedded on their [home screen](README.md)
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
| [S-F1-L01 Companies](../../../02-functional/f01-administration/screens/00-lists/s-f01-l01-companies.md) | Administration | All | UC-F1-01, UC-F1-23 |
| [S-F1-L02 Company sites](../../../02-functional/f01-administration/screens/00-lists/s-f01-l02-company-sites.md) | Administration | Needs attention | UC-F1-01, UC-F1-02 |
| [S-F1-L03 Users](../../../02-functional/f01-administration/screens/00-lists/s-f01-l03-users.md) | Administration | All | UC-F1-16, UC-F1-18 |
| [S-F1-L04 Invitations](../../../02-functional/f01-administration/screens/00-lists/s-f01-l04-invitations.md) | Administration | Needs attention | UC-F21-23 |
| [S-F1-L06 Roles](../../../02-functional/f01-administration/screens/00-lists/s-f01-l06-roles.md) | Administration | All | UC-F1-18 |
| [S-F1-L13 Approval delegations](../../../02-functional/f01-administration/screens/00-lists/s-f01-l13-approval-delegations.md) | Administration | Open: Planned, Active | UC-F1-16 |
| [S-F1-L16 Access review campaigns](../../../02-functional/f01-administration/screens/00-lists/s-f01-l16-access-review-campaigns.md) | Administration | Needs attention | UC-F1-18 |
| [S-F1-L18 API tokens](../../../02-functional/f01-administration/screens/00-lists/s-f01-l18-api-tokens.md) | Administration | Needs attention | UC-F3-22 |
| [S-F1-L20 SIEM destinations](../../../02-functional/f01-administration/screens/00-lists/s-f01-l20-siem-destinations.md) | Administration | All | UC-F1-22 |
| [S-F1-L21 Company closings](../../../02-functional/f01-administration/screens/00-lists/s-f01-l21-company-closings.md) | Administration | Needs attention | UC-F1-23 |
| [S-F1-L22 Record of processing activities](../../../02-functional/f01-administration/screens/00-lists/s-f01-l22-record-of-processing-activities.md) | Administration | All | UC-F1-12 |
| [S-F1-L25 Sharing rules](../../../02-functional/f01-administration/screens/00-lists/s-f01-l25-sharing-rules.md) | Administration | Needs attention | UC-F1-26 |
| [S-F2-L01 Custom fields](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l01-custom-fields.md) | No-code configuration | Needs attention | UC-F2-01 |
| [S-F2-L12 Spreadsheets](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l12-spreadsheets.md) | No-code configuration | All | UC-F2-12 |
| [S-F2-L17 Bookable resource settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l17-bookable-resource-settings.md) | No-code configuration | Needs attention | UC-SC09-12 |
| [S-F2-L18 Resource bookings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l18-resource-bookings.md) | No-code configuration | Open: Requested, Confirmed, NoShow | UC-SC18-17 |
| [S-F2-L24 Approval chains](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l24-approval-chains.md) | No-code configuration | Needs attention | UC-F2-29 |
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Open: Private, Shared | UC-F3-01, UC-F3-08, UC-F15-01 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-01, UC-F3-02, UC-F3-04, UC-F3-16 and more |
| [S-F3-L03 Suggested questions](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l03-suggested-questions.md) | Assistant | Needs attention | UC-F3-02 |
| [S-F3-L04 Assistant change batches](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l04-assistant-change-batches.md) | Assistant | Open: Proposed | UC-F3-03 |
| [S-F3-L05 Company writing styles](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l05-company-writing-styles.md) | Assistant | All | UC-F3-04 |
| [S-F3-L07 Personal connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l07-personal-connections.md) | Assistant | Needs attention | UC-F3-06 |
| [S-F3-L09 Knowledge items](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l09-knowledge-items.md) | Assistant | Needs attention | UC-F3-07 |
| [S-F3-L10 Knowledge folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l10-knowledge-folders.md) | Assistant | All | UC-F3-07 |
| [S-F3-L11 Knowledge proposals](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l11-knowledge-proposals.md) | Assistant | Needs attention | UC-F3-07, UC-F3-19 |
| [S-F3-L12 Conversation folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l12-conversation-folders.md) | Assistant | All | UC-F3-08 |
| [S-F3-L14 Answer feedbacks](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l14-answer-feedbacks.md) | Assistant | All | UC-F3-01 |
| [S-F3-L15 Agents](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l15-agents.md) | Assistant | Open: Paused | UC-F3-11 |
| [S-F3-L17 Evaluation questions](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l17-evaluation-questions.md) | Assistant | Open: Active | UC-F3-14 |
| [S-F3-L18 Evaluation runs](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l18-evaluation-runs.md) | Assistant | Needs attention | UC-F3-14 |
| [S-F3-L21 Unanswered topics](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l21-unanswered-topics.md) | Assistant | Needs attention | UC-F3-19 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | UC-F3-03, UC-F3-04, UC-F3-06 |
| [S-F3-L25 Add-in connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l25-add-in-connections.md) | Assistant | Needs attention | UC-F3-22 |
| [S-F3-L26 Briefings](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l26-briefings.md) | Assistant | Needs attention | UC-F3-23 |
| [S-F4-L01 Meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l01-meetings.md) | Meetings | Needs attention | UC-F4-01, UC-F4-02, UC-F4-05, UC-F4-09 and more |
| [S-F4-L02 Transcripts](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l02-transcripts.md) | Meetings | All | UC-F4-01, UC-F4-02 |
| [S-F4-L03 Summary templates](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l03-summary-templates.md) | Meetings | Needs attention | UC-F4-05 |
| [S-F4-L04 Action items](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l04-action-items.md) | Meetings | Needs attention | UC-F4-05 |
| [S-F4-L06 Scorecards](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l06-scorecards.md) | Meetings | All | UC-F4-12 |
| [S-F4-L08 Key moments](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l08-key-moments.md) | Meetings | All | D519, VC-10 |
| [S-F4-L09 Scheduled digests](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l09-scheduled-digests.md) | Meetings | All | UC-F4-15 |
| [S-F4-L13 Call topics](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l13-call-topics.md) | Meetings | All | UC-F4-20 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Needs attention | D519, VC-11 |
| [S-F4-L17 Meeting summaries](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l17-meeting-summaries.md) | Meetings | All | UC-F4-05 |
| [S-F4-L18 Recording notices](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l18-recording-notices.md) | Meetings | All | UC-F4-01 |
| [S-F4-L19 Follow-up emails](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l19-follow-up-emails.md) | Meetings | All | UC-F4-05 |
| [S-F4-L20 Human review requests](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l20-human-review-requests.md) | Meetings | All | UC-F4-12 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L24 Meeting prep briefs](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l24-meeting-prep-briefs.md) | Meetings | All | UC-F4-09 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | All | UC-F4-09 |
| [S-F5-L01 Posts](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l01-posts.md) | Social media and marketing | Needs attention | UC-F5-02, UC-F5-04, UC-F5-06 |
| [S-F5-L04 Social messages](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l04-social-messages.md) | Social media and marketing | All | UC-F5-27 |
| [S-F5-L05 Email or SMS campaigns](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l05-email-or-sms-campaigns.md) | Social media and marketing | Needs attention | UC-F5-23 |
| [S-F5-L07 Registration events](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l07-registration-events.md) | Social media and marketing | Needs attention | UC-SC08-12, UC-SC16-01 |
| [S-F5-L08 Surveys](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l08-surveys.md) | Social media and marketing | Needs attention | UC-F9-28 |
| [S-F5-L09 Contact segments](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l09-contact-segments.md) | Social media and marketing | Open: Active | UC-F5-14 |
| [S-F5-L10 Consent and suppression records](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l10-consent-and-suppression-records.md) | Social media and marketing | Open: Given, Suppressed | UC-F5-14 |
| [S-F5-L12 Event tickets](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l12-event-tickets.md) | Social media and marketing | All | UC-SC08-12 |
| [S-F5-L15 Brand assets](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l15-brand-assets.md) | Social media and marketing | Needs attention | UC-F5-21 |
| [S-F5-L17 Campaign budgets](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l17-campaign-budgets.md) | Social media and marketing | Needs attention | UC-F5-23 |
| [S-F5-L18 Contacts](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l18-contacts.md) | Social media and marketing | All | UC-F5-14 |
| [S-F5-L24 Brand mentions](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l24-brand-mentions.md) | Social media and marketing | Needs attention | UC-F5-27 |
| [S-F6-L01 Customer records](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l01-customer-records.md) | Customers and sales | All | UC-SC18-01, UC-SC18-19, UC-SC19-01, UC-SC19-09 |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Needs attention | D519, VC-14 |
| [S-F6-L04 Orders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l04-orders.md) | Customers and sales | Needs attention | UC-F6-18 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Needs attention | UC-F6-26 |
| [S-F6-L06 Customer payments](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l06-customer-payments.md) | Customers and sales | All | UC-SC18-01, UC-SC18-17 |
| [S-F6-L07 Subscription contracts](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l07-subscription-contracts.md) | Customers and sales | All | UC-SC14-25, UC-SC18-01, UC-SC18-04, UC-SC19-01 and more |
| [S-F6-L08 Sales price lists](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l08-sales-price-lists.md) | Customers and sales | All | UC-F6-12 |
| [S-F6-L12 Credit limits](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l12-credit-limits.md) | Customers and sales | All | UC-F6-18 |
| [S-F6-L18 Commission plan and targets](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l18-commission-plan-and-targets.md) | Customers and sales | Needs attention | UC-F6-25, UC-F6-26, UC-SC11-17 |
| [S-F6-L19 Commission lines](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l19-commission-lines.md) | Customers and sales | Open: Approved | UC-F6-25 |
| [S-F6-L20 Leads](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l20-leads.md) | Customers and sales | All | UC-F14-31 |
| [S-F7-L01 Supplier records](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l01-supplier-records.md) | Purchasing and stock | All | UC-F7-19 |
| [S-F7-L05 Supplier invoices](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l05-supplier-invoices.md) | Purchasing and stock | All | UC-F7-24 |
| [S-F7-L06 Items](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l06-items.md) | Purchasing and stock | All | UC-F7-11 |
| [S-F7-L11 Stock counts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l11-stock-counts.md) | Purchasing and stock | All | UC-F7-11 |
| [S-F7-L16 Supplier scores](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l16-supplier-scores.md) | Purchasing and stock | All | UC-F7-19 |
| [S-F7-L20 Emission factors](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l20-emission-factors.md) | Purchasing and stock | All | UC-F7-24, UC-F8-28 |
| [S-F8-L01 Accounts](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l01-accounts.md) | Accounting | All | UC-F8-11 |
| [S-F8-L03 Journal entries](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l03-journal-entries.md) | Accounting | Needs attention | UC-F8-11 |
| [S-F8-L04 Bank lines](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l04-bank-lines.md) | Accounting | All | UC-F8-04 |
| [S-F8-L08 Accounting budgets](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l08-accounting-budgets.md) | Accounting | All | UC-F8-09 |
| [S-F8-L10 Fiscal periods](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l10-fiscal-periods.md) | Accounting | All | UC-F8-25 |
| [S-F8-L11 Consolidation groups](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l11-consolidation-groups.md) | Accounting | All | UC-F8-13 |
| [S-F8-L16 Budget plans](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l16-budget-plans.md) | Accounting | All | UC-F8-19 |
| [S-F8-L18 Grants](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l18-grants.md) | Accounting | Open: Granted, Received | UC-SC04-14, UC-SC08-20, UC-SC08-08, UC-SC08-09 and more |
| [S-F8-L19 Dedicated funds](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l19-dedicated-funds.md) | Accounting | Needs attention | UC-SC08-14 |
| [S-F8-L21 Corporate tax computations](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l21-corporate-tax-computations.md) | Accounting | Needs attention | UC-SC14-24 |
| [S-F8-L22 Annual accounts files](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l22-annual-accounts-files.md) | Accounting | Needs attention | UC-F8-25 |
| [S-F8-L24 Variance comments](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l24-variance-comments.md) | Accounting | Needs attention | UC-F8-27 |
| [S-F8-L25 Sustainability reports](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l25-sustainability-reports.md) | Accounting | Needs attention | UC-F8-28 |
| [S-F8-L27 FEC files](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l27-fec-files.md) | Accounting | All | UC-F1-23 |
| [S-F8-L28 Payment runs](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l28-payment-runs.md) | Accounting | All | UC-F8-04 |
| [S-F8-L30 Analytic plans](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l30-analytic-plans.md) | Accounting | All | UC-F8-09 |
| [S-F8-L37 Cash forecasts](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l37-cash-forecasts.md) | Accounting | Needs attention | UC-F8-33 |
| [S-F8-L38 Payment orders](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l38-payment-orders.md) | Accounting | Needs attention | UC-F8-34 |
| [S-F9-L01 Employee records](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l01-employee-records.md) | HR and projects | All | UC-F9-20, UC-F9-28 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | UC-F3-08 |
| [S-F9-L05 HR duties](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l05-hr-duties.md) | HR and projects | Needs attention | UC-F9-22 |
| [S-F9-L06 Job positions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l06-job-positions.md) | HR and projects | All | UC-F9-44 |
| [S-F9-L16 Shifts](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l16-shifts.md) | HR and projects | Needs attention | UC-SC18-08, UC-SC18-19 |
| [S-F9-L18 Project and tasks](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l18-project-and-tasks.md) | HR and projects | Open: New, Planned, Active | UC-F9-29 |
| [S-F9-L20 Equality indexes](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l20-equality-indexes.md) | HR and projects | Needs attention | UC-F9-20 |
| [S-F9-L21 Whistleblowing reports](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l21-whistleblowing-reports.md) | HR and projects | Open: Received, Acknowledged | UC-F9-24 |
| [S-F9-L24 Risk assessment lines](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l24-risk-assessment-lines.md) | HR and projects | All | UC-F9-27 |
| [S-F9-L25 Resource allocations](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l25-resource-allocations.md) | HR and projects | Open: Planned | UC-F9-29 |
| [S-F9-L49 Positions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l49-positions.md) | HR and projects | Needs attention | UC-F9-44 |
| [S-F10-L02 Till sessions](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l02-till-sessions.md) | Point of sale (plugin) | Needs attention | UC-F10-28 |
| [S-F10-L03 Point of sale orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l03-point-of-sale-orders.md) | Point of sale (plugin) | Needs attention | UC-F10-28 |
| [S-F10-L04 Till payments](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l04-till-payments.md) | Point of sale (plugin) | All | UC-F10-24 |
| [S-F10-L06 Closures](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l06-closures.md) | Point of sale (plugin) | All | UC-F10-18 |
| [S-F10-L07 Till archives](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l07-till-archives.md) | Point of sale (plugin) | All | UC-F10-18 |
| [S-F10-L15 Till event logs](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l15-till-event-logs.md) | Point of sale (plugin) | All | UC-F10-18 |
| [S-F10-L18 Card settlements](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l18-card-settlements.md) | Point of sale (plugin) | All | UC-F10-24 |
| [S-F11-L05 Checkouts](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l05-checkouts.md) | Online shop (plugin) | All | UC-F11-29 |
| [S-F11-L08 Withdrawal requests](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l08-withdrawal-requests.md) | Online shop (plugin) | All | UC-F11-29 |
| [S-F11-L15 Tracker consents](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l15-tracker-consents.md) | Online shop (plugin) | All | UC-F11-17 |
| [S-F12-L04 Manufacturing orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l04-manufacturing-orders.md) | Manufacturing (plugin) | Needs attention | UC-F12-19 |
| [S-F12-L13 Machine signals](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l13-machine-signals.md) | Manufacturing (plugin) | All | UC-F12-13, UC-F12-19, UC-F12-29 |
| [S-F12-L23 Energy readings](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l23-energy-readings.md) | Manufacturing (plugin) | All | UC-F12-29 |
| [S-F13-L04 Payslip lines](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l04-payslip-lines.md) | Payroll (plugin) | All | UC-F13-16 |
| [S-F13-L06 Pay runs](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l06-pay-runs.md) | Payroll (plugin) | All | UC-F13-07, UC-F13-34 |
| [S-F13-L12 Payroll entries](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l12-payroll-entries.md) | Payroll (plugin) | All | UC-F13-28 |
| [S-F13-L15 Yearly payroll reports](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l15-yearly-payroll-reports.md) | Payroll (plugin) | All | UC-F13-18 |
| [S-F13-L18 Special pay regimes](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l18-special-pay-regimes.md) | Payroll (plugin) | Open: Active, Changed | UC-F13-23 |
| [S-F13-L21 Profit-sharing years](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l21-profit-sharing-years.md) | Payroll (plugin) | All | UC-F13-28 |
| [S-F13-L24 Payroll cost allocations](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l24-payroll-cost-allocations.md) | Payroll (plugin) | All | UC-F13-34 |
| [S-F13-L25 Analytic axis](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l25-analytic-axis.md) | Payroll (plugin) | All | UC-F13-34 |
| [S-F13-L27 Pay simulations](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l27-pay-simulations.md) | Payroll (plugin) | All | UC-F13-16 |
| [S-F14-L01 Store listings](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l01-store-listings.md) | Plugin store | Open: New, Complete, Refused | UC-F14-01, UC-F14-20 |
| [S-F14-L04 Plugin price plans](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l04-plugin-price-plans.md) | Plugin store | Open: Published | UC-F14-05 |
| [S-F14-L05 Plugin licences](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l05-plugin-licences.md) | Plugin store | All | UC-F14-05, UC-F14-06 |
| [S-F14-L12 Refunds](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l12-refunds.md) | Plugin store | All | UC-F14-17 |
| [S-F14-L19 Support terms](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l19-support-terms.md) | Plugin store | All | UC-F14-05 |
| [S-F14-L24 Partner listings](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l24-partner-listings.md) | Plugin store | Needs attention | UC-F14-31, UC-F21-26 |
| [S-F15-L01 Law packs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l01-law-packs.md) | Legal assistant | All | UC-F15-01, UC-F15-07 |
| [S-F15-L02 Legal warnings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l02-legal-warnings.md) | Legal assistant | All | UC-F15-01, UC-F15-02 |
| [S-F15-L03 Document checks](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l03-document-checks.md) | Legal assistant | All | UC-F15-01, UC-F15-03 |
| [S-F15-L04 Standard register entries](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l04-standard-register-entries.md) | Legal assistant | Needs attention | UC-F15-01, UC-F15-06 |
| [S-F15-L05 Compliance duties](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l05-compliance-duties.md) | Legal assistant | Needs attention | UC-F15-07, UC-F15-08, UC-F15-09 |
| [S-F15-L06 Contract records](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l06-contract-records.md) | Legal assistant | Open: Active, NoticeGiven, Renewed | UC-F15-08 |
| [S-F15-L07 Corporate decisions](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l07-corporate-decisions.md) | Legal assistant | All | UC-F15-09 |
| [S-F15-L09 AI uses](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l09-ai-uses.md) | Legal assistant | All | UC-F15-11 |
| [S-F15-L10 Lawyer hand-offs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l10-lawyer-hand-offs.md) | Legal assistant | Needs attention | UC-F15-01, UC-F15-12 |
| [S-F15-L11 Warning triggers](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l11-warning-triggers.md) | Legal assistant | All | UC-F15-02 |
| [S-F15-L13 Data protection impact assessments](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l13-data-protection-impact-assessments.md) | Legal assistant | All | UC-F15-11 |
| [S-F15-L14 Corporate filings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l14-corporate-filings.md) | Legal assistant | All | UC-F15-07 |
| [S-F15-L15 Shareholdings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l15-shareholdings.md) | Legal assistant | Needs attention | UC-F15-14, UC-F15-15, UC-F15-16, UC-F15-18 |
| [S-F15-L16 Equity grants](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l16-equity-grants.md) | Legal assistant | Needs attention | UC-F15-15, UC-F15-16 |
| [S-F15-L17 Funding rounds](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l17-funding-rounds.md) | Legal assistant | Needs attention | UC-F15-16, UC-F23-34 |
| [S-F15-L18 Clauses](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l18-clauses.md) | Legal assistant | Needs attention | UC-F15-17 |
| [S-F15-L19 General meetings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l19-general-meetings.md) | Legal assistant | Needs attention | UC-F15-18 |
| [S-F16-L02 Intents](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l02-intents.md) | Customer support agents | All | UC-F16-05 |
| [S-F16-L03 Resolution reviews](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l03-resolution-reviews.md) | Customer support agents | All | UC-F16-05 |
| [S-F16-L05 Service-level policies](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l05-service-level-policies.md) | Customer support agents | Open: Active, Changed | UC-F16-05 |
| [S-F16-L08 Satisfaction ratings](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l08-satisfaction-ratings.md) | Customer support agents | Needs attention | UC-F16-05 |
| [S-F17-L01 Competitors](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l01-competitors.md) | Competitive analysis | All | UC-F17-01, UC-F17-20 |
| [S-F17-L02 Company facts](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l02-company-facts.md) | Competitive analysis | All | UC-F17-09 |
| [S-F17-L03 Price points](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l03-price-points.md) | Competitive analysis | All | UC-F17-11 |
| [S-F17-L04 Job signals](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l04-job-signals.md) | Competitive analysis | All | UC-F17-04 |
| [S-F17-L05 Tender awards](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l05-tender-awards.md) | Competitive analysis | All | UC-F17-05 |
| [S-F17-L06 IP filings](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l06-ip-filings.md) | Competitive analysis | All | UC-F17-06 |
| [S-F17-L08 Mentions](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l08-mentions.md) | Competitive analysis | All | UC-F17-09, UC-F17-25 |
| [S-F17-L09 Data providers](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l09-data-providers.md) | Competitive analysis | All | UC-F17-22 |
| [S-F17-L10 Analysis](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l10-analysis.md) | Competitive analysis | All | UC-F17-11, UC-F17-12, UC-F17-20, UC-F17-16 and more |
| [S-F17-L13 Alerts](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l13-alerts.md) | Competitive analysis | All | UC-F17-16 |
| [S-F17-L14 Market estimates](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l14-market-estimates.md) | Competitive analysis | All | UC-F17-17 |
| [S-F17-L16 Tender opportunities](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l16-tender-opportunities.md) | Competitive analysis | All | UC-F17-05, UC-F17-21 |
| [S-F17-L17 Price indexes](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l17-price-indexes.md) | Competitive analysis | All | UC-F17-11, UC-F17-23, UC-F17-25 |
| [S-F17-L18 Price suggestions](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l18-price-suggestions.md) | Competitive analysis | All | UC-F17-23 |
| [S-F17-L19 Data cost lines](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l19-data-cost-lines.md) | Competitive analysis | All | UC-F17-22 |
| [S-F17-L22 Watched pages](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l22-watched-pages.md) | Competitive analysis | Needs attention | UC-F17-27 |
| [S-F18-L01 Hosted websites](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l01-hosted-websites.md) | Hosted websites and domains (hosted edition) | All | UC-F18-01, UC-F18-13, UC-F18-15 |
| [S-F18-L02 Pages](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l02-pages.md) | Hosted websites and domains (hosted edition) | All | UC-F18-01, UC-F18-08, UC-F18-25 |
| [S-F18-L07 Domains](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l07-domains.md) | Hosted websites and domains (hosted edition) | All | UC-F18-09 |
| [S-F18-L10 Publication check reports](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l10-publication-check-reports.md) | Hosted websites and domains (hosted edition) | All | UC-F18-15 |
| [S-F18-L17 Sector templates](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l17-sector-templates.md) | Hosted websites and domains (hosted edition) | All | UC-F18-25 |
| [S-F18-L19 Site backups](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l19-site-backups.md) | Hosted websites and domains (hosted edition) | Needs attention | UC-F18-27 |
| [S-F19-L01 Feature requests](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l01-feature-requests.md) | Feature factory (hosted edition) | All | UC-F19-01, UC-F19-02, UC-F19-09 |
| [S-F19-L02 Feature specifications](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l02-feature-specifications.md) | Feature factory (hosted edition) | All | UC-F19-02 |
| [S-F19-L03 Feature subscriptions](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l03-feature-subscriptions.md) | Feature factory (hosted edition) | All | UC-F19-03, UC-F19-11, UC-F19-19 |
| [S-F19-L04 Generated plugin versions](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l04-generated-plugin-versions.md) | Feature factory (hosted edition) | All | UC-F19-09 |
| [S-F19-L06 Try-out copies](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l06-try-out-copies.md) | Feature factory (hosted edition) | All | UC-F19-07, UC-F19-11 |
| [S-F19-L07 Feature promotions](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l07-feature-promotions.md) | Feature factory (hosted edition) | All | UC-F19-12, UC-F19-20 |
| [S-F19-L08 Promotion credits](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l08-promotion-credits.md) | Feature factory (hosted edition) | All | UC-F19-15, UC-F19-19 |
| [S-F19-L09 Hosted invoices](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l09-hosted-invoices.md) | Feature factory (hosted edition) | All | UC-F19-15, UC-F19-22 |
| [S-F19-L11 Delivery commitments](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l11-delivery-commitments.md) | Feature factory (hosted edition) | Needs attention | UC-F19-03, UC-F19-21, UC-F19-19 |
| [S-F19-L12 Feature refunds](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l12-feature-refunds.md) | Feature factory (hosted edition) | All | UC-F19-07, UC-F19-19, UC-F19-22 |
| [S-F19-L13 Code handovers](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l13-code-handovers.md) | Feature factory (hosted edition) | All | UC-F19-11, UC-F19-23 |
| [S-F19-L15 Factory postings](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l15-factory-postings.md) | Feature factory (hosted edition) | All | UC-F19-15, UC-F19-26 |
| [S-F19-L16 Feature defects](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l16-feature-defects.md) | Feature factory (hosted edition) | All | UC-F19-22 |
| [S-F19-L17 Catalogue changes](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l17-catalogue-changes.md) | Feature factory (hosted edition) | Needs attention | UC-F19-28 |
| [S-F19-L18 Funding pledges](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l18-funding-pledges.md) | Feature factory (hosted edition) | Needs attention | UC-F19-29 |
| [S-F19-L19 Maintenance plans](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l19-feature-maintenance-plans.md) | Feature factory (hosted edition) | Needs attention | UC-F19-30 |
| [S-F20-L01 Support requests](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l01-support-requests.md) | Hosted support assistant (hosted edition) | All | UC-F20-09 |
| [S-F20-L02 Messages](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l02-messages.md) | Hosted support assistant (hosted edition) | All | UC-F20-09 |
| [S-F20-L07 Service incidents](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l07-service-incidents.md) | Hosted support assistant (hosted edition) | All | UC-F20-15, UC-F20-23 |
| [S-F20-L09 Breach records](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l09-breach-records.md) | Hosted support assistant (hosted edition) | All | UC-F20-15 |
| [S-F20-L12 Support plans](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l12-support-plans.md) | Hosted support assistant (hosted edition) | All | UC-F20-19, UC-F20-24 |
| [S-F20-L13 Maintenance notices](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l13-maintenance-notices.md) | Hosted support assistant (hosted edition) | Open: Planned, Running, Overrun | UC-F20-21 |
| [S-F20-L15 Incident reports](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l15-incident-reports.md) | Hosted support assistant (hosted edition) | Needs attention | UC-F20-23 |
| [S-F20-L16 Service credits](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l16-service-credits.md) | Hosted support assistant (hosted edition) | Needs attention | UC-F20-19, UC-F20-24 |
| [S-F20-L17 NIS2 fact sheets](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l17-nis2-fact-sheets.md) | Hosted support assistant (hosted edition) | Needs attention | UC-F20-15, UC-F20-26 |
| [S-F20-L21 Health reports](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l21-health-reports.md) | Hosted support assistant (hosted edition) | Needs attention | UC-F20-31 |
| [S-F21-L01 Onboarding progresses](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l01-onboarding-progresses.md) | Onboarding and module activation | All | UC-F21-01, UC-F21-12, UC-F21-14 |
| [S-F21-L02 Company profiles](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l02-company-profiles.md) | Onboarding and module activation | All | UC-F21-02, UC-F21-07 |
| [S-F21-L03 Set-up templates](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l03-set-up-templates.md) | Onboarding and module activation | All | UC-F21-03 |
| [S-F21-L04 Module activations](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l04-module-activations.md) | Onboarding and module activation | All | UC-F21-04, UC-F21-18 |
| [S-F21-L09 Demo data sets](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l09-demo-data-sets.md) | Onboarding and module activation | All | UC-F21-13 |
| [S-F21-L11 Legal check items](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l11-legal-check-items.md) | Onboarding and module activation | Open: Missing | UC-F21-16 |
| [S-F21-L13 Onboarding figures](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l13-onboarding-figures.md) | Onboarding and module activation | All | UC-F21-20 |
| [S-F21-L16 Language settings](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l16-language-settings.md) | Onboarding and module activation | All | UC-F21-24 |
| [S-F21-L19 Expert sessions](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l19-expert-sessions.md) | Onboarding and module activation | Needs attention | UC-F21-26 |
| [S-F22-L01 Cost periods](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l01-cost-periods.md) | Unified platform cost management | All | UC-F22-01, UC-F22-24 |
| [S-F22-L02 Metered call records](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l02-metered-call-records.md) | Unified platform cost management | All | UC-F22-01, UC-F22-02, UC-F22-20, UC-F22-19 |
| [S-F22-L03 Provider price lists](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l03-provider-price-lists.md) | Unified platform cost management | All | UC-F22-02 |
| [S-F22-L04 Paid providers](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l04-paid-providers.md) | Unified platform cost management | Open: New | UC-F22-05 |
| [S-F22-L05 Hosted quotas](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l05-hosted-quotas.md) | Unified platform cost management | All | UC-F22-05, UC-F22-15 |
| [S-F22-L06 Cost budgets](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l06-cost-budgets.md) | Unified platform cost management | All | UC-F22-20, UC-F22-06, UC-F22-07, UC-F22-09 |
| [S-F22-L07 Cost alerts](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l07-cost-alerts.md) | Unified platform cost management | All | UC-F22-07 |
| [S-F22-L08 Budget approvals](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l08-budget-approvals.md) | Unified platform cost management | All | UC-F22-09 |
| [S-F22-L11 Forecasts](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l11-forecasts.md) | Unified platform cost management | All | UC-F22-12, UC-F22-19 |
| [S-F22-L13 Usage invoices](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l13-usage-invoices.md) | Unified platform cost management | All | UC-F22-15 |
| [S-F22-L14 Exchange rates](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l14-exchange-rates.md) | Unified platform cost management | All | UC-F22-01 |
| [S-F22-L15 Compute machines](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l15-compute-machines.md) | Unified platform cost management | Open: InService | UC-F22-01 |
| [S-F22-L16 Savings recommendations](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l16-savings-recommendations.md) | Unified platform cost management | All | UC-F22-23, UC-F22-24 |
| [S-F22-L18 Client usage statements](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l18-client-usage-statements.md) | Unified platform cost management | Needs attention | UC-F22-26 |
| [S-F22-L19 Credit packs](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l19-credit-packs.md) | Unified platform cost management | Needs attention | UC-F22-27 |
| [S-F23-L01 Baseline forecasts](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l01-baseline-forecasts.md) | What-if simulation and impact | All | UC-F23-01, UC-F23-24 |
| [S-F23-L02 Scenarios](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l02-scenarios.md) | What-if simulation and impact | All | UC-F23-02, UC-F23-20, UC-F23-15, UC-F23-19 and more |
| [S-F23-L03 Scenario changes](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l03-scenario-changes.md) | What-if simulation and impact | All | UC-F23-03, UC-F23-13, UC-F23-25 |
| [S-F23-L04 Simulation runs](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l04-simulation-runs.md) | What-if simulation and impact | All | UC-F23-20 |
| [S-F23-L05 Impact results](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l05-impact-results.md) | What-if simulation and impact | All | UC-F23-20, UC-F23-06, UC-F23-12, UC-F23-13 and more |
| [S-F23-L06 Sensitivities](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l06-sensitivities.md) | What-if simulation and impact | All | UC-F23-14, UC-F23-15 |
| [S-F23-L07 Counter-measures](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l07-counter-measures.md) | What-if simulation and impact | All | UC-F23-16 |
| [S-F23-L08 Action proposals](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l08-action-proposals.md) | What-if simulation and impact | Needs attention | UC-F23-17 |
| [S-F23-L09 Change warnings](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l09-change-warnings.md) | What-if simulation and impact | All | UC-F23-18 |
| [S-F23-L10 Scenario comments](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l10-scenario-comments.md) | What-if simulation and impact | All | UC-F23-19, UC-F23-29 |
| [S-F23-L11 Goals](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l11-goals.md) | What-if simulation and impact | All | UC-F23-21, UC-F23-22 |
| [S-F23-L12 Financing options](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l12-financing-options.md) | What-if simulation and impact | Needs attention | UC-F23-23, UC-F23-29 |
| [S-F23-L13 Driver accuracies](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l13-driver-accuracies.md) | What-if simulation and impact | All | UC-F23-01, UC-F23-24 |
| [S-F23-L14 Sector drivers](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l14-sector-drivers.md) | What-if simulation and impact | All | UC-F23-03, UC-F23-25 |
| [S-F23-L16 Forecast versions](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l16-forecast-versions.md) | What-if simulation and impact | Needs attention | UC-F23-32, UC-F23-34 |
| [S-F23-L17 Valuations](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l17-valuations.md) | What-if simulation and impact | Needs attention | UC-F23-34 |
| [S-F24-L01 Connectors](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l01-connectors.md) | Integrations hub | All | UC-F24-19 |
| [S-F24-L02 Tool connections](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l02-tool-connections.md) | Integrations hub | All | UC-F24-20, UC-F24-21 |
| [S-F24-L09 Connector actions](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l09-connector-actions.md) | Integrations hub | All | UC-F24-14, UC-F24-20 |
| [S-F24-L11 Connector categories](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l11-connector-categories.md) | Integrations hub | Open: Active | UC-F24-21 |
| [S-F24-L12 Integration icons](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l12-integration-icons.md) | Integrations hub | Open: Proposed, Approved, Replaced | UC-F24-21 |
| [S-F24-L13 Webhook subscriptions](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l13-webhook-subscriptions.md) | Integrations hub | Open: Active, Paused | UC-F24-20 |
| [S-F24-L16 Connector requests](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l16-connector-requests.md) | Integrations hub | All | UC-F24-19 |
| [S-F25-L01 Bug or feature requests](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l01-bug-or-feature-requests.md) | DevOps agents (hosted edition) | All | UC-F25-01, UC-F25-02, UC-F25-14, UC-F25-16 and more |
| [S-F25-L03 USER tickets](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l03-user-tickets.md) | DevOps agents (hosted edition) | Needs attention | UC-F25-24 |
| [S-F25-L05 Agent pull requests](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l05-agent-pull-requests.md) | DevOps agents (hosted edition) | Needs attention | UC-F25-36 |
| [S-F25-L09 Request status](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l09-request-status.md) | DevOps agents (hosted edition) | All | UC-F25-14, UC-F25-15, UC-F25-20 |
| [S-F25-L11 Triages](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l11-triages.md) | DevOps agents (hosted edition) | Needs attention | UC-F25-14 |
| [S-F25-L12 Vulnerability cases](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l12-vulnerability-cases.md) | DevOps agents (hosted edition) | Open: Reported, Confirmed, Fixed | UC-F25-01 |
| [S-F25-L14 Votes](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l14-votes.md) | DevOps agents (hosted edition) | Open: Counted | UC-F25-20, UC-F25-24 |
| [S-F25-L23 Run checkpoints](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l23-run-checkpoints.md) | DevOps agents (hosted edition) | Needs attention | UC-F25-36 |
| [S-SC01-L01 Construction sites](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l01-construction-sites.md) | Construction | Open: Planned, Running, Accepted | UC-SC01-14 |
| [S-SC01-L06 Progress bills](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l06-progress-bills.md) | Construction | Needs attention | UC-SC01-14 |
| [S-SC02-L01 Stores](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l01-stores.md) | Retail | Needs attention | UC-SC02-01, UC-SC02-14 |
| [S-SC02-L02 Assortments](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l02-assortments.md) | Retail | All | UC-SC02-01 |
| [S-SC02-L09 Store targets](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l09-store-targets.md) | Retail | All | UC-SC02-11 |
| [S-SC02-L12 Footfall counts](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l12-footfall-counts.md) | Retail | All | UC-SC02-14 |
| [S-SC02-L16 Franchisees](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l16-franchisees.md) | Retail | Needs attention | UC-SC02-19 |
| [S-SC03-L01 Engagements](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l01-engagements.md) | Services | Open: PreSales, Running | UC-SC03-10 |
| [S-SC03-L03 Rate cards](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l03-rate-cards.md) | Services | All | UC-SC03-02 |
| [S-SC03-L04 Staffing assignments](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l04-staffing-assignments.md) | Services | All | UC-SC03-04 |
| [S-SC03-L13 Satisfaction surveys](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l13-satisfaction-surveys.md) | Services | Open: Sent | UC-SC03-12 |
| [S-SC03-L14 Pricing models](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l14-pricing-models.md) | Services | All | UC-SC03-02 |
| [S-SC04-L10 Complaints](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l10-complaints.md) | Home care | Needs attention | UC-SC04-12 |
| [S-SC04-L12 Activity reports](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l12-activity-reports.md) | Home care | All | UC-SC04-14 |
| [S-SC05-L14 Management reviews](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l14-management-reviews.md) | Manufacturing | All | UC-SC05-14 |
| [S-SC06-L07 Rate plans](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l07-rate-plans.md) | Restaurant and hospitality | All | UC-SC06-14 |
| [S-SC06-L09 Folios](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l09-folios.md) | Restaurant and hospitality | Needs attention | UC-SC06-14 |
| [S-SC06-L16 Price rules](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l16-price-rules.md) | Restaurant and hospitality | Needs attention | UC-SC06-19 |
| [S-SC06-L17 Licences](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l17-licences.md) | Restaurant and hospitality | Needs attention | UC-SC06-20 |
| [S-SC07-L02 Trips](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l02-trips.md) | Transport and logistics | All | UC-SC07-18 |
| [S-SC07-L13 Transport invoice lines](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l13-transport-invoice-lines.md) | Transport and logistics | All | UC-SC07-18 |
| [S-SC08-L01 Members](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l01-members.md) | Non-profit association | All | UC-SC08-17, UC-SC08-19 |
| [S-SC08-L02 Dues payments](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l02-dues-payments.md) | Non-profit association | All | UC-SC08-23 |
| [S-SC08-L03 Assembly or board meetings](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l03-assembly-or-board-meetings.md) | Non-profit association | All | UC-SC08-02, UC-SC08-03 |
| [S-SC08-L04 Gifts](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l04-gifts.md) | Non-profit association | All | UC-SC08-20, UC-SC08-19 |
| [S-SC08-L09 Grant reports](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l09-grant-reports.md) | Non-profit association | Needs attention | UC-SC08-09, UC-SC08-14, UC-SC08-15 |
| [S-SC08-L10 Missions](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l10-missions.md) | Non-profit association | All | UC-SC08-10 |
| [S-SC08-L12 Association events](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l12-association-events.md) | Non-profit association | Open: Planned | UC-SC08-12 |
| [S-SC08-L15 Gift in kinds](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l15-gift-in-kinds.md) | Non-profit association | All | UC-SC08-16 |
| [S-SC08-L16 Grant applications](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l16-grant-applications.md) | Non-profit association | Needs attention | UC-SC08-21 |
| [S-SC08-L18 Member organisations](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l18-member-organisations.md) | Non-profit association | Needs attention | UC-SC08-23 |
| [S-SC09-L01 Appointments](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l01-appointments.md) | Health practices | Open: Booked, Confirmed, NoShow | UC-SC09-20, UC-SC09-11, UC-SC09-12 |
| [S-SC09-L02 Patients](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l02-patients.md) | Health practices | All | UC-SC09-17 |
| [S-SC09-L03 Clinical record entries](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l03-clinical-record-entries.md) | Health practices | All | UC-SC09-20, UC-SC09-04, UC-SC09-09, UC-SC09-10 and more |
| [S-SC09-L04 Prescriptions](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l04-prescriptions.md) | Health practices | All | UC-SC09-05 |
| [S-SC09-L05 Care sheets](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l05-care-sheets.md) | Health practices | Needs attention | UC-SC09-06, UC-SC09-18 |
| [S-SC09-L06 Insurer returns](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l06-insurer-returns.md) | Health practices | All | UC-SC09-15 |
| [S-SC09-L08 Health exchanges](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l08-health-exchanges.md) | Health practices | All | UC-SC09-09, UC-SC09-10 |
| [S-SC09-L09 Consulting rooms](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l09-consulting-rooms.md) | Health practices | All | UC-SC09-12 |
| [S-SC09-L10 Shared costs](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l10-shared-costs.md) | Health practices | All | UC-SC09-13, UC-SC09-15 |
| [S-SC09-L11 Sterilisation cycles](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l11-sterilisation-cycles.md) | Health practices | All | UC-SC09-14 |
| [S-SC09-L12 Locum agreements](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l12-locum-agreements.md) | Health practices | All | UC-SC09-16 |
| [S-SC09-L18 Centre activities](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l18-centre-activities.md) | Health practices | Needs attention | UC-SC09-25 |
| [S-SC11-L01 Client identities](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l01-client-identities.md) | Professional firms | All | UC-SC11-15 |
| [S-SC11-L06 Time entries](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l06-time-entries.md) | Professional firms | All | UC-SC11-14 |
| [S-SC11-L07 Fee bills](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l07-fee-bills.md) | Professional firms | All | UC-SC11-14, UC-SC11-19 |
| [S-SC11-L12 Vigilance records](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l12-vigilance-records.md) | Professional firms | All | UC-SC11-15 |
| [S-SC11-L13 Access walls](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l13-access-walls.md) | Professional firms | All | UC-SC11-16 |
| [S-SC11-L14 Partner shares](../../../08-sectors/sc11-professional-firms/screens/00-lists/s-sc11-l14-partner-shares.md) | Professional firms | All | UC-SC11-17, UC-SC11-19 |
| [S-SC12-L12 Quality evidences](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l12-quality-evidences.md) | Education and training | All | UC-SC12-12 |
| [S-SC14-L01 Software subscriptions](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l01-software-subscriptions.md) | IT and software | Open: Trial, Active | UC-SC14-18 |
| [S-SC14-L09 Health scores](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l09-health-scores.md) | IT and software | All | UC-SC14-18 |
| [S-SC14-L12 Security reports](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l12-security-reports.md) | IT and software | All | UC-SC14-13 |
| [S-SC14-L19 R&D projects](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l19-r-d-projects.md) | IT and software | Needs attention | UC-SC14-24 |
| [S-SC14-L20 Sponsorships](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l20-sponsorships.md) | IT and software | Needs attention | UC-SC14-25 |
| [S-SC15-L02 Rebate rules](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l02-rebate-rules.md) | Wholesale and distribution | All | UC-SC15-15 |
| [S-SC15-L03 Yearly agreements](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l03-yearly-agreements.md) | Wholesale and distribution | All | UC-SC15-03 |
| [S-SC15-L04 Sales orders](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l04-sales-orders.md) | Wholesale and distribution | All | UC-SC15-15 |
| [S-SC16-L01 Shows](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l01-shows.md) | Events and culture | Open: OnSale, Approved, Held | UC-SC16-01, UC-SC16-18 |
| [S-SC16-L02 Event budgets](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l02-event-budgets.md) | Events and culture | Needs attention | UC-SC16-01, UC-SC16-18 |
| [S-SC16-L11 Sponsorships](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l11-sponsorships.md) | Events and culture | All | UC-SC16-10 |
| [S-SC18-L01 Club memberships](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l01-club-memberships.md) | Sports and fitness | Needs attention | UC-SC18-01, UC-SC18-04, UC-SC18-09, UC-SC18-16 and more |
| [S-SC18-L04 Classes](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l04-classes.md) | Sports and fitness | Needs attention | UC-SC18-05, UC-SC18-08, UC-SC18-16 |
| [S-SC18-L06 Licences](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l06-licences.md) | Sports and fitness | Needs attention | UC-SC18-09, UC-SC18-16 |
| [S-SC18-L13 Court bookings](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l13-court-bookings.md) | Sports and fitness | Needs attention | UC-SC18-17 |
| [S-SC18-L15 Camp registrations](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l15-camp-registrations.md) | Sports and fitness | Needs attention | UC-SC18-19 |
| [S-SC19-L01 Maintenance contracts](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l01-maintenance-contracts.md) | Trades and home services | Needs attention | UC-SC19-01 |
| [S-SC19-L06 Household contracts](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l06-household-contracts.md) | Trades and home services | Needs attention | UC-SC19-09 |
| [S-SC19-L09 Labels](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l09-labels.md) | Trades and home services | Needs attention | UC-SC19-15 |
| [S-SC19-L12 Warranty certificates](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l12-warranty-certificates.md) | Trades and home services | Needs attention | UC-SC19-18 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Competitive analysis](../../../02-functional/f17-competitive-analysis/screens/00-lists/README.md),
[Construction](../../../08-sectors/sc01-construction/screens/00-lists/README.md),
[Customer support agents](../../../02-functional/f16-customer-support-agents/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[DevOps agents (hosted edition)](../../../02-functional/f25-devops-agents/screens/00-lists/README.md),
[Education and training](../../../08-sectors/sc12-education-and-training/screens/00-lists/README.md),
[Events and culture](../../../08-sectors/sc16-events-and-culture/screens/00-lists/README.md),
[Feature factory (hosted edition)](../../../02-functional/f19-feature-factory/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Health practices](../../../08-sectors/sc09-health-practices/screens/00-lists/README.md),
[Home care](../../../08-sectors/sc04-home-care/screens/00-lists/README.md),
[Hosted support assistant (hosted edition)](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/README.md),
[Hosted websites and domains (hosted edition)](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/README.md),
[IT and software](../../../08-sectors/sc14-it-and-software/screens/00-lists/README.md),
[Integrations hub](../../../02-functional/f24-integrations-hub/screens/00-lists/README.md),
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md),
[Manufacturing](../../../08-sectors/sc05-manufacturing/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Non-profit association](../../../08-sectors/sc08-non-profit/screens/00-lists/README.md),
[Onboarding and module activation](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md),
[Plugin store](../../../02-functional/f14-plugin-store/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Professional firms](../../../08-sectors/sc11-professional-firms/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Restaurant and hospitality](../../../08-sectors/sc06-hospitality/screens/00-lists/README.md),
[Retail](../../../08-sectors/sc02-retail/screens/00-lists/README.md),
[Services](../../../08-sectors/sc03-services/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md),
[Sports and fitness](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/README.md),
[Trades and home services](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/README.md),
[Transport and logistics](../../../08-sectors/sc07-transport/screens/00-lists/README.md),
[Unified platform cost management](../../../02-functional/f22-unified-cost-management/screens/00-lists/README.md),
[What-if simulation and impact](../../../02-functional/f23-what-if-simulation/screens/00-lists/README.md),
[Wholesale and distribution](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U13 | desktop | ![Workspace, U13, light](mockups/workspace-desktop-light.png) | ![Workspace, U13, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U13 | phone | ![Workspace, U13, light](mockups/workspace-phone-light.png) | ![Workspace, U13, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
