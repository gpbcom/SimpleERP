🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F13-06 Assistant](README.md) ›
🖥️ S-F13-20 Payroll assistant

# 🖥️ S-F13-20 Payroll assistant

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)

## Purpose

Ask the AI assistant about pay.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-06 step 1, U01 | phone | ![FL-F13-06 step 1, U01, light](../../images/06-assistant/u01-employee/1-ask-phone-light.png) | ![FL-F13-06 step 1, U01, dark](../../images/06-assistant/u01-employee/1-ask-phone-dark.png) |
| FL-F13-06 step 1, U01 | desktop | ![FL-F13-06 step 1, U01, light](../../images/06-assistant/u01-employee/1-ask-desktop-light.png) | ![FL-F13-06 step 1, U01, dark](../../images/06-assistant/u01-employee/1-ask-desktop-dark.png) |
| Error E1, U01 | phone | ![Error E1, U01, light](../../images/06-assistant/u01-employee/e1-other-pay-phone-light.png) | ![Error E1, U01, dark](../../images/06-assistant/u01-employee/e1-other-pay-phone-dark.png) |
| Error E1, U01 | desktop | ![Error E1, U01, light](../../images/06-assistant/u01-employee/e1-other-pay-desktop-light.png) | ![Error E1, U01, dark](../../images/06-assistant/u01-employee/e1-other-pay-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-20-payroll-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-20-payroll-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-20-payroll-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-20-payroll-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-20-payroll-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-20-payroll-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f13-20-payroll-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f13-20-payroll-assistant-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the conversation with answers from the user's own pay data and confirmations for actions.
- Empty: "Ask about your payslip": example questions are shown.
- Loading: the frame and titles show at once with placeholder rows for the conversation; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: an employee sees only their own data (BR-F13-15).
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

- [FL-F13-06 Assistant](../../flows/fl-f13-06-assistant.md)

## Open questions

None.

---

⬅️ [S-F13-19 Rate updates](../05-reports-and-rules/s-f13-19-rate-updates.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-21 Schemes](../07-schemes-and-special-contracts/s-f13-21-schemes.md)
