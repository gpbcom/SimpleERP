🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-09 Compliance and carbon](README.md) › 🖥️ S-F7-24 Purchase carbon

# 🖥️ S-F7-24 Purchase carbon

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Show the estimated emissions of purchases per supplier and category, with their method.

## Entry points

Reports › Purchase carbon.

## Wireframe

```text
+------------------------------------------------------------------+
| Purchase carbon 2026   410 t CO2e   18 % from supplier data       |
| Category          Spend      t CO2e   Method                      |
| Food and drinks   7.1 M      320      factor 0.045 kg/EUR         |
| Transport         0.6 M      62       carrier data                |
| Uncategorised     42,000 EUR not counted   [Categorise]           |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-09 step 3, U13 | desktop | ![FL-F7-09 step 3, U13, light](../../images/09-compliance-and-carbon/u13-owner/3-purchase-carbon-desktop-light.png) | ![FL-F7-09 step 3, U13, dark](../../images/09-compliance-and-carbon/u13-owner/3-purchase-carbon-desktop-dark.png) |
| FL-F7-09 step 3, U13 | phone | ![FL-F7-09 step 3, U13, light](../../images/09-compliance-and-carbon/u13-owner/3-purchase-carbon-phone-light.png) | ![FL-F7-09 step 3, U13, dark](../../images/09-compliance-and-carbon/u13-owner/3-purchase-carbon-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-24-purchase-carbon-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-24-purchase-carbon-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-24-purchase-carbon-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-24-purchase-carbon-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-24-purchase-carbon-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-24-purchase-carbon-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f07-24-purchase-carbon-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f07-24-purchase-carbon-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Spend, emissions, method | E-F7-20, E-F7-05 | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Ask suppliers for data | purchasing | Request in the portal |

## States

- Normal: show the estimated emissions of purchases per supplier and category, with their method.
- Empty: no posted purchase in the year: "Nothing to compute yet".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: always: figures are computed.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F7-20 Emission factor](../../data/e-f07-20-emission-factor.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-20 Emission factor | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f07-24-purchase-carbon-e-f07-20-emission-factor-recorded-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F7-09 Compliance and carbon](../../flows/fl-f07-09-compliance-and-carbon.md)

## Open questions

None.

---

⬅️ [S-F7-23 Dangerous goods](../02-receive-and-store/s-f07-23-dangerous-goods.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-25 Consignment stock](../10-consignment-scanning-and-edi/s-f07-25-consignment-stock.md)
