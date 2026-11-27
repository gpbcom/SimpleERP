🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-04 Decide](README.md) › 🖥️ S-F23-19 Sharing

# 🖥️ S-F23-19 Sharing

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)

## Purpose

Share and comment a scenario.

## Entry points

What-if simulation and impact in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-04 step 4, U13 | desktop | ![FL-F23-04 step 4, U13, light](../../images/04-decide/u13-owner/4-share-desktop-light.png) | ![FL-F23-04 step 4, U13, dark](../../images/04-decide/u13-owner/4-share-desktop-dark.png) |
| FL-F23-04 step 4, U13 | phone | ![FL-F23-04 step 4, U13, light](../../images/04-decide/u13-owner/4-share-phone-light.png) | ![FL-F23-04 step 4, U13, dark](../../images/04-decide/u13-owner/4-share-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-19-sharing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-19-sharing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-19-sharing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-19-sharing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-19-sharing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-19-sharing-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f23-19-sharing-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f23-19-sharing-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: readers, comments and versions.
- Empty: "Not shared".
- Loading: the frame and titles show at once with placeholder rows for the sharing; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: readers comment only.
- Offline: not available offline: shared online. D38 keeps only today's schedule, time and intervention records offline.
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

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

- [FL-F23-04 Decide](../../flows/fl-f23-04-decide.md)

## Open questions

None.

---

⬅️ [S-F23-18 Change warnings](../05-act-and-watch/s-f23-18-change-warnings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-20 What-if assistant](../02-run/s-f23-20-what-if-assistant.md)
