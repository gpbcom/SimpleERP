🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🤝 [Sales: app shell and home](README.md) › 🧰 U03 Sales: workspace

# 🧰 U03 Sales: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U03 Sales](../../../01-users/personas/u03-sales.md) works with, embedded on their [home screen](README.md)
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
| [S-F2-L14 Signature requests](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l14-signature-requests.md) | No-code configuration | Open: Sent, Signed, Refused | UC-F2-14 |
| [S-F2-L20 Offline form settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l20-offline-form-settings.md) | No-code configuration | Mine: roles | UC-F6-21 |
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Mine: owner | UC-F3-01, UC-F3-08 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-01, UC-F3-02, UC-F3-04 |
| [S-F3-L04 Assistant change batches](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l04-assistant-change-batches.md) | Assistant | Mine: user | UC-F3-03 |
| [S-F3-L07 Personal connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l07-personal-connections.md) | Assistant | Mine: user | UC-F3-06 |
| [S-F3-L12 Conversation folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l12-conversation-folders.md) | Assistant | Mine: owner | UC-F3-08 |
| [S-F3-L14 Answer feedbacks](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l14-answer-feedbacks.md) | Assistant | All | UC-F3-01 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | UC-F3-03, UC-F3-04, UC-F3-06 |
| [S-F4-L01 Meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l01-meetings.md) | Meetings | Open: Planned, Live, WaitingForReview | UC-F4-01, UC-F4-02, UC-F4-03, UC-F4-04 and more |
| [S-F4-L02 Transcripts](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l02-transcripts.md) | Meetings | All | UC-F4-01, UC-F4-02, UC-F4-03, UC-F4-04 and more |
| [S-F4-L03 Summary templates](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l03-summary-templates.md) | Meetings | All | UC-F4-05 |
| [S-F4-L04 Action items](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l04-action-items.md) | Meetings | Open: Open | UC-F4-05, UC-F4-26 |
| [S-F4-L06 Scorecards](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l06-scorecards.md) | Meetings | All | UC-F4-12 |
| [S-F4-L08 Key moments](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l08-key-moments.md) | Meetings | All | D519, VC-10 |
| [S-F4-L09 Scheduled digests](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l09-scheduled-digests.md) | Meetings | Mine: owner | UC-F4-15 |
| [S-F4-L11 Appointment types](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l11-appointment-types.md) | Meetings | All | UC-F4-18 |
| [S-F4-L12 Call routes](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l12-call-routes.md) | Meetings | All | UC-F4-19 |
| [S-F4-L13 Call topics](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l13-call-topics.md) | Meetings | All | UC-F4-20 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L17 Meeting summaries](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l17-meeting-summaries.md) | Meetings | All | UC-F4-05 |
| [S-F4-L18 Recording notices](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l18-recording-notices.md) | Meetings | All | UC-F4-01, UC-F4-04 |
| [S-F4-L19 Follow-up emails](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l19-follow-up-emails.md) | Meetings | All | UC-F4-05 |
| [S-F4-L20 Human review requests](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l20-human-review-requests.md) | Meetings | All | UC-F4-12 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L24 Meeting prep briefs](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l24-meeting-prep-briefs.md) | Meetings | All | UC-F4-09 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | UC-F4-09 |
| [S-F4-L27 Video messages](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l27-video-messages.md) | Meetings | Mine: author | UC-F4-28 |
| [S-F4-L29 Note templates](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l29-note-templates.md) | Meetings | Mine: created by | UC-F4-30 |
| [S-F6-L01 Customer records](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l01-customer-records.md) | Customers and sales | All | UC-F6-01, UC-F6-17 |
| [S-F6-L02 Opportunities](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l02-opportunities.md) | Customers and sales | All | UC-F6-01, UC-F6-02 |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Open: Draft, ToApprove, Sent | UC-F6-03, UC-F11-27 |
| [S-F6-L04 Orders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l04-orders.md) | Customers and sales | Open: Open, InProgress | UC-F6-05, UC-F6-18, UC-F6-21 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-F6-24 |
| [S-F6-L07 Subscription contracts](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l07-subscription-contracts.md) | Customers and sales | All | UC-F6-10 |
| [S-F6-L08 Sales price lists](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l08-sales-price-lists.md) | Customers and sales | All | UC-F6-03 |
| [S-F6-L09 Rentals](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l09-rentals.md) | Customers and sales | All | UC-F6-15 |
| [S-F6-L10 Rate plan and meters](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l10-rate-plan-and-meters.md) | Customers and sales | All | UC-F6-16 |
| [S-F6-L11 Timeline entries](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l11-timeline-entries.md) | Customers and sales | All | UC-F6-17 |
| [S-F6-L12 Credit limits](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l12-credit-limits.md) | Customers and sales | All | UC-F6-18, UC-SC15-16 |
| [S-F6-L17 Invoice disputes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l17-invoice-disputes.md) | Customers and sales | All | UC-F6-24 |
| [S-F6-L18 Commission plan and targets](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l18-commission-plan-and-targets.md) | Customers and sales | Open: Draft, Active | UC-SC15-14 |
| [S-F6-L19 Commission lines](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l19-commission-lines.md) | Customers and sales | Mine: rep | UC-SC14-19 |
| [S-F6-L20 Leads](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l20-leads.md) | Customers and sales | All | UC-F5-13, UC-F6-01, UC-F6-13 |
| [S-F6-L21 Payment reminders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l21-payment-reminders.md) | Customers and sales | All | UC-F6-24 |
| [S-F6-L23 Partners](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l23-partners.md) | Customers and sales | All | UC-F6-27, UC-F6-28 |
| [S-F6-L24 Company identifiers](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l24-company-identifiers.md) | Customers and sales | All | UC-F6-28, UC-F6-30 |
| [S-F6-L25 Frame contracts](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l25-frame-contracts.md) | Customers and sales | All | UC-F6-29 |
| [S-F6-L26 Solvency reports](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l26-solvency-reports.md) | Customers and sales | All | UC-F6-30 |
| [S-F7-L10 Lot or serials](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l10-lot-or-serials.md) | Purchasing and stock | All | UC-SC14-22, UC-SC15-23 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | UC-F3-08 |
| [S-F9-L18 Project and tasks](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l18-project-and-tasks.md) | HR and projects | Open: New, Planned, Active | UC-F9-17 |
| [S-F9-L26 Rounds](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l26-rounds.md) | HR and projects | Mine: person | UC-SC15-14 |
| [S-F11-L03 Online products](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l03-online-products.md) | Online shop (plugin) | All | UC-F11-20 |
| [S-F11-L04 Carts](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l04-carts.md) | Online shop (plugin) | Mine: owner | UC-F11-20 |
| [S-F11-L05 Checkouts](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l05-checkouts.md) | Online shop (plugin) | All | UC-F11-08 |
| [S-F11-L08 Withdrawal requests](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l08-withdrawal-requests.md) | Online shop (plugin) | All | UC-F11-09 |
| [S-F11-L09 Customer accounts](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l09-customer-accounts.md) | Online shop (plugin) | Mine: contact | UC-F11-11 |
| [S-F11-L11 Online promotion codes](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l11-online-promotion-codes.md) | Online shop (plugin) | All | UC-F11-03 |
| [S-F11-L22 Punch-out sessions](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l22-punch-out-sessions.md) | Online shop (plugin) | Open: Open, Returned | UC-F11-27 |
| [S-F17-L01 Competitors](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l01-competitors.md) | Competitive analysis | All | UC-F17-20 |
| [S-F17-L03 Price points](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l03-price-points.md) | Competitive analysis | All | UC-F17-03, UC-F17-11 |
| [S-F17-L05 Tender awards](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l05-tender-awards.md) | Competitive analysis | All | UC-F17-05 |
| [S-F17-L10 Analysis](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l10-analysis.md) | Competitive analysis | All | UC-F17-11, UC-F17-20 |
| [S-F17-L11 Battle cards](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l11-battle-cards.md) | Competitive analysis | All | UC-F17-13, UC-F17-24 |
| [S-F17-L12 Win-loss records](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l12-win-loss-records.md) | Competitive analysis | All | UC-F17-14 |
| [S-F17-L13 Alerts](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l13-alerts.md) | Competitive analysis | All | UC-F17-15 |
| [S-F17-L16 Tender opportunities](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l16-tender-opportunities.md) | Competitive analysis | All | UC-F17-05, UC-F17-21 |
| [S-F17-L17 Price indexes](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l17-price-indexes.md) | Competitive analysis | All | UC-F17-03, UC-F17-11, UC-F17-23 |
| [S-F17-L18 Price suggestions](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l18-price-suggestions.md) | Competitive analysis | All | UC-F17-23 |
| [S-F17-L20 Call topic signals](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l20-call-topic-signals.md) | Competitive analysis | All | UC-F17-13, UC-F17-24 |
| [S-F17-L24 Technology records](../../../02-functional/f17-competitive-analysis/screens/00-lists/s-f17-l24-technology-records.md) | Competitive analysis | All | UC-F17-29 |
| [S-F18-L21 Visits](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/s-f18-l21-visits.md) | Hosted websites and domains (hosted edition) | All | UC-F18-29 |
| [S-F23-L05 Impact results](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l05-impact-results.md) | What-if simulation and impact | All | UC-F23-06 |
| [S-F24-L06 Sync jobs](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l06-sync-jobs.md) | Integrations hub | All | UC-F24-10 |
| [S-F24-L07 Field mappings](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l07-field-mappings.md) | Integrations hub | Mine: owner | UC-F24-10 |
| [S-F24-L09 Connector actions](../../../02-functional/f24-integrations-hub/screens/00-lists/s-f24-l09-connector-actions.md) | Integrations hub | All | UC-F24-14 |
| [S-SC01-L01 Construction sites](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l01-construction-sites.md) | Construction | Open: Planned, Running, Accepted | UC-SC01-01 |
| [S-SC01-L02 Quote lots](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l02-quote-lots.md) | Construction | All | UC-SC01-01, UC-SC01-02, UC-SC01-12 |
| [S-SC01-L06 Progress bills](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l06-progress-bills.md) | Construction | Open: Draft, Sent | UC-SC01-13 |
| [S-SC01-L12 Public tenders](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l12-public-tenders.md) | Construction | Open: Watching, Answered | UC-SC01-13 |
| [S-SC03-L01 Engagements](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l01-engagements.md) | Services | Open: PreSales, Running | UC-SC03-01 |
| [S-SC03-L02 Statement of works](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l02-statement-of-works.md) | Services | All | UC-SC03-01 |
| [S-SC03-L20 Answers](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l20-answers.md) | Services | All | UC-SC03-19 |
| [S-SC05-L03 Configuration rules](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l03-configuration-rules.md) | Manufacturing | All | UC-SC05-03 |
| [S-SC05-L11 8D reports](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l11-8d-reports.md) | Manufacturing | All | UC-SC05-11 |
| [S-SC05-L17 Proofs](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l17-proofs.md) | Manufacturing | All | UC-SC05-18 |
| [S-SC06-L03 Hygiene records](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l03-hygiene-records.md) | Restaurant and hospitality | All | UC-SC06-17 |
| [S-SC06-L14 Catering orders](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l14-catering-orders.md) | Restaurant and hospitality | All | UC-SC06-17 |
| [S-SC07-L01 Transport orders](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l01-transport-orders.md) | Transport and logistics | All | UC-SC07-01 |
| [S-SC14-L01 Software subscriptions](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l01-software-subscriptions.md) | IT and software | Open: Trial, Active | UC-SC14-01, UC-SC14-10 |
| [S-SC14-L04 Software licences](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l04-software-licences.md) | IT and software | All | UC-SC14-04 |
| [S-SC14-L09 Health scores](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l09-health-scores.md) | IT and software | All | UC-SC14-10 |
| [S-SC14-L15 Partner deals](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l15-partner-deals.md) | IT and software | All | UC-SC14-19 |
| [S-SC14-L17 Leased devices](../../../08-sectors/sc14-it-and-software/screens/00-lists/s-sc14-l17-leased-devices.md) | IT and software | All | UC-SC14-22 |
| [S-SC15-L01 Price agreements](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l01-price-agreements.md) | Wholesale and distribution | Open: Active | UC-SC15-01, UC-SC15-20 |
| [S-SC15-L02 Rebate rules](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l02-rebate-rules.md) | Wholesale and distribution | All | UC-SC15-02, UC-SC15-15 |
| [S-SC15-L03 Yearly agreements](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l03-yearly-agreements.md) | Wholesale and distribution | All | UC-SC15-03 |
| [S-SC15-L04 Sales orders](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l04-sales-orders.md) | Wholesale and distribution | All | UC-SC15-04, UC-SC15-06, UC-SC15-07, UC-SC15-15 and more |
| [S-SC15-L06 Purchase proposals](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l06-purchase-proposals.md) | Wholesale and distribution | All | UC-SC15-07 |
| [S-SC15-L07 Return authorisations](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l07-return-authorisations.md) | Wholesale and distribution | All | UC-SC15-10 |
| [S-SC15-L08 Supplier funds](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l08-supplier-funds.md) | Wholesale and distribution | All | UC-SC15-11 |
| [S-SC15-L11 Visit reports](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l11-visit-reports.md) | Wholesale and distribution | All | UC-SC15-14 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Competitive analysis](../../../02-functional/f17-competitive-analysis/screens/00-lists/README.md),
[Construction](../../../08-sectors/sc01-construction/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Hosted websites and domains (hosted edition)](../../../02-functional/f18-hosted-websites-and-domains/screens/00-lists/README.md),
[IT and software](../../../08-sectors/sc14-it-and-software/screens/00-lists/README.md),
[Integrations hub](../../../02-functional/f24-integrations-hub/screens/00-lists/README.md),
[Manufacturing](../../../08-sectors/sc05-manufacturing/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Restaurant and hospitality](../../../08-sectors/sc06-hospitality/screens/00-lists/README.md),
[Services](../../../08-sectors/sc03-services/screens/00-lists/README.md),
[Transport and logistics](../../../08-sectors/sc07-transport/screens/00-lists/README.md),
[What-if simulation and impact](../../../02-functional/f23-what-if-simulation/screens/00-lists/README.md),
[Wholesale and distribution](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U03 | desktop | ![Workspace, U03, light](mockups/workspace-desktop-light.png) | ![Workspace, U03, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U03 | phone | ![Workspace, U03, light](mockups/workspace-phone-light.png) | ![Workspace, U03, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
