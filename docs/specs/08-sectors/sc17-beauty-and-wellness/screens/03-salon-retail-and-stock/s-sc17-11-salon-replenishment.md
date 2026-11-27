🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC17-03 Salon retail and stock](README.md) ›
🖥️ S-SC17-11 Salon replenishment

# 🖥️ S-SC17-11 Salon replenishment

**Status:** 🔄 waiting for the owner

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): the stock and the orders of their salon.

## Purpose

See what is below its minimum, order it from the suppliers and receive it.

## Entry points

Beauty and wellness › Replenishment; the stock list; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Replenishment: Rue Verte salon                                    [Send the orders]              |
| Product         Stock   Min   Proposed   Supplier                                                |
| Colour 6.3      3       5     6          Beta Hair Supply                                        |
| Developer 6%    2       4     4          Beta Hair Supply                                        |
| Facial cream    1       3     6          Lune Cosmetics                                          |
| Free delivery above 150 EUR: 38.00 EUR missing from Beta Hair Supply                             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC17-03 step 3, U23 | desktop | ![FL-SC17-03 step 3, U23, light](../../images/03-salon-retail-and-stock/u23-store-manager/3-salon-replenishment-desktop-light.png) | ![FL-SC17-03 step 3, U23, dark](../../images/03-salon-retail-and-stock/u23-store-manager/3-salon-replenishment-desktop-dark.png) |
| FL-SC17-03 step 3, U23 | phone | ![FL-SC17-03 step 3, U23, light](../../images/03-salon-retail-and-stock/u23-store-manager/3-salon-replenishment-phone-light.png) | ![FL-SC17-03 step 3, U23, dark](../../images/03-salon-retail-and-stock/u23-store-manager/3-salon-replenishment-phone-dark.png) |
| FL-SC17-03 step 3, U23 | tablet | ![FL-SC17-03 step 3, U23, light](../../images/03-salon-retail-and-stock/u23-store-manager/3-salon-replenishment-tablet-light.png) | ![FL-SC17-03 step 3, U23, dark](../../images/03-salon-retail-and-stock/u23-store-manager/3-salon-replenishment-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc17-11-salon-replenishment-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc17-11-salon-replenishment-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc17-11-salon-replenishment-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc17-11-salon-replenishment-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc17-11-salon-replenishment-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc17-11-salon-replenishment-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc17-11-salon-replenishment-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc17-11-salon-replenishment-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Product | E-F7-06 item | link | no | yes |
| Stock | E-F7-06 stock | number | no | no |
| Minimum | E-F7-09 minimum | number | yes | yes |
| Proposed quantity | E-F7-03 quantity | number | yes | yes |
| Supplier | E-F7-01 supplier record | link | yes | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send the orders | header | manager | one order per supplier is sent |
| Transfer from another salon | product row | manager | a transfer replaces the order line |
| Receive | order row | manager | the goods are received with their lots |

## States

- Normal: the products below their minimum with the proposed quantity and the supplier.
- Empty: Nothing below its minimum.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a product with
  no supplier price or a delivery with no lot.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop first; the tablet shows the stock of the salon.

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

⬅️ [S-SC17-10 Back bar](s-sc17-10-back-bar.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-12 Cosmetics safety](s-sc17-12-cosmetics-safety.md)
