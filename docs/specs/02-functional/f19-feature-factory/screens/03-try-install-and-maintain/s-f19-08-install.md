🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-03 Try, install and maintain](README.md) › 🖥️ S-F19-08 Install

# 🖥️ S-F19-08 Install

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Accept and install the feature.

## Entry points

Feature factory in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-03 step 2, U07 | desktop | ![FL-F19-03 step 2, U07, light](../../images/03-try-install-and-maintain/u07-administrator/2-install-desktop-light.png) | ![FL-F19-03 step 2, U07, dark](../../images/03-try-install-and-maintain/u07-administrator/2-install-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-08-install-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-08-install-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-08-install-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-08-install-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-08-install-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-08-install-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f19-08-install-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f19-08-install-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the install step and the billing start.
- Empty: never empty: it opens from an accepted try-out.
- Loading: the frame and titles show at once with placeholder rows for the install; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: installed versions are read-only.
- Offline: not available offline: installs run online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

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

- [FL-F19-03 Try, install and maintain](../../flows/fl-f19-03-try-install-and-maintain.md)

## Open questions

None.

---

⬅️ [S-F19-07 Try-out](s-f19-07-try-out.md) · ⬆️ [Up](README.md) · ➡️ [S-F19-09 Changes](s-f19-09-changes.md)
