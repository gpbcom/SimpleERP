🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-04 Alerts and sharing](README.md) › 🖥️ S-F17-19 Access

# 🖥️ S-F17-19 Access

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Restrict access to analyses.

## Entry points

Competitive analysis in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-04 step 3, U13 | desktop | ![FL-F17-04 step 3, U13, light](../../images/04-alerts-and-sharing/u13-owner/3-access-desktop-light.png) | ![FL-F17-04 step 3, U13, dark](../../images/04-alerts-and-sharing/u13-owner/3-access-desktop-dark.png) |
| FL-F17-04 step 3, U13 | phone | ![FL-F17-04 step 3, U13, light](../../images/04-alerts-and-sharing/u13-owner/3-access-phone-light.png) | ![FL-F17-04 step 3, U13, dark](../../images/04-alerts-and-sharing/u13-owner/3-access-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-19-access-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-19-access-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-19-access-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-19-access-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-19-access-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-19-access-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-19-access-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-19-access-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: roles granted per competitor file and the access log.
- Empty: "No access granted": only the owner sees analyses.
- Loading: the frame and titles show at once with placeholder rows for the grants; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the administrator reads the log.
- Offline: not available offline: access is set on the server. D38 keeps only today's schedule, time and intervention
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

- [FL-F17-04 Alerts and sharing](../../flows/fl-f17-04-alerts-and-sharing.md)

## Open questions

None.

---

⬅️ [S-F17-18 Collection settings](../01-set-up-and-profiles/s-f17-18-collection-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-20 Competitor assistant](../03-analyse-and-arm-sales/s-f17-20-competitor-assistant.md)
