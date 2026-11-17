🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F8-31 FX revaluation

# 🖥️ S-F8-31 FX revaluation

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the runs of their periods.

## Purpose

Revalue open foreign-currency items at the closing rate and post the unrealised difference.

## Entry points

Accounting › Closing › FX revaluation; the closing checklist's FX step.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| FX revaluation: October 2026                     Computed       [Post] [Recompute]           |
|---------------------------------------------------------------------------------------------|
| CURRENCY  ITEMS  BOOKED (EUR)  CLOSING RATE  AT CLOSING (EUR)  UNREALISED                    |
| USD       14     48,300        0.9412        47,500            -800                         |
| GBP       3      12,100        1.1560        11,660            -440                         |
| Items without a rate: 0                            Total unrealised: -1,240 EUR              |
| Reversal planned for 2026-11-01                                                              |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-11 step 3, U05 | desktop | ![FL-F8-11 step 3, U05, light](../../images/11-treasury-and-payment-means/u05-accounting/3-fx-revaluation-desktop-light.png) | ![FL-F8-11 step 3, U05, dark](../../images/11-treasury-and-payment-means/u05-accounting/3-fx-revaluation-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-31-fx-revaluation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-31-fx-revaluation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-31-fx-revaluation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-31-fx-revaluation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-31-fx-revaluation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-31-fx-revaluation-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-31-fx-revaluation-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-31-fx-revaluation-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Period | E-F8-36 period | month and year | no | yes |
| Currency, items, booked, closing | E-F8-36 lines | table | rate: yes | yes |
| Unrealised difference | E-F8-36 | amount with sign | no | yes |
| Entry and reversal | E-F8-03 | two links | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Recompute | header | accounting | the run is computed again with the rates shown |
| Override a rate | row | accounting | a rate for one item, with a reason |
| Post | header | accounting | the entry is posted and the reversal planned |

## States

- Normal: the currencies with their items, rates and unrealised differences.
- Empty: No foreign-currency item at this period end.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a currency
  without a rate is listed with its items.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-36 Revaluation run](../../data/e-f08-36-revaluation-run.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-36 Revaluation run | Computed | Badge "Computed"; a new record starts here; next: Posted (UC-F8-32); fields editable within the role | U05 | `u05-accounting/s-f08-31-fx-revaluation-e-f08-36-revaluation-run-computed-desktop-{light,dark}.png` |
| E-F8-36 Revaluation run | Posted | Badge "Posted"; next: Reversed (BR-F8-24); fields editable within the role | U05 | `u05-accounting/s-f08-31-fx-revaluation-e-f08-36-revaluation-run-posted-desktop-{light,dark}.png` |
| E-F8-36 Revaluation run | Reversed | Badge "Reversed"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f08-31-fx-revaluation-e-f08-36-revaluation-run-reversed-desktop-{light,dark}.png` |

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

- [FL-F8-11 Treasury and payment means](../../flows/fl-f08-11-treasury-and-payment-means.md)

## Open questions

None.

---

⬅️ [S-F8-30 Payment means](s-f08-30-payment-means.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-32 Cash position](s-f08-32-cash-position.md)
