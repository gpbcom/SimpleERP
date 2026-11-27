🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🛡️ [Administrator: app shell and home](README.md) › 🧰 U07 Administrator: workspace

# 🧰 U07 Administrator: workspace

**Status:** ✅ specified

## Purpose

The views [U07 Administrator](../../../01-users/personas/u07-administrator.md) works with, embedded on their
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
| [S-F1-L01 Companies](../../../02-functional/f01-administration/screens/00-lists/s-f01-l01-companies.md) | Administration | All | UC-F1-01, UC-F1-10, UC-F1-23 |
| [S-F1-L02 Company sites](../../../02-functional/f01-administration/screens/00-lists/s-f01-l02-company-sites.md) | Administration | Needs attention | UC-F1-01, UC-F1-02, UC-F1-15 |
| [S-F1-L03 Users](../../../02-functional/f01-administration/screens/00-lists/s-f01-l03-users.md) | Administration | All | UC-F1-03, UC-F1-04, UC-F1-05, UC-F1-13 and more |
| [S-F1-L04 Invitations](../../../02-functional/f01-administration/screens/00-lists/s-f01-l04-invitations.md) | Administration | Needs attention | UC-F1-03, UC-F1-14, UC-F21-08 |
| [S-F1-L05 Former-employee accesses](../../../02-functional/f01-administration/screens/00-lists/s-f01-l05-former-employee-accesses.md) | Administration | Needs attention | UC-F1-05 |
| [S-F1-L06 Roles](../../../02-functional/f01-administration/screens/00-lists/s-f01-l06-roles.md) | Administration | All | UC-F1-06, UC-F1-15, UC-F1-18, UC-F1-20 |
| [S-F1-L07 Record rules](../../../02-functional/f01-administration/screens/00-lists/s-f01-l07-record-rules.md) | Administration | All | UC-F1-06 |
| [S-F1-L08 Agent connections](../../../02-functional/f01-administration/screens/00-lists/s-f01-l08-agent-connections.md) | Administration | All | UC-F1-07, UC-F3-06, UC-F4-08, UC-F4-14 |
| [S-F1-L09 AI feature settings](../../../02-functional/f01-administration/screens/00-lists/s-f01-l09-ai-feature-settings.md) | Administration | All | UC-F1-08 |
| [S-F1-L10 Single sign-on settings](../../../02-functional/f01-administration/screens/00-lists/s-f01-l10-single-sign-on-settings.md) | Administration | All | UC-F1-09, UC-F1-13 |
| [S-F1-L11 Company templates](../../../02-functional/f01-administration/screens/00-lists/s-f01-l11-company-templates.md) | Administration | Needs attention | UC-F1-10 |
| [S-F1-L12 Provider sessions](../../../02-functional/f01-administration/screens/00-lists/s-f01-l12-provider-sessions.md) | Administration | Open: Live | UC-F1-11 |
| [S-F1-L14 Provisioning settings](../../../02-functional/f01-administration/screens/00-lists/s-f01-l14-provisioning-settings.md) | Administration | All | UC-F1-13 |
| [S-F1-L15 Bulk invitation batches](../../../02-functional/f01-administration/screens/00-lists/s-f01-l15-bulk-invitation-batches.md) | Administration | Needs attention | UC-F1-14 |
| [S-F1-L16 Access review campaigns](../../../02-functional/f01-administration/screens/00-lists/s-f01-l16-access-review-campaigns.md) | Administration | Needs attention | UC-F1-18 |
| [S-F1-L17 Portal accounts](../../../02-functional/f01-administration/screens/00-lists/s-f01-l17-portal-accounts.md) | Administration | Needs attention | UC-F1-19, UC-F2-20 |
| [S-F1-L18 API tokens](../../../02-functional/f01-administration/screens/00-lists/s-f01-l18-api-tokens.md) | Administration | Needs attention | UC-F1-20 |
| [S-F1-L19 Security policies](../../../02-functional/f01-administration/screens/00-lists/s-f01-l19-security-policies.md) | Administration | All | UC-F1-21 |
| [S-F1-L20 SIEM destinations](../../../02-functional/f01-administration/screens/00-lists/s-f01-l20-siem-destinations.md) | Administration | All | UC-F1-22 |
| [S-F1-L21 Company closings](../../../02-functional/f01-administration/screens/00-lists/s-f01-l21-company-closings.md) | Administration | Needs attention | UC-F1-23 |
| [S-F1-L22 Record of processing activities](../../../02-functional/f01-administration/screens/00-lists/s-f01-l22-record-of-processing-activities.md) | Administration | All | UC-F1-12 |
| [S-F1-L23 User sessions](../../../02-functional/f01-administration/screens/00-lists/s-f01-l23-user-sessions.md) | Administration | Needs attention | UC-F1-24 |
| [S-F1-L24 Retention policies](../../../02-functional/f01-administration/screens/00-lists/s-f01-l24-retention-policies.md) | Administration | Needs attention | UC-F1-25 |
| [S-F1-L25 Sharing rules](../../../02-functional/f01-administration/screens/00-lists/s-f01-l25-sharing-rules.md) | Administration | Needs attention | UC-F1-26 |
| [S-F1-L26 Act-as sessions](../../../02-functional/f01-administration/screens/00-lists/s-f01-l26-act-as-sessions.md) | Administration | Needs attention | UC-F1-27, UC-F20-30 |
| [S-F2-L01 Custom fields](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l01-custom-fields.md) | No-code configuration | Needs attention | UC-F2-01, UC-F2-23, UC-F2-27 |
| [S-F2-L02 Status and transitions](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l02-status-and-transitions.md) | No-code configuration | Needs attention | UC-F2-02 |
| [S-F2-L03 Form layouts](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l03-form-layouts.md) | No-code configuration | Needs attention | UC-F2-03, UC-F2-21 |
| [S-F2-L04 List views](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l04-list-views.md) | No-code configuration | Needs attention | UC-F2-03, UC-F2-17 |
| [S-F2-L05 Record types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l05-record-types.md) | No-code configuration | Needs attention | UC-F2-04, UC-F2-18, UC-F2-20 |
| [S-F2-L06 Document templates](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l06-document-templates.md) | No-code configuration | Needs attention | UC-F2-05 |
| [S-F2-L07 Email templates](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l07-email-templates.md) | No-code configuration | Needs attention | UC-F2-06 |
| [S-F2-L08 Automation rules](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l08-automation-rules.md) | No-code configuration | Needs attention | UC-F2-07, UC-F2-24 |
| [S-F2-L09 Workflows](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l09-workflows.md) | No-code configuration | Needs attention | UC-F2-08 |
| [S-F2-L10 Configuration versions](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l10-configuration-versions.md) | No-code configuration | All | UC-F2-09, UC-F2-10, UC-F2-23, UC-F2-25 and more |
| [S-F2-L11 Configuration packs](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l11-configuration-packs.md) | No-code configuration | All | UC-F2-11, UC-F2-25 |
| [S-F2-L13 Documents](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l13-documents.md) | No-code configuration | Open: ToSort, ToValidate | UC-F2-13 |
| [S-F2-L15 Sandboxes](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l15-sandboxes.md) | No-code configuration | All | UC-F2-15, UC-F2-16 |
| [S-F2-L16 Visual views](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l16-visual-views.md) | No-code configuration | Needs attention | UC-F2-17 |
| [S-F2-L17 Bookable resource settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l17-bookable-resource-settings.md) | No-code configuration | Needs attention | UC-F2-18 |
| [S-F2-L19 Portal exposures](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l19-portal-exposures.md) | No-code configuration | Needs attention | UC-F2-20 |
| [S-F2-L20 Offline form settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l20-offline-form-settings.md) | No-code configuration | Needs attention | UC-F2-21 |
| [S-F2-L21 Test cases](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l21-test-cases.md) | No-code configuration | Open: Active | UC-F2-24 |
| [S-F2-L22 Field rules](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l22-field-rules.md) | No-code configuration | Needs attention | UC-F2-27 |
| [S-F2-L23 Translations](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l23-translations.md) | No-code configuration | Needs attention | UC-F2-28 |
| [S-F2-L24 Approval chains](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l24-approval-chains.md) | No-code configuration | Needs attention | UC-F2-29 |
| [S-F2-L25 Request types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l25-request-types.md) | No-code configuration | Needs attention | UC-F2-30, UC-F9-34 |
| [S-F2-L26 Configuration drafts](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l26-configuration-drafts.md) | No-code configuration | All | UC-F2-02, UC-F2-09, UC-F2-11, UC-F2-23 |
| [S-F2-L27 Legal mentions](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l27-legal-mentions.md) | No-code configuration | All | UC-F2-05 |
| [S-F2-L29 Workflow templates](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l29-workflow-templates.md) | No-code configuration | All | UC-F2-08 |
| [S-F2-L30 Script steps](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l30-script-steps.md) | No-code configuration | Needs attention | UC-F2-31 |
| [S-F2-L32 Scheduled triggers](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l32-scheduled-triggers.md) | No-code configuration | Needs attention | UC-F2-33 |
| [S-F2-L33 Translation entries](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l33-translation-entries.md) | No-code configuration | Needs attention | UC-F2-34 |
| [S-F2-L34 Cleaning rules](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l34-cleaning-rules.md) | No-code configuration | Needs attention | UC-F2-35 |
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Open: Private, Shared | UC-F3-01, UC-F3-08, UC-F15-01 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-01, UC-F3-02, UC-F3-04, UC-F3-15 |
| [S-F3-L03 Suggested questions](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l03-suggested-questions.md) | Assistant | Needs attention | UC-F3-02 |
| [S-F3-L04 Assistant change batches](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l04-assistant-change-batches.md) | Assistant | Open: Proposed | UC-F3-03 |
| [S-F3-L05 Company writing styles](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l05-company-writing-styles.md) | Assistant | All | UC-F3-04 |
| [S-F3-L06 Configuration requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l06-configuration-requests.md) | Assistant | Needs attention | UC-F3-05 |
| [S-F3-L07 Personal connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l07-personal-connections.md) | Assistant | Needs attention | UC-F3-06 |
| [S-F3-L08 Outside calls](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l08-outside-calls.md) | Assistant | Needs attention | UC-F3-06 |
| [S-F3-L09 Knowledge items](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l09-knowledge-items.md) | Assistant | Needs attention | UC-F3-07 |
| [S-F3-L10 Knowledge folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l10-knowledge-folders.md) | Assistant | All | UC-F3-07 |
| [S-F3-L11 Knowledge proposals](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l11-knowledge-proposals.md) | Assistant | Needs attention | UC-F3-07, UC-F3-19 |
| [S-F3-L12 Conversation folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l12-conversation-folders.md) | Assistant | All | UC-F3-08 |
| [S-F3-L14 Answer feedbacks](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l14-answer-feedbacks.md) | Assistant | All | UC-F3-01 |
| [S-F3-L15 Agents](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l15-agents.md) | Assistant | Open: Paused | UC-F3-10, UC-F3-11 |
| [S-F3-L16 AI fields](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l16-ai-fields.md) | Assistant | All | UC-F3-12 |
| [S-F3-L17 Evaluation questions](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l17-evaluation-questions.md) | Assistant | Open: Active | UC-F3-14 |
| [S-F3-L18 Evaluation runs](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l18-evaluation-runs.md) | Assistant | Needs attention | UC-F3-14 |
| [S-F3-L19 Injection alerts](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l19-injection-alerts.md) | Assistant | All | UC-F3-15 |
| [S-F3-L21 Unanswered topics](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l21-unanswered-topics.md) | Assistant | Needs attention | UC-F3-19 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | UC-F3-03, UC-F3-04, UC-F3-06 |
| [S-F3-L24 Agent templates](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l24-agent-templates.md) | Assistant | Needs attention | UC-F3-21 |
| [S-F4-L02 Transcripts](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l02-transcripts.md) | Meetings | All | UC-F4-23 |
| [S-F4-L05 Calendar syncs](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l05-calendar-syncs.md) | Meetings | All | UC-F4-08 |
| [S-F4-L12 Call routes](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l12-call-routes.md) | Meetings | All | UC-F4-19 |
| [S-F4-L14 Speaker requests](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l14-speaker-requests.md) | Meetings | Open: Received, Refused | UC-F4-23 |
| [S-F4-L15 Accuracy measures](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l15-accuracy-measures.md) | Meetings | All | UC-F4-24 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Needs attention | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L25 Meeting recording settings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l25-meeting-recording-settings.md) | Meetings | All | UC-F4-08 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | All | flow charts (VR-3) |
| [S-F5-L01 Posts](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l01-posts.md) | Social media and marketing | Needs attention | UC-F5-03, UC-F5-07 |
| [S-F5-L02 Social accounts](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l02-social-accounts.md) | Social media and marketing | All | UC-F5-07 |
| [S-F5-L03 Automatic post rules](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l03-automatic-post-rules.md) | Social media and marketing | All | UC-F5-03 |
| [S-F5-L05 Email or SMS campaigns](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l05-email-or-sms-campaigns.md) | Social media and marketing | Needs attention | UC-F5-16 |
| [S-F5-L10 Consent and suppression records](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l10-consent-and-suppression-records.md) | Social media and marketing | Open: Given, Suppressed | UC-F5-16 |
| [S-F5-L19 Trigger events](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l19-trigger-events.md) | Social media and marketing | All | UC-F5-03 |
| [S-F7-L07 Locations](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l07-locations.md) | Purchasing and stock | All | UC-F7-13 |
| [S-F7-L08 Routes](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l08-routes.md) | Purchasing and stock | All | UC-F7-13 |
| [S-F7-L09 Reordering rules](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l09-reordering-rules.md) | Purchasing and stock | All | UC-F7-13 |
| [S-F8-L01 Accounts](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l01-accounts.md) | Accounting | All | UC-F8-01 |
| [S-F8-L02 Journals](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l02-journals.md) | Accounting | All | UC-F8-01 |
| [S-F8-L10 Fiscal periods](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l10-fiscal-periods.md) | Accounting | All | UC-F8-01 |
| [S-F8-L27 FEC files](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l27-fec-files.md) | Accounting | All | UC-F1-23, UC-F8-01 |
| [S-F8-L29 Entry annotations](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l29-entry-annotations.md) | Accounting | All | UC-F8-01 |
| [S-F8-L33 Tax rates](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l33-tax-rates.md) | Accounting | All | UC-F8-01 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | UC-F3-08 |
| [S-F9-L06 Job positions](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l06-job-positions.md) | HR and projects | All | UC-F9-40 |
| [S-F9-L13 Company vehicles](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l13-company-vehicles.md) | HR and projects | All | UC-F9-12 |
| [S-F9-L26 Rounds](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l26-rounds.md) | HR and projects | Needs attention | UC-F9-34 |
| [S-F9-L28 Assignment proposals](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l28-assignment-proposals.md) | HR and projects | Needs attention | UC-F9-34 |
| [S-F9-L30 Qualification types](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l30-qualification-types.md) | HR and projects | Open: Active | UC-F2-30 |
| [S-F9-L33 Automatic scheduling settings](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l33-automatic-scheduling-settings.md) | HR and projects | All | UC-F9-34 |
| [S-F9-L44 Sourcing searches](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l44-sourcing-searches.md) | HR and projects | Needs attention | UC-F9-40, UC-F9-41 |
| [S-F9-L45 Prospects](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l45-prospects.md) | HR and projects | Needs attention | UC-F9-40, UC-F9-41 |
| [S-F9-L46 Outreach sequences](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l46-outreach-sequences.md) | HR and projects | Needs attention | UC-F9-41 |
| [S-F9-L47 Outreach messages](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l47-outreach-messages.md) | HR and projects | Needs attention | UC-F9-41 |
| [S-F10-L01 Point of sales](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l01-point-of-sales.md) | Point of sale (plugin) | All | UC-F10-15 |
| [S-F10-L11 Floor and tables](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l11-floor-and-tables.md) | Point of sale (plugin) | All | UC-F10-15 |
| [S-F10-L14 Point of sale devices](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l14-point-of-sale-devices.md) | Point of sale (plugin) | All | UC-F10-15 |
| [S-F11-L01 Websites](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l01-websites.md) | Online shop (plugin) | All | UC-F11-01, UC-F11-16 |
| [S-F11-L02 Web pages](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l02-web-pages.md) | Online shop (plugin) | Needs attention | UC-F11-01, UC-F11-16 |
| [S-F11-L06 Payment providers](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l06-payment-providers.md) | Online shop (plugin) | All | D519, VC-15 |
| [S-F11-L13 Channel listings](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l13-channel-listings.md) | Online shop (plugin) | All | UC-F11-18 |
| [S-F11-L14 Legal pages](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l14-legal-pages.md) | Online shop (plugin) | All | UC-F11-19 |
| [S-F12-L02 Work centres](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l02-work-centres.md) | Manufacturing (plugin) | All | UC-F12-14 |
| [S-F12-L13 Machine signals](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l13-machine-signals.md) | Manufacturing (plugin) | All | UC-F12-14 |
| [S-F12-L14 Product compliance files](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l14-product-compliance-files.md) | Manufacturing (plugin) | All | UC-F12-16 |
| [S-F13-L01 Payroll establishments](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l01-payroll-establishments.md) | Payroll (plugin) | All | UC-F13-01 |
| [S-F13-L16 Rate sets](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l16-rate-sets.md) | Payroll (plugin) | All | UC-F13-19 |
| [S-F13-L23 Agreement families](../../../02-functional/f13-payroll/screens/00-lists/s-f13-l23-agreement-families.md) | Payroll (plugin) | All | UC-F13-01, UC-F13-19 |
| [S-F14-L01 Store listings](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l01-store-listings.md) | Plugin store | Open: New, Complete, Refused | UC-F14-01, UC-F14-02, UC-F14-20, UC-F14-22 and more |
| [S-F14-L02 Plugin installations](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l02-plugin-installations.md) | Plugin store | All | UC-F14-02, UC-F14-03, UC-F14-04, UC-F14-24 and more |
| [S-F14-L03 Plugin versions](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l03-plugin-versions.md) | Plugin store | All | UC-F14-03 |
| [S-F14-L04 Plugin price plans](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l04-plugin-price-plans.md) | Plugin store | Open: Published | UC-F14-05, UC-F14-27 |
| [S-F14-L05 Plugin licences](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l05-plugin-licences.md) | Plugin store | All | UC-F14-05, UC-F14-06 |
| [S-F14-L06 Plugin reviews](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l06-plugin-reviews.md) | Plugin store | All | UC-F14-07 |
| [S-F14-L15 End-of-life notices](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l15-end-of-life-notices.md) | Plugin store | Open: Announced, TakenOver | UC-F14-22 |
| [S-F14-L16 Maintainer transfers](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l16-maintainer-transfers.md) | Plugin store | Open: Asked, Approved, Refused | UC-F14-23 |
| [S-F14-L17 Rollouts](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l17-rollouts.md) | Plugin store | Open: Beta, Running, Paused | UC-F14-24 |
| [S-F14-L19 Support terms](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l19-support-terms.md) | Plugin store | All | UC-F14-05, UC-F14-27 |
| [S-F14-L20 Rollback points](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l20-rollback-points.md) | Plugin store | Needs attention | UC-F14-03, UC-F14-28 |
| [S-F14-L21 Plugin security reviews](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l21-plugin-security-reviews.md) | Plugin store | All | UC-F14-23 |
| [S-F14-L23 Trials](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l23-trials.md) | Plugin store | Needs attention | UC-F14-30 |
| [S-F15-L01 Law packs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l01-law-packs.md) | Legal assistant | All | UC-F15-01, UC-F15-04, UC-F15-05 |
| [S-F15-L02 Legal warnings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l02-legal-warnings.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L03 Document checks](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l03-document-checks.md) | Legal assistant | All | UC-F15-01 |
| [S-F15-L04 Standard register entries](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l04-standard-register-entries.md) | Legal assistant | Needs attention | UC-F15-01, UC-F15-06 |
| [S-F15-L08 Data-subject requests](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l08-data-subject-requests.md) | Legal assistant | Needs attention | UC-F15-10 |
| [S-F15-L09 AI uses](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l09-ai-uses.md) | Legal assistant | All | UC-F15-11 |
| [S-F15-L10 Lawyer hand-offs](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l10-lawyer-hand-offs.md) | Legal assistant | Needs attention | UC-F15-01 |
| [S-F15-L11 Warning triggers](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l11-warning-triggers.md) | Legal assistant | All | UC-F15-04 |
| [S-F15-L12 Legal sources](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l12-legal-sources.md) | Legal assistant | All | UC-F15-05 |
| [S-F15-L13 Data protection impact assessments](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l13-data-protection-impact-assessments.md) | Legal assistant | All | UC-F15-11 |
| [S-F16-L04 Helpdesk connections](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l04-helpdesk-connections.md) | Customer support agents | All | UC-F16-06 |
| [S-F16-L12 Work requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l12-work-requests.md) | Customer support agents | Needs attention | UC-F9-34 |
| [S-F17-L09 Data providers](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l09-data-providers.md) | Competitive analysis | All | UC-F17-10, UC-F17-22 |
| [S-F17-L10 Analysis](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l10-analysis.md) | Competitive analysis | All | UC-F17-19 |
| [S-F17-L15 Collection rules](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l15-collection-rules.md) | Competitive analysis | All | UC-F17-18 |
| [S-F17-L19 Data cost lines](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l19-data-cost-lines.md) | Competitive analysis | All | UC-F17-10, UC-F17-22 |
| [S-F18-L07 Domains](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l07-domains.md) | Hosted websites and domains (hosted edition) | All | UC-F18-09, UC-F18-10, UC-F18-20 |
| [S-F18-L08 DNS records](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l08-dns-records.md) | Hosted websites and domains (hosted edition) | All | UC-F18-10, UC-F18-11, UC-F18-12 |
| [S-F18-L09 TLS certificates](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l09-tls-certificates.md) | Hosted websites and domains (hosted edition) | All | UC-F18-11, UC-F18-20 |
| [S-F18-L10 Publication check reports](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l10-publication-check-reports.md) | Hosted websites and domains (hosted edition) | All | UC-F18-30 |
| [S-F18-L12 Uptime events](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l12-uptime-events.md) | Hosted websites and domains (hosted edition) | All | UC-F18-20 |
| [S-F18-L14 Redirects](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l14-redirects.md) | Hosted websites and domains (hosted edition) | All | UC-F18-10, UC-F18-22 |
| [S-F18-L15 Mailboxes](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l15-mailboxes.md) | Hosted websites and domains (hosted edition) | Open: Active, Forwarding | UC-F18-23 |
| [S-F18-L22 Accessibility statements](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l22-accessibility-statements.md) | Hosted websites and domains (hosted edition) | Needs attention | UC-F18-30 |
| [S-F19-L01 Feature requests](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l01-feature-requests.md) | Feature factory (hosted edition) | All | UC-F19-01 |
| [S-F19-L02 Feature specifications](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l02-feature-specifications.md) | Feature factory (hosted edition) | All | UC-F19-28 |
| [S-F19-L03 Feature subscriptions](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l03-feature-subscriptions.md) | Feature factory (hosted edition) | All | UC-F19-08 |
| [S-F19-L04 Generated plugin versions](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l04-generated-plugin-versions.md) | Feature factory (hosted edition) | All | UC-F19-08, UC-F19-10 |
| [S-F19-L06 Try-out copies](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l06-try-out-copies.md) | Feature factory (hosted edition) | All | UC-F19-07 |
| [S-F19-L09 Hosted invoices](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l09-hosted-invoices.md) | Feature factory (hosted edition) | All | UC-F19-28 |
| [S-F19-L11 Delivery commitments](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l11-delivery-commitments.md) | Feature factory (hosted edition) | Needs attention | UC-F19-28 |
| [S-F19-L12 Feature refunds](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l12-feature-refunds.md) | Feature factory (hosted edition) | All | UC-F19-07, UC-F19-10 |
| [S-F19-L14 Security and privacy reviews](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l14-security-and-privacy-reviews.md) | Feature factory (hosted edition) | Needs attention | UC-F19-24 |
| [S-F19-L16 Feature defects](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l16-feature-defects.md) | Feature factory (hosted edition) | All | UC-F19-10 |
| [S-F19-L17 Catalogue changes](../../../02-functional/f19-feature-factory/screens/00-lists/s-f19-l17-catalogue-changes.md) | Feature factory (hosted edition) | Needs attention | UC-F19-28 |
| [S-F20-L01 Support requests](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l01-support-requests.md) | Hosted support assistant (hosted edition) | All | UC-F20-01, UC-F20-02, UC-F20-09, UC-F20-20 |
| [S-F20-L02 Messages](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l02-messages.md) | Hosted support assistant (hosted edition) | All | UC-F20-02, UC-F20-09, UC-F20-12, UC-F20-05 and more |
| [S-F20-L03 Screenshots](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l03-screenshots.md) | Hosted support assistant (hosted edition) | All | UC-F20-03, UC-F20-20 |
| [S-F20-L04 Diagnosis](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l04-diagnosis.md) | Hosted support assistant (hosted edition) | All | UC-F20-05, UC-F20-14 |
| [S-F20-L05 Cluster readings](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l05-cluster-readings.md) | Hosted support assistant (hosted edition) | All | UC-F20-14 |
| [S-F20-L06 Fix proposals](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l06-fix-proposals.md) | Hosted support assistant (hosted edition) | All | UC-F20-13 |
| [S-F20-L08 Restores](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l08-restores.md) | Hosted support assistant (hosted edition) | All | UC-F20-13 |
| [S-F20-L10 Ratings](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l10-ratings.md) | Hosted support assistant (hosted edition) | All | UC-F20-16 |
| [S-F20-L13 Maintenance notices](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l13-maintenance-notices.md) | Hosted support assistant (hosted edition) | Open: Planned, Running, Overrun | UC-F20-21 |
| [S-F20-L14 Upgrade release notes](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l14-upgrade-release-notes.md) | Hosted support assistant (hosted edition) | Needs attention | UC-F20-22 |
| [S-F20-L18 Support conversation exports](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l18-support-conversation-exports.md) | Hosted support assistant (hosted edition) | All | UC-F20-20 |
| [S-F20-L19 Engineer calls](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l19-engineer-calls.md) | Hosted support assistant (hosted edition) | Needs attention | UC-F20-29, UC-F20-30 |
| [S-F20-L20 Access grants](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l20-access-grants.md) | Hosted support assistant (hosted edition) | Needs attention | UC-F20-30 |
| [S-F20-L21 Health reports](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/s-f20-l21-health-reports.md) | Hosted support assistant (hosted edition) | Needs attention | UC-F20-31 |
| [S-F21-L01 Onboarding progresses](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l01-onboarding-progresses.md) | Onboarding and module activation | All | UC-F21-11 |
| [S-F21-L04 Module activations](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l04-module-activations.md) | Onboarding and module activation | All | UC-F21-04, UC-F21-05, UC-F21-06, UC-F21-11 |
| [S-F21-L05 Module dependencies](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l05-module-dependencies.md) | Onboarding and module activation | All | UC-F21-05 |
| [S-F21-L07 Import jobs](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l07-import-jobs.md) | Onboarding and module activation | All | UC-F21-09, UC-F21-21 |
| [S-F21-L14 Migration sources](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l14-migration-sources.md) | Onboarding and module activation | Needs attention | UC-F21-09, UC-F21-21 |
| [S-F21-L17 Migration guides](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l17-migration-guides.md) | Onboarding and module activation | All | UC-F21-21 |
| [S-F21-L18 Module guides](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l18-module-guides.md) | Onboarding and module activation | All | UC-F21-11 |
| [S-F21-L20 Cutover plans](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/s-f21-l20-cutover-plans.md) | Onboarding and module activation | Needs attention | UC-F21-27 |
| [S-F22-L02 Metered call records](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l02-metered-call-records.md) | Unified platform cost management | All | UC-F22-22, UC-F22-11, UC-F22-18 |
| [S-F22-L03 Provider price lists](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l03-provider-price-lists.md) | Unified platform cost management | All | UC-F22-04, UC-F22-21 |
| [S-F22-L04 Paid providers](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l04-paid-providers.md) | Unified platform cost management | Open: New | UC-F22-04, UC-F22-05 |
| [S-F22-L05 Hosted quotas](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l05-hosted-quotas.md) | Unified platform cost management | All | UC-F22-05 |
| [S-F22-L06 Cost budgets](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l06-cost-budgets.md) | Unified platform cost management | All | UC-F22-07, UC-F22-08 |
| [S-F22-L07 Cost alerts](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l07-cost-alerts.md) | Unified platform cost management | All | UC-F22-07, UC-F22-18 |
| [S-F22-L08 Budget approvals](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l08-budget-approvals.md) | Unified platform cost management | All | UC-F22-08 |
| [S-F22-L10 Run estimates](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l10-run-estimates.md) | Unified platform cost management | Open: Running | UC-F22-10, UC-F22-11 |
| [S-F22-L14 Exchange rates](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l14-exchange-rates.md) | Unified platform cost management | All | UC-F22-04, UC-F22-21 |
| [S-F22-L15 Compute machines](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l15-compute-machines.md) | Unified platform cost management | Open: InService | UC-F22-22 |
| [S-F22-L16 Savings recommendations](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l16-savings-recommendations.md) | Unified platform cost management | All | UC-F22-23 |
| [S-F22-L19 Credit packs](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l19-credit-packs.md) | Unified platform cost management | Needs attention | UC-F22-27 |
| [S-F22-L20 SaaS subscriptions](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l20-saas-subscriptions.md) | Unified platform cost management | Needs attention | UC-F22-28 |
| [S-F22-L21 Routing rules](../../../02-functional/f22-unified-cost-management/screens/00-lists/s-f22-l21-routing-rules.md) | Unified platform cost management | Needs attention | UC-F22-30 |
| [S-F24-L01 Connectors](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l01-connectors.md) | Integrations hub | All | UC-F24-01 |
| [S-F24-L02 Tool connections](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l02-tool-connections.md) | Integrations hub | All | UC-F9-40, UC-F9-41, UC-F21-10, UC-F24-02 and more |
| [S-F24-L03 Suite components](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l03-suite-components.md) | Integrations hub | All | UC-F24-03, UC-F24-09 |
| [S-F24-L05 Calendar links](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l05-calendar-links.md) | Integrations hub | All | UC-F24-29 |
| [S-F24-L06 Sync jobs](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l06-sync-jobs.md) | Integrations hub | All | UC-F24-13, UC-F24-23 |
| [S-F24-L07 Field mappings](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l07-field-mappings.md) | Integrations hub | All | UC-F24-12 |
| [S-F24-L08 Sync log entries](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l08-sync-log-entries.md) | Integrations hub | All | UC-F24-13, UC-F24-15, UC-F24-17 |
| [S-F24-L09 Connector actions](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l09-connector-actions.md) | Integrations hub | All | UC-F24-20 |
| [S-F24-L10 Connector incidents](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l10-connector-incidents.md) | Integrations hub | Needs attention | UC-F24-15, UC-F24-16 |
| [S-F24-L11 Connector categories](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l11-connector-categories.md) | Integrations hub | Open: Active | UC-F24-01, UC-F24-21 |
| [S-F24-L12 Integration icons](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l12-integration-icons.md) | Integrations hub | Open: Proposed, Approved, Replaced | UC-F24-01, UC-F24-02, UC-F24-21 |
| [S-F24-L13 Webhook subscriptions](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l13-webhook-subscriptions.md) | Integrations hub | Open: Active, Paused | UC-F24-20, UC-F24-22 |
| [S-F24-L14 E-invoicing registrations](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l14-e-invoicing-registrations.md) | Integrations hub | Needs attention | UC-F24-24 |
| [S-F24-L17 Connector drafts](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l17-connector-drafts.md) | Integrations hub | Needs attention | UC-F24-28 |
| [S-F24-L18 Export pipelines](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l18-export-pipelines.md) | Integrations hub | Needs attention | UC-F24-30 |
| [S-F25-L01 Bug or feature requests](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l01-bug-or-feature-requests.md) | DevOps agents (hosted edition) | All | UC-F25-01, UC-F25-02, UC-F25-14, UC-F25-20 |
| [S-F25-L03 USER tickets](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l03-user-tickets.md) | DevOps agents (hosted edition) | Needs attention | UC-F25-24 |
| [S-F25-L09 Request status](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l09-request-status.md) | DevOps agents (hosted edition) | All | UC-F25-14, UC-F25-20 |
| [S-F25-L11 Triages](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l11-triages.md) | DevOps agents (hosted edition) | Needs attention | UC-F25-14 |
| [S-F25-L12 Vulnerability cases](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l12-vulnerability-cases.md) | DevOps agents (hosted edition) | Open: Reported, Confirmed, Fixed | UC-F25-01 |
| [S-F25-L14 Votes](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l14-votes.md) | DevOps agents (hosted edition) | Open: Counted | UC-F25-20, UC-F25-24 |
| [S-F25-L17 Beta enrolments](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l17-beta-enrolments.md) | DevOps agents (hosted edition) | Needs attention | UC-F25-26 |
| [S-F25-L18 Report credits](../../../02-functional/f25-devops-agents/screens/00-lists/s-f25-l18-report-credits.md) | DevOps agents (hosted edition) | Needs attention | UC-F25-27 |
| [S-T01-L01 Companies](../../../03-technical/t01-companies-and-data-isolation/screens/00-lists/s-t01-l01-companies.md) | Companies and data isolation | All | admin list (D494) |
| [S-T01-L02 Company stores](../../../03-technical/t01-companies-and-data-isolation/screens/00-lists/s-t01-l02-company-stores.md) | Companies and data isolation | All | admin list (D494) |
| [S-T01-L03 Provider sessions](../../../03-technical/t01-companies-and-data-isolation/screens/00-lists/s-t01-l03-provider-sessions.md) | Companies and data isolation | All | admin list (D494) |
| [S-T01-L04 Copy or overlays](../../../03-technical/t01-companies-and-data-isolation/screens/00-lists/s-t01-l04-copy-or-overlays.md) | Companies and data isolation | All | admin list (D494) |
| [S-T02-L01 User accounts](../../../03-technical/t02-identity-and-access/screens/00-lists/s-t02-l01-user-accounts.md) | Identity and access engine | All | admin list (D494) |
| [S-T02-L02 Role and policies](../../../03-technical/t02-identity-and-access/screens/00-lists/s-t02-l02-role-and-policies.md) | Identity and access engine | All | admin list (D494) |
| [S-T02-L03 Service accounts](../../../03-technical/t02-identity-and-access/screens/00-lists/s-t02-l03-service-accounts.md) | Identity and access engine | All | admin list (D494) |
| [S-T02-L04 Federated identity providers](../../../03-technical/t02-identity-and-access/screens/00-lists/s-t02-l04-federated-identity-providers.md) | Identity and access engine | All | admin list (D494) |
| [S-T03-L01 Audit entries](../../../03-technical/t03-audit-trail/screens/00-lists/s-t03-l01-audit-entries.md) | Audit trail | All | admin list (D494) |
| [S-T03-L02 AI action details](../../../03-technical/t03-audit-trail/screens/00-lists/s-t03-l02-ai-action-details.md) | Audit trail | All | admin list (D494) |
| [S-T03-L03 Chain checkpoints](../../../03-technical/t03-audit-trail/screens/00-lists/s-t03-l03-chain-checkpoints.md) | Audit trail | All | admin list (D494) |
| [S-T04-L01 Modules](../../../03-technical/t04-plugin-runtime/screens/00-lists/s-t04-l01-modules.md) | Plugin runtime | All | admin list (D494) |
| [S-T04-L02 Plugin packages](../../../03-technical/t04-plugin-runtime/screens/00-lists/s-t04-l02-plugin-packages.md) | Plugin runtime | All | admin list (D494) |
| [S-T04-L03 Plugin installations](../../../03-technical/t04-plugin-runtime/screens/00-lists/s-t04-l03-plugin-installations.md) | Plugin runtime | All | admin list (D494) |
| [S-T04-L04 Plugin limits](../../../03-technical/t04-plugin-runtime/screens/00-lists/s-t04-l04-plugin-limits.md) | Plugin runtime | All | admin list (D494) |
| [S-T05-L01 API clients](../../../03-technical/t05-api-and-webhooks/screens/00-lists/s-t05-l01-api-clients.md) | API and webhooks | All | admin list (D494) |
| [S-T05-L02 Webhook subscriptions](../../../03-technical/t05-api-and-webhooks/screens/00-lists/s-t05-l02-webhook-subscriptions.md) | API and webhooks | All | admin list (D494) |
| [S-T05-L03 Webhook deliveries](../../../03-technical/t05-api-and-webhooks/screens/00-lists/s-t05-l03-webhook-deliveries.md) | API and webhooks | All | admin list (D494) |
| [S-T05-L04 Idempotency keys](../../../03-technical/t05-api-and-webhooks/screens/00-lists/s-t05-l04-idempotency-keys.md) | API and webhooks | All | admin list (D494) |
| [S-T06-L01 Tools](../../../03-technical/t06-mcp-and-a2a-gateway/screens/00-lists/s-t06-l01-tools.md) | MCP and A2A gateway | All | admin list (D494) |
| [S-T06-L02 Agent cards](../../../03-technical/t06-mcp-and-a2a-gateway/screens/00-lists/s-t06-l02-agent-cards.md) | MCP and A2A gateway | All | admin list (D494) |
| [S-T06-L03 Outside connections](../../../03-technical/t06-mcp-and-a2a-gateway/screens/00-lists/s-t06-l03-outside-connections.md) | MCP and A2A gateway | All | admin list (D494) |
| [S-T06-L04 Tool call records](../../../03-technical/t06-mcp-and-a2a-gateway/screens/00-lists/s-t06-l04-tool-call-records.md) | MCP and A2A gateway | All | admin list (D494) |
| [S-T07-L01 Models](../../../03-technical/t07-ai-providers-and-models/screens/00-lists/s-t07-l01-models.md) | AI providers and models | All | admin list (D494) |
| [S-T07-L02 AI feature settings](../../../03-technical/t07-ai-providers-and-models/screens/00-lists/s-t07-l02-ai-feature-settings.md) | AI providers and models | All | admin list (D494) |
| [S-T07-L03 Prompt template versions](../../../03-technical/t07-ai-providers-and-models/screens/00-lists/s-t07-l03-prompt-template-versions.md) | AI providers and models | All | admin list (D494) |
| [S-T07-L04 Evaluation results](../../../03-technical/t07-ai-providers-and-models/screens/00-lists/s-t07-l04-evaluation-results.md) | AI providers and models | All | admin list (D494) |
| [S-T08-L01 Collections](../../../03-technical/t08-rag-platform/screens/00-lists/s-t08-l01-collections.md) | RAG platform (Milvus) | All | admin list (D494) |
| [S-T08-L02 Chunks](../../../03-technical/t08-rag-platform/screens/00-lists/s-t08-l02-chunks.md) | RAG platform (Milvus) | All | admin list (D494) |
| [S-T08-L03 Index jobs](../../../03-technical/t08-rag-platform/screens/00-lists/s-t08-l03-index-jobs.md) | RAG platform (Milvus) | All | admin list (D494) |
| [S-T09-L01 Server installations](../../../03-technical/t09-install-backups-and-updates/screens/00-lists/s-t09-l01-server-installations.md) | Install, backups and updates | All | admin list (D494) |
| [S-T09-L02 Restore points](../../../03-technical/t09-install-backups-and-updates/screens/00-lists/s-t09-l02-restore-points.md) | Install, backups and updates | All | admin list (D494) |
| [S-T09-L03 Upgrade runs](../../../03-technical/t09-install-backups-and-updates/screens/00-lists/s-t09-l03-upgrade-runs.md) | Install, backups and updates | All | admin list (D494) |
| [S-T09-L04 Namespace access grants](../../../03-technical/t09-install-backups-and-updates/screens/00-lists/s-t09-l04-namespace-access-grants.md) | Install, backups and updates | All | admin list (D494) |
| [S-T10-L01 Translation strings](../../../03-technical/t10-translations-and-notifications/screens/00-lists/s-t10-l01-translation-strings.md) | Translations and notifications | All | admin list (D494) |
| [S-T10-L02 Notifications](../../../03-technical/t10-translations-and-notifications/screens/00-lists/s-t10-l02-notifications.md) | Translations and notifications | All | admin list (D494) |
| [S-T10-L03 User preferences](../../../03-technical/t10-translations-and-notifications/screens/00-lists/s-t10-l03-user-preferences.md) | Translations and notifications | All | admin list (D494) |
| [S-T11-L01 Country packs](../../../03-technical/t11-legal-corpora/screens/00-lists/s-t11-l01-country-packs.md) | Legal corpora | All | admin list (D494) |
| [S-T11-L02 Country rules](../../../03-technical/t11-legal-corpora/screens/00-lists/s-t11-l02-country-rules.md) | Legal corpora | All | admin list (D494) |
| [S-T11-L03 Article versions](../../../03-technical/t11-legal-corpora/screens/00-lists/s-t11-l03-article-versions.md) | Legal corpora | All | admin list (D494) |
| [S-T11-L04 Rule flags](../../../03-technical/t11-legal-corpora/screens/00-lists/s-t11-l04-rule-flags.md) | Legal corpora | Needs attention | admin list (D494) |
| [S-T12-L01 Connectors](../../../03-technical/t12-connectors-and-scrapers/screens/00-lists/s-t12-l01-connectors.md) | Connectors and scrapers | All | admin list (D494) |
| [S-T12-L02 Credentials](../../../03-technical/t12-connectors-and-scrapers/screens/00-lists/s-t12-l02-credentials.md) | Connectors and scrapers | All | admin list (D494) |
| [S-T12-L03 Generated connectors](../../../03-technical/t12-connectors-and-scrapers/screens/00-lists/s-t12-l03-generated-connectors.md) | Connectors and scrapers | All | admin list (D494) |
| [S-T12-L04 Connector runs](../../../03-technical/t12-connectors-and-scrapers/screens/00-lists/s-t12-l04-connector-runs.md) | Connectors and scrapers | All | admin list (D494) |
| [S-T12-L05 Tool connections](../../../03-technical/t12-connectors-and-scrapers/screens/00-lists/s-t12-l05-tool-connections.md) | Connectors and scrapers | All | admin list (D494) |
| [S-T12-L06 Sync states](../../../03-technical/t12-connectors-and-scrapers/screens/00-lists/s-t12-l06-sync-states.md) | Connectors and scrapers | All | admin list (D494) |
| [S-T12-L07 Generated scraper versions](../../../03-technical/t12-connectors-and-scrapers/screens/00-lists/s-t12-l07-generated-scraper-versions.md) | Connectors and scrapers | All | admin list (D494) |
| [S-T13-L04 Geodata sources](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l04-geodata-sources.md) | Maps and geodata | Needs attention | admin list (D494) |
| [S-SC05-L01 Production setups](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l01-production-setups.md) | Manufacturing | All | UC-SC05-01 |
| [S-SC09-L13 Certified modules](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l13-certified-modules.md) | Health practices | Needs attention | UC-SC09-19 |
| [S-SC14-L10 Processor agreements](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l10-processor-agreements.md) | IT and software | All | UC-SC14-11 |
| [S-SC14-L12 Security reports](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l12-security-reports.md) | IT and software | All | UC-SC14-13 |
| [S-SC14-L13 Data exports](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l13-data-exports.md) | IT and software | All | UC-SC14-14 |

## Navigation

Each view also sits in its capability's menu (D495):
[AI providers and models](../../../03-technical/t07-ai-providers-and-models/screens/00-lists/README.md),
[API and webhooks](../../../03-technical/t05-api-and-webhooks/screens/00-lists/README.md),
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Audit trail](../../../03-technical/t03-audit-trail/screens/00-lists/README.md),
[Companies and data isolation](../../../03-technical/t01-companies-and-data-isolation/screens/00-lists/README.md),
[Competitive analysis](../../../02-functional/f17-competitive-analysis/screens/00-lists/README.md),
[Connectors and scrapers](../../../03-technical/t12-connectors-and-scrapers/screens/00-lists/README.md),
[Customer support agents](../../../02-functional/f16-customer-support-agents/screens/00-lists/README.md),
[DevOps agents (hosted edition)](../../../02-functional/f25-devops-agents/screens/00-lists/README.md),
[Feature factory (hosted edition)](../../../02-functional/f19-feature-factory/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Health practices](../../../08-sectors/sc09-health-practices/screens/00-lists/README.md),
[Hosted support assistant (hosted edition)](../../../02-functional/f20-hosted-support-assistant/screens/00-lists/README.md),
[Hosted websites and domains (hosted edition)](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/README.md),
[IT and software](../../../08-sectors/sc14-it-and-software/screens/00-lists/README.md),
[Identity and access engine](../../../03-technical/t02-identity-and-access/screens/00-lists/README.md),
[Install, backups and updates](../../../03-technical/t09-install-backups-and-updates/screens/00-lists/README.md),
[Integrations hub](../../../02-functional/f24-integrations-hub/screens/00-lists/README.md),
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md),
[Legal corpora](../../../03-technical/t11-legal-corpora/screens/00-lists/README.md),
[MCP and A2A gateway](../../../03-technical/t06-mcp-and-a2a-gateway/screens/00-lists/README.md),
[Manufacturing](../../../08-sectors/sc05-manufacturing/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Maps and geodata](../../../03-technical/t13-maps-and-geodata/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Onboarding and module activation](../../../02-functional/f21-onboarding-and-modules/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md),
[Payroll (plugin)](../../../02-functional/f13-payroll/screens/00-lists/README.md),
[Plugin runtime](../../../03-technical/t04-plugin-runtime/screens/00-lists/README.md),
[Plugin store](../../../02-functional/f14-plugin-store/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[RAG platform (Milvus)](../../../03-technical/t08-rag-platform/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md),
[Translations and notifications](../../../03-technical/t10-translations-and-notifications/screens/00-lists/README.md),
[Unified platform cost management](../../../02-functional/f22-unified-cost-management/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U07 | desktop | ![Workspace, U07, light](mockups/workspace-desktop-light.png) | ![Workspace, U07, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U07 | phone | ![Workspace, U07, light](mockups/workspace-phone-light.png) | ![Workspace, U07, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
