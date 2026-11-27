🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-05 Store operations](README.md) › 🖥️ S-F14-19 Moderation

# 🖥️ S-F14-19 Moderation

**Status:** ✅ specified

## Personas

- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)

## Purpose

Moderate the store with transparent ranking.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-05 step 3, U11 | desktop | ![FL-F14-05 step 3, U11, light](../../images/05-store-operations/u11-provider-admin/3-moderate-desktop-light.png) | ![FL-F14-05 step 3, U11, dark](../../images/05-store-operations/u11-provider-admin/3-moderate-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-19-moderation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-19-moderation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-19-moderation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-19-moderation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-19-moderation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-19-moderation-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-19-moderation-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-19-moderation-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: reported listings and reviews, actions taken and the ranking rules published.
- Empty: "Nothing reported".
- Loading: the frame and titles show at once with placeholder rows for the reports; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: published ranking rules are read-only until a new version.
- Offline: not available offline: moderation acts on the store. D38 keeps only today's schedule, time and intervention
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

- [FL-F14-05 Store operations](../../flows/fl-f14-05-store-operations.md)

## Open questions

None.

---

⬅️ [S-F14-18 Publisher dashboard](../04-money-and-taxes/s-f14-18-publisher-dashboard.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-20 Store assistant](../01-find-and-install/s-f14-20-store-assistant.md)
