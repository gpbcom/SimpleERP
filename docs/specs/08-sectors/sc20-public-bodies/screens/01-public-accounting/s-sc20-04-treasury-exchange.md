🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-01 Public accounting](README.md) › 🖥️ S-SC20-04 Treasury exchange

# 🖥️ S-SC20-04 Treasury exchange

**Status:** 🔄 waiting for the owner

## Personas

- [U54 Public finance officer](../../../../01-users/personas/u54-public-finance-officer.md): the batches, their sending
  and the accountant's answers.

## Purpose

Send the signed orders to the public accountant in the national format and apply the answers.

## Entry points

Public bodies › Treasury exchanges; a signed batch waiting.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Treasury exchanges                                         [Build batch] [Send] [Check format]   |
| Batch    Date        Orders   Format   Sent         Acknowledged   State                         |
| B-0112   12 Mar       14       valid    12 Mar 16:02 12 Mar 16:10   Accepted                     |
| B-0111   5 Mar        9        valid    5 Mar 11:45  5 Mar 11:52    Accepted                     |
| B-0113   19 Mar       6        2 errors -            -              Prepared                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-01 step 4, U54 | desktop | ![FL-SC20-01 step 4, U54, light](../../images/01-public-accounting/u54-public-finance-officer/4-treasury-exchange-desktop-light.png) | ![FL-SC20-01 step 4, U54, dark](../../images/01-public-accounting/u54-public-finance-officer/4-treasury-exchange-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-04-treasury-exchange-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-04-treasury-exchange-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-04-treasury-exchange-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-04-treasury-exchange-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-04-treasury-exchange-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-04-treasury-exchange-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-04-treasury-exchange-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-04-treasury-exchange-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Batch | E-SC20-04 batch | text | no | yes |
| Orders | E-SC20-04 orders | list of orders | yes while Prepared | yes |
| Format check | E-SC20-04 format | valid, errors | no | yes |
| Sent at | E-SC20-04 sent | date and time | no | no |
| Answer | E-SC20-04 answer | per order paid or rejected | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Build batch | header | public finance officer | the signed orders are put in a batch |
| Check format | row | public finance officer | the batch is checked against the format |
| Send | row | public finance officer | the batch is sent with the signature |

## States

- Normal: the batches with orders, format check, sending, answer and state.
- Empty: No batch yet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a format error,
  a certificate expired, an unknown answer, with the batch named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-04 Treasury exchange](../../data/e-sc20-04-treasury-exchange.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-04 Treasury exchange | Prepared | Badge "Prepared"; a new record starts here; next: Sent (BR-SC20-04); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-04-treasury-exchange-e-sc20-04-treasury-exchange-prepared-desktop-{light,dark}.png` |
| E-SC20-04 Treasury exchange | Sent | Badge "Sent"; next: Accepted or Rejected (UC-SC20-04); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-04-treasury-exchange-e-sc20-04-treasury-exchange-sent-desktop-{light,dark}.png` |
| E-SC20-04 Treasury exchange | Accepted | Badge "Accepted"; final: read-only, no next state; the history shows how it got here | U54 | `u54-public-finance-officer/s-sc20-04-treasury-exchange-e-sc20-04-treasury-exchange-accepted-desktop-{light,dark}.png` |
| E-SC20-04 Treasury exchange | Rejected | Badge "Rejected"; next: Prepared (UC-SC20-04); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-04-treasury-exchange-e-sc20-04-treasury-exchange-rejected-desktop-{light,dark}.png` |

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

- [FL-SC20-01 Public accounting](../../flows/fl-sc20-01-public-accounting.md)

## Open questions

None.

---

⬅️ [S-SC20-03 Orders and titles](s-sc20-03-orders-and-titles.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-05 Tender file](../02-public-procurement/s-sc20-05-tender-file.md)
