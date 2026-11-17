🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-08 Budgets, rolling forecasts, group and valuation](README.md) › 🖥️ S-F23-26 Rolling forecast

# 🖥️ S-F23-26 Rolling forecast

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the version being rolled, its variances and its
  assumptions.
- [U13 Owner](../../../../01-users/personas/u13-owner.md): the published versions and what moved.

## Purpose

Roll the forecast forward each month, review its assumptions and publish a numbered version.

## Entry points

What-if simulation › Rolling forecast; the month-close checklist; the owner's briefing.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Rolling forecast   Horizon 2026-11 to 2027-10   Draft version 11   Previous 10      [Publish]  |
|---------------------------------------------------------------------------------------------|
| LINE            V10       V11       MOVE     BUDGET    ACTUAL OCT   ASSUMPTION              |
| Revenue         1,820 k   1,790 k   -30 k    1,850 k   142 k        2 deals slipped         |
| Costs           1,610 k   1,625 k   +15 k    1,600 k   131 k        supplier +3 %           |
| Cash low point  2027-03   2027-04   +3 weeks -         -            payment terms           |
| [Edit assumption] [Compare versions] [Publish] [Discard draft]                              |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-08 step 2, U05 | desktop | ![FL-F23-08 step 2, U05, light](../../images/08-budgets-rolling-group-and-valuation/u05-accounting/2-rolling-forecast-desktop-light.png) | ![FL-F23-08 step 2, U05, dark](../../images/08-budgets-rolling-group-and-valuation/u05-accounting/2-rolling-forecast-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-26-rolling-forecast-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-26-rolling-forecast-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-26-rolling-forecast-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-26-rolling-forecast-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-26-rolling-forecast-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-26-rolling-forecast-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f23-26-rolling-forecast-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f23-26-rolling-forecast-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Version and horizon | E-F23-16 number, horizon | text | no | yes |
| Lines by version | E-F23-16 totals | amounts with currency | no | yes |
| Move | difference to the previous version | amount and percent | no | no |
| Assumptions | E-F23-16 assumptions | text per line | while Draft | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Edit assumption | row | accounting | changes an assumption of a month ahead |
| Compare versions | toolbar | accounting, owner | shows two versions side by side |
| Publish | header | accounting | publishes the draft and supersedes the previous version |
| Discard draft | header | accounting | drops the draft |

## States

- Normal: the draft version against the previous one, the budget and the latest actuals.
- Empty: No version yet, with Roll the first forecast from the baseline.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused roll
  names the open period and links to the close checklist.
- Read-only: A published or superseded version shows its figures and assumptions; it is never edited.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F23-16 Forecast version](../../data/e-f23-16-forecast-version.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F23-16 Forecast version | Draft | Badge "Draft"; a new record starts here; next: Published or Discarded (UC-F23-32); fields editable within the role | U05, U13 | `u05-accounting/s-f23-26-rolling-forecast-e-f23-16-forecast-version-draft-desktop-{light,dark}.png`, `u13-owner/s-f23-26-rolling-forecast-e-f23-16-forecast-version-draft-{desktop,phone}-{light,dark}.png` |
| E-F23-16 Forecast version | Published | Badge "Published"; next: Superseded (BR-F23-19); fields editable within the role | U05, U13 | `u05-accounting/s-f23-26-rolling-forecast-e-f23-16-forecast-version-published-desktop-{light,dark}.png`, `u13-owner/s-f23-26-rolling-forecast-e-f23-16-forecast-version-published-{desktop,phone}-{light,dark}.png` |
| E-F23-16 Forecast version | Discarded | Badge "Discarded"; final: read-only, no next state; the history shows how it got here | U05, U13 | `u05-accounting/s-f23-26-rolling-forecast-e-f23-16-forecast-version-discarded-desktop-{light,dark}.png`, `u13-owner/s-f23-26-rolling-forecast-e-f23-16-forecast-version-discarded-{desktop,phone}-{light,dark}.png` |
| E-F23-16 Forecast version | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U05, U13 | `u05-accounting/s-f23-26-rolling-forecast-e-f23-16-forecast-version-superseded-desktop-{light,dark}.png`, `u13-owner/s-f23-26-rolling-forecast-e-f23-16-forecast-version-superseded-{desktop,phone}-{light,dark}.png` |

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

- [FL-F23-08](../../flows/fl-f23-08-budgets-rolling-group-and-valuation.md)

## Open questions

None.

---

⬅️ [S-F23-25 Collaborative budget](s-f23-25-collaborative-budget.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-27 Group scenario](s-f23-27-group-scenario.md)
