🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-03 Licences and competitions](README.md) › 🖥️ S-SC18-12 Results

# 🖥️ S-SC18-12 Results

**Status:** ✅ specified

## Personas

- [U53 Coach](../../../../01-users/personas/u53-coach.md): the results of their teams.

## Purpose

Enter a result, have it validated and publish it in the standings and the app.

## Entry points

Sports and fitness › Results; the match's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Results: District league U15                                              Day 9                  |
| Match                       Score   Entered by   Validated by   State                            |
| U15 Club - Rivals          3 - 1   Hugo B.      Karim A.       Published                         |
| U15 Club - North City      2 - 2   Hugo B.      -              Entered                           |
| U15 Club - East End        0 - 1   Hugo B.      Karim A.       Contested                         |
| [Enter a result]  [Validate]  [Publish]  [Contest]                                               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-03 step 4, U53 | phone | ![FL-SC18-03 step 4, U53, light](../../images/03-licences-and-competitions/u53-coach/4-results-phone-light.png) | ![FL-SC18-03 step 4, U53, dark](../../images/03-licences-and-competitions/u53-coach/4-results-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc18-12-results-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc18-12-results-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc18-12-results-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc18-12-results-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc18-12-results-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc18-12-results-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-12-results-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-12-results-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Match | E-SC18-09 match | link | no | yes |
| Score | E-SC18-09 score | numbers | yes while Entered | yes |
| Notes | E-SC18-09 notes | text | yes while Entered | no |
| Entered by | E-SC18-09 entered by | employee | no | yes |
| Validated by | E-SC18-09 validated by | person | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Enter a result | header | coach | a result is saved Entered |
| Validate | result row | second person | the result becomes Validated |
| Publish | result row | owner, coach | the result becomes Published |
| Contest | result row | owner, other team | the result becomes Contested |

## States

- Normal: the results with their validation and publication.
- Empty: No result entered yet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a publication
  with no validation, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-09 Result](../../data/e-sc18-09-result.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-09 Result | Entered | Badge "Entered"; a new record starts here; next: Validated (BR-SC18-12); fields editable within the role | U53 | `u53-coach/s-sc18-12-results-e-sc18-09-result-entered-phone-{light,dark}.png` |
| E-SC18-09 Result | Validated | Badge "Validated"; next: Published (BR-SC18-12); fields editable within the role | U53 | `u53-coach/s-sc18-12-results-e-sc18-09-result-validated-phone-{light,dark}.png` |
| E-SC18-09 Result | Published | Badge "Published"; next: Contested (UC-SC18-12); fields editable within the role | U53 | `u53-coach/s-sc18-12-results-e-sc18-09-result-published-phone-{light,dark}.png` |
| E-SC18-09 Result | Contested | Badge "Contested"; next: Validated (UC-SC18-12); fields editable within the role | U53 | `u53-coach/s-sc18-12-results-e-sc18-09-result-contested-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coach and the member use the phone, the owner and the treasurer a desktop, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-03 Licences and competitions](../../flows/fl-sc18-03-licences-and-competitions.md)

## Open questions

None.

---

⬅️ [S-SC18-11 Teams and competitions](s-sc18-11-teams-and-competitions.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-13 Coaching packages](../04-personal-training/s-sc18-13-coaching-packages.md)
