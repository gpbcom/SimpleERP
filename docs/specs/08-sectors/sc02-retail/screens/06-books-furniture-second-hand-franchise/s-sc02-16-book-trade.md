🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🛍️ [SC02 Retail](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC02-06 Books, furniture, second-hand and franchise](README.md) ›
🖥️ S-SC02-16 Book trade

# 🖥️ S-SC02-16 Book trade

**Status:** 🔄 waiting for the owner

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md): the title being sold and its lowest price.
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): every title, price and discount.

## Purpose

Sell a book at the publisher's price within the allowed discount and keep the titles and their prices up to date.

## Entry points

Retail › Book titles; the till when an ISBN is scanned; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Title: Les Jours clairs, Editions du Nord              ISBN 978-2-00-000412-7        Listed      |
| Publisher's price  21.00 EUR    Lowest price allowed  19.95 EUR (5 %)                            |
| Discount asked     10 %         -> refused: lowest price is 19.95 EUR                            |
| Loyalty reward     2.00 EUR     Cut to 0.00 EUR (the discount is at the cap)                     |
| Price to charge    19.95 EUR                                   [Sell] [Cancel]                   |
| Stock 7   Sold this month 31   Discounts refused 2                                               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC02-06 step 1, U17 | tablet | ![FL-SC02-06 step 1, U17, light](../../images/06-books-furniture-second-hand-franchise/u17-cashier/1-book-trade-tablet-light.png) | ![FL-SC02-06 step 1, U17, dark](../../images/06-books-furniture-second-hand-franchise/u17-cashier/1-book-trade-tablet-dark.png) |
| FL-SC02-06 step 1, U17 | desktop | ![FL-SC02-06 step 1, U17, light](../../images/06-books-furniture-second-hand-franchise/u17-cashier/1-book-trade-desktop-light.png) | ![FL-SC02-06 step 1, U17, dark](../../images/06-books-furniture-second-hand-franchise/u17-cashier/1-book-trade-desktop-dark.png) |
| FL-SC02-06 step 1, U17 | phone | ![FL-SC02-06 step 1, U17, light](../../images/06-books-furniture-second-hand-franchise/u17-cashier/1-book-trade-phone-light.png) | ![FL-SC02-06 step 1, U17, dark](../../images/06-books-furniture-second-hand-franchise/u17-cashier/1-book-trade-phone-dark.png) |
| Error E1, U17 | tablet | ![Error E1, U17, light](../../images/06-books-furniture-second-hand-franchise/u17-cashier/e1-the-discount-is-over-the-cap-tablet-light.png) | ![Error E1, U17, dark](../../images/06-books-furniture-second-hand-franchise/u17-cashier/e1-the-discount-is-over-the-cap-tablet-dark.png) |
| Error E1, U17 | desktop | ![Error E1, U17, light](../../images/06-books-furniture-second-hand-franchise/u17-cashier/e1-the-discount-is-over-the-cap-desktop-light.png) | ![Error E1, U17, dark](../../images/06-books-furniture-second-hand-franchise/u17-cashier/e1-the-discount-is-over-the-cap-desktop-dark.png) |
| Error E1, U17 | phone | ![Error E1, U17, light](../../images/06-books-furniture-second-hand-franchise/u17-cashier/e1-the-discount-is-over-the-cap-phone-light.png) | ![Error E1, U17, dark](../../images/06-books-furniture-second-hand-franchise/u17-cashier/e1-the-discount-is-over-the-cap-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc02-16-book-trade-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc02-16-book-trade-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc02-16-book-trade-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc02-16-book-trade-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc02-16-book-trade-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc02-16-book-trade-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc02-16-book-trade-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc02-16-book-trade-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| ISBN | E-SC02-13 ISBN | 13 digits | yes while Listed | yes |
| Title and publisher | E-SC02-13 title, publisher | text | yes while Listed | yes |
| Publisher's price | E-SC02-13 publisher's price | amount including VAT | yes while Listed | yes |
| Lowest price allowed | E-SC02-13 lowest price | amount | no | no |
| Discount asked | sale line | percentage or amount | yes | no |
| Price to charge | sale line | amount | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Sell | sale | cashier | the line is recorded at the checked price |
| New title | header | store manager | a title in Listed |
| Change the publisher's price | title | store manager | the new price applies from the next sale |
| Withdraw | title | store manager | the title is Withdrawn and no longer listed |

## States

- Normal: the scanned title with its publisher's price, the lowest price allowed and the discount asked.
- Empty: No title yet, with New title.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a discount
  below the lowest price allowed, with the price the till accepts.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC02-13 Book title](../../data/e-sc02-13-book-title.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC02-13 Book title | Listed | Badge "Listed"; a new record starts here; next: Withdrawn (UC-SC02-16); fields editable within the role | U17, U23 | `u17-cashier/s-sc02-16-book-trade-e-sc02-13-book-title-listed-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-sc02-16-book-trade-e-sc02-13-book-title-listed-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC02-13 Book title | Withdrawn | Badge "Withdrawn"; next: Listed (UC-SC02-16); fields editable within the role | U17, U23 | `u17-cashier/s-sc02-16-book-trade-e-sc02-13-book-title-withdrawn-{desktop,phone,tablet}-{light,dark}.png`, `u23-store-manager/s-sc02-16-book-trade-e-sc02-13-book-title-withdrawn-{desktop,phone,tablet}-{light,dark}.png` |

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

⬅️ [S-SC02-15 Store assistant](../05-unsold-goods-and-performance/s-sc02-15-store-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC02-17 Furniture orders](s-sc02-17-furniture-orders.md)
