🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-07 Equity, contracts, meetings and disputes](README.md) › 🖥️ S-F15-14 Dilution

# 🖥️ S-F15-14 Dilution

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the rounds and their scenarios.
- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md): the numbers behind each scenario.

## Purpose

Simulate a round, compare scenarios and see each holder's dilution, with nothing recorded.

## Entry points

Administration › Company records › Dilution; the planning screens of the treasurer.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Round: Series A (simulation)                     Draft simulation    [Share copy] [Save]     |
|---------------------------------------------------------------------------------------------|
| Raised 800,000   Pre-money 3,200,000   Price 320.00   New shares 2,500   Pool top-up 5%     |
| HOLDER           BEFORE   AFTER    CHANGE                                                   |
| Anne Verdier     60.0     48.0     -12.0                                                    |
| Marc Leroy       22.0     17.6     -4.4                                                     |
| Investors        0.0      20.0     +20.0                                                    |
| Simulation only: the register is unchanged.                                                 |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-07 step 3, U13 | desktop | ![FL-F15-07 step 3, U13, light](../../images/07-equity-contracts-and-disputes/u13-owner/3-dilution-desktop-light.png) | ![FL-F15-07 step 3, U13, dark](../../images/07-equity-contracts-and-disputes/u13-owner/3-dilution-desktop-dark.png) |
| FL-F15-07 step 3, U13 | phone | ![FL-F15-07 step 3, U13, light](../../images/07-equity-contracts-and-disputes/u13-owner/3-dilution-phone-light.png) | ![FL-F15-07 step 3, U13, dark](../../images/07-equity-contracts-and-disputes/u13-owner/3-dilution-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-14-dilution-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-14-dilution-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-14-dilution-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-14-dilution-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-14-dilution-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-14-dilution-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f15-14-dilution-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f15-14-dilution-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Round | E-F15-17 name, date | text and date | while Simulating | yes |
| Amount and pre-money | E-F15-17 amount, valuation | two amounts | while Simulating | yes |
| Price and new shares | E-F15-17 price, new shares | amount and number | no | yes |
| Investors | E-F15-17 investors | list with amounts | while Simulating | no |
| Before and after | E-F15-17 table | percentages per holder | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New scenario | header | owner, treasurer | a copy of the round with other terms |
| Compare | header | owner, treasurer | two scenarios side by side |
| Share copy | header | owner | a read-only copy for the investors |
| Mark executed | row | owner | links the real subscriptions of the register |

## States

- Normal: the round's terms and the table before and after.
- Empty: No round yet, with New round.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused term
  shows the field and the limit.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F15-17 Funding round](../../data/e-f15-17-funding-round.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-17 Funding round | Simulating | Badge "Simulating"; a new record starts here; next: Shared or Abandoned (UC-F15-16); fields editable within the role | U13, U31 | `u13-owner/s-f15-14-dilution-e-f15-17-funding-round-simulating-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f15-14-dilution-e-f15-17-funding-round-simulating-{desktop,phone}-{light,dark}.png` |
| E-F15-17 Funding round | Shared | Badge "Shared"; next: Executed or Abandoned (BR-F15-20, UC-F15-16); fields editable within the role | U13, U31 | `u13-owner/s-f15-14-dilution-e-f15-17-funding-round-shared-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f15-14-dilution-e-f15-17-funding-round-shared-{desktop,phone}-{light,dark}.png` |
| E-F15-17 Funding round | Executed | Badge "Executed"; final: read-only, no next state; the history shows how it got here | U13, U31 | `u13-owner/s-f15-14-dilution-e-f15-17-funding-round-executed-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f15-14-dilution-e-f15-17-funding-round-executed-{desktop,phone}-{light,dark}.png` |
| E-F15-17 Funding round | Abandoned | Badge "Abandoned"; final: read-only, no next state; the history shows how it got here | U13, U31 | `u13-owner/s-f15-14-dilution-e-f15-17-funding-round-abandoned-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f15-14-dilution-e-f15-17-funding-round-abandoned-{desktop,phone}-{light,dark}.png` |

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

- [FL-F15-07](../../flows/fl-f15-07-equity-contracts-and-disputes.md)

## Open questions

None.

---

⬅️ [S-F15-13 Employee equity](s-f15-13-employee-equity.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-15 Contract drafting](s-f15-15-contract-drafting.md)
