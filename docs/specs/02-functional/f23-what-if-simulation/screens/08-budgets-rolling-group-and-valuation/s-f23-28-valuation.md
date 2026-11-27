🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-08 Budgets, rolling forecasts, group and valuation](README.md) › 🖥️ S-F23-28 Valuation

# 🖥️ S-F23-28 Valuation

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the company's valuations, their methods and assumptions.
- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md): the organisation's net assets and reserve.

## Purpose

Value the company from a forecast or a scenario, with every method and assumption shown.

## Entry points

What-if simulation › Valuation; a forecast version; the funding round screen.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Valuation   Based on: Forecast version 11   Purpose: funding round        [Issue] [Compare]  |
|---------------------------------------------------------------------------------------------|
| METHOD              LOW        CENTRAL    HIGH       KEY ASSUMPTIONS                        |
| Multiple of revenue 2.2 M      2.8 M      3.3 M      1.2 to 1.8, source: sector drivers      |
| Discounted cash     4.1 M      4.8 M      5.6 M      rate 11 %, growth 2 %                   |
| Net assets          1.9 M      1.9 M      1.9 M      book value, no adjustments               |
| [Open method] [Edit assumptions] [Add method]                                               |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-08 step 4, U13 | desktop | ![FL-F23-08 step 4, U13, light](../../images/08-budgets-rolling-group-and-valuation/u13-owner/4-valuation-desktop-light.png) | ![FL-F23-08 step 4, U13, dark](../../images/08-budgets-rolling-group-and-valuation/u13-owner/4-valuation-desktop-dark.png) |
| FL-F23-08 step 4, U13 | phone | ![FL-F23-08 step 4, U13, light](../../images/08-budgets-rolling-group-and-valuation/u13-owner/4-valuation-phone-light.png) | ![FL-F23-08 step 4, U13, dark](../../images/08-budgets-rolling-group-and-valuation/u13-owner/4-valuation-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-28-valuation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-28-valuation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-28-valuation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-28-valuation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-28-valuation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-28-valuation-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f23-28-valuation-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f23-28-valuation-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Based on | E-F23-17 forecast version or scenario | link | while Draft | yes |
| Purpose | E-F23-17 purpose | text | while Draft | yes |
| Method and range | E-F23-17 methods | low, central, high amounts | no | yes |
| Assumptions | E-F23-17 assumptions | values with their source | while Draft | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add method | toolbar | owner, treasurer | adds a method with its assumptions |
| Edit assumptions | row | owner, treasurer | changes the assumptions, while Draft |
| Compare | toolbar | owner, treasurer, accounting | compares two valuations |
| Issue | header | owner, treasurer | issues the valuation |

## States

- Normal: the methods with their low, central and high values and the assumptions of each.
- Empty: No valuation yet, with Start a valuation from a forecast version.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  assumption is named on its method and the value is not shown.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F23-17 Valuation](../../data/e-f23-17-valuation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F23-17 Valuation | Draft | Badge "Draft"; a new record starts here; next: Issued or Discarded (BR-F23-21, UC-F23-34); fields editable within the role | U13, U31 | `u13-owner/s-f23-28-valuation-e-f23-17-valuation-draft-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f23-28-valuation-e-f23-17-valuation-draft-{desktop,phone}-{light,dark}.png` |
| E-F23-17 Valuation | Issued | Badge "Issued"; next: Superseded (UC-F23-34); fields editable within the role | U13, U31 | `u13-owner/s-f23-28-valuation-e-f23-17-valuation-issued-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f23-28-valuation-e-f23-17-valuation-issued-{desktop,phone}-{light,dark}.png` |
| E-F23-17 Valuation | Discarded | Badge "Discarded"; final: read-only, no next state; the history shows how it got here | U13, U31 | `u13-owner/s-f23-28-valuation-e-f23-17-valuation-discarded-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f23-28-valuation-e-f23-17-valuation-discarded-{desktop,phone}-{light,dark}.png` |
| E-F23-17 Valuation | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U13, U31 | `u13-owner/s-f23-28-valuation-e-f23-17-valuation-superseded-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f23-28-valuation-e-f23-17-valuation-superseded-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F23-27 Group scenario](s-f23-27-group-scenario.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-L01 Baseline forecasts](../00-lists/s-f23-l01-baseline-forecasts.md)
