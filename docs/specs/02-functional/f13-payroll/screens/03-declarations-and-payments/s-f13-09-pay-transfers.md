🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-03 Declarations and payments](README.md) › 🖥️ S-F13-09 Pay transfers

# 🖥️ S-F13-09 Pay transfers

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Pay employees by SEPA transfer.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-03 step 1, U45 | desktop | ![FL-F13-03 step 1, U45, light](../../images/03-declarations-and-payments/u45-payroll-officer/1-transfers-desktop-light.png) | ![FL-F13-03 step 1, U45, dark](../../images/03-declarations-and-payments/u45-payroll-officer/1-transfers-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-09-pay-transfers-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-09-pay-transfers-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-09-pay-transfers-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-09-pay-transfers-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-09-pay-transfers-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-09-pay-transfers-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-09-pay-transfers-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-09-pay-transfers-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the transfers of the run per employee, their IBAN check and the bank file state.
- Empty: "No transfer to prepare": shown before the run is approved.
- Loading: the frame and titles show at once with placeholder rows for the transfers; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: a sent file is read-only; accounting sends, the payroll officer prepares.
- Offline: not available offline: the bank file is sent through the bank connector. D38 keeps only today's schedule,
  time and intervention records offline. A banner says the connection is lost; what is on screen stays visible, every
  action is disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-08 Pay transfer](../../data/e-f13-08-pay-transfer.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-08 Pay transfer | Sent | Badge "Sent"; a new record starts here; next: Held (UC-F13-09); fields editable within the role | U05, U45 | `u05-accounting/s-f13-09-pay-transfers-e-f13-08-pay-transfer-sent-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-09-pay-transfers-e-f13-08-pay-transfer-sent-desktop-{light,dark}.png` |
| E-F13-08 Pay transfer | Held | Badge "Held"; next: Sent (UC-F13-09); fields editable within the role | U05, U45 | `u05-accounting/s-f13-09-pay-transfers-e-f13-08-pay-transfer-held-desktop-{light,dark}.png`, `u45-payroll-officer/s-f13-09-pay-transfers-e-f13-08-pay-transfer-held-desktop-{light,dark}.png` |

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

- [FL-F13-03 Declarations and payments](../../flows/fl-f13-03-declarations-and-payments.md)

## Open questions

None.

---

⬅️ [S-F13-08 Payslips](../02-monthly-pay-run/s-f13-08-payslips.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-10 Social declaration](s-f13-10-social-declaration.md)
