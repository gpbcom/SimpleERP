🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-06 Excise, refurbishment, personalisation and cutting](README.md) ›
🖥️ S-SC05-19 Cutting

# 🖥️ S-SC05-19 Cutting

**Status:** ✅ specified

## Personas

- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md): the layouts of each order and the
  waste they leave.
- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md): the cuts to make, with the
  leftover to measure.

## Purpose

Plan the cuts of an order on remnants and new stock, release the layout and put usable leftovers back into stock.

## Entry points

Manufacturing › Remnants; a manufacturing order's Cutting tab; the operator's tablet.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Order MO-310  Steel plate 6 mm  12 parts                    Layout 2 of 3   [Release layout]     |
| Source             Size (mm)      Parts   Waste    Leftover                                      |
| Remnant R-102      1200 x 600     5       6 %      420 x 300 -> remnant                          |
| Remnant R-107      900 x 500      4       9 %      150 x 90  -> scrap                            |
| New sheet S-77     2000 x 1000    3       14 %     600 x 400 -> remnant                          |
| Minimum remnant size 200 x 200 mm           Waste of the layout 8 %                              |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-06 step 4, U21 | desktop | ![FL-SC05-06 step 4, U21, light](../../images/06-excise-refurbishment-and-cutting/u21-production-planner/4-cutting-desktop-light.png) | ![FL-SC05-06 step 4, U21, dark](../../images/06-excise-refurbishment-and-cutting/u21-production-planner/4-cutting-desktop-dark.png) |
| FL-SC05-06 step 4, U21 | phone | ![FL-SC05-06 step 4, U21, light](../../images/06-excise-refurbishment-and-cutting/u21-production-planner/4-cutting-phone-light.png) | ![FL-SC05-06 step 4, U21, dark](../../images/06-excise-refurbishment-and-cutting/u21-production-planner/4-cutting-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-19-cutting-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-19-cutting-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-19-cutting-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-19-cutting-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-19-cutting-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-19-cutting-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc05-19-cutting-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc05-19-cutting-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Source piece | E-SC05-18 source lot | link | no | yes |
| Length and width | E-SC05-18 length, width | numbers in mm | yes while Planned | yes |
| Thickness | E-SC05-18 thickness | number in mm | no | yes |
| Material certificate | E-SC05-18 certificate | file | no | no |
| Rack | E-SC05-18 location | link | yes | no |
| Cost | E-SC05-18 cost | amount in EUR | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Propose layouts | header | production planner | up to three layouts with their waste |
| Release layout | header | production planner | the cuts go to the operator's tablet |
| Confirm cut | tablet | production operator | the material is consumed and the leftover is asked for |
| Put into stock | leftover | production operator | the remnant is created in its rack |

## States

- Normal: the layouts with their waste and the remnants they would use or create.
- Empty: No remnant yet, with Plan an order's cuts.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a part that
  fits no piece in stock or a leftover with no dimensions, with the field to correct.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC05-18 Remnant](../../data/e-sc05-18-remnant.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-18 Remnant | Planned | Badge "Planned"; a new record starts here; next: Stocked (BR-SC05-19); fields editable within the role | U21, U20 | `u21-production-planner/s-sc05-19-cutting-e-sc05-18-remnant-planned-{desktop,phone}-{light,dark}.png`, `u20-production-operator/s-sc05-19-cutting-e-sc05-18-remnant-planned-tablet-{light,dark}.png` |
| E-SC05-18 Remnant | Stocked | Badge "Stocked"; next: Used or Scrapped (UC-SC05-19); fields editable within the role | U21, U20 | `u21-production-planner/s-sc05-19-cutting-e-sc05-18-remnant-stocked-{desktop,phone}-{light,dark}.png`, `u20-production-operator/s-sc05-19-cutting-e-sc05-18-remnant-stocked-tablet-{light,dark}.png` |
| E-SC05-18 Remnant | Used | Badge "Used"; final: read-only, no next state; the history shows how it got here | U21, U20 | `u21-production-planner/s-sc05-19-cutting-e-sc05-18-remnant-used-{desktop,phone}-{light,dark}.png`, `u20-production-operator/s-sc05-19-cutting-e-sc05-18-remnant-used-tablet-{light,dark}.png` |
| E-SC05-18 Remnant | Scrapped | Badge "Scrapped"; final: read-only, no next state; the history shows how it got here | U21, U20 | `u21-production-planner/s-sc05-19-cutting-e-sc05-18-remnant-scrapped-{desktop,phone}-{light,dark}.png`, `u20-production-operator/s-sc05-19-cutting-e-sc05-18-remnant-scrapped-tablet-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the planner. The operator uses the tablet with the layout drawn to scale and the measurement fields in large
type.

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

⬅️ [S-SC05-18 Personalisation](s-sc05-18-personalisation.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-L01 Production setups](../00-lists/s-sc05-l01-production-setups.md)
