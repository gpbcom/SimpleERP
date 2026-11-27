🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-06 Excise, refurbishment, personalisation and cutting](README.md) ›
🖥️ S-SC05-16 Alcohol excise

# 🖥️ S-SC05-16 Alcohol excise

**Status:** 🔄 waiting for the owner

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md): the lots in the bonded warehouse
  and their movements.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the monthly declaration and the duty to post.

## Purpose

Follow the bonded stock by lot, record each release or movement under suspension and prepare the monthly excise
declaration.

## Entry points

Manufacturing › Bonded stock; a finished batch's page; the reminder of the monthly declaration.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Bonded warehouse: Brewery site 1                           Month 2026-10   [Review declaration]  |
| Lot     Item          Litres   Strength  Category  Hl pure   State        Movement               |
| B-204   Pale ale      1,000    5.0 %     Beer      0.50      Released     Release 2026-10-03     |
| B-205   Pale ale      2,400    5.0 %     Beer      1.20      Bonded       -                      |
| S-031   Whisky        600      42.0 %    Spirits   2.52      Shipped      Suspension to FR-0123  |
| Month: 14 releases, 41.6 hl pure alcohol, duty 6,812.40 EUR       [Release] [Send] [Export]      |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-06 step 1, U21 | desktop | ![FL-SC05-06 step 1, U21, light](../../images/06-excise-refurbishment-and-cutting/u21-production-planner/1-alcohol-excise-desktop-light.png) | ![FL-SC05-06 step 1, U21, dark](../../images/06-excise-refurbishment-and-cutting/u21-production-planner/1-alcohol-excise-desktop-dark.png) |
| FL-SC05-06 step 1, U21 | phone | ![FL-SC05-06 step 1, U21, light](../../images/06-excise-refurbishment-and-cutting/u21-production-planner/1-alcohol-excise-phone-light.png) | ![FL-SC05-06 step 1, U21, dark](../../images/06-excise-refurbishment-and-cutting/u21-production-planner/1-alcohol-excise-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-16-alcohol-excise-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-16-alcohol-excise-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-16-alcohol-excise-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-16-alcohol-excise-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-16-alcohol-excise-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-16-alcohol-excise-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc05-16-alcohol-excise-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc05-16-alcohol-excise-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Lot and item | E-SC05-15 lot, item | links | no | yes |
| Litres | E-SC05-15 volume | number in litres | yes while Bonded | yes |
| Strength | E-SC05-15 strength | percent with one decimal | yes while Bonded | yes |
| Category | E-SC05-15 category | beer, wine, spirits or other | yes while Bonded | yes |
| Hectolitres of pure alcohol | E-SC05-15 pure alcohol | number | no | no |
| Movement | E-SC05-15 movement | release, suspension, export, loss, destruction | yes | no |
| Duty | E-SC05-15 duty | amount in EUR | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Release for consumption | row | production planner | the lot is Released and the duty line is added to the month |
| Send under suspension | row | production planner | the accompanying document is prepared and the lot is Shipped |
| Review declaration | header | accounting | the month's lines with their totals and gaps |
| File declaration | declaration | accounting | the lines are Declared and the duty is posted |

## States

- Normal: the bonded stock by lot with its volume, strength, state and the month's totals.
- Empty: No bonded stock yet, with Create from a finished batch.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  strength, category or approval number, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC05-15 Bonded stock](../../data/e-sc05-15-bonded-stock.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-15 Bonded stock | Bonded | Badge "Bonded"; a new record starts here; next: Released or Shipped (BR-SC05-16, UC-SC05-16); fields editable within the role | U21, U05 | `u21-production-planner/s-sc05-16-alcohol-excise-e-sc05-15-bonded-stock-bonded-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc05-16-alcohol-excise-e-sc05-15-bonded-stock-bonded-desktop-{light,dark}.png` |
| E-SC05-15 Bonded stock | Released | Badge "Released"; next: Declared (UC-SC05-16); fields editable within the role | U21, U05 | `u21-production-planner/s-sc05-16-alcohol-excise-e-sc05-15-bonded-stock-released-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc05-16-alcohol-excise-e-sc05-15-bonded-stock-released-desktop-{light,dark}.png` |
| E-SC05-15 Bonded stock | Shipped | Badge "Shipped"; final: read-only, no next state; the history shows how it got here | U21, U05 | `u21-production-planner/s-sc05-16-alcohol-excise-e-sc05-15-bonded-stock-shipped-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc05-16-alcohol-excise-e-sc05-15-bonded-stock-shipped-desktop-{light,dark}.png` |
| E-SC05-15 Bonded stock | Declared | Badge "Declared"; final: read-only, no next state; the history shows how it got here | U21, U05 | `u21-production-planner/s-sc05-16-alcohol-excise-e-sc05-15-bonded-stock-declared-{desktop,phone}-{light,dark}.png`, `u05-accounting/s-sc05-16-alcohol-excise-e-sc05-15-bonded-stock-declared-desktop-{light,dark}.png` |

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

- [FL-SC05-06](../../flows/fl-sc05-06-excise-refurbishment-and-cutting.md)

## Open questions

None.

---

⬅️ [S-SC05-15 Quality assistant](../04-quality-system/s-sc05-15-quality-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-17 Refurbishment](s-sc05-17-refurbishment.md)
