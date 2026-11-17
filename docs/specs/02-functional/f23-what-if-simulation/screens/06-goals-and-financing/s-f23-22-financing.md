🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔮 [F23 What-if simulation and impact](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F23-06 Goals and financing](README.md) › 🖥️ S-F23-22 Financing

# 🖥️ S-F23-22 Financing

**Status:** ✅ specified

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)

## Purpose

Compare financing options and export the bank pack.

## Entry points

A scenario, Financing.

## Wireframe

```text
Financing options                                   [Add option] [Export pack]
-------------------------------------------------------------------------------
Option     Amount    Rate   Months   Cost       Cash low    Covenant
Loan       80 000    4.2 %  60       8 840      21 000      3.4 in March
Leasing    -         -      48       79 200     34 000      ok
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F23-06 step 3, U31 | desktop | ![FL-F23-06 step 3, U31, light](../../images/06-goals-and-financing/u31-treasurer/3-financing-desktop-light.png) | ![FL-F23-06 step 3, U31, dark](../../images/06-goals-and-financing/u31-treasurer/3-financing-desktop-dark.png) |
| FL-F23-06 step 3, U31 | phone | ![FL-F23-06 step 3, U31, light](../../images/06-goals-and-financing/u31-treasurer/3-financing-phone-light.png) | ![FL-F23-06 step 3, U31, dark](../../images/06-goals-and-financing/u31-treasurer/3-financing-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f23-22-financing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f23-22-financing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f23-22-financing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f23-22-financing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f23-22-financing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f23-22-financing-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f23-22-financing-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f23-22-financing-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Kind | E-F23-12 kind | list | yes | yes |
| Amount, rate, months | E-F23-12 | numbers | yes | yes |
| Covenant | E-F23-12 covenants | ratio | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Add option | header | treasurer, owner | option simulated |
| Export pack | header | accountant, owner | file |

## States

- Normal: options compared.
- Empty: "No option yet".
- Loading: the frame and titles show at once with placeholder rows for the options; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a covenant breach flagged.
- Read-only: accounting reads.
- Offline: not available offline: simulations run on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F23-05 Impact result](../../data/e-f23-05-impact-result.md),
[E-F23-12 Financing option](../../data/e-f23-12-financing-option.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F23-05 Impact result | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U08, U13, U31 | `u08-external-accountant/s-f23-22-financing-e-f23-05-impact-result-recorded-desktop-{light,dark}.png`, `u13-owner/s-f23-22-financing-e-f23-05-impact-result-recorded-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f23-22-financing-e-f23-05-impact-result-recorded-{desktop,phone}-{light,dark}.png` |
| E-F23-12 Financing option | Draft | Badge "Draft"; a new record starts here; next: Simulated (UC-F23-29); fields editable within the role | U08, U13, U31 | `u08-external-accountant/s-f23-22-financing-e-f23-12-financing-option-draft-desktop-{light,dark}.png`, `u13-owner/s-f23-22-financing-e-f23-12-financing-option-draft-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f23-22-financing-e-f23-12-financing-option-draft-{desktop,phone}-{light,dark}.png` |
| E-F23-12 Financing option | Simulated | Badge "Simulated"; next: Chosen (UC-F23-23); fields editable within the role | U08, U13, U31 | `u08-external-accountant/s-f23-22-financing-e-f23-12-financing-option-simulated-desktop-{light,dark}.png`, `u13-owner/s-f23-22-financing-e-f23-12-financing-option-simulated-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f23-22-financing-e-f23-12-financing-option-simulated-{desktop,phone}-{light,dark}.png` |
| E-F23-12 Financing option | Chosen | Badge "Chosen"; final: read-only, no next state; the history shows how it got here | U08, U13, U31 | `u08-external-accountant/s-f23-22-financing-e-f23-12-financing-option-chosen-desktop-{light,dark}.png`, `u13-owner/s-f23-22-financing-e-f23-12-financing-option-chosen-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-f23-22-financing-e-f23-12-financing-option-chosen-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F23-06 Goals and financing](../../flows/fl-f23-06-goals-and-financing.md)

## Open questions

None.

---

⬅️ [S-F23-21 Goal seeking](s-f23-21-goal-seeking.md) · ⬆️ [Up](README.md) ·
➡️ [S-F23-23 Forecast accuracy](../07-accuracy-and-drivers/s-f23-23-forecast-accuracy.md)
