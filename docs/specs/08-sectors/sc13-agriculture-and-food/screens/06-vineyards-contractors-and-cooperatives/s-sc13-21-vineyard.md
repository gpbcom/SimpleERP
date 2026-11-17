🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC13-06 Vineyards, contractors, cooperatives, baskets, forests](README.md) › 🖥️ S-SC13-21 Vineyard

# 🖥️ S-SC13-21 Vineyard

**Status:** 🔄 waiting for the owner

## Personas

- [U40 Farmer](../../../../01-users/personas/u40-farmer.md): the plots with their yields and the cellar, at the desk and
  in the vines.

## Purpose

Follow each vine plot and its harvest, compare the yield with the appellation's limit and prepare the harvest, stock and
excise declarations from the records.

## Entry points

Agriculture › Vineyard; a plot's page; the reminder of a declaration date.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Vineyard: Domaine des Lauzes                  Campaign 2026      [Record harvest] [Declarations] |
| Plot  Variety     Appellation   Area ha  Harvest hl  Yield hl/ha  Limit  State                   |
| P07   Syrah       Red AOP       2.0      118         59           60     Declared                |
| P12   Grenache    Red AOP       2.0      130         65           60     Harvested               |
| P15   Viognier    White IGP     1.2      -           -            80     In production           |
| Harvest declaration: 1 plot missing, 1 above limit               [Review] [File]                 |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-06 step 1, U40 | desktop | ![FL-SC13-06 step 1, U40, light](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/1-vineyard-desktop-light.png) | ![FL-SC13-06 step 1, U40, dark](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/1-vineyard-desktop-dark.png) |
| FL-SC13-06 step 1, U40 | phone | ![FL-SC13-06 step 1, U40, light](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/1-vineyard-phone-light.png) | ![FL-SC13-06 step 1, U40, dark](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/1-vineyard-phone-dark.png) |
| Error E1, U40 | desktop | ![Error E1, U40, light](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/e1-a-declaration-is-late-desktop-light.png) | ![Error E1, U40, dark](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/e1-a-declaration-is-late-desktop-dark.png) |
| Error E1, U40 | phone | ![Error E1, U40, light](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/e1-a-declaration-is-late-phone-light.png) | ![Error E1, U40, dark](../../images/06-vineyards-contractors-and-cooperatives/u40-farmer/e1-a-declaration-is-late-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc13-21-vineyard-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc13-21-vineyard-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc13-21-vineyard-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc13-21-vineyard-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc13-21-vineyard-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc13-21-vineyard-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc13-21-vineyard-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc13-21-vineyard-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Plot | E-SC13-17 plot | link | no | yes |
| Variety | E-SC13-17 variety | text | yes while Planted | yes |
| Appellation | E-SC13-17 appellation | text | yes while Planted | yes |
| Area in hectares | E-SC13-17 area | number | yes while Planted | yes |
| Harvest in hectolitres | E-SC13-17 harvest | number | yes while In production | no |
| Yield limit | E-SC13-17 yield limit | number in hl per hectare | no | no |
| Declared on | E-SC13-17 declared on | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Record harvest | plot row | farmer | the harvest is saved, the plot is Harvested and the yield is compared with the limit |
| Review declaration | header | farmer | the plots with their harvest and the gaps |
| File declaration | declaration | farmer | the plots are Declared and the date is kept |
| Open cellar | header | farmer | the lots and vats made from the harvest |

## States

- Normal: the plots with their variety, appellation, area, harvest, yield against the limit and state.
- Empty: No plot yet, with Map a plot.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  appellation or variety, a harvest after the declaration, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC13-17 Vine plot](../../data/e-sc13-17-vine-plot.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-17 Vine plot | Planted | Badge "Planted"; a new record starts here; next: In production (UC-SC13-21); fields editable within the role | U40 | `u40-farmer/s-sc13-21-vineyard-e-sc13-17-vine-plot-planted-{desktop,phone}-{light,dark}.png` |
| E-SC13-17 Vine plot | In production | Badge "In production"; next: Harvested or Grubbed up (BR-SC13-16, UC-SC13-21); fields editable within the role | U40 | `u40-farmer/s-sc13-21-vineyard-e-sc13-17-vine-plot-in-production-{desktop,phone}-{light,dark}.png` |
| E-SC13-17 Vine plot | Harvested | Badge "Harvested"; next: Declared (BR-SC13-16); fields editable within the role | U40 | `u40-farmer/s-sc13-21-vineyard-e-sc13-17-vine-plot-harvested-{desktop,phone}-{light,dark}.png` |
| E-SC13-17 Vine plot | Declared | Badge "Declared"; next: In production (UC-SC13-21); fields editable within the role | U40 | `u40-farmer/s-sc13-21-vineyard-e-sc13-17-vine-plot-declared-{desktop,phone}-{light,dark}.png` |
| E-SC13-17 Vine plot | Grubbed up | Badge "Grubbed up"; final: read-only, no next state; the history shows how it got here | U40 | `u40-farmer/s-sc13-21-vineyard-e-sc13-17-vine-plot-grubbed-up-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-SC13-20 Farm assistant](../03-farm-business/s-sc13-20-farm-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-22 Farm contractor](s-sc13-22-farm-contractor.md)
