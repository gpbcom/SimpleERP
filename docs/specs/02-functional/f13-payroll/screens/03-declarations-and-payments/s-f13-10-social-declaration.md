🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-03 Declarations and payments](README.md) › 🖥️ S-F13-10 Social declaration

# 🖥️ S-F13-10 Social declaration

**Status:** ✅ specified

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)

## Purpose

File the monthly social declaration and handle returns.

## Entry points

Payroll in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-03 step 2, U45 | desktop | ![FL-F13-03 step 2, U45, light](../../images/03-declarations-and-payments/u45-payroll-officer/2-declaration-desktop-light.png) | ![FL-F13-03 step 2, U45, dark](../../images/03-declarations-and-payments/u45-payroll-officer/2-declaration-desktop-dark.png) |
| Error E1, U45 | desktop | ![Error E1, U45, light](../../images/03-declarations-and-payments/u45-payroll-officer/e1-rejected-desktop-light.png) | ![Error E1, U45, dark](../../images/03-declarations-and-payments/u45-payroll-officer/e1-rejected-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-10-social-declaration-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-10-social-declaration-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-10-social-declaration-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-10-social-declaration-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-10-social-declaration-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-10-social-declaration-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-10-social-declaration-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-10-social-declaration-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the monthly declaration's state, its deadline and the returns to handle.
- Empty: "No declaration for this period yet": shown before the run is paid.
- Loading: the frame and titles show at once with placeholder rows for the declaration and its returns; within 1 second
  (D408) the data replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: a filed and accepted declaration is read-only.
- Offline: not available offline: filing needs the connector (T12). D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F13-09 Social declaration](../../data/e-f13-09-social-declaration.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-09 Social declaration | Accepted | Badge "Accepted"; a new record starts here; next: Filed, Late or Rejected (UC-F13-24, UC-F13-10); fields editable within the role | U45 | `u45-payroll-officer/s-f13-10-social-declaration-e-f13-09-social-declaration-accepted-desktop-{light,dark}.png` |
| E-F13-09 Social declaration | Filed | Badge "Filed"; next: Returned or Rejected (UC-F13-10); fields editable within the role | U45 | `u45-payroll-officer/s-f13-10-social-declaration-e-f13-09-social-declaration-filed-desktop-{light,dark}.png` |
| E-F13-09 Social declaration | Late | Badge "Late"; next: Filed (UC-F13-24); fields editable within the role | U45 | `u45-payroll-officer/s-f13-10-social-declaration-e-f13-09-social-declaration-late-desktop-{light,dark}.png` |
| E-F13-09 Social declaration | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U45 | `u45-payroll-officer/s-f13-10-social-declaration-e-f13-09-social-declaration-rejected-desktop-{light,dark}.png` |
| E-F13-09 Social declaration | Returned | Badge "Returned"; final: read-only, no next state; the history shows how it got here | U45 | `u45-payroll-officer/s-f13-10-social-declaration-e-f13-09-social-declaration-returned-desktop-{light,dark}.png` |

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

⬅️ [S-F13-09 Pay transfers](s-f13-09-pay-transfers.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-11 Corrections](s-f13-11-corrections.md)
