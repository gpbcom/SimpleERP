🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-08 Report and assist](README.md) › 🖥️ S-F12-19 Manufacturing dashboard

# 🖥️ S-F12-19 Manufacturing dashboard

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)

## Purpose

Report production.

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-08 step 1, U13 | desktop | ![FL-F12-08 step 1, U13, light](../../images/08-report-and-assist/u13-owner/1-reports-desktop-light.png) | ![FL-F12-08 step 1, U13, dark](../../images/08-report-and-assist/u13-owner/1-reports-desktop-dark.png) |
| FL-F12-08 step 1, U13 | phone | ![FL-F12-08 step 1, U13, light](../../images/08-report-and-assist/u13-owner/1-reports-phone-light.png) | ![FL-F12-08 step 1, U13, dark](../../images/08-report-and-assist/u13-owner/1-reports-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-19-production-reports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-19-production-reports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-19-production-reports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-19-production-reports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-19-production-reports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-19-production-reports-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-19-production-reports-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-19-production-reports-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Report production, as the wireframe shows.
- Empty: No production in the period yet, with Change the period.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done manufacturing orders and recorded checks, corrected by a new record.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F12-08 Report and assist](../../flows/fl-f12-08-report-and-assist.md)

## Open questions

None.

---

⬅️ [S-F12-18 Waste register](../07-compliance-and-safety/s-f12-18-waste-register.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-20 Production assistant](s-f12-20-production-assistant.md)
