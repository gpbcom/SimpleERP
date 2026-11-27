🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-05 On-call, warranties, van stock and site quotes](README.md) › 🖥️ S-SC19-19 Van stock

# 🖥️ S-SC19-19 Van stock

**Status:** 🔄 waiting for the owner

## Personas

- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): my van's stock, the reload list and the count
  on the phone.
- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md): the vans with their standard loads,
  differences and reloads.

## Purpose

Keep the standard load of each van, follow its use and count it at every reload.

## Entry points

Trades and home services › Van stock; the reload reminder; a part's page.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Van stock: Van 4, Leroy                                [Reload] [Count] [Explain]                |
| Part            Min   Max   Expected   Counted   Difference   State                              |
| Seal 20/27      10     40   11         10        -1           Counted                            |
| Mixer cartridge  2     10   2          2         0            Reconciled                         |
| Fitting 15 mm    5     30   3          -         -            Refill due                         |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-05 step 3, U14 | phone | ![FL-SC19-05 step 3, U14, light](../../images/05-on-call-warranties-van-stock-and-site-quotes/u14-field-worker/3-van-stock-phone-light.png) | ![FL-SC19-05 step 3, U14, dark](../../images/05-on-call-warranties-van-stock-and-site-quotes/u14-field-worker/3-van-stock-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc19-19-van-stock-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc19-19-van-stock-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc19-19-van-stock-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc19-19-van-stock-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc19-19-van-stock-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc19-19-van-stock-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-19-van-stock-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-19-van-stock-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Van | E-SC19-13 van | link to a location | no | yes |
| Part | E-SC19-13 part | link | no | yes |
| Minimum and maximum | E-SC19-13 limits | two numbers | yes for purchasing | yes |
| Expected | E-SC19-13 expected | number | no | no |
| Counted | E-SC19-13 counted | number | yes for the technician | no |
| Explanation | E-SC19-13 explanation | text | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Reload | header | technician | the van is loaded to its maximum and the load is confirmed |
| Count | row | technician | the counted quantity is saved |
| Explain | row | purchasing | a difference is explained or written off |

## States

- Normal: the van's parts with limits, expected, counted, difference and state.
- Empty: No van yet, with Add a van.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a van not
  counted, a reload over the maximum, with the part named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-13 Van stock](../../data/e-sc19-13-van-stock.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-13 Van stock | Loaded | Badge "Loaded"; a new record starts here; next: Refill due or Counted (BR-SC19-07, BR-SC19-19); fields editable within the role | U14, U04 | `u14-field-worker/s-sc19-19-van-stock-e-sc19-13-van-stock-loaded-phone-{light,dark}.png`, `u04-purchasing/s-sc19-19-van-stock-e-sc19-13-van-stock-loaded-desktop-{light,dark}.png` |
| E-SC19-13 Van stock | Refill due | Badge "Refill due"; next: Counted (BR-SC19-19); fields editable within the role | U14, U04 | `u14-field-worker/s-sc19-19-van-stock-e-sc19-13-van-stock-refill-due-phone-{light,dark}.png`, `u04-purchasing/s-sc19-19-van-stock-e-sc19-13-van-stock-refill-due-desktop-{light,dark}.png` |
| E-SC19-13 Van stock | Counted | Badge "Counted"; next: Reconciled (BR-SC19-19); fields editable within the role | U14, U04 | `u14-field-worker/s-sc19-19-van-stock-e-sc19-13-van-stock-counted-phone-{light,dark}.png`, `u04-purchasing/s-sc19-19-van-stock-e-sc19-13-van-stock-counted-desktop-{light,dark}.png` |
| E-SC19-13 Van stock | Reconciled | Badge "Reconciled"; next: Loaded (UC-SC19-19); fields editable within the role | U14, U04 | `u14-field-worker/s-sc19-19-van-stock-e-sc19-13-van-stock-reconciled-phone-{light,dark}.png`, `u04-purchasing/s-sc19-19-van-stock-e-sc19-13-van-stock-reconciled-desktop-{light,dark}.png` |

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

- [FL-SC19-05](../../flows/fl-sc19-05-on-call-warranties-van-stock-and-site-quotes.md)

## Open questions

None.

---

⬅️ [S-SC19-18 Builders' warranties](s-sc19-18-builders-warranties.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-20 Site quotes](s-sc19-20-site-quotes.md)
