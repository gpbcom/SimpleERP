🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-03 Salon retail and stock](README.md) › 🖥️ S-SC17-10 Back bar

# 🖥️ S-SC17-10 Back bar

**Status:** ✅ specified

## Personas

- [U52 Beautician](../../../../01-users/personas/u52-beautician.md): the products they used in their services.

## Purpose

Record the products used in a service from its recipe and take them off the stock by lot.

## Entry points

Beauty and wellness › Product uses; the visit's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Back bar: Colour, Camille R., 2026-11-21 14:30                          Ines B.                  |
| Product            Recipe     Used      Lot        State                                         |
| Colour 6.3         60 g       65 g      L-7782     Recorded                                      |
| Developer 6%       90 ml      90 ml     L-5530     Recorded                                      |
| Cost of the service 8.40 EUR                      Recipe cost 8.00 EUR                           |
| [Save the use]  [Add a product]                                                                  |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-03 step 2, U52 | tablet | ![FL-SC17-03 step 2, U52, light](../../images/03-salon-retail-and-stock/u52-beautician/2-back-bar-tablet-light.png) | ![FL-SC17-03 step 2, U52, dark](../../images/03-salon-retail-and-stock/u52-beautician/2-back-bar-tablet-dark.png) |
| FL-SC17-03 step 2, U52 | phone | ![FL-SC17-03 step 2, U52, light](../../images/03-salon-retail-and-stock/u52-beautician/2-back-bar-phone-light.png) | ![FL-SC17-03 step 2, U52, dark](../../images/03-salon-retail-and-stock/u52-beautician/2-back-bar-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc17-10-back-bar-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc17-10-back-bar-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc17-10-back-bar-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc17-10-back-bar-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc17-10-back-bar-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc17-10-back-bar-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-10-back-bar-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-10-back-bar-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Visit | E-SC17-07 salon booking | link | no | yes |
| Product | E-SC17-07 product | stock item | yes while Recorded | yes |
| Quantity used | E-SC17-07 quantity | number and unit | yes while Recorded | yes |
| Lot | E-SC17-07 lot | lot | yes while Recorded | yes |
| Recipe quantity | E-SC17-07 recipe quantity | number and unit | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Save the use | footer | beautician | the use becomes Posted and stock falls |
| Add a product | header | beautician | a product outside the recipe, flagged |
| Cancel | use row | beautician, manager | a Recorded use is cancelled |

## States

- Normal: the recipe of the service, the real quantities and the lots.
- Empty: No use yet, with Add a product.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a recalled lot
  or a stock too low, with another lot.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC17-07 Product use](../../data/e-sc17-07-product-use.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC17-07 Product use | Recorded | Badge "Recorded"; a new record starts here; next: Posted or Cancelled (BR-SC17-10, UC-SC17-10); fields editable within the role | U52 | `u52-beautician/s-sc17-10-back-bar-e-sc17-07-product-use-recorded-{phone,tablet}-{light,dark}.png` |
| E-SC17-07 Product use | Posted | Badge "Posted"; next: Cancelled (UC-SC17-10); fields editable within the role | U52 | `u52-beautician/s-sc17-10-back-bar-e-sc17-07-product-use-posted-{phone,tablet}-{light,dark}.png` |
| E-SC17-07 Product use | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U52 | `u52-beautician/s-sc17-10-back-bar-e-sc17-07-product-use-cancelled-{phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The beautician works on the tablet at the chair, the manager on a desktop and the customer on a phone, with the same
actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC17-03 Salon retail and stock](../../flows/fl-sc17-03-salon-retail-and-stock.md)

## Open questions

None.

---

⬅️ [S-SC17-09 Salon retail](s-sc17-09-salon-retail.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-11 Salon replenishment](s-sc17-11-salon-replenishment.md)
