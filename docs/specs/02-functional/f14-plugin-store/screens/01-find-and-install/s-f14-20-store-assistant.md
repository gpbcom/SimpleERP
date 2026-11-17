🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-01 Find and install](README.md) › 🖥️ S-F14-20 Store assistant

# 🖥️ S-F14-20 Store assistant

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Ask the AI assistant to find or set up a plugin.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-01 step 5, U07 | desktop | ![FL-F14-01 step 5, U07, light](../../images/01-find-and-install/u07-administrator/5-assistant-desktop-light.png) | ![FL-F14-01 step 5, U07, dark](../../images/01-find-and-install/u07-administrator/5-assistant-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-20-store-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-20-store-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-20-store-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-20-store-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-20-store-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-20-store-assistant-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-20-store-assistant-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-20-store-assistant-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the conversation with plugins proposed and installs to confirm.
- Empty: "Ask for a plugin for your need": example questions.
- Loading: the frame and titles show at once with placeholder rows for the conversation; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: users without install rights get answers but no install button.
- Offline: the AI assistant says it is offline; the question is queued and answered when the network is back, with a
  notification (D182).

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

⬅️ [S-F14-19 Moderation](../05-store-operations/s-f14-19-moderation.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-21 Dependency report](../03-publish/s-f14-21-dependency-report.md)
