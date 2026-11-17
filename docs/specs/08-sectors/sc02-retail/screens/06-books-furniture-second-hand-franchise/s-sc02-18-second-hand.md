🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-06 Books, furniture, second-hand and franchise](README.md) ›
🖥️ S-SC02-18 Second-hand

# 🖥️ S-SC02-18 Second-hand

**Status:** 🔄 waiting for the owner

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md): the purchase being recorded.
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): the register and its lines.

## Purpose

Record a purchase from a person in the register, pay only once it is saved, and follow the object to its sale.

## Entry points

Retail › Second-hand purchases; the tablet till's Buy back action; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Purchase 2026-0412                                              Registered   [Save] [Pay]        |
| Object  Wristwatch, steel case, ref. W809, serial 7A0412, good cond.     [Photo]                 |
| Seller  Amir K., 12 rue des Lilas, Lyon    Identity card 7612 4455   [Scan]                      |
| Price   120.00 EUR   Means  Bank transfer   Date 2026-11-14 10:41                                |
| Register line  2026-0412  saved at 10:41      Stock item  ITM-90017                              |
| Sale  waiting        Return to the authorities  none                                             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-06 step 3, U17 | tablet | ![FL-SC02-06 step 3, U17, light](../../images/06-books-furniture-second-hand-franchise/u17-cashier/3-second-hand-tablet-light.png) | ![FL-SC02-06 step 3, U17, dark](../../images/06-books-furniture-second-hand-franchise/u17-cashier/3-second-hand-tablet-dark.png) |
| FL-SC02-06 step 3, U17 | desktop | ![FL-SC02-06 step 3, U17, light](../../images/06-books-furniture-second-hand-franchise/u17-cashier/3-second-hand-desktop-light.png) | ![FL-SC02-06 step 3, U17, dark](../../images/06-books-furniture-second-hand-franchise/u17-cashier/3-second-hand-desktop-dark.png) |
| FL-SC02-06 step 3, U17 | phone | ![FL-SC02-06 step 3, U17, light](../../images/06-books-furniture-second-hand-franchise/u17-cashier/3-second-hand-phone-light.png) | ![FL-SC02-06 step 3, U17, dark](../../images/06-books-furniture-second-hand-franchise/u17-cashier/3-second-hand-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-18-second-hand-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-18-second-hand-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-18-second-hand-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-18-second-hand-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-18-second-hand-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-18-second-hand-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-18-second-hand-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-18-second-hand-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Object | E-SC02-15 object | kind, brand, model, serial | yes while Draft | yes |
| Photo | E-SC02-15 photo | image | yes while Draft | no |
| Seller | E-SC02-15 seller | name, address, document | yes while Draft | yes |
| Price and means | E-SC02-15 price, means | amount and means | yes while Draft | yes |
| Register line | E-SC02-15 register number | number | no | yes |
| Sale date and buyer type | E-SC02-15 sale | date and type | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Scan identity | seller block | cashier | the seller's details are filled in |
| Save and pay | header | cashier | the line is written, then the payment is allowed |
| Withdraw from sale | purchase | store manager | the object is Withdrawn |
| Export register | toolbar | store manager | a file of the lines of a period |

## States

- Normal: the object, the seller as checked, the price and means and the register line.
- Empty: No purchase yet, with New purchase.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  identity document or a register line that cannot be saved, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC02-15 Second-hand purchase](../../data/e-sc02-15-second-hand-purchase.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC02-15 Second-hand purchase | Registered | Badge "Registered"; a new record starts here; next: On sale (UC-SC02-18); fields editable within the role | U17, U23 | `u17-cashier/s-sc02-18-second-hand-e-sc02-15-second-hand-purchase-registered-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-sc02-18-second-hand-e-sc02-15-second-hand-purchase-registered-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-15 Second-hand purchase | On sale | Badge "On sale"; next: Sold or Withdrawn (UC-SC02-18); fields editable within the role | U17, U23 | `u17-cashier/s-sc02-18-second-hand-e-sc02-15-second-hand-purchase-on-sale-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-sc02-18-second-hand-e-sc02-15-second-hand-purchase-on-sale-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-15 Second-hand purchase | Sold | Badge "Sold"; final: read-only, no next state; the history shows how it got here | U17, U23 | `u17-cashier/s-sc02-18-second-hand-e-sc02-15-second-hand-purchase-sold-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-sc02-18-second-hand-e-sc02-15-second-hand-purchase-sold-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-15 Second-hand purchase | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U17, U23 | `u17-cashier/s-sc02-18-second-hand-e-sc02-15-second-hand-purchase-withdrawn-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-sc02-18-second-hand-e-sc02-15-second-hand-purchase-withdrawn-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The cashier works on the tablet at the counter and the store manager on a desktop; on a phone, the app asks to continue
on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC02-06](../../flows/fl-sc02-06-books-furniture-second-hand-franchise.md)

## Open questions

None.

---

⬅️ [S-SC02-17 Furniture orders](s-sc02-17-furniture-orders.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-19 Franchise network](s-sc02-19-franchise-network.md)
