🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 🪟 [Views](../README.md) ›
🗳️ [Elected official: app shell and home](README.md) › 🧰 U55 Elected official: workspace

# 🧰 U55 Elected official: workspace

**Status:** ✅ specified

## Purpose

The views [U55 Elected official](../../../01-users/personas/u55-elected-official.md) works with, embedded on their
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
| [S-F3-L01 Conversations](../../../02-functional/f03-assistant/screens/00-lists/s-f03-l01-conversations.md) | Assistant | Open: Private, Shared | UC-SC20-16 |
| [S-SC20-L01 Budgets](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l01-budgets.md) | Public bodies | Needs attention | UC-SC20-01, UC-SC20-16, UC-SC20-17 |
| [S-SC20-L05 Tender files](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l05-tender-files.md) | Public bodies | Needs attention | UC-SC20-07 |
| [S-SC20-L06 Bids](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l06-bids.md) | Public bodies | Needs attention | UC-SC20-07 |
| [S-SC20-L10 Council decisions](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l10-council-decisions.md) | Public bodies | Needs attention | UC-SC20-12, UC-SC20-17 |
| [S-SC20-L12 Deliberations](../../../08-sectors/sc20-public-bodies/screens/00-lists/s-sc20-l12-deliberations.md) | Public bodies | Needs attention | UC-SC20-01, UC-SC20-12, UC-SC20-17 |

## Navigation

Each view also sits in its capability's menu (D495):
[Assistant](../../../02-functional/f03-assistant/screens/00-lists/README.md),
[Public bodies](../../../08-sectors/sc20-public-bodies/screens/00-lists/README.md).

## Example images

Drawn in step S8 (36k), with the list pages (D490): the workspace on a desktop and a phone, light and dark.

| Shows | Device | Light | Dark |
|---|---|---|---|
| Workspace, U55 | desktop | ![Workspace, U55, light](mockups/workspace-desktop-light.png) | ![Workspace, U55, dark](mockups/workspace-desktop-dark.png) |
| Workspace, U55 | phone | ![Workspace, U55, light](mockups/workspace-phone-light.png) | ![Workspace, U55, dark](mockups/workspace-phone-dark.png) |

---

⬆️ [Up](README.md)
