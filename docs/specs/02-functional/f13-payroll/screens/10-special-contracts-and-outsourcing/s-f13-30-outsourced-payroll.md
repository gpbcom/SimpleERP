🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F13-10 Special contracts and outsourced payroll](README.md) › 🖥️ S-F13-30 Outsourced payroll

# 🖥️ S-F13-30 Outsourced payroll

**Status:** 🔄 waiting for the owner

## Personas

- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md): the month's handover from freeze to
  approval.
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md): the handover and the entries, to
  read.

## Purpose

Freeze the month's inputs, send them to the payroll firm and check what comes back.

## Entry points

Payroll (plugin) › Outsourced payroll; the pay run's calendar when the establishment is outsourced.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Handover: November 2026                                 Frozen   [Freeze] [Send] [Approve]  |
|---------------------------------------------------------------------------------------------|
| Firm  Payroll firm connection OK     Employees 42     Inputs complete 42 of 42              |
| Sent 2026-11-24 09:12   Acknowledged 09:13   Returned 2026-11-26                            |
| Net to pay  96,420.10 EUR   Last month  95,880.40 EUR   Differences  2 lines                |
| EMPLOYEE   INPUT NET   RETURNED NET   GAP                                                   |
| Karim D.   2,104.50    2,014.50       -90.00   [Ask the firm]                               |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F13-10 step 3, U45 | desktop | ![FL-F13-10 step 3, U45, light](../../images/10-special-contracts-and-outsourcing/u45-payroll-officer/3-outsourced-payroll-desktop-light.png) | ![FL-F13-10 step 3, U45, dark](../../images/10-special-contracts-and-outsourcing/u45-payroll-officer/3-outsourced-payroll-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f13-30-outsourced-payroll-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f13-30-outsourced-payroll-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f13-30-outsourced-payroll-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f13-30-outsourced-payroll-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f13-30-outsourced-payroll-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f13-30-outsourced-payroll-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f13-30-outsourced-payroll-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f13-30-outsourced-payroll-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Month and firm | E-F13-30 month, firm | text | no | yes |
| Inputs complete | E-F13-30 counts | two numbers | no | yes |
| Sent and acknowledged | E-F13-30 send log | date and time | no | no |
| Returned totals | E-F13-30 returned | amounts | no | yes |
| Differences | E-F13-30 differences | list of employees and amounts | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Freeze | header | payroll officer | the inputs of the month are locked |
| Send | header | payroll officer | the file goes to the firm |
| Ask the firm | row | payroll officer | a message to the firm about one line |
| Approve | header | payroll officer | the payment file and the entries are prepared |
| Correction handover | header | payroll officer | reopens the employees concerned only |

## States

- Normal: the month's inputs, the send log, the returned totals and the differences.
- Empty: No handover yet, with Set the establishment to outsourced payroll.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused file
  shows its format error and the line numbers.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F13-30 Payroll handover](../../data/e-f13-30-payroll-handover.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F13-30 Payroll handover | Draft | Badge "Draft"; a new record starts here; next: Frozen (BR-F13-27); fields editable within the role | U45, U08 | `u45-payroll-officer/s-f13-30-outsourced-payroll-e-f13-30-payroll-handover-draft-desktop-{light,dark}.png`, `u08-external-accountant/s-f13-30-outsourced-payroll-e-f13-30-payroll-handover-draft-desktop-{light,dark}.png` |
| E-F13-30 Payroll handover | Frozen | Badge "Frozen"; next: Sent (UC-F13-37); fields editable within the role | U45, U08 | `u45-payroll-officer/s-f13-30-outsourced-payroll-e-f13-30-payroll-handover-frozen-desktop-{light,dark}.png`, `u08-external-accountant/s-f13-30-outsourced-payroll-e-f13-30-payroll-handover-frozen-desktop-{light,dark}.png` |
| E-F13-30 Payroll handover | Sent | Badge "Sent"; next: Returned (UC-F13-37); fields editable within the role | U45, U08 | `u45-payroll-officer/s-f13-30-outsourced-payroll-e-f13-30-payroll-handover-sent-desktop-{light,dark}.png`, `u08-external-accountant/s-f13-30-outsourced-payroll-e-f13-30-payroll-handover-sent-desktop-{light,dark}.png` |
| E-F13-30 Payroll handover | Returned | Badge "Returned"; next: Approved (UC-F13-37); fields editable within the role | U45, U08 | `u45-payroll-officer/s-f13-30-outsourced-payroll-e-f13-30-payroll-handover-returned-desktop-{light,dark}.png`, `u08-external-accountant/s-f13-30-outsourced-payroll-e-f13-30-payroll-handover-returned-desktop-{light,dark}.png` |
| E-F13-30 Payroll handover | Approved | Badge "Approved"; next: Closed (UC-F13-37); fields editable within the role | U45, U08 | `u45-payroll-officer/s-f13-30-outsourced-payroll-e-f13-30-payroll-handover-approved-desktop-{light,dark}.png`, `u08-external-accountant/s-f13-30-outsourced-payroll-e-f13-30-payroll-handover-approved-desktop-{light,dark}.png` |
| E-F13-30 Payroll handover | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U45, U08 | `u45-payroll-officer/s-f13-30-outsourced-payroll-e-f13-30-payroll-handover-closed-desktop-{light,dark}.png`, `u08-external-accountant/s-f13-30-outsourced-payroll-e-f13-30-payroll-handover-closed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F13-10](../../flows/fl-f13-10-special-contracts-and-outsourcing.md)

## Open questions

None.

---

⬅️ [S-F13-29 Days-based contracts](s-f13-29-days-based-contracts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-31 Staff representatives](s-f13-31-staff-representatives.md)
