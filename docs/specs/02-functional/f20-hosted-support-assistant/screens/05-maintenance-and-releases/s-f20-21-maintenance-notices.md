🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-05 Maintenance and releases](README.md) › 🖥️ S-F20-21 Maintenance notices

# 🖥️ S-F20-21 Maintenance notices

**Status:** ✅ specified

## Personas

- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Plan and show maintenance windows.

## Entry points

Support, Notices; the banner in SimpleERP.

## Wireframe

```text
Maintenance notices                            [Plan maintenance] (engineer)
-------------------------------------------------------------------------------
Window                       Title               Effect                 State
2026-11-22 22:00 to 23:00    Database upgrade    up to 10 min down      planned
-------------------------------------------------------------------------------
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-05 step 1, U48 | desktop | ![FL-F20-05 step 1, U48, light](../../images/05-maintenance-and-releases/u48-hosting-engineer/1-maintenance-notices-desktop-light.png) | ![FL-F20-05 step 1, U48, dark](../../images/05-maintenance-and-releases/u48-hosting-engineer/1-maintenance-notices-desktop-dark.png) |
| FL-F20-05 step 1, U48 | phone | ![FL-F20-05 step 1, U48, light](../../images/05-maintenance-and-releases/u48-hosting-engineer/1-maintenance-notices-phone-light.png) | ![FL-F20-05 step 1, U48, dark](../../images/05-maintenance-and-releases/u48-hosting-engineer/1-maintenance-notices-phone-dark.png) |
| Error E1, U48 | desktop | ![Error E1, U48, light](../../images/05-maintenance-and-releases/u48-hosting-engineer/e1-maintenance-notices-refused-desktop-light.png) | ![Error E1, U48, dark](../../images/05-maintenance-and-releases/u48-hosting-engineer/e1-maintenance-notices-refused-desktop-dark.png) |
| Error E1, U48 | phone | ![Error E1, U48, light](../../images/05-maintenance-and-releases/u48-hosting-engineer/e1-maintenance-notices-refused-phone-light.png) | ![Error E1, U48, dark](../../images/05-maintenance-and-releases/u48-hosting-engineer/e1-maintenance-notices-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-21-maintenance-notices-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-21-maintenance-notices-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-21-maintenance-notices-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-21-maintenance-notices-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-21-maintenance-notices-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-21-maintenance-notices-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f20-21-maintenance-notices-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f20-21-maintenance-notices-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Window | E-F20-13 window | date and times | yes (engineer) | yes |
| Title | E-F20-13 title | text | yes | yes |
| Effect | E-F20-13 effect | text | yes | yes |
| State | E-F20-13 status | list | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Plan | header | hosting engineer | notice sent |
| Close | row | hosting engineer | done |

## States

- Normal: notices with windows and states.
- Empty: "No maintenance planned".
- Loading: the frame and titles show at once with placeholder rows for the notices; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a notice too late, refused.
- Read-only: customers read.
- Offline: The banner last loaded stays visible. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F20-13 Maintenance notice](../../data/e-f20-13-maintenance-notice.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-13 Maintenance notice | Planned | Badge "Planned"; a new record starts here; next: Running (UC-F20-21); fields editable within the role | U07, U13, U48 | `u07-administrator/s-f20-21-maintenance-notices-e-f20-13-maintenance-notice-planned-desktop-{light,dark}.png`, `u13-owner/s-f20-21-maintenance-notices-e-f20-13-maintenance-notice-planned-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f20-21-maintenance-notices-e-f20-13-maintenance-notice-planned-{desktop,phone}-{light,dark}.png` |
| E-F20-13 Maintenance notice | Running | Badge "Running"; next: Done or Overrun (UC-F20-21); fields editable within the role | U07, U13, U48 | `u07-administrator/s-f20-21-maintenance-notices-e-f20-13-maintenance-notice-running-desktop-{light,dark}.png`, `u13-owner/s-f20-21-maintenance-notices-e-f20-13-maintenance-notice-running-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f20-21-maintenance-notices-e-f20-13-maintenance-notice-running-{desktop,phone}-{light,dark}.png` |
| E-F20-13 Maintenance notice | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U07, U13, U48 | `u07-administrator/s-f20-21-maintenance-notices-e-f20-13-maintenance-notice-done-desktop-{light,dark}.png`, `u13-owner/s-f20-21-maintenance-notices-e-f20-13-maintenance-notice-done-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f20-21-maintenance-notices-e-f20-13-maintenance-notice-done-{desktop,phone}-{light,dark}.png` |
| E-F20-13 Maintenance notice | Overrun | Badge "Overrun"; next: Done (UC-F20-21); fields editable within the role | U07, U13, U48 | `u07-administrator/s-f20-21-maintenance-notices-e-f20-13-maintenance-notice-overrun-desktop-{light,dark}.png`, `u13-owner/s-f20-21-maintenance-notices-e-f20-13-maintenance-notice-overrun-{desktop,phone}-{light,dark}.png`, `u48-hosting-engineer/s-f20-21-maintenance-notices-e-f20-13-maintenance-notice-overrun-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; customers read on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F20-05 Maintenance and releases](../../flows/fl-f20-05-maintenance-and-releases.md)

## Open questions

None.

---

⬅️ [S-F20-20 Export](../04-govern-the-assistant/s-f20-20-export.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-22 Release notes](s-f20-22-release-notes.md)
