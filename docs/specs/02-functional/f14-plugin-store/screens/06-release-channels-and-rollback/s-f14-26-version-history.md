🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-06 Release channels and rollback](README.md) › 🖥️ S-F14-26 Version history

# 🖥️ S-F14-26 Version history

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Show an installed plugin's versions and roll back to the previous one with its data.

## Entry points

The installed plugin's page, "Version history"; the update done notification.

## Wireframe

```text
Gate Booking, version history
-------------------------------------------------------------------------------
2.4.0   installed 2026-11-02   current
2.3.1   installed 2026-08-14   rollback point until 2026-12-02   [Roll back]
2.3.0   installed 2026-06-01   -
-------------------------------------------------------------------------------
Rolling back exports the changes made since 2026-11-02 (3 days).
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-06 step 3, U07 | desktop | ![FL-F14-06 step 3, U07, light](../../images/06-release-channels-and-rollback/u07-administrator/3-version-history-desktop-light.png) | ![FL-F14-06 step 3, U07, dark](../../images/06-release-channels-and-rollback/u07-administrator/3-version-history-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-26-version-history-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-26-version-history-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-26-version-history-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-26-version-history-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-26-version-history-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-26-version-history-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-26-version-history-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-26-version-history-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Version | E-F14-20 version | number | no | yes |
| Installed | E-F14-02 installation | date | no | yes |
| Rollback point | E-F14-20 expires | date | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Roll back | version row | administrator | changes exported, previous version and data restored |

## States

- Normal: the installed versions with the rollback point and its expiry.
- Empty: "Only one version installed": no rollback offered.
- Loading: the frame and titles show at once with placeholder rows for the versions; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an expired rollback point or a version withdrawn for security.
- Read-only: other roles see the history without the rollback button.
- Offline: not available offline: a rollback runs on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-20 Rollback point](../../data/e-f14-20-rollback-point.md),
[E-F14-02 Plugin installation](../../data/e-f14-02-plugin-installation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-20 Rollback point | Kept | Badge "Kept"; a new record starts here; next: Restored or Expired (UC-F14-03, UC-F14-28); fields editable within the role | U07 | `u07-administrator/s-f14-26-version-history-e-f14-20-rollback-point-kept-desktop-{light,dark}.png` |
| E-F14-20 Rollback point | Restored | Badge "Restored"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f14-26-version-history-e-f14-20-rollback-point-restored-desktop-{light,dark}.png` |
| E-F14-02 Plugin installation | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f14-26-version-history-e-f14-02-plugin-installation-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; tablet.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F14-06 Release channels and rollback](../../flows/fl-f14-06-release-channels-and-rollback.md)

## Open questions

None.

---

⬅️ [S-F14-25 Support terms](../02-buy-and-licence/s-f14-25-support-terms.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-27 Test instances](../08-trials-instances-and-partners/s-f14-27-test-instances.md)
