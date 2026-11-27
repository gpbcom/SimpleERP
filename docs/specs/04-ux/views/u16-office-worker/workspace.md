🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
💻 [Office worker: app shell and home](README.md) › 🧰 U16 Office worker: workspace

# 🧰 U16 Office worker: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U16 Office worker](../../../01-users/personas/u16-office-worker.md) works with, embedded on their
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
| [S-F2-L01 Custom fields](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l01-custom-fields.md) | No-code configuration | Open: Draft, Live | UC-F2-01 |
| [S-F2-L06 Document templates](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l06-document-templates.md) | No-code configuration | All | UC-F2-05 |
| [S-F2-L07 Email templates](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l07-email-templates.md) | No-code configuration | All | UC-F2-06 |
| [S-F2-L13 Documents](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l13-documents.md) | No-code configuration | Open: ToSort, ToValidate | UC-F2-13 |
| [S-F2-L14 Signature requests](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l14-signature-requests.md) | No-code configuration | Open: Sent, Signed, Refused | UC-F2-14 |
| [S-F2-L25 Request types](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l25-request-types.md) | No-code configuration | Open: Draft, Published | UC-F16-16 |
| [S-F2-L27 Legal mentions](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l27-legal-mentions.md) | No-code configuration | All | UC-F2-05 |
| [S-F2-L31 Bulk operations](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l31-bulk-operations.md) | No-code configuration | Mine: run by | UC-F2-32 |
| [S-F2-L34 Cleaning rules](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l34-cleaning-rules.md) | No-code configuration | Mine: none, the rules belong to the company | UC-F2-35 |
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Mine: owner | UC-F3-01, UC-F3-08 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-01, UC-F3-02, UC-F3-04 |
| [S-F3-L04 Assistant change batches](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l04-assistant-change-batches.md) | Assistant | Mine: user | UC-F3-03 |
| [S-F3-L07 Personal connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l07-personal-connections.md) | Assistant | Mine: user | UC-F3-06 |
| [S-F3-L12 Conversation folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l12-conversation-folders.md) | Assistant | Mine: owner | UC-F3-08 |
| [S-F3-L14 Answer feedbacks](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l14-answer-feedbacks.md) | Assistant | All | UC-F3-01 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | UC-F3-03, UC-F3-04, UC-F3-06 |
| [S-F3-L27 To-dos](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l27-to-dos.md) | Assistant | Mine: owner, the only view: to-dos are private | UC-F3-24 |
| [S-F4-L02 Transcripts](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l02-transcripts.md) | Meetings | All | UC-F16-20 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F5-L01 Posts](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l01-posts.md) | Social media and marketing | All | UC-F5-05 |
| [S-F5-L04 Social messages](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l04-social-messages.md) | Social media and marketing | All | UC-F5-05 |
| [S-F6-L04 Orders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l04-orders.md) | Customers and sales | Open: Open, InProgress | UC-F6-05 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-F6-06, UC-F6-19 |
| [S-F6-L13 Public buyer settings](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l13-public-buyer-settings.md) | Customers and sales | All | UC-F6-19 |
| [S-F6-L20 Leads](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l20-leads.md) | Customers and sales | All | UC-F5-05 |
| [S-F6-L27 Warranties](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l27-warranties.md) | Customers and sales | All | UC-F6-31 |
| [S-F7-L14 Repair orders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l14-repair-orders.md) | Purchasing and stock | Open: ToDo, InRepair, Invoiced | UC-F6-31 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | UC-F3-08 |
| [S-F9-L15 Visitors](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l15-visitors.md) | HR and projects | Mine: host | UC-F9-14 |
| [S-F9-L42 Reception kiosks](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l42-reception-kiosks.md) | HR and projects | All | UC-F9-14 |
| [S-F9-L43 Visitor badges](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l43-visitor-badges.md) | HR and projects | All | UC-F9-14 |
| [S-F16-L01 Customer requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l01-customer-requests.md) | Customer support agents | Open: New, InProgress, Waiting | UC-F16-01, UC-F16-04, UC-F16-08, UC-F16-11 and more |
| [S-F16-L03 Resolution reviews](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l03-resolution-reviews.md) | Customer support agents | All | UC-F16-04 |
| [S-F16-L06 Queues](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l06-queues.md) | Customer support agents | Open: Open, Paused | UC-F16-08 |
| [S-F16-L07 Macros](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l07-macros.md) | Customer support agents | Open: Active | UC-F16-08 |
| [S-F16-L08 Satisfaction ratings](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l08-satisfaction-ratings.md) | Customer support agents | Open: Asked, Answered | UC-F16-01, UC-F16-04 |
| [S-F16-L11 Fraud signals](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l11-fraud-signals.md) | Customer support agents | All | UC-F16-15 |
| [S-F16-L12 Work requests](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l12-work-requests.md) | Customer support agents | Mine: confirmed by | UC-F16-16 |
| [S-F16-L13 Forum posts](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l13-forum-posts.md) | Customer support agents | All | UC-F16-18 |
| [S-F16-L14 Chat sessions](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l14-chat-sessions.md) | Customer support agents | All | UC-F16-19 |
| [S-F16-L15 Outreaches](../../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l15-outreaches.md) | Customer support agents | All | UC-F16-21 |
| [S-F24-L03 Suite components](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l03-suite-components.md) | Integrations hub | All | UC-F24-04, UC-F24-08 |
| [S-F24-L04 Linked documents](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l04-linked-documents.md) | Integrations hub | All | UC-F24-04 |
| [S-T13-L01 Geocoded places](../../../03-technical/t13-maps-and-geodata/screens/00-lists/s-t13-l01-geocoded-places.md) | Maps and geodata | All | UC-F16-16 |
| [S-SC03-L01 Engagements](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l01-engagements.md) | Services | Open: PreSales, Running | UC-SC03-15 |
| [S-SC03-L05 Timesheets](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l05-timesheets.md) | Services | Open: Draft, Submitted, Approved | UC-SC03-05, UC-SC03-15 |
| [S-SC03-L06 Rebillable costs](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l06-rebillable-costs.md) | Services | All | UC-SC03-05 |
| [S-SC03-L11 Skills](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l11-skills.md) | Services | All | UC-SC03-13 |
| [S-SC14-L06 Managed assets](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l06-managed-assets.md) | IT and software | All | UC-SC14-06 |
| [S-SC14-L07 Sprints](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l07-sprints.md) | IT and software | All | UC-SC14-07 |
| [S-SC14-L08 Software release notes](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l08-software-release-notes.md) | IT and software | All | UC-SC14-08, UC-SC14-21 |
| [S-SC14-L09 Health scores](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l09-health-scores.md) | IT and software | All | UC-SC14-20 |
| [S-SC14-L11 Components](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l11-components.md) | IT and software | All | UC-SC14-12 |
| [S-SC14-L16 Tracked features](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l16-tracked-features.md) | IT and software | All | UC-SC14-21, UC-SC14-20 |
| [S-SC20-L08 Citizen requests](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l08-citizen-requests.md) | Public bodies | All | UC-SC20-09 |
| [S-SC20-L13 Civil records](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l13-civil-records.md) | Public bodies | All | UC-SC20-18 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customer support agents](../../../02-functional/f16-customer-support-agents/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[IT and software](../../../08-sectors/sc14-it-and-software/screens/00-lists/README.md),
[Integrations hub](../../../02-functional/f24-integrations-hub/screens/00-lists/README.md),
[Maps and geodata](../../../03-technical/t13-maps-and-geodata/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Public bodies](../../../08-sectors/sc20-public-bodies/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Services](../../../08-sectors/sc03-services/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U16 | desktop | ![Workspace, U16, light](mockups/workspace-desktop-light.png) | ![Workspace, U16, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U16 | phone | ![Workspace, U16, light](mockups/workspace-phone-light.png) | ![Workspace, U16, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
