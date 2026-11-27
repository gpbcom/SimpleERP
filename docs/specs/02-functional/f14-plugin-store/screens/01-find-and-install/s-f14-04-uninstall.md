🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-01 Find and install](README.md) › 🖥️ S-F14-04 Uninstall

# 🖥️ S-F14-04 Uninstall

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Uninstall and export the plugin's data.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-01 step 4, U07 | desktop | ![FL-F14-01 step 4, U07, light](../../images/01-find-and-install/u07-administrator/4-uninstall-desktop-light.png) | ![FL-F14-01 step 4, U07, dark](../../images/01-find-and-install/u07-administrator/4-uninstall-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-04-uninstall-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-04-uninstall-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-04-uninstall-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-04-uninstall-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-04-uninstall-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-04-uninstall-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-04-uninstall-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-04-uninstall-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the plugin to remove, the dependent plugins, the export format and the confirmation.
- Empty: "No dependent plugin": shown when none depends on it.
- Loading: the frame and titles show at once with placeholder rows for the dependencies and export; within 1 second
  (D408) the data replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: roles other than the administrator cannot uninstall.
- Offline: not available offline: the export runs on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

⬅️ [S-F14-03 Updates](s-f14-03-updates.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-05 Purchase](../02-buy-and-licence/s-f14-05-purchase.md)
