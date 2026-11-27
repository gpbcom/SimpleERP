🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🧑‍🤝‍🧑 [Human resources: app shell and home](README.md) › 🧰 U06 Human resources: workspace

# 🧰 U06 Human resources: workspace

**Status:** ✅ specified

## Purpose

The views [U06 Human resources](../../../01-users/personas/u06-hr.md) works with, embedded on their
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
| [S-F2-L01 Custom fields](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l01-custom-fields.md) | No-code configuration | Needs attention | UC-F2-27 |
| [S-F2-L14 Signature requests](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l14-signature-requests.md) | No-code configuration | Needs attention | UC-F2-14 |
| [S-F2-L22 Field rules](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l22-field-rules.md) | No-code configuration | Needs attention | UC-F2-27 |
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Open: Private, Shared | UC-F3-01, UC-F3-08, UC-F15-01 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-01, UC-F3-02, UC-F3-04 |
| [S-F3-L04 Assistant change batches](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l04-assistant-change-batches.md) | Assistant | Open: Proposed | UC-F3-03 |
| [S-F3-L07 Personal connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l07-personal-connections.md) | Assistant | Needs attention | UC-F3-06 |
| [S-F3-L09 Knowledge items](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l09-knowledge-items.md) | Assistant | Needs attention | UC-F3-07 |
| [S-F3-L10 Knowledge folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l10-knowledge-folders.md) | Assistant | All | UC-F3-07 |
| [S-F3-L11 Knowledge proposals](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l11-knowledge-proposals.md) | Assistant | Needs attention | UC-F3-07, UC-F3-19 |
| [S-F3-L12 Conversation folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l12-conversation-folders.md) | Assistant | All | UC-F3-08 |
| [S-F3-L14 Answer feedbacks](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l14-answer-feedbacks.md) | Assistant | All | UC-F3-01 |
| [S-F3-L21 Unanswered topics](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l21-unanswered-topics.md) | Assistant | Needs attention | UC-F3-19 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | UC-F3-03, UC-F3-04, UC-F3-06 |
| [S-F4-L01 Meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l01-meetings.md) | Meetings | Needs attention | UC-F4-07 |
| [S-F4-L06 Scorecards](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l06-scorecards.md) | Meetings | All | D519, VC-9 |
| [S-F4-L07 Evaluation grids](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l07-evaluation-grids.md) | Meetings | All | UC-F4-13 |
| [S-F4-L08 Key moments](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l08-key-moments.md) | Meetings | All | D519, VC-10 |
| [S-F4-L09 Scheduled digests](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l09-scheduled-digests.md) | Meetings | All | UC-F4-15 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Needs attention | D519, VC-11 |
| [S-F4-L17 Meeting summaries](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l17-meeting-summaries.md) | Meetings | All | UC-F4-07 |
| [S-F4-L18 Recording notices](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l18-recording-notices.md) | Meetings | All | D519, VC-12 |
| [S-F4-L21 Interview debriefs](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l21-interview-debriefs.md) | Meetings | All | UC-F4-13 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | All | flow charts (VR-3) |
| [S-F4-L29 Note templates](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l29-note-templates.md) | Meetings | Needs attention | UC-F4-30 |
| [S-F5-L08 Surveys](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l08-surveys.md) | Social media and marketing | Needs attention | UC-F5-12, UC-F9-28 |
| [S-F9-L01 Employee records](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l01-employee-records.md) | HR and projects | All | UC-F9-01, UC-F9-02, UC-F9-03, UC-F9-20 and more |
| [S-F9-L02 Contracts](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l02-contracts.md) | HR and projects | Needs attention | UC-F9-01, UC-F9-07 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | UC-F3-08, UC-F9-01 |
| [S-F9-L04 Activity plans](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l04-activity-plans.md) | HR and projects | All | UC-F9-02 |
| [S-F9-L05 HR duties](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l05-hr-duties.md) | HR and projects | Needs attention | UC-F9-03, UC-F9-21, UC-F9-22, UC-F9-23 |
| [S-F9-L06 Job positions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l06-job-positions.md) | HR and projects | All | UC-F9-05, UC-F9-40, UC-F9-42 |
| [S-F9-L07 Applicants](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l07-applicants.md) | HR and projects | All | UC-F9-05, UC-F9-06, UC-F9-07, UC-F9-08 and more |
| [S-F9-L08 Time-off allocations](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l08-time-off-allocations.md) | HR and projects | All | UC-F9-09 |
| [S-F9-L09 Time-off requests](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l09-time-off-requests.md) | HR and projects | Open: ToApprove, Approved, Refused | UC-F9-09 |
| [S-F9-L11 Appraisals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l11-appraisals.md) | HR and projects | All | UC-F9-11 |
| [S-F9-L12 Certifications](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l12-certifications.md) | HR and projects | Needs attention | UC-F9-11, UC-F9-25, UC-F9-38, UC-F9-39 and more |
| [S-F9-L13 Company vehicles](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l13-company-vehicles.md) | HR and projects | All | UC-F9-12 |
| [S-F9-L18 Project and tasks](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l18-project-and-tasks.md) | HR and projects | Messages to send | UC-F9-41, D570 |
| [S-F9-L19 Contract templates](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l19-contract-templates.md) | HR and projects | Needs attention | UC-F9-19 |
| [S-F9-L20 Equality indexes](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l20-equality-indexes.md) | HR and projects | Needs attention | UC-F9-20 |
| [S-F9-L21 Whistleblowing reports](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l21-whistleblowing-reports.md) | HR and projects | Open: Received, Acknowledged | UC-F9-24 |
| [S-F9-L22 Training sessions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l22-training-sessions.md) | HR and projects | Open: Planned, Held | UC-F9-25 |
| [S-F9-L23 Work accidents](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l23-work-accidents.md) | HR and projects | Open: Active | UC-F9-26 |
| [S-F9-L24 Risk assessment lines](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l24-risk-assessment-lines.md) | HR and projects | All | UC-F9-27 |
| [S-F9-L29 Degrees](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l29-degrees.md) | HR and projects | Needs attention | UC-F9-38, UC-F9-39 |
| [S-F9-L30 Qualification types](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l30-qualification-types.md) | HR and projects | Open: Active | UC-F9-38, UC-F9-39 |
| [S-F9-L31 Attribute readings](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l31-attribute-readings.md) | HR and projects | Needs attention | UC-F9-38, UC-F9-39 |
| [S-F9-L36 Employee referrals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l36-employee-referrals.md) | HR and projects | All | UC-F9-08 |
| [S-F9-L38 Job offers](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l38-job-offers.md) | HR and projects | All | UC-F9-07 |
| [S-F9-L40 Personnel registers](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l40-personnel-registers.md) | HR and projects | All | UC-F9-01 |
| [S-F9-L41 Pre-hiring declaration (DPAE)s](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l41-pre-hiring-declaration-dpae-s.md) | HR and projects | All | UC-F9-03 |
| [S-F9-L44 Sourcing searches](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l44-sourcing-searches.md) | HR and projects | Needs attention | UC-F9-40, UC-F9-41 |
| [S-F9-L45 Prospects](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l45-prospects.md) | HR and projects | Needs attention | UC-F9-40, UC-F9-41, UC-F9-42 |
| [S-F9-L46 Outreach sequences](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l46-outreach-sequences.md) | HR and projects | Needs attention | UC-F9-41, UC-F9-42 |
| [S-F9-L47 Outreach messages](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l47-outreach-messages.md) | HR and projects | Needs attention | UC-F9-41, UC-F9-42 |
| [S-F9-L49 Positions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l49-positions.md) | HR and projects | Needs attention | UC-F9-44, UC-F9-45 |
| [S-F9-L50 Succession plans](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l50-succession-plans.md) | HR and projects | Needs attention | UC-F9-45 |
| [S-F12-L17 Qualification requirements](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l17-qualification-requirements.md) | Manufacturing (plugin) | All | UC-F12-22, UC-SC05-13 |
| [S-F13-L02 Employee pay profiles](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l02-employee-pay-profiles.md) | Payroll (plugin) | All | UC-F13-02, UC-F13-21, UC-F13-22 |
| [S-F13-L03 Pay inputs](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l03-pay-inputs.md) | Payroll (plugin) | Needs attention | UC-F13-03, UC-F13-14, UC-F13-33 |
| [S-F13-L13 Sick leaves](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l13-sick-leaves.md) | Payroll (plugin) | Open: New | UC-F13-14 |
| [S-F13-L14 End-of-contract files](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l14-end-of-contract-files.md) | Payroll (plugin) | All | UC-F13-15 |
| [S-F13-L17 Scheme memberships](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l17-scheme-memberships.md) | Payroll (plugin) | Open: Enrolled, Exempted | UC-F13-21 |
| [S-F13-L18 Special pay regimes](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l18-special-pay-regimes.md) | Payroll (plugin) | Open: Active, Changed | UC-F13-22 |
| [S-F13-L23 Agreement families](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l23-agreement-families.md) | Payroll (plugin) | All | UC-F13-33 |
| [S-F13-L31 Delegation hours](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l31-delegation-hours.md) | Payroll (plugin) | Needs attention | UC-F13-38 |
| [S-F15-L01 Law packs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l01-law-packs.md) | Legal assistant | All | UC-F15-01, UC-F15-07 |
| [S-F15-L02 Legal warnings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l02-legal-warnings.md) | Legal assistant | All | UC-F15-01, UC-F15-02 |
| [S-F15-L03 Document checks](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l03-document-checks.md) | Legal assistant | All | UC-F15-01, UC-F15-03 |
| [S-F15-L04 Standard register entries](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l04-standard-register-entries.md) | Legal assistant | Needs attention | UC-F15-01 |
| [S-F15-L05 Compliance duties](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l05-compliance-duties.md) | Legal assistant | Needs attention | UC-F15-07 |
| [S-F15-L08 Data-subject requests](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l08-data-subject-requests.md) | Legal assistant | Needs attention | UC-F15-10 |
| [S-F15-L10 Lawyer hand-offs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l10-lawyer-hand-offs.md) | Legal assistant | Needs attention | UC-F15-01, UC-F15-12 |
| [S-F15-L11 Warning triggers](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l11-warning-triggers.md) | Legal assistant | All | UC-F15-02 |
| [S-F15-L14 Corporate filings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l14-corporate-filings.md) | Legal assistant | All | UC-F15-07 |
| [S-F18-L05 Job postings](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l05-job-postings.md) | Hosted websites and domains (hosted edition) | Needs attention | UC-F18-05, UC-F18-06 |
| [S-F18-L06 Applications](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l06-applications.md) | Hosted websites and domains (hosted edition) | Needs attention | UC-F18-06, UC-F18-07 |
| [S-F23-L05 Impact results](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l05-impact-results.md) | What-if simulation and impact | All | UC-F23-11 |
| [S-F24-L02 Tool connections](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l02-tool-connections.md) | Integrations hub | All | UC-F9-40, UC-F9-41, UC-F24-23 |
| [S-F24-L06 Sync jobs](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l06-sync-jobs.md) | Integrations hub | All | UC-F24-11, UC-F24-23 |
| [S-F24-L07 Field mappings](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l07-field-mappings.md) | Integrations hub | All | UC-F24-11 |
| [S-SC03-L11 Skills](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l11-skills.md) | Services | All | UC-SC03-13 |
| [S-SC04-L11 Carer qualifications](../../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l11-carer-qualifications.md) | Home care | All | UC-SC04-13 |
| [S-SC05-L13 Operation qualifications](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l13-operation-qualifications.md) | Manufacturing | All | UC-SC05-13 |
| [S-SC07-L04 Driver documents](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l04-driver-documents.md) | Transport and logistics | All | UC-SC07-04 |
| [S-SC08-L17 Integration pathways](../../../08-sectors/sc08-non-profit/screens/00-lists/s-sc08-l17-integration-pathways.md) | Non-profit association | Needs attention | UC-SC08-22 |
| [S-SC20-L11 Grades](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l11-grades.md) | Public bodies | Needs attention | UC-SC20-13 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Home care](../../../08-sectors/sc04-home-care/screens/00-lists/README.md),
[Hosted websites and domains (hosted edition)](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/README.md),
[Integrations hub](../../../02-functional/f24-integrations-hub/screens/00-lists/README.md),
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md),
[Manufacturing](../../../08-sectors/sc05-manufacturing/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Non-profit association](../../../08-sectors/sc08-non-profit/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md),
[Public bodies](../../../08-sectors/sc20-public-bodies/screens/00-lists/README.md),
[Services](../../../08-sectors/sc03-services/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md),
[Transport and logistics](../../../08-sectors/sc07-transport/screens/00-lists/README.md),
[What-if simulation and impact](../../../02-functional/f23-what-if-simulation/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U06 | desktop | ![Workspace, U06, light](mockups/workspace-desktop-light.png) | ![Workspace, U06, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U06 | phone | ![Workspace, U06, light](mockups/workspace-phone-light.png) | ![Workspace, U06, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
