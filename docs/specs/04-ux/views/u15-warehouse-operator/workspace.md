🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🏷️ [Warehouse operator: app shell and home](README.md) › 🧰 U15 Warehouse operator: workspace

# 🧰 U15 Warehouse operator: workspace

**Status:** ✅ specified

## Purpose

The views [U15 Warehouse operator](../../../01-users/personas/u15-warehouse-operator.md) works with, embedded on their
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
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Mine: owner | UC-F3-01, UC-F3-08 |
| [S-F3-L02 Assistant answers](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l02-assistant-answers.md) | Assistant | All | UC-F3-01, UC-F3-02, UC-F3-04 |
| [S-F3-L04 Assistant change batches](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l04-assistant-change-batches.md) | Assistant | Mine: user | UC-F3-03 |
| [S-F3-L07 Personal connections](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l07-personal-connections.md) | Assistant | Mine: user | UC-F3-06 |
| [S-F3-L12 Conversation folders](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l12-conversation-folders.md) | Assistant | Mine: owner | UC-F3-08 |
| [S-F3-L14 Answer feedbacks](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l14-answer-feedbacks.md) | Assistant | All | UC-F3-01 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | UC-F3-03, UC-F3-04, UC-F3-06 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F6-L04 Orders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l04-orders.md) | Customers and sales | Open: Open, InProgress | UC-SC15-23 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-F7-28, UC-SC15-23 |
| [S-F6-L09 Rentals](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l09-rentals.md) | Customers and sales | All | UC-F6-15 |
| [S-F7-L04 Transfers](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l04-transfers.md) | Purchasing and stock | Open: Sent, Received, Reserved | UC-F7-03, UC-F7-06, UC-F7-10, UC-F10-26 and more |
| [S-F7-L06 Items](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l06-items.md) | Purchasing and stock | All | UC-F7-03, UC-F7-06 |
| [S-F7-L07 Locations](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l07-locations.md) | Purchasing and stock | All | UC-F7-03, UC-F7-23, UC-F7-06, UC-F7-07 |
| [S-F7-L10 Lot or serials](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l10-lot-or-serials.md) | Purchasing and stock | All | UC-F7-03, UC-F7-06 |
| [S-F7-L11 Stock counts](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l11-stock-counts.md) | Purchasing and stock | All | UC-F7-07 |
| [S-F7-L14 Repair orders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l14-repair-orders.md) | Purchasing and stock | Open: ToDo, InRepair, Invoiced | UC-F7-17 |
| [S-F7-L19 Safety data sheets](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l19-safety-data-sheets.md) | Purchasing and stock | All | UC-F7-23 |
| [S-F7-L22 Delivery notes](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l22-delivery-notes.md) | Purchasing and stock | All | UC-F7-03 |
| [S-F7-L23 Stock owners](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l23-stock-owners.md) | Purchasing and stock | All | UC-F7-25 |
| [S-F7-L25 Packaging deposits](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l25-packaging-deposits.md) | Purchasing and stock | All | UC-F7-28 |
| [S-F7-L27 Slotting proposals](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l27-slotting-proposals.md) | Purchasing and stock | All | UC-F7-30 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | UC-F3-08 |
| [S-F10-L03 Point of sale orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l03-point-of-sale-orders.md) | Point of sale (plugin) | Mine: customer | UC-F10-26 |
| [S-F11-L07 Delivery methods](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l07-delivery-methods.md) | Online shop (plugin) | All | UC-F11-07 |
| [S-F11-L23 Store fulfilments](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l23-store-fulfilments.md) | Online shop (plugin) | All | UC-F11-28 |
| [S-F12-L06 Component consumptions](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l06-component-consumptions.md) | Manufacturing (plugin) | All | UC-F12-15, UC-F12-06 |
| [S-F12-L15 Waste register lines](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l15-waste-register-lines.md) | Manufacturing (plugin) | All | UC-F12-18 |
| [S-SC02-L05 Replenishment rules](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l05-replenishment-rules.md) | Retail | All | UC-SC02-03 |
| [S-SC02-L10 Unsold goods donations](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l10-unsold-goods-donations.md) | Retail | All | UC-SC02-13 |
| [S-SC05-L05 Customer-supplied parts](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l05-customer-supplied-parts.md) | Manufacturing | All | UC-SC05-05 |
| [S-SC05-L06 Label templates](../../../08-sectors/sc05-manufacturing/screens/00-lists/s-sc05-l06-label-templates.md) | Manufacturing | All | UC-SC05-06 |
| [S-SC07-L14 Client stocks](../../../08-sectors/sc07-transport/screens/00-lists/s-sc07-l14-client-stocks.md) | Transport and logistics | All | UC-SC07-14 |
| [S-SC13-L04 Lots](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l04-lots.md) | Agriculture and food | Open: Blocked, Refused | UC-SC13-17 |
| [S-SC13-L15 Recalls](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/s-sc13-l15-recalls.md) | Agriculture and food | All | UC-SC13-17 |
| [S-SC15-L04 Sales orders](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l04-sales-orders.md) | Wholesale and distribution | All | UC-SC15-04, UC-SC15-06 |
| [S-SC15-L05 Pick waves](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l05-pick-waves.md) | Wholesale and distribution | All | UC-SC15-08, UC-SC15-09 |
| [S-SC15-L07 Return authorisations](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l07-return-authorisations.md) | Wholesale and distribution | All | UC-SC15-10 |
| [S-SC15-L14 Pallets](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/s-sc15-l14-pallets.md) | Wholesale and distribution | All | UC-SC05-06, UC-SC15-09 |

## Navigation

Each view also sits in its capability's menu (D495):
[Agriculture and food](../../../08-sectors/sc13-agriculture-and-food/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Manufacturing](../../../08-sectors/sc05-manufacturing/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Retail](../../../08-sectors/sc02-retail/screens/00-lists/README.md),
[Transport and logistics](../../../08-sectors/sc07-transport/screens/00-lists/README.md),
[Wholesale and distribution](../../../08-sectors/sc15-wholesale-and-distribution/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U15 | desktop | ![Workspace, U15, light](mockups/workspace-desktop-light.png) | ![Workspace, U15, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U15 | phone | ![Workspace, U15, light](mockups/workspace-phone-light.png) | ![Workspace, U15, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
