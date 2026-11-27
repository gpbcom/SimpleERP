🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-01 Public accounting](README.md) › 🖥️ S-SC20-01 Budget vote

# 🖥️ S-SC20-01 Budget vote

**Status:** ✅ specified

## Personas

- [U54 Public finance officer](../../../../01-users/personas/u54-public-finance-officer.md): the budget by chapter, with
  its balance and its vote.
- [U55 Elected official](../../../../01-users/personas/u55-elected-official.md): the budget to read and the vote to
  follow.

## Purpose

Prepare the yearly budget by chapter, check its balance, record the council's vote and transmit it.

## Entry points

Public bodies › Budgets; the budget season reminder.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Budget 2027: Commune of Valmont                         State: Draft   [Check balance]           |
| Section      Chapter                 Credit voted   Committed   Paid                             |
| Operation    Staff costs             1,820,000      -           -                                |
| Operation    General services        640,000        -           -                                |
| Investment   Roads and networks      900,000        -           -                                |
| Balance: operation OK, investment OK      Vote on 28 March 2027   [Record vote] [Transmit]       |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-01 step 1, U54 | desktop | ![FL-SC20-01 step 1, U54, light](../../images/01-public-accounting/u54-public-finance-officer/1-budget-vote-desktop-light.png) | ![FL-SC20-01 step 1, U54, dark](../../images/01-public-accounting/u54-public-finance-officer/1-budget-vote-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-01-budget-vote-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-01-budget-vote-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-01-budget-vote-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-01-budget-vote-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-01-budget-vote-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-01-budget-vote-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-01-budget-vote-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-01-budget-vote-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Year | E-SC20-01 year | number | no | yes |
| Kind | E-SC20-01 kind | primary, supplementary | yes while Draft | yes |
| Chapters | E-SC20-01 chapters | section, chapter and credit | yes while Draft | yes |
| Revenue | E-SC20-01 revenue | list of source and amount | yes while Draft | yes |
| Vote date | E-SC20-01 vote date | date | yes | yes to vote |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Check balance | header | public finance officer | each section is checked for balance |
| Record vote | header | public finance officer | the credits are opened with the vote date |
| Transmit | header | public finance officer | the budget is sent to the prefecture |

## States

- Normal: the budget with its chapters, credits, balance, vote date and state.
- Empty: No budget yet, with Start the year's budget.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an unbalanced
  section, a chapter without credit, a transmission failed, with the chapter named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-01 Budget](../../data/e-sc20-01-budget.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-01 Budget | Draft | Badge "Draft"; a new record starts here; next: Voted (BR-SC20-01); fields editable within the role | U54, U55 | `u54-public-finance-officer/s-sc20-01-budget-vote-e-sc20-01-budget-draft-desktop-{light,dark}.png`, `u55-elected-official/s-sc20-01-budget-vote-e-sc20-01-budget-draft-desktop-{light,dark}.png` |
| E-SC20-01 Budget | Voted | Badge "Voted"; next: Transmitted (UC-SC20-01); fields editable within the role | U54, U55 | `u54-public-finance-officer/s-sc20-01-budget-vote-e-sc20-01-budget-voted-desktop-{light,dark}.png`, `u55-elected-official/s-sc20-01-budget-vote-e-sc20-01-budget-voted-desktop-{light,dark}.png` |
| E-SC20-01 Budget | Transmitted | Badge "Transmitted"; next: Closed (UC-SC20-04); fields editable within the role | U54, U55 | `u54-public-finance-officer/s-sc20-01-budget-vote-e-sc20-01-budget-transmitted-desktop-{light,dark}.png`, `u55-elected-official/s-sc20-01-budget-vote-e-sc20-01-budget-transmitted-desktop-{light,dark}.png` |
| E-SC20-01 Budget | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U54, U55 | `u54-public-finance-officer/s-sc20-01-budget-vote-e-sc20-01-budget-closed-desktop-{light,dark}.png`, `u55-elected-official/s-sc20-01-budget-vote-e-sc20-01-budget-closed-desktop-{light,dark}.png` |

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

- [FL-SC20-01 Public accounting](../../flows/fl-sc20-01-public-accounting.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC20-02 Commitments](s-sc20-02-commitments.md)
