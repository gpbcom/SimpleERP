🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
👷 [Employee: app shell and home](README.md) › 🧰 U01 Employee: workspace

# 🧰 U01 Employee: workspace

**Status:** ✅ specified

## Purpose

The views [U01 Employee](../../../01-users/personas/u01-employee.md) works with, embedded on their
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
| [S-F1-L03 Users](../../../02-functional/f01-administration/screens/00-lists/s-f01-l03-users.md) | Administration | Mine: manager | UC-F1-03, UC-F1-04, UC-F1-05 |
| [S-F1-L04 Invitations](../../../02-functional/f01-administration/screens/00-lists/s-f01-l04-invitations.md) | Administration | Open: Sent, Accepted, NotDelivered | UC-F1-03, UC-F21-17 |
| [S-F1-L05 Former-employee accesses](../../../02-functional/f01-administration/screens/00-lists/s-f01-l05-former-employee-accesses.md) | Administration | Mine: former user | UC-F1-05 |
| [S-F1-L23 User sessions](../../../02-functional/f01-administration/screens/00-lists/s-f01-l23-user-sessions.md) | Administration | Mine: user | UC-F1-24 |
| [S-F1-L26 Act-as sessions](../../../02-functional/f01-administration/screens/00-lists/s-f01-l26-act-as-sessions.md) | Administration | Mine: target user | UC-F1-27 |
| [S-F2-L18 Resource bookings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l18-resource-bookings.md) | No-code configuration | Open: Requested, Confirmed, NoShow | UC-F4-21 |
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Mine: owner | UC-F3-01, UC-F3-08, UC-F3-09, UC-F15-01 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-01, UC-F3-02, UC-F3-04, UC-F3-15 and more |
| [S-F3-L04 Assistant change batches](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l04-assistant-change-batches.md) | Assistant | Mine: user | UC-F3-03 |
| [S-F3-L07 Personal connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l07-personal-connections.md) | Assistant | Mine: user | UC-F3-06 |
| [S-F3-L12 Conversation folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l12-conversation-folders.md) | Assistant | Mine: owner | UC-F3-08 |
| [S-F3-L13 Queued questions](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l13-queued-questions.md) | Assistant | All | UC-F3-09 |
| [S-F3-L14 Answer feedbacks](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l14-answer-feedbacks.md) | Assistant | All | UC-F3-01 |
| [S-F3-L19 Injection alerts](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l19-injection-alerts.md) | Assistant | Mine: user | UC-F3-15 |
| [S-F3-L20 Memory items](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l20-memory-items.md) | Assistant | Mine: user | UC-F3-17 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | UC-F3-03, UC-F3-04, UC-F3-06 |
| [S-F3-L27 To-dos](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l27-to-dos.md) | Assistant | Mine: owner, the only view: to-dos are private | UC-F3-24 |
| [S-F4-L01 Meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l01-meetings.md) | Meetings | Open: Planned, Live, WaitingForReview | UC-F4-07, UC-F4-21 |
| [S-F4-L02 Transcripts](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l02-transcripts.md) | Meetings | All | UC-F4-22 |
| [S-F4-L04 Action items](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l04-action-items.md) | Meetings | Open: Open | UC-F4-27 |
| [S-F4-L08 Key moments](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l08-key-moments.md) | Meetings | All | D519, VC-10 |
| [S-F4-L10 Chat channels](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l10-chat-channels.md) | Meetings | All | UC-F4-17 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L17 Meeting summaries](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l17-meeting-summaries.md) | Meetings | All | UC-F4-07 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F4-L27 Video messages](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l27-video-messages.md) | Meetings | Mine: author | UC-F4-28 |
| [S-F5-L08 Surveys](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l08-surveys.md) | Social media and marketing | Open: Draft, Sent | UC-F9-28 |
| [S-F7-L02 Purchase requests](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l02-purchase-requests.md) | Purchasing and stock | All | UC-F7-01, UC-F7-20 |
| [S-F7-L03 Purchase orders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l03-purchase-orders.md) | Purchasing and stock | All | UC-F7-01 |
| [S-F7-L17 Approved catalogues](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l17-approved-catalogues.md) | Purchasing and stock | Open: Active | UC-F7-20 |
| [S-F8-L03 Journal entries](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l03-journal-entries.md) | Accounting | All | UC-F8-29 |
| [S-F8-L09 Expense claims](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l09-expense-claims.md) | Accounting | Mine: employee | UC-F8-12 |
| [S-F8-L15 Company cards](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l15-company-cards.md) | Accounting | All | UC-F8-18 |
| [S-F8-L26 Accountant requests](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l26-accountant-requests.md) | Accounting | Mine: assignee | UC-F8-29 |
| [S-F8-L43 Trips](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l43-trips.md) | Accounting | All | UC-F8-39 |
| [S-F9-L01 Employee records](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l01-employee-records.md) | HR and projects | Mine: manager | UC-F9-04, UC-F9-20, UC-F9-21, UC-F9-28 and more |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | UC-F3-08 |
| [S-F9-L05 HR duties](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l05-hr-duties.md) | HR and projects | Mine: employee | UC-F9-21 |
| [S-F9-L07 Applicants](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l07-applicants.md) | HR and projects | All | UC-F9-08 |
| [S-F9-L08 Time-off allocations](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l08-time-off-allocations.md) | HR and projects | All | UC-F9-09 |
| [S-F9-L09 Time-off requests](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l09-time-off-requests.md) | HR and projects | Open: ToApprove, Approved, Refused | UC-F9-09 |
| [S-F9-L10 Attendances](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l10-attendances.md) | HR and projects | Mine: employee | UC-F9-10 |
| [S-F9-L11 Appraisals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l11-appraisals.md) | HR and projects | Mine: employee | UC-F9-11 |
| [S-F9-L12 Certifications](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l12-certifications.md) | HR and projects | Mine: employee | UC-F9-11, UC-F9-25, UC-F9-38, UC-F9-39 |
| [S-F9-L14 Approval requests](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l14-approval-requests.md) | HR and projects | Mine: requester | UC-F9-13 |
| [S-F9-L17 Timesheet lines](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l17-timesheet-lines.md) | HR and projects | Mine: employee | UC-F9-16 |
| [S-F9-L20 Equality indexes](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l20-equality-indexes.md) | HR and projects | All | UC-F9-20 |
| [S-F9-L21 Whistleblowing reports](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l21-whistleblowing-reports.md) | HR and projects | Open: Received, Acknowledged | UC-F9-24 |
| [S-F9-L22 Training sessions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l22-training-sessions.md) | HR and projects | Open: Planned, Held | UC-F9-25 |
| [S-F9-L29 Degrees](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l29-degrees.md) | HR and projects | Mine: employee | UC-F9-38, UC-F9-39 |
| [S-F9-L30 Qualification types](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l30-qualification-types.md) | HR and projects | Open: Active | UC-F9-38, UC-F9-39 |
| [S-F9-L31 Attribute readings](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l31-attribute-readings.md) | HR and projects | Mine: employee | UC-F9-38, UC-F9-39 |
| [S-F9-L34 Attendance kiosks](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l34-attendance-kiosks.md) | HR and projects | All | UC-F9-10 |
| [S-F9-L35 Employee badges](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l35-employee-badges.md) | HR and projects | All | UC-F9-10 |
| [S-F9-L36 Employee referrals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l36-employee-referrals.md) | HR and projects | All | UC-F9-08 |
| [S-F9-L39 Lunch orders](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l39-lunch-orders.md) | HR and projects | All | UC-F9-13 |
| [S-F9-L48 Work location days](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l48-work-location-days.md) | HR and projects | Mine: employee | UC-F9-43 |
| [S-F9-L52 Online courses](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l52-online-courses.md) | HR and projects | Mine: learner | UC-F9-47 |
| [S-F11-L03 Online products](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l03-online-products.md) | Online shop (plugin) | All | UC-F9-47 |
| [S-F13-L07 Payslips](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l07-payslips.md) | Payroll (plugin) | Mine: employee | UC-F13-08, UC-F13-20 |
| [S-F13-L08 Pay transfers](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l08-pay-transfers.md) | Payroll (plugin) | Mine: employee | UC-F13-27 |
| [S-F13-L12 Payroll entries](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l12-payroll-entries.md) | Payroll (plugin) | All | UC-F13-28 |
| [S-F13-L20 Pay advances](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l20-pay-advances.md) | Payroll (plugin) | Mine: employee | UC-F13-27 |
| [S-F13-L21 Profit-sharing years](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l21-profit-sharing-years.md) | Payroll (plugin) | All | UC-F13-28 |
| [S-F13-L29 Days packages](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l29-days-packages.md) | Payroll (plugin) | All | UC-F13-36 |
| [S-F15-L01 Law packs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l01-law-packs.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L02 Legal warnings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l02-legal-warnings.md) | Legal assistant | Mine: shown to | UC-F15-01, UC-F15-02 |
| [S-F15-L03 Document checks](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l03-document-checks.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L04 Standard register entries](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l04-standard-register-entries.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L08 Data-subject requests](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l08-data-subject-requests.md) | Legal assistant | All | UC-F15-10 |
| [S-F15-L10 Lawyer hand-offs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l10-lawyer-hand-offs.md) | Legal assistant | All | UC-F15-01, UC-F15-12 |
| [S-F15-L11 Warning triggers](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l11-warning-triggers.md) | Legal assistant | All | UC-F15-02 |
| [S-F15-L15 Shareholdings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l15-shareholdings.md) | Legal assistant | All | UC-F15-15 |
| [S-F15-L16 Equity grants](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l16-equity-grants.md) | Legal assistant | All | UC-F15-15 |
| [S-F18-L15 Mailboxes](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l15-mailboxes.md) | Hosted websites and domains (hosted edition) | Mine: owner | UC-F18-23 |
| [S-F20-L01 Support requests](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l01-support-requests.md) | Hosted support assistant (hosted edition) | Mine: author | UC-F20-01, UC-F20-28 |
| [S-F20-L02 Messages](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l02-messages.md) | Hosted support assistant (hosted edition) | Mine: author | UC-F20-12, UC-F20-25, UC-F20-27 |
| [S-F20-L03 Screenshots](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l03-screenshots.md) | Hosted support assistant (hosted edition) | All | UC-F20-28 |
| [S-F20-L14 Upgrade release notes](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l14-upgrade-release-notes.md) | Hosted support assistant (hosted edition) | Open: Draft, Published | UC-F20-22 |
| [S-F21-L01 Onboarding progresses](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l01-onboarding-progresses.md) | Onboarding and module activation | All | UC-F21-25 |
| [S-F21-L10 Tours](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l10-tours.md) | Onboarding and module activation | All | UC-F21-15, UC-F21-17 |
| [S-F21-L16 Language settings](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l16-language-settings.md) | Onboarding and module activation | All | UC-F21-24 |
| [S-F24-L02 Tool connections](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l02-tool-connections.md) | Integrations hub | Mine: linked user | UC-F24-03, UC-F24-26 |
| [S-F24-L03 Suite components](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l03-suite-components.md) | Integrations hub | All | UC-F24-03, UC-F24-04, UC-F24-05, UC-F24-06 |
| [S-F24-L04 Linked documents](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l04-linked-documents.md) | Integrations hub | All | UC-F24-04 |
| [S-F24-L05 Calendar links](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l05-calendar-links.md) | Integrations hub | Mine: user | UC-F24-05, UC-F24-25 |
| [S-T03-L01 Audit entries](../../../03-technical/t03-audit-trail/screens/00-lists/s-t03-l01-audit-entries.md) | Audit trail | All | UC-F1-27 |
| [S-SC08-L17 Integration pathways](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l17-integration-pathways.md) | Non-profit association | All | UC-SC08-22 |
| [S-SC12-L05 Training fundings](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l05-training-fundings.md) | Education and training | All | UC-SC12-21 |
| [S-SC12-L20 Apprenticeship contracts](../../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l20-apprenticeship-contracts.md) | Education and training | All | UC-SC12-21 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Audit trail](../../../03-technical/t03-audit-trail/screens/00-lists/README.md),
[Education and training](../../../08-sectors/sc12-education-and-training/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Hosted support assistant (hosted edition)](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/README.md),
[Hosted websites and domains (hosted edition)](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/README.md),
[Integrations hub](../../../02-functional/f24-integrations-hub/screens/00-lists/README.md),
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Non-profit association](../../../08-sectors/sc08-non-profit/screens/00-lists/README.md),
[Onboarding and module activation](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U01 | desktop | ![Workspace, U01, light](mockups/workspace-desktop-light.png) | ![Workspace, U01, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U01 | phone | ![Workspace, U01, light](mockups/workspace-phone-light.png) | ![Workspace, U01, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
