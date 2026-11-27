🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F8-32 Cash position

# 🖥️ S-F8-32 Cash position

**Status:** ✅ specified

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md): the position and the alerts, on a phone.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the position and the alerts, on a phone.

## Purpose

Read today's cash and the forecast of the coming weeks, and see what is behind each day.

## Entry points

The home screen's cash tile on a phone; Accounting › Cash position; the alert.

## Wireframe

```text
+---------------------------------------------+
| Cash position          2026-11-14           |
|---------------------------------------------|
| Today          84,300 EUR                   |
| Lowest point   12,100 EUR  on 2027-01-05    |
| Floor          20,000 EUR   [alert 3 days]  |
|---------------------------------------------|
| [chart: balance, next 13 weeks]             |
| 2027-01-05  rent run, VAT, payroll          |
| [See the items] [What if...] [Ask]          |
+---------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-11 step 4, U31 | phone | ![FL-F8-11 step 4, U31, light](../../images/11-treasury-and-payment-means/u31-treasurer/4-cash-position-phone-light.png) | ![FL-F8-11 step 4, U31, dark](../../images/11-treasury-and-payment-means/u31-treasurer/4-cash-position-phone-dark.png) |
| FL-F8-11 step 4, U31 | desktop | ![FL-F8-11 step 4, U31, light](../../images/11-treasury-and-payment-means/u31-treasurer/4-cash-position-desktop-light.png) | ![FL-F8-11 step 4, U31, dark](../../images/11-treasury-and-payment-means/u31-treasurer/4-cash-position-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-32-cash-position-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-32-cash-position-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-32-cash-position-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-32-cash-position-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-32-cash-position-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-32-cash-position-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f08-32-cash-position-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f08-32-cash-position-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Balance today | E-F8-04 | amount with currency | no | yes |
| Lowest point and date | E-F8-37 | amount and date | no | yes |
| Floor | E-F8-37 | amount with currency | yes, by treasurer | yes |
| Chart | E-F8-37 daily balances | line chart | no | yes |
| Items of a day | E-F6-05, E-F7-05, E-F8-34, E-F8-16 | list | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| See the items | day | treasurer, owner | the open items and plans behind a day |
| What if | chart | treasurer | moves a payment or receipt to see the forecast; not saved |
| Set the floor | header | treasurer | the amount that raises an alert |
| Ask | header | treasurer, owner | the AI assistant answers from the forecast |

## States

- Normal: the balance today, the lowest point, the floor and the chart of the next weeks.
- Empty: No bank account connected, with Connect a bank.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a bank
  connection that failed shows the account and the age of its last balance.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-37 Cash forecast](../../data/e-f08-37-cash-forecast.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-37 Cash forecast | Current | Badge "Current"; a new record starts here; next: Superseded (UC-F8-33); fields editable within the role | U31, U13 | `u31-treasurer/s-f08-32-cash-position-e-f08-37-cash-forecast-current-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f08-32-cash-position-e-f08-37-cash-forecast-current-{desktop,phone}-{light,dark}.png` |
| E-F8-37 Cash forecast | Superseded | Badge "Superseded"; next: Archived (UC-F8-33); fields editable within the role | U31, U13 | `u31-treasurer/s-f08-32-cash-position-e-f08-37-cash-forecast-superseded-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f08-32-cash-position-e-f08-37-cash-forecast-superseded-{desktop,phone}-{light,dark}.png` |
| E-F8-37 Cash forecast | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U31, U13 | `u31-treasurer/s-f08-32-cash-position-e-f08-37-cash-forecast-archived-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f08-32-cash-position-e-f08-37-cash-forecast-archived-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Built for a phone first: the balance, the lowest point and the chart on one screen; items open as a drawer. The desktop
page adds the table of days.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F8-11 Treasury and payment means](../../flows/fl-f08-11-treasury-and-payment-means.md)

## Open questions

None.

---

⬅️ [S-F8-31 FX revaluation](s-f08-31-fx-revaluation.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-33 Payment initiation](s-f08-33-payment-initiation.md)
