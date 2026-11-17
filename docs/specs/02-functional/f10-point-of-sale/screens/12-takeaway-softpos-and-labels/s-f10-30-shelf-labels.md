🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F10-12](README.md) ›
🖥️ S-F10-30 Shelf labels

# 🖥️ S-F10-30 Shelf labels

**Status:** ✅ specified

## Personas

- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md): links the labels and repairs those that
  failed.

## Purpose

Link labels to products and shelves and see which labels do not match the till.

## Entry points

Point of sale › Shelf labels; the notification of labels in Mismatch.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Shelf labels                       Labels: 1 240   Mismatch: 3   Faulty: 1   [Scan a label] [Print] |
| ------------------------------------------------------------------------------------------- |
| LABEL   PRODUCT          SHELF         SHOWN   TILL    BATTERY  STATE                       |
| 8841    Olive oil 1 L    Aisle 4 / 2   6.90    6.90    78       Up to date                  |
| 8850    Pasta 500 g      Aisle 2 / 1   1.80    1.60    64       Mismatch   [Retry] [Print paper] |
| 8862    Rice 1 kg        Aisle 2 / 3   -       2.40    4        Faulty     [Replace]        |
| Last full update: 09:42   Label connector: connected                                        |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f10-30-shelf-labels-empty-desktop-{light,dark}.png`,
`s-f10-30-shelf-labels-loading-desktop-{light,dark}.png`, `s-f10-30-shelf-labels-offline-desktop-{light,dark}.png`,
`s-f10-30-shelf-labels-read-only-desktop-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-12 step 3, U23 | desktop | ![FL-F10-12 step 3, U23, light](../../images/12-takeaway-softpos-and-labels/u23-store-manager/3-shelf-labels-desktop-light.png) | ![FL-F10-12 step 3, U23, dark](../../images/12-takeaway-softpos-and-labels/u23-store-manager/3-shelf-labels-desktop-dark.png) |
| FL-F10-12 step 3, U23 | desktop | ![FL-F10-12 step 3, U23, light](../../images/12-takeaway-softpos-and-labels/u23-store-manager/3-shelf-labels-desktop-light.png) | ![FL-F10-12 step 3, U23, dark](../../images/12-takeaway-softpos-and-labels/u23-store-manager/3-shelf-labels-desktop-dark.png) |
| FL-F10-12 step 3, U23 | phone | ![FL-F10-12 step 3, U23, light](../../images/12-takeaway-softpos-and-labels/u23-store-manager/3-shelf-labels-phone-light.png) | ![FL-F10-12 step 3, U23, dark](../../images/12-takeaway-softpos-and-labels/u23-store-manager/3-shelf-labels-phone-dark.png) |
| FL-F10-12 step 3, U23 | tablet | ![FL-F10-12 step 3, U23, light](../../images/12-takeaway-softpos-and-labels/u23-store-manager/3-shelf-labels-tablet-light.png) | ![FL-F10-12 step 3, U23, dark](../../images/12-takeaway-softpos-and-labels/u23-store-manager/3-shelf-labels-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-30-shelf-labels-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-30-shelf-labels-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-30-shelf-labels-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-30-shelf-labels-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-30-shelf-labels-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-30-shelf-labels-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-30-shelf-labels-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-30-shelf-labels-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Label and product | E-F10-23 code and product | text | link only | yes |
| Shelf position | E-F10-23 shelf position | text | yes | yes |
| Shown and till price | E-F10-23 and the till price | money | no | yes |
| Battery | E-F10-23 battery | percent | no | no |
| State | E-F10-23 state | badge | by action | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Scan a label | header | the store manager | a Registered label |
| Link | row | the store manager | the label is tied to a product and a shelf |
| Retry | row | the store manager | the update is sent again |
| Print paper | row | the store manager | a paper label with the till price is printed |
| Retire | row | the store manager | the label is removed from use |

## States

- Normal: the labels with the shown price next to the till price, battery and state.
- Empty: No label yet: a hint to scan the first label.
- Loading: The labels as placeholders, then the comparison with the till.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a connector
  that is down says so with the time of the last update.
- Read-only: a role that may only read: shown, with no action.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F10-23 Shelf label](../../data/e-f10-23-shelf-label.md),
[E-F7-06 Item](../../../f07-purchasing-and-stock/data/e-f07-06-item.md),
[E-F7-07 Location](../../../f07-purchasing-and-stock/data/e-f07-07-location.md),
[E-F10-08 Price promotion](../../data/e-f10-08-price-promotion.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F10-23 Shelf label | Registered | Badge "Registered"; a new record starts here; next: Linked (UC-F10-31); fields editable within the role | U23 | `u23-store-manager/s-f10-30-shelf-labels-e-f10-23-shelf-label-registered-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-23 Shelf label | Linked | Badge "Linked"; next: Updating (BR-F10-25); fields editable within the role | U23 | `u23-store-manager/s-f10-30-shelf-labels-e-f10-23-shelf-label-linked-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-23 Shelf label | Updating | Badge "Updating"; next: Up to date or Mismatch (BR-F10-25); fields editable within the role | U23 | `u23-store-manager/s-f10-30-shelf-labels-e-f10-23-shelf-label-updating-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-23 Shelf label | Up to date | Badge "Up to date"; next: Updating or Faulty (BR-F10-25, UC-F10-31); fields editable within the role | U23 | `u23-store-manager/s-f10-30-shelf-labels-e-f10-23-shelf-label-up-to-date-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-23 Shelf label | Mismatch | Badge "Mismatch"; next: Updating (UC-F10-31); fields editable within the role | U23 | `u23-store-manager/s-f10-30-shelf-labels-e-f10-23-shelf-label-mismatch-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-23 Shelf label | Faulty | Badge "Faulty"; next: Retired (UC-F10-31); fields editable within the role | U23 | `u23-store-manager/s-f10-30-shelf-labels-e-f10-23-shelf-label-faulty-{desktop,phone,tablet}-{light,dark}.png` |
| E-F10-23 Shelf label | Retired | Badge "Retired"; final state, read-only | U23 | `u23-store-manager/s-f10-30-shelf-labels-e-f10-23-shelf-label-retired-{desktop,phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

Desktop only; the scan action also works on a phone.

## Accessibility

A mismatch is a word and a difference of price, not only a colour; keyboard: next label, retry.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F10-12 Takeaway, tap to pay, labels and layaway](../../flows/fl-f10-12-takeaway-softpos-and-labels.md)

## Open questions

None.

---

⬅️ [S-F10-29 Tap to pay](s-f10-29-tap-to-pay.md) · ⬆️ [Up](README.md) · ➡️ [S-F10-31 Layaway](s-f10-31-layaway.md)
