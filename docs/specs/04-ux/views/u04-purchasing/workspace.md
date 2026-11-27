🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🛍️ [Purchasing and stock: app shell and home](README.md) › 🧰 U04 Purchasing and stock: workspace

# 🧰 U04 Purchasing and stock: workspace

**Status:** 🔄 waiting for the owner

## Purpose

The views [U04 Purchasing and stock](../../../01-users/personas/u04-purchasing.md) works with, embedded on their
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
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Mine: owner | UC-F3-01, UC-F3-08 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-01, UC-F3-02, UC-F3-04 |
| [S-F3-L04 Assistant change batches](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l04-assistant-change-batches.md) | Assistant | Mine: user | UC-F3-03 |
| [S-F3-L07 Personal connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l07-personal-connections.md) | Assistant | Mine: user | UC-F3-06 |
| [S-F3-L12 Conversation folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l12-conversation-folders.md) | Assistant | Mine: owner | UC-F3-08 |
| [S-F3-L14 Answer feedbacks](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l14-answer-feedbacks.md) | Assistant | All | UC-F3-01 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | UC-F3-03, UC-F3-04, UC-F3-06 |
| [S-F4-L01 Meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l01-meetings.md) | Meetings | Open: Planned, Live, WaitingForReview | UC-F4-04 |
| [S-F4-L02 Transcripts](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l02-transcripts.md) | Meetings | All | UC-F4-04 |
| [S-F4-L08 Key moments](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l08-key-moments.md) | Meetings | All | D519, VC-10 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L18 Recording notices](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l18-recording-notices.md) | Meetings | All | UC-F4-04 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F6-L04 Orders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l04-orders.md) | Customers and sales | Open: Open, InProgress | UC-SC15-21 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-F7-28, UC-SC15-21, UC-SC15-22 |
| [S-F6-L06 Customer payments](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l06-customer-payments.md) | Customers and sales | All | UC-SC15-22 |
| [S-F7-L01 Supplier records](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l01-supplier-records.md) | Purchasing and stock | All | UC-F7-02, UC-F7-18, UC-F7-19 |
| [S-F7-L02 Purchase requests](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l02-purchase-requests.md) | Purchasing and stock | All | UC-F7-01, UC-F7-20 |
| [S-F7-L03 Purchase orders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l03-purchase-orders.md) | Purchasing and stock | All | UC-F7-01, UC-F7-02, UC-F7-05 |
| [S-F7-L04 Transfers](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l04-transfers.md) | Purchasing and stock | Open: Sent, Received, Reserved | UC-F7-08 |
| [S-F7-L05 Supplier invoices](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l05-supplier-invoices.md) | Purchasing and stock | All | UC-F7-24 |
| [S-F7-L06 Items](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l06-items.md) | Purchasing and stock | All | UC-F7-05, UC-F7-21, UC-F7-11, UC-F7-22 |
| [S-F7-L07 Locations](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l07-locations.md) | Purchasing and stock | All | UC-F7-23 |
| [S-F7-L09 Reordering rules](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l09-reordering-rules.md) | Purchasing and stock | All | UC-F7-05, UC-F7-21 |
| [S-F7-L10 Lot or serials](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l10-lot-or-serials.md) | Purchasing and stock | All | UC-F7-08 |
| [S-F7-L11 Stock counts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l11-stock-counts.md) | Purchasing and stock | All | UC-F7-11 |
| [S-F7-L13 Call for tenders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l13-call-for-tenders.md) | Purchasing and stock | All | UC-F7-14 |
| [S-F7-L15 Supplier contracts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l15-supplier-contracts.md) | Purchasing and stock | Open: Draft, Active, Renewed | UC-F7-18 |
| [S-F7-L16 Supplier scores](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l16-supplier-scores.md) | Purchasing and stock | All | UC-F7-19 |
| [S-F7-L17 Approved catalogues](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l17-approved-catalogues.md) | Purchasing and stock | Open: Active | UC-F7-20 |
| [S-F7-L18 Eco-contribution scales](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l18-eco-contribution-scales.md) | Purchasing and stock | All | UC-F7-22 |
| [S-F7-L19 Safety data sheets](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l19-safety-data-sheets.md) | Purchasing and stock | All | UC-F7-23 |
| [S-F7-L20 Emission factors](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l20-emission-factors.md) | Purchasing and stock | All | UC-F7-24 |
| [S-F7-L21 Demand forecasts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l21-demand-forecasts.md) | Purchasing and stock | All | UC-F7-21, UC-F12-03 |
| [S-F7-L22 Delivery notes](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l22-delivery-notes.md) | Purchasing and stock | All | UC-F7-28, UC-F7-29, UC-SC15-24 |
| [S-F7-L23 Stock owners](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l23-stock-owners.md) | Purchasing and stock | All | UC-F7-25 |
| [S-F7-L24 Periodic counts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l24-periodic-counts.md) | Purchasing and stock | All | UC-F7-27 |
| [S-F7-L25 Packaging deposits](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l25-packaging-deposits.md) | Purchasing and stock | All | UC-F7-28, UC-SC15-21 |
| [S-F7-L26 EDI messages](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l26-edi-messages.md) | Purchasing and stock | All | UC-F7-29 |
| [S-F7-L27 Slotting proposals](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l27-slotting-proposals.md) | Purchasing and stock | All | UC-F7-30 |
| [S-F8-L03 Journal entries](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l03-journal-entries.md) | Accounting | All | UC-F7-27 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | UC-F3-08 |
| [S-F11-L03 Online products](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l03-online-products.md) | Online shop (plugin) | All | UC-F11-23, UC-F11-25 |
| [S-F11-L18 Product contents](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l18-product-contents.md) | Online shop (plugin) | All | UC-F11-23 |
| [S-F11-L20 Product safety informations](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l20-product-safety-informations.md) | Online shop (plugin) | All | UC-F11-25 |
| [S-F12-L04 Manufacturing orders](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l04-manufacturing-orders.md) | Manufacturing (plugin) | Open: Draft, Confirmed, InProgress | UC-F12-03, UC-F12-09 |
| [S-F12-L12 Master plan lines](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l12-master-plan-lines.md) | Manufacturing (plugin) | All | UC-F12-03 |
| [S-F15-L05 Compliance duties](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l05-compliance-duties.md) | Legal assistant | Mine: owner | UC-F15-08 |
| [S-F15-L06 Contract records](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l06-contract-records.md) | Legal assistant | Open: Active, NoticeGiven, Renewed | UC-F15-08 |
| [S-F23-L05 Impact results](../../../02-functional/f23-what-if-simulation/screens/00-lists/s-f23-l05-impact-results.md) | What-if simulation and impact | All | UC-F23-09 |
| [S-SC01-L07 Subcontracts](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l07-subcontracts.md) | Construction | All | UC-SC01-07 |
| [S-SC01-L08 Equipment assignments](../../../08-sectors/sc01-construction/screens/00-lists/s-sc01-l08-equipment-assignments.md) | Construction | All | UC-SC01-08 |
| [S-SC03-L10 Freelance contracts](../../../08-sectors/sc03-services/screens/00-lists/s-sc03-l10-freelance-contracts.md) | Services | All | UC-SC03-09 |
| [S-SC05-L10 Supplier ratings](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l10-supplier-ratings.md) | Manufacturing | Mine: supplier | UC-SC05-10 |
| [S-SC07-L12 Charters](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l12-charters.md) | Transport and logistics | All | UC-SC07-12 |
| [S-SC15-L04 Sales orders](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l04-sales-orders.md) | Wholesale and distribution | All | UC-SC15-07 |
| [S-SC15-L06 Purchase proposals](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l06-purchase-proposals.md) | Wholesale and distribution | All | UC-SC15-07, UC-SC15-17 |
| [S-SC15-L08 Supplier funds](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l08-supplier-funds.md) | Wholesale and distribution | All | UC-SC15-11 |
| [S-SC15-L09 Import files](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l09-import-files.md) | Wholesale and distribution | All | UC-SC15-12 |
| [S-SC15-L13 Supplier scorecards](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l13-supplier-scorecards.md) | Wholesale and distribution | All | UC-SC15-19 |
| [S-SC15-L15 Bar loans](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l15-bar-loans.md) | Wholesale and distribution | All | UC-SC15-21 |
| [S-SC15-L16 Van stocks](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l16-van-stocks.md) | Wholesale and distribution | All | UC-SC15-22, UC-SC19-19 |
| [S-SC15-L17 Device lots](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l17-device-lots.md) | Wholesale and distribution | All | UC-SC15-24 |
| [S-SC19-L13 Van stocks](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/s-sc19-l13-van-stocks.md) | Trades and home services | All | UC-SC19-19 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Construction](../../../08-sectors/sc01-construction/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md),
[Manufacturing](../../../08-sectors/sc05-manufacturing/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Services](../../../08-sectors/sc03-services/screens/00-lists/README.md),
[Trades and home services](../../../08-sectors/sc19-trades-and-home-services/screens/00-lists/README.md),
[Transport and logistics](../../../08-sectors/sc07-transport/screens/00-lists/README.md),
[What-if simulation and impact](../../../02-functional/f23-what-if-simulation/screens/00-lists/README.md),
[Wholesale and distribution](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U04 | desktop | ![Workspace, U04, light](mockups/workspace-desktop-light.png) | ![Workspace, U04, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U04 | phone | ![Workspace, U04, light](mockups/workspace-phone-light.png) | ![Workspace, U04, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
