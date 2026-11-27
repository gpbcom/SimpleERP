🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
💅 [Beautician: app shell and home](README.md) › 🧰 U52 Beautician: workspace

# 🧰 U52 Beautician: workspace

**Status:** ✅ specified

## Purpose

The views [U52 Beautician](../../../01-users/personas/u52-beautician.md) works with, embedded on their
[home screen](README.md)
([D484](../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D493](../../../06-decisions/ux/d493-persona-workspaces-from-the-use-cases.md),
[D495](../../../06-decisions/ux/d495-views-listed-under-each-capabilitys-menu.md)): the list of each record type their
use cases and flow charts work on, with the owner's review of 2026-11-13
([D519](../../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md)). Each view opens on the
persona's default saved view. The default is the view's "Mine" for a persona who works on their own records,
"Needs attention" for one who oversees others' (managers, the owner, HR, the administrators, the planner roles, the
shareholder and the elected official), else "Open", else "All".

## Embedded views

| View | Capability | Default saved view | Why |
|---|---|---|---|
| [S-F2-L18 Resource bookings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l18-resource-bookings.md) | No-code configuration | Open: Requested, Confirmed, NoShow | UC-SC17-17 |
| [S-F6-L01 Customer records](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l01-customer-records.md) | Customers and sales | All | UC-SC17-03, UC-SC17-05, UC-SC17-17, UC-SC17-19 |
| [S-F6-L07 Subscription contracts](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l07-subscription-contracts.md) | Customers and sales | All | UC-SC17-17 |
| [S-F6-L19 Commission lines](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l19-commission-lines.md) | Customers and sales | Mine: rep | UC-SC17-09, UC-SC17-15 |
| [S-F7-L06 Items](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l06-items.md) | Purchasing and stock | All | UC-SC17-09, UC-SC17-10 |
| [S-F10-L03 Point of sale orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l03-point-of-sale-orders.md) | Point of sale (plugin) | Mine: customer | UC-SC17-05, UC-SC17-07, UC-SC17-09, UC-SC17-15 |
| [S-F10-L10 Loyalty card and gift cards](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l10-loyalty-card-and-gift-cards.md) | Point of sale (plugin) | Mine: customer | UC-SC17-07 |
| [S-SC17-L02 Salon bookings](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l02-salon-bookings.md) | Beauty and wellness | All | UC-SC17-03, UC-SC17-09, UC-SC17-10 |
| [S-SC17-L04 Session packages](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l04-session-packages.md) | Beauty and wellness | All | UC-SC17-05 |
| [S-SC17-L06 Gift vouchers](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l06-gift-vouchers.md) | Beauty and wellness | All | UC-SC17-07 |
| [S-SC17-L07 Product uses](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l07-product-uses.md) | Beauty and wellness | All | UC-SC17-10 |
| [S-SC17-L10 Tips](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l10-tips.md) | Beauty and wellness | All | UC-SC17-14 |
| [S-SC17-L11 Rental contracts](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l11-rental-contracts.md) | Beauty and wellness | All | UC-SC17-17 |
| [S-SC17-L12 Care records](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l12-care-records.md) | Beauty and wellness | All | UC-SC17-18, UC-SC17-19 |
| [S-SC17-L13 Client files](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/s-sc17-l13-client-files.md) | Beauty and wellness | All | UC-SC17-18, UC-SC17-19 |

## Navigation

Each view also sits in its capability's menu (D495):
[Beauty and wellness](../../../08-sectors/sc17-beauty-and-wellness/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U52 | desktop | ![Workspace, U52, light](mockups/workspace-desktop-light.png) | ![Workspace, U52, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U52 | phone | ![Workspace, U52, light](mockups/workspace-phone-light.png) | ![Workspace, U52, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
