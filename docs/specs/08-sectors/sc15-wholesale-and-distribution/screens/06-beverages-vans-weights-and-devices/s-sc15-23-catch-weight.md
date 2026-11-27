🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-06 Beverages, van sales, catch weight and medical devices](README.md) › 🖥️ S-SC15-23 Catch weight

# 🖥️ S-SC15-23 Catch weight

**Status:** ✅ specified

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md): the cases to weigh and the scale on
  the phone.
- [U03 Sales](../../../../01-users/personas/u03-sales.md): the ordered and the delivered weights and the invoice.

## Purpose

Weigh each case at picking, compare the delivered weight with the ordered one and invoice the weight actually delivered
at the price per kilo.

## Entry points

Wholesale › Catch weight; an order line sold by weight; the picking list on the phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Order SO-4410  Maison Dupuis                  Item: Cured ham, 18.00 EUR / kg  [Weigh] [Confirm] |
| Case   Lot       Weight kg   Source                                                              |
| 1      L-2210    5.12        Scale 2                                                             |
| 2      L-2210    4.87        Scale 2                                                             |
| 3      L-2211    5.31        Typed (flagged)                                                     |
| Total 10 cases: 51.4 kg   Nominal 50.0 kg   Difference +2.8 percent   Amount 925.20 EUR          |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-06 step 3, U15 | phone | ![FL-SC15-06 step 3, U15, light](../../images/06-beverages-vans-weights-and-devices/u15-warehouse-operator/3-catch-weight-phone-light.png) | ![FL-SC15-06 step 3, U15, dark](../../images/06-beverages-vans-weights-and-devices/u15-warehouse-operator/3-catch-weight-phone-dark.png) |
| FL-SC15-06 step 3, U15 | tablet | ![FL-SC15-06 step 3, U15, light](../../images/06-beverages-vans-weights-and-devices/u15-warehouse-operator/3-catch-weight-tablet-light.png) | ![FL-SC15-06 step 3, U15, dark](../../images/06-beverages-vans-weights-and-devices/u15-warehouse-operator/3-catch-weight-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc15-23-catch-weight-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc15-23-catch-weight-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc15-23-catch-weight-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc15-23-catch-weight-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc15-23-catch-weight-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc15-23-catch-weight-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-23-catch-weight-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-23-catch-weight-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Case | E-F6-04 case number | number | no | yes |
| Lot | E-F7-10 lot | link | no | yes |
| Weight | E-F6-04 weight | number in kilograms | yes while picking | yes |
| Source | E-F6-04 weight source | scale or typed | no | no |
| Total weight | E-F6-04 total weight | number in kilograms | no | no |
| Price per kilo | E-F6-04 price per kilo | amount in EUR | no | no |
| Amount | E-F6-04 amount | amount in EUR | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Weigh | phone | warehouse operator | the case's weight is saved from the scale |
| Type weight | phone | warehouse operator | the weight is saved and flagged as typed |
| Confirm | order line | warehouse operator | the line is delivered with its total weight |
| Invoice | order | sales | the invoice from the delivered weight |

## States

- Normal: the cases of the line with lot, weight and source, and the total against the nominal weight.
- Empty: No catch-weight line on this order.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a case without
  a weight or a scale whose verification has expired, with the case to weigh.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

The operator's phone shows the case to weigh and the weight received from the scale in large figures.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC15-06](../../flows/fl-sc15-06-beverages-vans-weights-and-devices.md)

## Open questions

None.

---

⬅️ [S-SC15-22 Van sales](s-sc15-22-van-sales.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-24 Medical devices](s-sc15-24-medical-devices.md)
