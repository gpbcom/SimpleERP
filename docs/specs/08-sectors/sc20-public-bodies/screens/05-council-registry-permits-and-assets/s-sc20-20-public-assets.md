🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-05 Council, civil registry, permits and assets](README.md) ›
🖥️ S-SC20-20 Public assets

# 🖥️ S-SC20-20 Public assets

**Status:** ✅ specified

## Personas

- [U54 Public finance officer](../../../../01-users/personas/u54-public-finance-officer.md): the register of assets with
  their depreciation and the comparison with the accountant.

## Purpose

Keep the register of the body's assets and depreciate them under the M57 framework.

## Entry points

Public bodies › Public assets; an acquisition paid by an order.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Public assets                                             [New asset] [Commission] [Compare]     |
| Inventory   Asset              Category     Value      Commissioned  Years  State                |
| A-0412      Primary school     Building     2,400,000  1 Sep 2019    40     In service           |
| A-0455      Road, rue Haute    Road         180,000    -             -      In progress          |
| A-0388      Utility van        Vehicle      34,000     1 Mar 2020    5      Fully depreciated    |
| Difference with the accountant: 1 asset                          [Explain]                       |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-05 step 4, U54 | desktop | ![FL-SC20-05 step 4, U54, light](../../images/05-council-registry-permits-and-assets/u54-public-finance-officer/4-public-assets-desktop-light.png) | ![FL-SC20-05 step 4, U54, dark](../../images/05-council-registry-permits-and-assets/u54-public-finance-officer/4-public-assets-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-20-public-assets-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-20-public-assets-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-20-public-assets-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-20-public-assets-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-20-public-assets-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-20-public-assets-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-20-public-assets-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-20-public-assets-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Inventory number | E-SC20-15 number | text | no | yes |
| Asset | E-SC20-15 name | text | yes while In progress | yes |
| Category | E-SC20-15 category | list of the pack | yes while In progress | yes |
| Value | E-SC20-15 value | amount | yes while In progress | yes |
| Commissioned on | E-SC20-15 commissioned | date | yes once | yes to depreciate |
| Duration | E-SC20-15 duration | years from the category | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New asset | header | public finance officer | an asset is created from an acquisition |
| Commission | row | public finance officer | the date is set and the depreciation starts |
| Compare | header | public finance officer | the register is compared with the accountant's |

## States

- Normal: the assets with inventory number, category, value, commissioning date, duration and state.
- Empty: No asset yet, with New asset.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a category
  without a duration, a difference not explained, with the asset named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-15 Public asset](../../data/e-sc20-15-public-asset.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-15 Public asset | In progress | Badge "In progress"; a new record starts here; next: In service (BR-SC20-20); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-20-public-assets-e-sc20-15-public-asset-in-progress-desktop-{light,dark}.png` |
| E-SC20-15 Public asset | In service | Badge "In service"; next: Fully depreciated or Disposed (BR-SC20-20, UC-SC20-20); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-20-public-assets-e-sc20-15-public-asset-in-service-desktop-{light,dark}.png` |
| E-SC20-15 Public asset | Fully depreciated | Badge "Fully depreciated"; next: Disposed (UC-SC20-20); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-20-public-assets-e-sc20-15-public-asset-fully-depreciated-desktop-{light,dark}.png` |
| E-SC20-15 Public asset | Disposed | Badge "Disposed"; final: read-only, no next state; the history shows how it got here | U54 | `u54-public-finance-officer/s-sc20-20-public-assets-e-sc20-15-public-asset-disposed-desktop-{light,dark}.png` |

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

- [FL-SC20-05](../../flows/fl-sc20-05-council-registry-permits-and-assets.md)

## Open questions

None.

---

⬅️ [S-SC20-19 Planning permits](s-sc20-19-planning-permits.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-L01 Budgets](../00-lists/s-sc20-l01-budgets.md)
