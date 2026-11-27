🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🤝 [Reseller partner: app shell and home](README.md) › 🧰 U51 Reseller partner: workspace

# 🧰 U51 Reseller partner: workspace

**Status:** ✅ specified

## Purpose

The views [U51 Reseller partner](../../../01-users/personas/u51-reseller-partner.md) works with, embedded on their
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
| [S-F6-L02 Opportunities](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l02-opportunities.md) | Customers and sales | All | UC-F6-27 |
| [S-F6-L19 Commission lines](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l19-commission-lines.md) | Customers and sales | Mine: rep | UC-F6-27 |
| [S-F6-L20 Leads](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l20-leads.md) | Customers and sales | All | UC-F6-27, UC-F14-31 |
| [S-F6-L23 Partners](../../../02-functional/f06-customers-and-sales/screens/00-lists/s-f06-l23-partners.md) | Customers and sales | All | UC-F6-27, UC-F14-31 |
| [S-F14-L24 Partner listings](../../../02-functional/f14-plugin-store/screens/00-lists/s-f14-l24-partner-listings.md) | Plugin store | All | UC-F14-31 |

## Navigation

Each view also sits in its capability's menu (D495):
[Customers and sales](../../../02-functional/f06-customers-and-sales/screens/00-lists/README.md),
[Plugin store](../../../02-functional/f14-plugin-store/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U51 | desktop | ![Workspace, U51, light](mockups/workspace-desktop-light.png) | ![Workspace, U51, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U51 | phone | ![Workspace, U51, light](mockups/workspace-phone-light.png) | ![Workspace, U51, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
