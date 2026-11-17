🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🏋️ [Coach: app shell and home](README.md) › 🧰 U53 Coach: workspace

# 🧰 U53 Coach: workspace

**Status:** ✅ specified

## Purpose

The views [U53 Coach](../../../01-users/personas/u53-coach.md) works with, embedded on their [home screen](README.md)
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
| [S-F2-L13 Documents](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l13-documents.md) | No-code configuration | Open: ToSort, ToValidate | UC-SC18-10 |
| [S-F2-L18 Resource bookings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l18-resource-bookings.md) | No-code configuration | Open: Requested, Confirmed, NoShow | UC-SC18-13, UC-SC18-18 |
| [S-F5-L12 Event tickets](../../../02-functional/f05-social-media/screens/00-lists/s-f05-l12-event-tickets.md) | Social media and marketing | Mine: holder | UC-SC18-18 |
| [S-F6-L06 Customer payments](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l06-customer-payments.md) | Customers and sales | All | UC-SC18-20 |
| [S-F7-L14 Repair orders](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/s-f07-l14-repair-orders.md) | Purchasing and stock | Open: ToDo, InRepair, Invoiced | UC-SC18-20 |
| [S-F9-L16 Shifts](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l16-shifts.md) | HR and projects | Mine: role | UC-SC18-08 |
| [S-F10-L03 Point of sale orders](../../../02-functional/f10-point-of-sale/screens/00-lists/s-f10-l03-point-of-sale-orders.md) | Point of sale (plugin) | Mine: customer | UC-SC18-13 |
| [S-SC18-L04 Classes](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l04-classes.md) | Sports and fitness | All | UC-SC18-07, UC-SC18-08 |
| [S-SC18-L05 Class bookings](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l05-class-bookings.md) | Sports and fitness | All | UC-SC18-07 |
| [S-SC18-L07 Medical certificates](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l07-medical-certificates.md) | Sports and fitness | All | UC-SC18-10, UC-SC18-11 |
| [S-SC18-L08 Teams](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l08-teams.md) | Sports and fitness | All | UC-SC18-10, UC-SC18-11, UC-SC18-12 |
| [S-SC18-L09 Results](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l09-results.md) | Sports and fitness | All | UC-SC18-11, UC-SC18-12, UC-SC18-18 |
| [S-SC18-L10 Coaching packages](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l10-coaching-packages.md) | Sports and fitness | All | UC-SC18-13, UC-SC18-14 |
| [S-SC18-L11 Training programmes](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l11-training-programmes.md) | Sports and fitness | All | UC-SC18-14, UC-SC18-15 |
| [S-SC18-L12 Progress records](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l12-progress-records.md) | Sports and fitness | All | UC-SC18-14, UC-SC18-15 |
| [S-SC18-L14 Tournaments](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l14-tournaments.md) | Sports and fitness | All | UC-SC18-12, UC-SC18-18 |
| [S-SC18-L16 Rental items](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/s-sc18-l16-rental-items.md) | Sports and fitness | All | UC-SC18-20 |

## Navigation

Each view also sits in its capability's menu (D495):
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Point of sale (plugin)](../../../02-functional/f10-point-of-sale/screens/00-lists/README.md),
[Purchasing and stock](../../../02-functional/f07-purchasing-and-stock/screens/00-lists/README.md),
[Social media and marketing](../../../02-functional/f05-social-media/screens/00-lists/README.md),
[Sports and fitness](../../../08-sectors/sc18-sports-and-fitness/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U53 | desktop | ![Workspace, U53, light](mockups/workspace-desktop-light.png) | ![Workspace, U53, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U53 | phone | ![Workspace, U53, light](mockups/workspace-phone-light.png) | ![Workspace, U53, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
