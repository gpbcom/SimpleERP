🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
📈 [Shareholder: app shell and home](README.md) › 🧰 U50 Shareholder: workspace

# 🧰 U50 Shareholder: workspace

**Status:** ✅ specified

## Purpose

The views [U50 Shareholder](../../../01-users/personas/u50-shareholder.md) works with, embedded on their
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
| [S-F15-L07 Corporate decisions](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l07-corporate-decisions.md) | Legal assistant | All | UC-F15-14, UC-F15-18 |
| [S-F15-L14 Corporate filings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l14-corporate-filings.md) | Legal assistant | All | UC-F15-14, UC-F15-18 |
| [S-F15-L15 Shareholdings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l15-shareholdings.md) | Legal assistant | Needs attention | UC-F15-14, UC-F15-18 |
| [S-F15-L19 General meetings](../../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l19-general-meetings.md) | Legal assistant | Needs attention | UC-F15-18 |

## Navigation

Each view also sits in its capability's menu (D495):
[Legal assistant](../../../02-functional/f15-legal-assistant/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U50 | desktop | ![Workspace, U50, light](mockups/workspace-desktop-light.png) | ![Workspace, U50, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U50 | phone | ![Workspace, U50, light](mockups/workspace-phone-light.png) | ![Workspace, U50, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
