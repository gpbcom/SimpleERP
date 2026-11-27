🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🧾 [Cashier: app shell and home](README.md) › 🧰 U17 Cashier: workspace

# 🧰 U17 Cashier: workspace

**Status:** ✅ specified

## Purpose

The views [U17 Cashier](../../../01-users/personas/u17-cashier.md) works with, embedded on their
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
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Open: Planned, Waiting, Live | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | Mine: employee | flow charts (VR-3) |
| [S-F6-L01 Customer records](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l01-customer-records.md) | Customers and sales | All | UC-F10-25 |
| [S-F7-L04 Transfers](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l04-transfers.md) | Purchasing and stock | Open: Sent, Received, Reserved | UC-F10-26, UC-F11-28 |
| [S-F7-L06 Items](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l06-items.md) | Purchasing and stock | All | UC-F10-32, UC-SC02-16, UC-SC02-18, UC-SC09-21 and more |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F10-L01 Point of sales](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l01-point-of-sales.md) | Point of sale (plugin) | All | UC-F10-01, UC-F10-16 |
| [S-F10-L02 Till sessions](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l02-till-sessions.md) | Point of sale (plugin) | Open: Open, Closing, Posted | UC-F10-01, UC-F10-14, UC-F10-20, UC-F10-23 |
| [S-F10-L03 Point of sale orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l03-point-of-sale-orders.md) | Point of sale (plugin) | Mine: customer | UC-F10-02, UC-F10-03, UC-F10-05, UC-F10-08 and more |
| [S-F10-L04 Till payments](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l04-till-payments.md) | Point of sale (plugin) | All | UC-F10-03, UC-F10-04, UC-F10-14, UC-F10-21 |
| [S-F10-L05 Receipts](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l05-receipts.md) | Point of sale (plugin) | All | UC-F10-05, UC-F10-04, UC-F10-27 |
| [S-F10-L06 Closures](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l06-closures.md) | Point of sale (plugin) | All | UC-F10-01 |
| [S-F10-L08 Price promotions](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l08-price-promotions.md) | Point of sale (plugin) | All | UC-F10-06 |
| [S-F10-L09 Combos](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l09-combos.md) | Point of sale (plugin) | All | UC-F10-06 |
| [S-F10-L10 Loyalty card and gift cards](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l10-loyalty-card-and-gift-cards.md) | Point of sale (plugin) | Mine: customer | UC-F10-07 |
| [S-F10-L14 Point of sale devices](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l14-point-of-sale-devices.md) | Point of sale (plugin) | All | UC-F10-08, UC-F10-19 |
| [S-F10-L15 Till event logs](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l15-till-event-logs.md) | Point of sale (plugin) | Mine: user | UC-F10-01 |
| [S-F10-L16 Age checks](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l16-age-checks.md) | Point of sale (plugin) | All | UC-F10-22 |
| [S-F10-L17 Cash movements](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l17-cash-movements.md) | Point of sale (plugin) | All | UC-F10-23 |
| [S-F10-L19 Clienteling profiles](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l19-clienteling-profiles.md) | Point of sale (plugin) | All | UC-F10-25 |
| [S-F10-L20 Tax-free forms](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l20-tax-free-forms.md) | Point of sale (plugin) | Open: Issued, Validated, Refunded | UC-F10-27 |
| [S-F10-L24 Layaways](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l24-layaways.md) | Point of sale (plugin) | Mine: seller | UC-F10-32 |
| [S-F11-L23 Store fulfilments](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l23-store-fulfilments.md) | Online shop (plugin) | All | UC-F11-28 |
| [S-SC02-L01 Stores](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l01-stores.md) | Retail | Open: Planned, Open | UC-SC02-07, UC-SC02-08, UC-SC02-09, UC-SC02-15 |
| [S-SC02-L06 Store transfers](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l06-store-transfers.md) | Retail | All | UC-SC02-15 |
| [S-SC02-L07 Shelf labels](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l07-shelf-labels.md) | Retail | Open: ToPrint | UC-SC02-05 |
| [S-SC02-L11 Customer profiles](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l11-customer-profiles.md) | Retail | Mine: contact | UC-SC02-10 |
| [S-SC02-L13 Book titles](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l13-book-titles.md) | Retail | All | UC-SC02-16 |
| [S-SC02-L15 Second-hand purchases](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l15-second-hand-purchases.md) | Retail | All | UC-SC02-18 |
| [S-SC06-L12 Meal voucher payments](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l12-meal-voucher-payments.md) | Restaurant and hospitality | All | UC-SC06-13 |
| [S-SC09-L04 Prescriptions](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l04-prescriptions.md) | Health practices | All | UC-SC09-21, UC-SC09-22 |
| [S-SC09-L07 Patient invoices](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l07-patient-invoices.md) | Health practices | All | UC-SC09-22 |
| [S-SC09-L14 Dispensations](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l14-dispensations.md) | Health practices | All | UC-SC09-21 |
| [S-SC09-L15 Eyewear orders](../../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l15-eyewear-orders.md) | Health practices | All | UC-SC09-22 |
| [S-SC16-L13 Event tills](../../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l13-event-tills.md) | Events and culture | All | UC-SC16-12 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[Events and culture](../../../08-sectors/sc16-events-and-culture/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Health practices](../../../08-sectors/sc09-health-practices/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Restaurant and hospitality](../../../08-sectors/sc06-hospitality/screens/00-lists/README.md),
[Retail](../../../08-sectors/sc02-retail/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U17 | desktop | ![Workspace, U17, light](mockups/workspace-desktop-light.png) | ![Workspace, U17, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U17 | phone | ![Workspace, U17, light](mockups/workspace-phone-light.png) | ![Workspace, U17, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
