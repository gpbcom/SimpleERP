🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-06 Experts, cutover, parallel run and set-up from documents](README.md) › 🖥️ S-F21-28 Parallel run

# 🖥️ S-F21-28 Parallel run

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the accounting comparison and its explanations.
- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md): the payroll comparison, net pay per
  employee.

## Purpose

Compare the old tool's results with SimpleERP's for a period and explain every difference.

## Entry points

Onboarding and module activation › Parallel runs; the cutover plan's parallel step; the migration guide.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Parallel run: accounting, October 2026     Old tool: Old invoicing tool       State: Compared    |
|---------------------------------------------------------------------------------------------|
| Measures compared 42     Differences 3     Explained 1     Tolerance 0.50 EUR                  |
| MEASURE               OLD TOOL      SIMPLE-ERP    GAP      EXPLANATION                         |
| Account 445710 VAT    12,410.20     12,410.70     +0.50    Rounding (explained)               |
| Account 411 Customers 88,300.00     88,130.00     -170.00  [Choose an explanation]            |
| Invoice total Oct     141,020.00    141,020.00    0        -                                   |
| [Explain] [Accept with a note] [Open a correction] [Mark the old tool stopped] (locked)       |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-06 step 3, U05 | desktop | ![FL-F21-06 step 3, U05, light](../../images/06-experts-cutover-and-parallel-run/u05-accounting/3-parallel-run-desktop-light.png) | ![FL-F21-06 step 3, U05, dark](../../images/06-experts-cutover-and-parallel-run/u05-accounting/3-parallel-run-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-28-parallel-run-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-28-parallel-run-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-28-parallel-run-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-28-parallel-run-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-28-parallel-run-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-28-parallel-run-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f21-28-parallel-run-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f21-28-parallel-run-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Area and period | E-F21-21 area, period | list and month | yes while Planned | yes |
| Old tool | E-F21-21 old tool | migration source | yes while Planned | yes |
| Measures and gaps | E-F21-21 measures | figure, figure, gap | no | yes |
| Explanation of a gap | E-F21-21 explanation | rounding, rule, timing, old error, new error, not migrated | by the person in charge | for each gap |
| Tolerance | E-F21-21 tolerance | amount | by the administrator | yes |
| Run state | E-F21-21 state | badge | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Load the old results | header | accounting, payroll officer | reads the old tool's export |
| Explain a gap | row | accounting, payroll officer | sets the explanation and a note |
| Open a correction | row | accounting, payroll officer | a defect of SimpleERP is opened |
| Mark the old tool stopped | header | administrator | possible only when every gap is explained |

## States

- Normal: the measures with their gaps, explanations and the run's state.
- Empty: No run yet, with Plan a parallel run.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an unreadable
  export shows the lines that could not be read.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F21-21 Parallel run](../../data/e-f21-21-parallel-run.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-21 Parallel run | Planned | Badge "Planned"; a new record starts here; next: Running or Abandoned (UC-F21-28); fields editable within the role | U05, U45 | `u05-accounting/s-f21-28-parallel-run-e-f21-21-parallel-run-planned-desktop-{light,dark}.png`, `u45-payroll-officer/s-f21-28-parallel-run-e-f21-21-parallel-run-planned-desktop-{light,dark}.png` |
| E-F21-21 Parallel run | Running | Badge "Running"; next: Compared or Abandoned (UC-F21-28); fields editable within the role | U05, U45 | `u05-accounting/s-f21-28-parallel-run-e-f21-21-parallel-run-running-desktop-{light,dark}.png`, `u45-payroll-officer/s-f21-28-parallel-run-e-f21-21-parallel-run-running-desktop-{light,dark}.png` |
| E-F21-21 Parallel run | Compared | Badge "Compared"; next: Explained or Running (BR-F21-19, UC-F21-28); fields editable within the role | U05, U45 | `u05-accounting/s-f21-28-parallel-run-e-f21-21-parallel-run-compared-desktop-{light,dark}.png`, `u45-payroll-officer/s-f21-28-parallel-run-e-f21-21-parallel-run-compared-desktop-{light,dark}.png` |
| E-F21-21 Parallel run | Explained | Badge "Explained"; next: Closed (BR-F21-19); fields editable within the role | U05, U45 | `u05-accounting/s-f21-28-parallel-run-e-f21-21-parallel-run-explained-desktop-{light,dark}.png`, `u45-payroll-officer/s-f21-28-parallel-run-e-f21-21-parallel-run-explained-desktop-{light,dark}.png` |
| E-F21-21 Parallel run | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U05, U45 | `u05-accounting/s-f21-28-parallel-run-e-f21-21-parallel-run-closed-desktop-{light,dark}.png`, `u45-payroll-officer/s-f21-28-parallel-run-e-f21-21-parallel-run-closed-desktop-{light,dark}.png` |
| E-F21-21 Parallel run | Abandoned | Badge "Abandoned"; final: read-only, no next state; the history shows how it got here | U05, U45 | `u05-accounting/s-f21-28-parallel-run-e-f21-21-parallel-run-abandoned-desktop-{light,dark}.png`, `u45-payroll-officer/s-f21-28-parallel-run-e-f21-21-parallel-run-abandoned-desktop-{light,dark}.png` |

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

- [FL-F21-06](../../flows/fl-f21-06-experts-cutover-and-parallel-run.md)

## Open questions

None.

---

⬅️ [S-F21-27 Cutover](s-f21-27-cutover.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-29 Set up from documents](s-f21-29-setup-from-documents.md)
