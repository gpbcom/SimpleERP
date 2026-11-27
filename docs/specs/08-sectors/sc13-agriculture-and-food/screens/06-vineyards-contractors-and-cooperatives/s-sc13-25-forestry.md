🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC13-06 Vineyards, contractors, cooperatives, baskets, forests](README.md) › 🖥️ S-SC13-25 Forestry

# 🖥️ S-SC13-25 Forestry

**Status:** ✅ specified

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md): the parcels, the plan, the lots and the sales.

## Purpose

Plan the fellings of the management plan, mark and sell timber lots and follow what leaves the forest, each load traced
to its parcel.

## Entry points

Agriculture › Forestry; a parcel's page; the lots of the year.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Forest: Bois des Fosses         Plan 2024-2033            [Mark lot] [Record sale] [Record load] |
| Lot   Parcel  Species  Volume m3  Sale        Price m3  Plan left  State                         |
| T-12  P4      Oak      220 est.   Standing    62.00     80 m3      Marked                        |
| T-13  P2      Pine     150        Felled      38.00     -          Sold                          |
| T-14  P2      Pine     150        Felled      38.00     -          Delivered                     |
| Year 2026: 520 m3 planned, 340 m3 marked, 150 m3 delivered                                       |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-06 step 5, U40 | desktop | ![FL-SC13-06 step 5, U40, light](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/5-forestry-desktop-light.png) | ![FL-SC13-06 step 5, U40, dark](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/5-forestry-desktop-dark.png) |
| FL-SC13-06 step 5, U40 | phone | ![FL-SC13-06 step 5, U40, light](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/5-forestry-phone-light.png) | ![FL-SC13-06 step 5, U40, dark](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/5-forestry-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-25-forestry-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-25-forestry-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-25-forestry-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-25-forestry-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-25-forestry-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-25-forestry-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-25-forestry-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-25-forestry-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Parcel | E-SC13-21 parcel | link | yes while Marked | yes |
| Species | E-SC13-21 species | text | yes while Marked | yes |
| Volume | E-SC13-21 volume | number in cubic metres | yes while Marked or Sold | yes |
| Sale kind | E-SC13-21 sale kind | standing or felled | yes while Marked | yes to sell |
| Price | E-SC13-21 price | amount in EUR per cubic metre | yes while Marked | yes to sell |
| Buyer | E-SC13-21 buyer | customer link | yes while Marked | yes to sell |
| Plan volume left | E-SC13-21 plan left | number in cubic metres | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Mark lot | header | forest manager | a lot in state Marked, checked against the plan |
| Record sale | lot | forest manager | the buyer and the price are kept and the lot is Sold |
| Measure | lot | forest manager | the measured volume replaces the estimate |
| Record load | lot | forest manager | a delivery note with the parcel and the lot is Delivered when all is out |

## States

- Normal: the lots with parcel, species, volume, sale, price, volume left in the plan and state.
- Empty: No lot yet, with Mark lot.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a lot outside
  the plan's year or volume, a missing parcel, with the figures.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC13-21 Timber lot](../../data/e-sc13-21-timber-lot.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-21 Timber lot | Marked | Badge "Marked"; a new record starts here; next: Sold or Withdrawn (UC-SC13-25); fields editable within the role | U40 | `u40-farmer/s-sc13-25-forestry-e-sc13-21-timber-lot-marked-{desktop,phone}-{light,dark}.png` |
| E-SC13-21 Timber lot | Sold | Badge "Sold"; next: Felled (UC-SC13-25); fields editable within the role | U40 | `u40-farmer/s-sc13-25-forestry-e-sc13-21-timber-lot-sold-{desktop,phone}-{light,dark}.png` |
| E-SC13-21 Timber lot | Felled | Badge "Felled"; next: Delivered (UC-SC13-25); fields editable within the role | U40 | `u40-farmer/s-sc13-25-forestry-e-sc13-21-timber-lot-felled-{desktop,phone}-{light,dark}.png` |
| E-SC13-21 Timber lot | Delivered | Badge "Delivered"; final: read-only, no next state; the history shows how it got here | U40 | `u40-farmer/s-sc13-25-forestry-e-sc13-21-timber-lot-delivered-{desktop,phone}-{light,dark}.png` |
| E-SC13-21 Timber lot | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U40 | `u40-farmer/s-sc13-25-forestry-e-sc13-21-timber-lot-withdrawn-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC13-06](../../flows/fl-sc13-06-vineyards-contractors-and-cooperatives.md)

## Open questions

None.

---

⬅️ [S-SC13-24 Basket subscriptions](s-sc13-24-baskets.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-L01 Plots](../00-lists/s-sc13-l01-plots.md)
