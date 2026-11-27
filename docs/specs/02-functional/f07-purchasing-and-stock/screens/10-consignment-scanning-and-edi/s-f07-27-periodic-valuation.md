🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F7-27 Periodic valuation

# 🖥️ S-F7-27 Periodic valuation

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the valuation and its entry.
- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md): the count and the goods in transit.

## Purpose

Value the counted stock at the end of a period and post the stock variation.

## Entry points

Accounting › Closing › Stock; Purchasing and stock › Periodic valuation.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Periodic valuation: October 2026                       Counted    [Approve] [Post at period end]|
|---------------------------------------------------------------------------------------------|
| Opening stock   55,100 EUR     Purchases   20,400 EUR     Closing stock   61,300 EUR        |
| Stock variation   +6,200 EUR (increase)                                                     |
| CATEGORY      QUANTITY   COST METHOD   CLOSING VALUE   VARIATION                            |
| Timber        2,300      average       31,200          +2,100                               |
| Hardware      2,520      standard      30,100          +4,100                               |
| Items without a cost: 0      Goods in transit: 2 lines    Consigned goods left out: 380      |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-10 step 3, U05 | desktop | ![FL-F7-10 step 3, U05, light](../../images/10-consignment-scanning-and-edi/u05-accounting/3-periodic-valuation-desktop-light.png) | ![FL-F7-10 step 3, U05, dark](../../images/10-consignment-scanning-and-edi/u05-accounting/3-periodic-valuation-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-27-periodic-valuation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-27-periodic-valuation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-27-periodic-valuation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-27-periodic-valuation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-27-periodic-valuation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-27-periodic-valuation-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-27-periodic-valuation-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-27-periodic-valuation-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Period | E-F7-24 period | month and year | no | yes |
| Opening, purchases, closing | E-F7-24 | three amounts | no | yes |
| Stock variation | E-F7-24 | amount with sign | no | yes |
| Category lines | E-F7-11 count | table | yes while Counted | yes |
| Items without a cost | E-F7-06 | count and list | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Approve | header | accounting | the valuation is fixed |
| Post at period end | header | accounting | one entry is posted on the last day of the period |
| Correct a quantity | row | accounting, purchasing | the count changes with a reason |
| Value again | header | accounting | recomputes while the period is open |

## States

- Normal: the opening, purchases and closing values, the variation and the lines per category.
- Empty: No count to value, with Open the stock count.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an item without
  a cost is listed with a link to its record.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-24 Periodic count](../../data/e-f07-24-periodic-count.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-24 Periodic count | Counted | Badge "Counted"; a new record starts here; next: Valued (UC-F7-27); fields editable within the role | U05, U04 | `u05-accounting/s-f07-27-periodic-valuation-e-f07-24-periodic-count-counted-desktop-{light,dark}.png`, `u04-purchasing/s-f07-27-periodic-valuation-e-f07-24-periodic-count-counted-desktop-{light,dark}.png` |
| E-F7-24 Periodic count | Valued | Badge "Valued"; next: Approved (UC-F7-27); fields editable within the role | U05, U04 | `u05-accounting/s-f07-27-periodic-valuation-e-f07-24-periodic-count-valued-desktop-{light,dark}.png`, `u04-purchasing/s-f07-27-periodic-valuation-e-f07-24-periodic-count-valued-desktop-{light,dark}.png` |
| E-F7-24 Periodic count | Approved | Badge "Approved"; next: Posted (BR-F7-21); fields editable within the role | U05, U04 | `u05-accounting/s-f07-27-periodic-valuation-e-f07-24-periodic-count-approved-desktop-{light,dark}.png`, `u04-purchasing/s-f07-27-periodic-valuation-e-f07-24-periodic-count-approved-desktop-{light,dark}.png` |
| E-F7-24 Periodic count | Posted | Badge "Posted"; next: Reversed (UC-F7-27); fields editable within the role | U05, U04 | `u05-accounting/s-f07-27-periodic-valuation-e-f07-24-periodic-count-posted-desktop-{light,dark}.png`, `u04-purchasing/s-f07-27-periodic-valuation-e-f07-24-periodic-count-posted-desktop-{light,dark}.png` |
| E-F7-24 Periodic count | Reversed | Badge "Reversed"; next: Valued (UC-F7-27); fields editable within the role | U05, U04 | `u05-accounting/s-f07-27-periodic-valuation-e-f07-24-periodic-count-reversed-desktop-{light,dark}.png`, `u04-purchasing/s-f07-27-periodic-valuation-e-f07-24-periodic-count-reversed-desktop-{light,dark}.png` |

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

- [FL-F7-10](../../flows/fl-f07-10-consignment-scanning-and-edi.md)

## Open questions

None.

---

⬅️ [S-F7-26 Warehouse barcode app](s-f07-26-barcode-app.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-28 Returnable packaging](s-f07-28-returnable-packaging.md)
