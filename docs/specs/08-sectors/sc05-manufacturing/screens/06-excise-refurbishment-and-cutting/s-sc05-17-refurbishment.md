🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-06 Excise, refurbishment, personalisation and cutting](README.md) ›
🖥️ S-SC05-17 Refurbishment

# 🖥️ S-SC05-17 Refurbishment

**Status:** 🔄 waiting for the owner

## Personas

- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md): the units on their bench, with
  the checklist and the grade.
- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md): the daily sample, the grades and the
  return rate.

## Purpose

Test, repair and grade each used unit at the bench and let the quality manager check the grades before sale.

## Entry points

Manufacturing › Graded units; the tablet's scan button; a returned unit's record.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Unit 358812  Phone, 128 GB                                     State: Tested    [Propose grade]  |
| Step                 Result       Reading      By         Time                                   |
| Data erasure         Passed       Certificate  Karim      09:12                                  |
| Battery health       Passed       91 %         Karim      09:20                                  |
| Screen               Replaced     Part P-884   Karim      09:41                                  |
| Grade proposed: B   Warranty 12 months     [Confirm grade]  [Send to repair]                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-06 step 2, U20 | tablet | ![FL-SC05-06 step 2, U20, light](../../images/06-excise-refurbishment-and-cutting/u20-production-operator/2-refurbishment-tablet-light.png) | ![FL-SC05-06 step 2, U20, dark](../../images/06-excise-refurbishment-and-cutting/u20-production-operator/2-refurbishment-tablet-dark.png) |
| Empty | tablet | ![Empty, light](../../images/states/s-sc05-17-refurbishment-empty-tablet-light.png) | ![Empty, dark](../../images/states/s-sc05-17-refurbishment-empty-tablet-dark.png) |
| Loading | tablet | ![Loading, light](../../images/states/s-sc05-17-refurbishment-loading-tablet-light.png) | ![Loading, dark](../../images/states/s-sc05-17-refurbishment-loading-tablet-dark.png) |
| Read-only | tablet | ![Read-only, light](../../images/states/s-sc05-17-refurbishment-read-only-tablet-light.png) | ![Read-only, dark](../../images/states/s-sc05-17-refurbishment-read-only-tablet-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc05-17-refurbishment-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc05-17-refurbishment-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Serial number | E-SC05-16 serial number | text | no | yes |
| Product | E-SC05-16 item | link | no | yes |
| Battery health | E-SC05-16 battery health | percent | yes while Received or Tested | no |
| Data erasure certificate | E-SC05-16 erasure certificate | file | yes while Received | yes |
| Parts replaced | E-SC05-16 parts | list of items | yes while Tested | no |
| Grade | E-SC05-16 grade | A, B or C | quality manager | yes to sell |
| Warranty end | E-SC05-16 warranty end | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Scan a unit | tablet header | production operator | the unit's record opens or is created |
| Propose grade | unit | production operator | a grade from the criteria and the readings |
| Confirm grade | unit | quality manager | the unit becomes Graded and enters stock |
| Send to repair | unit | production operator | a repair order and the unit returns to tests |

## States

- Normal: the unit's steps with their results, the parts used and the proposed grade.
- Empty: No unit yet, with Scan a unit.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  erasure certificate or battery reading, with the step to complete.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC05-16 Graded unit](../../data/e-sc05-16-graded-unit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-16 Graded unit | Received | Badge "Received"; a new record starts here; next: Tested or Scrapped (UC-SC05-17); fields editable within the role | U20, U27 | `u20-production-operator/s-sc05-17-refurbishment-e-sc05-16-graded-unit-received-tablet-{light,dark}.png`, `u27-quality-manager/s-sc05-17-refurbishment-e-sc05-16-graded-unit-received-{desktop,tablet}-{light,dark}.png` |
| E-SC05-16 Graded unit | Tested | Badge "Tested"; next: Graded (BR-SC05-17); fields editable within the role | U20, U27 | `u20-production-operator/s-sc05-17-refurbishment-e-sc05-16-graded-unit-tested-tablet-{light,dark}.png`, `u27-quality-manager/s-sc05-17-refurbishment-e-sc05-16-graded-unit-tested-{desktop,tablet}-{light,dark}.png` |
| E-SC05-16 Graded unit | Graded | Badge "Graded"; next: Sold (UC-SC05-17); fields editable within the role | U20, U27 | `u20-production-operator/s-sc05-17-refurbishment-e-sc05-16-graded-unit-graded-tablet-{light,dark}.png`, `u27-quality-manager/s-sc05-17-refurbishment-e-sc05-16-graded-unit-graded-{desktop,tablet}-{light,dark}.png` |
| E-SC05-16 Graded unit | Sold | Badge "Sold"; final: read-only, no next state; the history shows how it got here | U20, U27 | `u20-production-operator/s-sc05-17-refurbishment-e-sc05-16-graded-unit-sold-tablet-{light,dark}.png`, `u27-quality-manager/s-sc05-17-refurbishment-e-sc05-16-graded-unit-sold-{desktop,tablet}-{light,dark}.png` |
| E-SC05-16 Graded unit | Scrapped | Badge "Scrapped"; final: read-only, no next state; the history shows how it got here | U20, U27 | `u20-production-operator/s-sc05-17-refurbishment-e-sc05-16-graded-unit-scrapped-tablet-{light,dark}.png`, `u27-quality-manager/s-sc05-17-refurbishment-e-sc05-16-graded-unit-scrapped-{desktop,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Tablet at the bench with large buttons and the camera scan. The quality manager's review is on a desktop.

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

⬅️ [S-SC05-16 Alcohol excise](s-sc05-16-alcohol-excise.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-18 Personalisation](s-sc05-18-personalisation.md)
