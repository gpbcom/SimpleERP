🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-02 Receive and store](README.md) › 🖥️ S-F7-23 Dangerous goods

# 🖥️ S-F7-23 Dangerous goods

**Status:** ✅ specified

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)
- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md)
- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)

## Purpose

Keep safety data sheets and see hazardous stock per location.

## Entry points

Stock › Dangerous goods; the scanner at receipt.

## Wireframe

```text
+------------------------------------------------------------------+
| Dangerous goods                                 [Register PDF]    |
| Item             Class  Sheet       Location    Qty   Limit      |
| Fungicide 20 L   6.1    v4 current  Store C     340 L 500 L      |
| Solvent 5 L      3      v2 OUTDATED Store B     40 L  200 L      |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-02 step 3, U15 | phone | ![FL-F7-02 step 3, U15, light](../../images/02-receive-and-store/u15-warehouse-operator/3-dangerous-goods-phone-light.png) | ![FL-F7-02 step 3, U15, dark](../../images/02-receive-and-store/u15-warehouse-operator/3-dangerous-goods-phone-dark.png) |
| FL-F7-02 step 3, U15 | tablet | ![FL-F7-02 step 3, U15, light](../../images/02-receive-and-store/u15-warehouse-operator/3-dangerous-goods-tablet-light.png) | ![FL-F7-02 step 3, U15, dark](../../images/02-receive-and-store/u15-warehouse-operator/3-dangerous-goods-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f07-23-dangerous-goods-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f07-23-dangerous-goods-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f07-23-dangerous-goods-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f07-23-dangerous-goods-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f07-23-dangerous-goods-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f07-23-dangerous-goods-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f07-23-dangerous-goods-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f07-23-dangerous-goods-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Item, class, sheet, location, quantity | E-F7-19, E-F7-07 | sheets |

## Actions

| Action | Who | Result |
|---|---|---|
| Attach a sheet | purchasing, quality | Version kept |
| Register | anyone allowed | PDF |

## States

- Normal: keep safety data sheets and see hazardous stock per location.
- Empty: no hazardous item: "No item is marked hazardous".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for operators: read, and the scanner's checks.
- Offline: The scanner keeps the sheets' versions and storage classes loaded before going offline, and checks receipts
  against them ([D271](../../../../06-decisions/f07-purchasing-and-stock/d271-warehouse-operations.md)); new sheets wait
  for the network.

Shown entities (VD-15): [E-F7-19 Safety data sheet](../../data/e-f07-19-safety-data-sheet.md),
[E-F7-07 Location](../../data/e-f07-07-location.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-19 Safety data sheet | Active | Badge "Active"; a new record starts here; next: Superseded (UC-F7-23); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-23-dangerous-goods-e-f07-19-safety-data-sheet-active-{phone,tablet}-{light,dark}.png` |
| E-F7-19 Safety data sheet | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U15 | `u15-warehouse-operator/s-f07-23-dangerous-goods-e-f07-19-safety-data-sheet-superseded-{phone,tablet}-{light,dark}.png` |
| E-F7-07 Location | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U04, U15, U27 | `u04-purchasing/s-f07-23-dangerous-goods-e-f07-07-location-active-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-23-dangerous-goods-e-f07-07-location-active-{phone,tablet}-{light,dark}.png`, `u27-quality-manager/s-f07-23-dangerous-goods-e-f07-07-location-active-{desktop,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the checks on the scanner.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F7-09 Compliance and carbon](../../flows/fl-f07-09-compliance-and-carbon.md)

## Open questions

None.

---

⬅️ [S-F7-22 Eco-contributions](../09-compliance-and-carbon/s-f07-22-eco-contributions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-24 Purchase carbon](../09-compliance-and-carbon/s-f07-24-purchase-carbon.md)
