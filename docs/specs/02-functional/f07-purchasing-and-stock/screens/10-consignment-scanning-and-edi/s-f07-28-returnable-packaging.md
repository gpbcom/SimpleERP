🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F7-28 Returnable packaging

# 🖥️ S-F7-28 Returnable packaging

**Status:** 🔄 waiting for the owner

## Personas

- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md): the deposits and balances per party.
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md): the packaging out and back, on a
  phone.

## Purpose

Record packaging out and back, charge and refund the deposit, and see who holds what.

## Entry points

Purchasing and stock › Returnable packaging; the delivery's packaging step on the warehouse app.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Returnable packaging: Bois et Fils                    Open    Deposit held 200 EUR          |
|---------------------------------------------------------------------------------------------|
| PACKAGING   UNIT DEPOSIT   OUT   RETURNED   STILL OUT   DEPOSIT HELD   REFUNDED             |
| Crate 40 L  5.00 EUR       40    30         10          50.00 EUR      150.00 EUR           |
| Pallet      12.00 EUR      6     6          0           0.00 EUR       72.00 EUR            |
| [Record packaging out] [Record a return] [Write off]                                        |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-10 step 4, U04 | desktop | ![FL-F7-10 step 4, U04, light](../../images/10-consignment-scanning-and-edi/u04-purchasing/4-returnable-packaging-desktop-light.png) | ![FL-F7-10 step 4, U04, dark](../../images/10-consignment-scanning-and-edi/u04-purchasing/4-returnable-packaging-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-28-returnable-packaging-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-28-returnable-packaging-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-28-returnable-packaging-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-28-returnable-packaging-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-28-returnable-packaging-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-28-returnable-packaging-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-28-returnable-packaging-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-28-returnable-packaging-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Packaging type | E-F7-06 | name | no | yes |
| Unit deposit | E-F7-25 | amount with currency | no | yes |
| Out, returned, still out | E-F7-25 | three numbers | no | yes |
| Deposit held, refunded | E-F7-25 | two amounts | no | yes |
| State of returned packaging | E-F7-25 return lines | good, damaged | yes | for a return |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Record packaging out | delivery | warehouse operator | quantity out and the deposit on the invoice |
| Record a return | row | warehouse operator | quantity back; the refund is computed |
| Write off | row | purchasing | the packaging is lost; the deposit is kept |
| Send the statement | header | purchasing | the party receives its deposit statement |

## States

- Normal: the packaging types with their quantities and amounts for one party.
- Empty: No packaging out, with Record packaging out.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a return above
  the quantity out shows both numbers.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-25 Packaging deposit](../../data/e-f07-25-packaging-deposit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-25 Packaging deposit | Open | Badge "Open"; a new record starts here; next: Partly returned or Closed (UC-F7-28, BR-F7-22); fields editable within the role | U04, U15 | `u04-purchasing/s-f07-28-returnable-packaging-e-f07-25-packaging-deposit-open-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-28-returnable-packaging-e-f07-25-packaging-deposit-open-{phone,tablet}-{light,dark}.png` |
| E-F7-25 Packaging deposit | Partly returned | Badge "Partly returned"; next: Closed or Written off (BR-F7-22, UC-F7-28); fields editable within the role | U04, U15 | `u04-purchasing/s-f07-28-returnable-packaging-e-f07-25-packaging-deposit-partly-returned-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-28-returnable-packaging-e-f07-25-packaging-deposit-partly-returned-{phone,tablet}-{light,dark}.png` |
| E-F7-25 Packaging deposit | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U04, U15 | `u04-purchasing/s-f07-28-returnable-packaging-e-f07-25-packaging-deposit-closed-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-28-returnable-packaging-e-f07-25-packaging-deposit-closed-{phone,tablet}-{light,dark}.png` |
| E-F7-25 Packaging deposit | Written off | Badge "Written off"; final: read-only, no next state; the history shows how it got here | U04, U15 | `u04-purchasing/s-f07-28-returnable-packaging-e-f07-25-packaging-deposit-written-off-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-28-returnable-packaging-e-f07-25-packaging-deposit-written-off-{phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The operator records packaging out and back on a phone with the delivery: counters and a state choice. Purchasing's
balances are desktop only.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F7-10](../../flows/fl-f07-10-consignment-scanning-and-edi.md)

## Open questions

None.

---

⬅️ [S-F7-27 Periodic valuation](s-f07-27-periodic-valuation.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-29 Supplier EDI](s-f07-29-supplier-edi.md)
