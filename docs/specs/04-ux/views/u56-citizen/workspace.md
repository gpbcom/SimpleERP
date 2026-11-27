🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🏘️ [Citizen: app shell and home](README.md) › 🧰 U56 Citizen: workspace

# 🧰 U56 Citizen: workspace

**Status:** ✅ specified

## Purpose

The views [U56 Citizen](../../../01-users/personas/u56-citizen.md) works with, embedded on their
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
| [S-F2-L18 Resource bookings](../../../02-functional/f02-no-code-configuration/screens/00-lists/s-f02-l18-resource-bookings.md) | No-code configuration | Open: Requested, Confirmed, NoShow | UC-SC20-10 |
| [S-SC20-L03 Orders and titles](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l03-payment-orders.md) | Public bodies | All | UC-SC20-10, UC-SC20-11 |
| [S-SC20-L08 Citizen requests](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l08-citizen-requests.md) | Public bodies | All | UC-SC20-09, UC-SC20-19 |
| [S-SC20-L09 Hall bookings](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l09-hall-bookings.md) | Public bodies | All | UC-SC20-10 |
| [S-SC20-L10 Council decisions](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l10-council-decisions.md) | Public bodies | All | UC-SC20-19 |
| [S-SC20-L13 Civil records](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l13-civil-records.md) | Public bodies | All | UC-SC20-18 |
| [S-SC20-L14 Permit requests](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l14-permit-requests.md) | Public bodies | All | UC-SC20-19 |

## Navigation

Each view also sits in its capability's menu (D495):
[No-code configuration](../../../02-functional/f02-no-code-configuration/screens/00-lists/README.md),
[Public bodies](../../../08-sectors/sc20-public-bodies/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U56 | desktop | ![Workspace, U56, light](mockups/workspace-desktop-light.png) | ![Workspace, U56, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U56 | phone | ![Workspace, U56, light](mockups/workspace-phone-light.png) | ![Workspace, U56, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
