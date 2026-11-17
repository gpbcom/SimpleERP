🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🏛️ [Public finance officer: app shell and home](README.md) › 🧰 U54 Public finance officer: workspace

# 🧰 U54 Public finance officer: workspace

**Status:** ✅ specified

## Purpose

The views [U54 Public finance officer](../../../01-users/personas/u54-public-finance-officer.md) works with, embedded on
their [home screen](README.md)
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
| [S-F6-L05 Invoices](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l05-invoices.md) | Customers and sales | Open: Sent, Received, Draft | UC-SC20-03 |
| [S-F8-L02 Journals](../../../02-functional/f08-accounting/screens/00-lists/s-f08-l02-journals.md) | Accounting | All | UC-SC20-04 |
| [S-SC20-L01 Budgets](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l01-budgets.md) | Public bodies | All | UC-SC20-01, UC-SC20-02, UC-SC20-17 |
| [S-SC20-L02 Commitments](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l02-commitments.md) | Public bodies | All | UC-SC20-02, UC-SC20-03 |
| [S-SC20-L03 Orders and titles](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l03-payment-orders.md) | Public bodies | All | UC-SC20-03, UC-SC20-04, UC-SC20-08, UC-SC20-20 |
| [S-SC20-L04 Treasury exchanges](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l04-treasury-exchanges.md) | Public bodies | All | UC-SC20-04 |
| [S-SC20-L05 Tender files](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l05-tender-files.md) | Public bodies | All | UC-SC20-05, UC-SC20-06, UC-SC20-07 |
| [S-SC20-L06 Bids](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l06-bids.md) | Public bodies | All | UC-SC20-07 |
| [S-SC20-L07 Public contracts](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l07-public-contracts.md) | Public bodies | All | UC-SC20-08 |
| [S-SC20-L10 Council decisions](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l10-council-decisions.md) | Public bodies | All | UC-SC20-17, UC-SC20-19 |
| [S-SC20-L12 Deliberations](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l12-deliberations.md) | Public bodies | All | UC-SC20-01, UC-SC20-17 |
| [S-SC20-L14 Permit requests](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l14-permit-requests.md) | Public bodies | All | UC-SC20-19 |
| [S-SC20-L15 Public assets](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l15-public-assets.md) | Public bodies | All | UC-SC20-20 |

## Navigation

Each view also sits in its capability's menu (D495):
[Accounting](../../../02-functional/f08-accounting/screens/00-lists/README.md),
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[Public bodies](../../../08-sectors/sc20-public-bodies/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U54 | desktop | ![Workspace, U54, light](mockups/workspace-desktop-light.png) | ![Workspace, U54, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U54 | phone | ![Workspace, U54, light](mockups/workspace-phone-light.png) | ![Workspace, U54, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
