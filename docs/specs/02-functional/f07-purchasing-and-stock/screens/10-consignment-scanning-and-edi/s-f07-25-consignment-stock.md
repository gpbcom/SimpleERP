🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F7-25 Consignment stock

# 🖥️ S-F7-25 Consignment stock

**Status:** 🔄 waiting for the owner

## Personas

- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md): the agreements, the consumption and the
  settlement.
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md): the receipt and the storage of
  consigned goods, on a phone.

## Purpose

Receive consigned goods, see who owns what, record the use and settle it.

## Entry points

Purchasing and stock › Consignment; the warehouse app's Receive step.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Consignment stock: Menuiserie Dupont                 Owner: supplier   Location CONS-A      |
|---------------------------------------------------------------------------------------------|
| ITEM              LOT      RECEIVED  USED   LEFT   OWNER      TO SETTLE                     |
| Oak plank 30mm    L-4412   500       120    380    Supplier   1,440 EUR                     |
| Brass hinge       L-4420   200       0      200    Supplier   0 EUR                         |
| [Receive] [Record use] [Settle with the supplier] [Return unused]                           |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-10 step 1, U04 | desktop | ![FL-F7-10 step 1, U04, light](../../images/10-consignment-scanning-and-edi/u04-purchasing/1-consignment-stock-desktop-light.png) | ![FL-F7-10 step 1, U04, dark](../../images/10-consignment-scanning-and-edi/u04-purchasing/1-consignment-stock-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-25-consignment-stock-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-25-consignment-stock-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-25-consignment-stock-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-25-consignment-stock-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-25-consignment-stock-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-25-consignment-stock-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-25-consignment-stock-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-25-consignment-stock-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Item and lot | E-F7-23 item, lot | text | no | yes |
| Received, used, left | E-F7-23 quantities | three numbers | no | yes |
| Owner | E-F7-23 owner | badge: supplier, customer, company | yes while Held | yes |
| To settle | E-F7-23 value used | amount with currency | no | yes |
| Location | E-F7-07 | text | yes while Held | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Receive | header | warehouse operator | a quantity in the consignment location with its owner |
| Record use | row | warehouse operator, production | the quantity is consumed and the purchase is created |
| Settle | header | purchasing | the uses become a purchase order or a self-billed invoice |
| Return unused | row | purchasing | a return to the supplier; the owner's quantity falls |

## States

- Normal: the consigned lots with their quantities, owner and amount to settle.
- Empty: No consigned goods, with Receive consigned goods.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a receipt that
  differs from the supplier's note shows both quantities.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-23 Stock owner](../../data/e-f07-23-stock-owner.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-23 Stock owner | Held | Badge "Held"; a new record starts here; next: Used or Returned (UC-F7-25); fields editable within the role | U04, U15 | `u04-purchasing/s-f07-25-consignment-stock-e-f07-23-stock-owner-held-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-25-consignment-stock-e-f07-23-stock-owner-held-{phone,tablet}-{light,dark}.png` |
| E-F7-23 Stock owner | Used | Badge "Used"; next: Settled (UC-F7-25); fields editable within the role | U04, U15 | `u04-purchasing/s-f07-25-consignment-stock-e-f07-23-stock-owner-used-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-25-consignment-stock-e-f07-23-stock-owner-used-{phone,tablet}-{light,dark}.png` |
| E-F7-23 Stock owner | Settled | Badge "Settled"; next: Held or Returned (BR-F7-19, UC-F7-25); fields editable within the role | U04, U15 | `u04-purchasing/s-f07-25-consignment-stock-e-f07-23-stock-owner-settled-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-25-consignment-stock-e-f07-23-stock-owner-settled-{phone,tablet}-{light,dark}.png` |
| E-F7-23 Stock owner | Returned | Badge "Returned"; final: read-only, no next state; the history shows how it got here | U04, U15 | `u04-purchasing/s-f07-25-consignment-stock-e-f07-23-stock-owner-returned-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-25-consignment-stock-e-f07-23-stock-owner-returned-{phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The warehouse operator receives and stores on a phone: scan the lot, confirm the quantity, choose the location.
Purchasing's settlement is desktop only.

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

⬅️ [S-F7-24 Purchase carbon](../09-compliance-and-carbon/s-f07-24-purchase-carbon.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-26 Warehouse barcode app](s-f07-26-barcode-app.md)
