🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-03 Salon retail and stock](README.md) › 🖥️ S-SC17-09 Salon retail

# 🖥️ S-SC17-09 Salon retail

**Status:** 🔄 waiting for the owner

## Personas

- [U52 Beautician](../../../../01-users/personas/u52-beautician.md): the sales of the visit and the products they sold.

## Purpose

Sell products with the services of a visit on the certified till and apply the customer's balances.

## Entry points

Beauty and wellness › Salon retail; the till; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Sale: Camille R.                                                      Till 1 open                |
| Line                          Qty    Price      Seller                                           |
| Facial 60 min                 1      55.00      Ines B.                                          |
| Shampoo 250 ml                1      18.50      Ines B.                                          |
| Voucher G-4471               -1     -18.00                                                       |
| Total to pay 55.50 EUR     [Pay by card] [Pay in cash] [Split]                                   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-03 step 1, U52 | tablet | ![FL-SC17-03 step 1, U52, light](../../images/03-salon-retail-and-stock/u52-beautician/1-salon-retail-tablet-light.png) | ![FL-SC17-03 step 1, U52, dark](../../images/03-salon-retail-and-stock/u52-beautician/1-salon-retail-tablet-dark.png) |
| FL-SC17-03 step 1, U52 | phone | ![FL-SC17-03 step 1, U52, light](../../images/03-salon-retail-and-stock/u52-beautician/1-salon-retail-phone-light.png) | ![FL-SC17-03 step 1, U52, dark](../../images/03-salon-retail-and-stock/u52-beautician/1-salon-retail-phone-dark.png) |
| Error E1, U52 | tablet | ![Error E1, U52, light](../../images/03-salon-retail-and-stock/u52-beautician/e1-the-product-is-out-of-stock-tablet-light.png) | ![Error E1, U52, dark](../../images/03-salon-retail-and-stock/u52-beautician/e1-the-product-is-out-of-stock-tablet-dark.png) |
| Error E1, U52 | phone | ![Error E1, U52, light](../../images/03-salon-retail-and-stock/u52-beautician/e1-the-product-is-out-of-stock-phone-light.png) | ![Error E1, U52, dark](../../images/03-salon-retail-and-stock/u52-beautician/e1-the-product-is-out-of-stock-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc17-09-salon-retail-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc17-09-salon-retail-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc17-09-salon-retail-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc17-09-salon-retail-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc17-09-salon-retail-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc17-09-salon-retail-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-09-salon-retail-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-09-salon-retail-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-F6-01 customer record | link | yes while open | no |
| Lines | E-F10-03 lines | product or service, quantity, price | yes while open | yes |
| Seller | E-F10-03 seller | employee | yes while open | yes |
| Balances applied | E-F10-03 payments | voucher, session, deposit | yes while open | no |
| Total | E-F10-03 total | amount | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add a product | header | beautician | a line is added and the stock reserved |
| Pay | footer | beautician | the sale is closed on the certified till |
| Refund a line | sale | manager | a credit is issued and the stock returned |

## States

- Normal: the visit's lines, the products added, the balances applied and the total.
- Empty: No line yet, with Add a product.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a product out
  of stock or a declined card, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

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

⬅️ [S-SC17-08 Customer balances](../02-packages-and-memberships/s-sc17-08-customer-balances.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-10 Back bar](s-sc17-10-back-bar.md)
