🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-06 Campsites, catering, groups, pricing and licences](README.md) › 🖥️ S-SC06-17 Catering

# 🖥️ S-SC06-17 Catering

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md): the quotes and orders of their customers.
- [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md): the production list and the delivery of the
  day.

## Purpose

Quote an event meal per head with its allergens, confirm it and give the kitchen what to prepare and when to leave.

## Entry points

Restaurant and hospitality › Catering orders; the quotes list; the kitchen's day view.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Order CT-118  Company party, 80 guests, 14 Dec 2026        State: Confirmed   [Send quote]       |
| Dish                 Per head   Allergens                    Cost    Price                       |
| Salmon, lemon sauce  18.00      fish, milk                   6.10    18.00                       |
| Vegetable tart       12.00      gluten, egg, milk           3.20    12.00                        |
| Staff 3 x 6 h        -          -                            240     420.00                      |
| Delivery 40 km       -          -                            35      90.00      Total 2,950.00   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-06 step 2, U03 | desktop | ![FL-SC06-06 step 2, U03, light](../../images/06-campsites-catering-groups-and-pricing/u03-sales/2-catering-desktop-light.png) | ![FL-SC06-06 step 2, U03, dark](../../images/06-campsites-catering-groups-and-pricing/u03-sales/2-catering-desktop-dark.png) |
| FL-SC06-06 step 2, U03 | phone | ![FL-SC06-06 step 2, U03, light](../../images/06-campsites-catering-groups-and-pricing/u03-sales/2-catering-phone-light.png) | ![FL-SC06-06 step 2, U03, dark](../../images/06-campsites-catering-groups-and-pricing/u03-sales/2-catering-phone-dark.png) |
| FL-SC06-06 step 2, U03 | tablet | ![FL-SC06-06 step 2, U03, light](../../images/06-campsites-catering-groups-and-pricing/u03-sales/2-catering-tablet-light.png) | ![FL-SC06-06 step 2, U03, dark](../../images/06-campsites-catering-groups-and-pricing/u03-sales/2-catering-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-17-catering-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-17-catering-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-17-catering-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-17-catering-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-17-catering-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-17-catering-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc06-17-catering-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc06-17-catering-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-SC06-14 customer | link | no | yes |
| Event date and place | E-SC06-14 event date, place | date and text | yes while Quoted | yes |
| Headcount | E-SC06-14 headcount | number | yes while Quoted | yes |
| Menu | E-SC06-14 menu | list of dishes | yes while Quoted | yes |
| Allergens | E-SC06-14 allergens | list from the recipes | no | no |
| Total | E-SC06-14 total | amount in EUR | no | no |
| Delivery slot | E-SC06-14 delivery slot | date and time | yes while Confirmed | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send quote | header | sales | the quote goes to the customer with the allergens |
| Confirm | header | sales | the order is Confirmed and the kitchen sees it |
| Record delivery | kitchen view | kitchen staff | temperatures, time and signature are kept and the order is Delivered |
| Invoice | header | sales | the final invoice on the final headcount |

## States

- Normal: the menu with the allergens, the cost, the price and the delivery slot.
- Empty: No catering order yet, with New quote.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a dish without
  allergens or a date over capacity, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC06-14 Catering order](../../data/e-sc06-14-catering-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-14 Catering order | Quoted | Badge "Quoted"; a new record starts here; next: Confirmed or Lost (UC-SC06-17); fields editable within the role | U03, U19 | `u03-sales/s-sc06-17-catering-e-sc06-14-catering-order-quoted-{desktop,phone,tablet}-{light,dark}.png`, `u19-kitchen-staff/s-sc06-17-catering-e-sc06-14-catering-order-quoted-desktop-{light,dark}.png` |
| E-SC06-14 Catering order | Confirmed | Badge "Confirmed"; next: Delivered (UC-SC06-17); fields editable within the role | U03, U19 | `u03-sales/s-sc06-17-catering-e-sc06-14-catering-order-confirmed-{desktop,phone,tablet}-{light,dark}.png`, `u19-kitchen-staff/s-sc06-17-catering-e-sc06-14-catering-order-confirmed-desktop-{light,dark}.png` |
| E-SC06-14 Catering order | Delivered | Badge "Delivered"; next: Invoiced (UC-SC06-17); fields editable within the role | U03, U19 | `u03-sales/s-sc06-17-catering-e-sc06-14-catering-order-delivered-{desktop,phone,tablet}-{light,dark}.png`, `u19-kitchen-staff/s-sc06-17-catering-e-sc06-14-catering-order-delivered-desktop-{light,dark}.png` |
| E-SC06-14 Catering order | Invoiced | Badge "Invoiced"; final: read-only, no next state; the history shows how it got here | U03, U19 | `u03-sales/s-sc06-17-catering-e-sc06-14-catering-order-invoiced-{desktop,phone,tablet}-{light,dark}.png`, `u19-kitchen-staff/s-sc06-17-catering-e-sc06-14-catering-order-invoiced-desktop-{light,dark}.png` |
| E-SC06-14 Catering order | Lost | Badge "Lost"; final: read-only, no next state; the history shows how it got here | U03, U19 | `u03-sales/s-sc06-17-catering-e-sc06-14-catering-order-lost-{desktop,phone,tablet}-{light,dark}.png`, `u19-kitchen-staff/s-sc06-17-catering-e-sc06-14-catering-order-lost-desktop-{light,dark}.png` |

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

- [FL-SC06-06](../../flows/fl-sc06-06-campsites-catering-groups-and-pricing.md)

## Open questions

None.

---

⬅️ [S-SC06-16 Campsite](s-sc06-16-campsite.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-18 Groups and seminars](s-sc06-18-groups-and-seminars.md)
