🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🧩 [Plugin publisher: app shell and home](README.md) › 🧰 U46 Plugin publisher: workspace

# 🧰 U46 Plugin publisher: workspace

**Status:** ✅ specified

## Purpose

The views [U46 Plugin publisher](../../../01-users/personas/u46-plugin-publisher.md) works with, embedded on their
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
| [S-F9-L03 Departments](../../../02-functional/f09-hr-and-projects/screens/00-lists/s-f09-l03-departments.md) | HR and projects | Mine: manager | D519, VC-8 |
| [S-F11-L01 Websites](../../../02-functional/f11-online-shop/screens/00-lists/s-f11-l01-websites.md) | Online shop (plugin) | All | UC-F14-32 |
| [S-F14-L01 Store listings](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l01-store-listings.md) | Plugin store | Open: New, Complete, Refused | UC-F14-08, UC-F14-22, UC-F14-23 |
| [S-F14-L02 Plugin installations](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l02-plugin-installations.md) | Plugin store | All | UC-F14-24 |
| [S-F14-L03 Plugin versions](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l03-plugin-versions.md) | Plugin store | All | UC-F14-08, UC-F14-09, UC-F14-10, UC-F14-11 |
| [S-F14-L04 Plugin price plans](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l04-plugin-price-plans.md) | Plugin store | Open: Published | UC-F14-27, UC-F14-12 |
| [S-F14-L06 Plugin reviews](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l06-plugin-reviews.md) | Plugin store | All | UC-F14-07 |
| [S-F14-L07 Plugin check reports](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l07-plugin-check-reports.md) | Plugin store | All | UC-F14-09, UC-F14-10, UC-F14-21 |
| [S-F14-L08 Payouts](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l08-payouts.md) | Plugin store | Open: Sent, Reconciled, Held | UC-F14-13, UC-F14-18 |
| [S-F14-L13 Usage metrics](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l13-usage-metrics.md) | Plugin store | All | UC-F14-18 |
| [S-F14-L14 Software bill of materials](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l14-software-bill-of-materials.md) | Plugin store | All | UC-F14-21 |
| [S-F14-L15 End-of-life notices](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l15-end-of-life-notices.md) | Plugin store | Open: Announced, TakenOver | UC-F14-22 |
| [S-F14-L16 Maintainer transfers](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l16-maintainer-transfers.md) | Plugin store | Open: Asked, Approved, Refused | UC-F14-23 |
| [S-F14-L17 Rollouts](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l17-rollouts.md) | Plugin store | Open: Beta, Running, Paused | UC-F14-24, UC-F14-25 |
| [S-F14-L18 Listing translations](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l18-listing-translations.md) | Plugin store | All | UC-F14-26 |
| [S-F14-L19 Support terms](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l19-support-terms.md) | Plugin store | All | UC-F14-27 |
| [S-F14-L21 Plugin security reviews](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l21-plugin-security-reviews.md) | Plugin store | All | UC-F14-10, UC-F14-23 |
| [S-F14-L22 Test instances](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l22-test-instances.md) | Plugin store | All | UC-F14-29 |
| [S-F14-L25 Themes](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l25-themes.md) | Plugin store | All | UC-F14-32 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[HR and projects](../../../02-functional/f09-hr-and-projects/screens/00-lists/README.md),
[Online shop (plugin)](../../../02-functional/f11-online-shop/screens/00-lists/README.md),
[Plugin store](../../../02-functional/f14-plugin-store/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U46 | desktop | ![Workspace, U46, light](mockups/workspace-desktop-light.png) | ![Workspace, U46, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U46 | phone | ![Workspace, U46, light](mockups/workspace-phone-light.png) | ![Workspace, U46, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
