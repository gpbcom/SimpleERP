🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-08 Report and assist](README.md) › 🖥️ S-F12-20 Production assistant

# 🖥️ S-F12-20 Production assistant

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md)
- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md)

## Purpose

Ask the AI assistant about production.

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-08 step 3, U21 | desktop | ![FL-F12-08 step 3, U21, light](../../images/08-report-and-assist/u21-production-planner/3-production-assistant-desktop-light.png) | ![FL-F12-08 step 3, U21, dark](../../images/08-report-and-assist/u21-production-planner/3-production-assistant-desktop-dark.png) |
| FL-F12-08 step 3, U21 | phone | ![FL-F12-08 step 3, U21, light](../../images/08-report-and-assist/u21-production-planner/3-production-assistant-phone-light.png) | ![FL-F12-08 step 3, U21, dark](../../images/08-report-and-assist/u21-production-planner/3-production-assistant-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-20-production-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-20-production-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-20-production-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-20-production-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-20-production-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-20-production-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-20-production-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-20-production-assistant-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Ask the AI assistant about production, as the wireframe shows.
- Empty: No question yet, with Ask a question.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done manufacturing orders and recorded checks, corrected by a new record.
- Offline: The AI assistant says it is offline; questions are queued and answered when the network is back, with a
  notification, and changes still need confirmation then
  ([D182](../../../../06-decisions/f03-assistant/d182-offline-assistant.md)).

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

⬅️ [S-F12-19 Manufacturing dashboard](s-f12-19-manufacturing-dashboard.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-21 Calibration](../10-people-and-tools/s-f12-21-calibration.md)
