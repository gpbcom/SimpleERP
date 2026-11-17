🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-01 Find and install](README.md) › 🖥️ S-F14-03 Updates

# 🖥️ S-F14-03 Updates

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Update with compatibility checks.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-01 step 3, U07 | desktop | ![FL-F14-01 step 3, U07, light](../../images/01-find-and-install/u07-administrator/3-update-desktop-light.png) | ![FL-F14-01 step 3, U07, dark](../../images/01-find-and-install/u07-administrator/3-update-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-03-updates-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-03-updates-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-03-updates-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-03-updates-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-03-updates-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-03-updates-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-03-updates-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-03-updates-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: updates available with their compatibility check and any new permission.
- Empty: "Everything is up to date".
- Loading: the frame and titles show at once with placeholder rows for the updates; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: roles other than the administrator see updates only.
- Offline: not available offline: updates run on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-03 Plugin version](../../data/e-f14-03-plugin-version.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-03 Plugin version | New | Badge "New"; a new record starts here; next: Submitted (UC-F14-08); fields editable within the role | U07 | `u07-administrator/s-f14-03-updates-e-f14-03-plugin-version-new-desktop-{light,dark}.png` |
| E-F14-03 Plugin version | Signed | Badge "Signed"; next: Running (UC-F14-03); fields editable within the role | U07 | `u07-administrator/s-f14-03-updates-e-f14-03-plugin-version-signed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F14-01 Find and install](../../flows/fl-f14-01-find-and-install.md)

## Open questions

None.

---

⬅️ [S-F14-02 Install](s-f14-02-install.md) · ⬆️ [Up](README.md) · ➡️ [S-F14-04 Uninstall](s-f14-04-uninstall.md)
