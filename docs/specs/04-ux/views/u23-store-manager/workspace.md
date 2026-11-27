🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🏬 [Store manager: app shell and home](README.md) › 🧰 U23 Store manager: workspace

# 🧰 U23 Store manager: workspace

**Status:** ✅ specified

## Purpose

The views [U23 Store manager](../../../01-users/personas/u23-store-manager.md) works with, embedded on their
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
| [S-F1-L02 Company sites](../../../02-functional/f01-administration/screens/00-lists/s-f01-l02-company-sites.md) | Administration | Needs attention | UC-F1-15 |
| [S-F1-L03 Users](../../../02-functional/f01-administration/screens/00-lists/s-f01-l03-users.md) | Administration | All | UC-F1-15 |
| [S-F1-L06 Roles](../../../02-functional/f01-administration/screens/00-lists/s-f01-l06-roles.md) | Administration | All | UC-F1-15 |
| [S-F2-L17 Bookable resource settings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l17-bookable-resource-settings.md) | No-code configuration | Needs attention | UC-SC06-07 |
| [S-F2-L18 Resource bookings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l18-resource-bookings.md) | No-code configuration | Open: Requested, Confirmed, NoShow | UC-SC17-17 |
| [S-F3-L22 AI assistant requests](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l22-ai-assistant-requests.md) | Assistant | All | D519, VC-7 |
| [S-F4-L11 Appointment types](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l11-appointment-types.md) | Meetings | All | UC-SC17-01 |
| [S-F4-L16 Client video meetings](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l16-client-video-meetings.md) | Meetings | Needs attention | D519, VC-11 |
| [S-F4-L22 Meeting agendas](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l22-meeting-agendas.md) | Meetings | All | D519, VC-13 |
| [S-F4-L26 Employee calendars](../../../02-functional/f04-meetings/screens/00-lists/s-f04-l26-employee-calendars.md) | Meetings | All | flow charts (VR-3) |
| [S-F5-L04 Social messages](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l04-social-messages.md) | Social media and marketing | All | UC-F5-20 |
| [S-F5-L14 WhatsApp templates](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l14-whatsapp-templates.md) | Social media and marketing | Needs attention | UC-F5-20 |
| [S-F6-L01 Customer records](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l01-customer-records.md) | Customers and sales | All | UC-F10-25 |
| [S-F6-L03 Quotes](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l03-quotes.md) | Customers and sales | Needs attention | D519, VC-14 |
| [S-F6-L04 Orders](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l04-orders.md) | Customers and sales | Open: Open, InProgress | UC-SC02-17 |
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-SC02-19, UC-SC17-06 |
| [S-F6-L07 Subscription contracts](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l07-subscription-contracts.md) | Customers and sales | All | UC-SC17-06, UC-SC17-17 |
| [S-F6-L18 Commission plan and targets](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l18-commission-plan-and-targets.md) | Customers and sales | Needs attention | UC-F6-25 |
| [S-F6-L19 Commission lines](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l19-commission-lines.md) | Customers and sales | Open: Approved | UC-F6-25 |
| [S-F7-L03 Purchase orders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l03-purchase-orders.md) | Purchasing and stock | All | UC-SC02-17, UC-SC17-11 |
| [S-F7-L04 Transfers](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l04-transfers.md) | Purchasing and stock | Open: Sent, Received, Reserved | UC-F10-26, UC-F11-28 |
| [S-F7-L06 Items](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l06-items.md) | Purchasing and stock | All | UC-F10-31, UC-F10-32, UC-SC02-16, UC-SC02-18 and more |
| [S-F7-L10 Lot or serials](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l10-lot-or-serials.md) | Purchasing and stock | All | UC-SC17-12 |
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | All | D519, VC-8 |
| [S-F10-L02 Till sessions](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l02-till-sessions.md) | Point of sale (plugin) | Needs attention | UC-F10-23, UC-F10-28 |
| [S-F10-L03 Point of sale orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l03-point-of-sale-orders.md) | Point of sale (plugin) | Needs attention | UC-F10-26, UC-F10-28 |
| [S-F10-L10 Loyalty card and gift cards](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l10-loyalty-card-and-gift-cards.md) | Point of sale (plugin) | Mine: customer | UC-F11-32, UC-SC17-08, UC-SC17-20 |
| [S-F10-L17 Cash movements](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l17-cash-movements.md) | Point of sale (plugin) | All | UC-F10-23 |
| [S-F10-L19 Clienteling profiles](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l19-clienteling-profiles.md) | Point of sale (plugin) | All | UC-F10-25 |
| [S-F10-L23 Shelf labels](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l23-shelf-labels.md) | Point of sale (plugin) | Mine: shop | UC-F10-31 |
| [S-F10-L24 Layaways](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l24-layaways.md) | Point of sale (plugin) | Mine: seller | UC-F10-32 |
| [S-F11-L23 Store fulfilments](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l23-store-fulfilments.md) | Online shop (plugin) | All | UC-F11-28 |
| [S-F11-L26 Gift cards](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l26-online-gift-cards.md) | Online shop (plugin) | Mine: buyer | UC-F11-32 |
| [S-F12-L25 Recipes](../../../02-functional/f12-manufacturing/screens/00-lists/s-f12-l25-recipes.md) | Manufacturing (plugin) | Needs attention | UC-SC06-01 |
| [S-SC02-L01 Stores](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l01-stores.md) | Retail | Needs attention | UC-SC02-01, UC-SC02-07, UC-SC02-12, UC-SC02-14 and more |
| [S-SC02-L02 Assortments](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l02-assortments.md) | Retail | All | UC-SC02-01 |
| [S-SC02-L03 Product grids](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l03-product-grids.md) | Retail | All | UC-SC02-02 |
| [S-SC02-L04 Seasons](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l04-seasons.md) | Retail | Open: Planned, Selling, Clearing | UC-SC02-02 |
| [S-SC02-L05 Replenishment rules](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l05-replenishment-rules.md) | Retail | All | UC-SC02-03 |
| [S-SC02-L06 Store transfers](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l06-store-transfers.md) | Retail | Needs attention | UC-SC02-04, UC-SC02-15 |
| [S-SC02-L07 Shelf labels](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l07-shelf-labels.md) | Retail | Open: ToPrint | UC-SC02-05 |
| [S-SC02-L08 Markdowns](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l08-markdowns.md) | Retail | All | UC-SC02-06 |
| [S-SC02-L09 Store targets](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l09-store-targets.md) | Retail | All | UC-SC02-11 |
| [S-SC02-L10 Unsold goods donations](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l10-unsold-goods-donations.md) | Retail | All | UC-SC02-13 |
| [S-SC02-L11 Customer profiles](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l11-customer-profiles.md) | Retail | All | UC-SC02-10 |
| [S-SC02-L12 Footfall counts](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l12-footfall-counts.md) | Retail | All | UC-SC02-14 |
| [S-SC02-L13 Book titles](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l13-book-titles.md) | Retail | All | UC-SC02-16 |
| [S-SC02-L14 Furniture orders](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l14-furniture-orders.md) | Retail | All | UC-SC02-17 |
| [S-SC02-L15 Second-hand purchases](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l15-second-hand-purchases.md) | Retail | All | UC-SC02-18 |
| [S-SC02-L16 Franchisees](../../../08-sectors/sc02-retail/screens/00-lists/s-sc02-l16-franchisees.md) | Retail | All | UC-SC02-19 |
| [S-SC06-L02 Menu dishes](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l02-menu-dishes.md) | Restaurant and hospitality | All | UC-SC06-01, UC-SC06-02, UC-SC06-15 |
| [S-SC06-L03 Hygiene records](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l03-hygiene-records.md) | Restaurant and hospitality | All | UC-SC06-03 |
| [S-SC06-L04 Waste records](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l04-waste-records.md) | Restaurant and hospitality | All | UC-SC06-04 |
| [S-SC06-L05 Staff benefits](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l05-staff-benefits.md) | Restaurant and hospitality | All | UC-SC06-05, UC-SC06-06 |
| [S-SC06-L06 Hotel rooms](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l06-hotel-rooms.md) | Restaurant and hospitality | All | UC-SC06-07 |
| [S-SC06-L07 Rate plans](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l07-rate-plans.md) | Restaurant and hospitality | All | UC-SC06-07, UC-SC06-14 |
| [S-SC06-L08 Room reservations](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l08-room-reservations.md) | Restaurant and hospitality | Open: Booked, Arrived, Departed | UC-SC06-15 |
| [S-SC06-L09 Folios](../../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l09-folios.md) | Restaurant and hospitality | Needs attention | UC-SC06-14 |
| [S-SC17-L01 Cabins](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l01-cabins.md) | Beauty and wellness | All | UC-SC17-01, UC-SC17-17 |
| [S-SC17-L02 Salon bookings](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l02-salon-bookings.md) | Beauty and wellness | All | UC-SC17-04, UC-SC17-16 |
| [S-SC17-L03 Booking deposits](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l03-booking-deposits.md) | Beauty and wellness | All | UC-SC17-04 |
| [S-SC17-L05 Salon memberships](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l05-salon-memberships.md) | Beauty and wellness | All | UC-SC17-06, UC-SC17-08 |
| [S-SC17-L08 Safety records](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l08-safety-records.md) | Beauty and wellness | All | UC-SC17-12 |
| [S-SC17-L09 Commission plans](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l09-commission-plans.md) | Beauty and wellness | All | UC-SC17-13 |
| [S-SC17-L10 Tips](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l10-tips.md) | Beauty and wellness | All | UC-SC17-14 |
| [S-SC17-L11 Rental contracts](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l11-rental-contracts.md) | Beauty and wellness | All | UC-SC17-17 |

## Navigation

Each view also sits in its capability's menu (D495):
[Administration](../../../02-functional/f01-administration/screens/00-lists/README.md),
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Beauty and wellness](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Manufacturing (plugin)](../../../02-functional/f12-manufacturing/screens/00-lists/README.md),
[Meetings](../../../02-functional/f04-meetings/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Restaurant and hospitality](../../../08-sectors/sc06-hospitality/screens/00-lists/README.md),
[Retail](../../../08-sectors/sc02-retail/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U23 | desktop | ![Workspace, U23, light](mockups/workspace-desktop-light.png) | ![Workspace, U23, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U23 | phone | ![Workspace, U23, light](mockups/workspace-phone-light.png) | ![Workspace, U23, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
