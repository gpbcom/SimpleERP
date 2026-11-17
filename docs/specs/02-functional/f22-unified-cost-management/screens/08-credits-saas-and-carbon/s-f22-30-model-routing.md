🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-08 Credits, SaaS subscriptions, carbon and routing](README.md) › 🖥️ S-F22-30 Model routing

# 🖥️ S-F22-30 Model routing

**Status:** 🔄 waiting for the owner

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): every rule, its scores and its saving.

## Purpose

Route each kind of AI task to the cheapest model that meets its quality bar, and show the saving.

## Entry points

Platform costs › Model routing; a savings recommendation; the AI settings.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Model routing                                   Active 4   Paused 1   Saved this month 212 EUR |
|---------------------------------------------------------------------------------------------|
| TASK KIND       MODELS (IN ORDER)   BAR   SCORE  COST/CALL  SAVED    STATE                  |
| Summaries       small, large        0.85  0.88   0.004 EUR  120 EUR  Active                 |
| Invoice reading medium, large       0.92  0.89   0.020 EUR  0 EUR    Testing                |
| Drafts          small, large        0.80  0.78   0.006 EUR  92 EUR   Paused                 |
| [New rule] [Run evaluation] [Activate] [Retire]                                             |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-08 step 4, U07 | desktop | ![FL-F22-08 step 4, U07, light](../../images/08-credits-saas-and-carbon/u07-administrator/4-model-routing-desktop-light.png) | ![FL-F22-08 step 4, U07, dark](../../images/08-credits-saas-and-carbon/u07-administrator/4-model-routing-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-30-model-routing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-30-model-routing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-30-model-routing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-30-model-routing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-30-model-routing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-30-model-routing-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f22-30-model-routing-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f22-30-model-routing-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Task kind | E-F22-21 task kind | text | while Draft | yes |
| Models in order | E-F22-21 models | list of models | while Draft or Testing | yes |
| Quality bar | E-F22-21 bar | number from 0 to 1 | while Draft or Testing | yes |
| Score measured | E-F22-21 score | number from 0 to 1 | no | no |
| Cost cap per call | E-F22-21 cost cap | amount with currency | yes | no |
| Saved | E-F22-21 saving | amount with currency | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New rule | header | administrator | creates a rule in Draft |
| Run evaluation | row | administrator | runs the task kind's evaluation set on each model |
| Activate | row | administrator | makes the rule live when the bar is reached |
| Retire | row | administrator | ends the rule; calls go back to the default model |

## States

- Normal: the rules with task kind, models, bar, score, cost per call, saving and state.
- Empty: No rule yet, with New rule and the savings recommendations that could start one.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  activation shows the score, the bar and the model that fell short.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F22-21 Routing rule](../../data/e-f22-21-routing-rule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-21 Routing rule | Draft | Badge "Draft"; a new record starts here; next: Testing or Retired (UC-F22-30); fields editable within the role | U07 | `u07-administrator/s-f22-30-model-routing-e-f22-21-routing-rule-draft-desktop-{light,dark}.png` |
| E-F22-21 Routing rule | Testing | Badge "Testing"; next: Active or Draft (BR-F22-21); fields editable within the role | U07 | `u07-administrator/s-f22-30-model-routing-e-f22-21-routing-rule-testing-desktop-{light,dark}.png` |
| E-F22-21 Routing rule | Active | Badge "Active"; next: Paused or Retired (BR-F22-21, UC-F22-30); fields editable within the role | U07 | `u07-administrator/s-f22-30-model-routing-e-f22-21-routing-rule-active-desktop-{light,dark}.png` |
| E-F22-21 Routing rule | Paused | Badge "Paused"; next: Testing (UC-F22-30); fields editable within the role | U07 | `u07-administrator/s-f22-30-model-routing-e-f22-21-routing-rule-paused-desktop-{light,dark}.png` |
| E-F22-21 Routing rule | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f22-30-model-routing-e-f22-21-routing-rule-retired-desktop-{light,dark}.png` |

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

- [FL-F22-08](../../flows/fl-f22-08-credits-saas-and-carbon.md)

## Open questions

None.

---

⬅️ [S-F22-29 Compute carbon](s-f22-29-compute-carbon.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-L01 Cost periods](../00-lists/s-f22-l01-cost-periods.md)
