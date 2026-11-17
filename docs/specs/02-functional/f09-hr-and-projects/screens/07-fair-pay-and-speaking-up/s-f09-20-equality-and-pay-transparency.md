🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-07 Fair pay and speaking up](README.md) › 🖥️ S-F9-20 Equality and pay transparency

# 🖥️ S-F9-20 Equality and pay transparency

**Status:** ✅ specified

## Personas

- [U06 Human resources](../../../../01-users/personas/u06-hr.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md)

## Purpose

Compute the equality index and pay gaps, plan measures and publish.

## Entry points

HR › Equality and pay.

## Wireframe

```text
+------------------------------------------------------------------+
| Equality index 2026    Score 84/100           [Publish] [Declare] |
| Pay gap 6 pts  Raises 20  Promotions 15  Maternity 15  Top 10: 2  |
| Category       Women  Men  Gap     Measures                       |
| Technicians    9      21   6 %     raise review 2027 [Edit]       |
| Drivers        2      9    not shown (too few)                    |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-07 step 1, U06 | desktop | ![FL-F9-07 step 1, U06, light](../../images/07-fair-pay-and-speaking-up/u06-hr/1-equality-and-pay-transparency-desktop-light.png) | ![FL-F9-07 step 1, U06, dark](../../images/07-fair-pay-and-speaking-up/u06-hr/1-equality-and-pay-transparency-desktop-dark.png) |
| Error E1, U06 | desktop | ![Error E1, U06, light](../../images/07-fair-pay-and-speaking-up/u06-hr/e1-equality-and-pay-transparency-refused-desktop-light.png) | ![Error E1, U06, dark](../../images/07-fair-pay-and-speaking-up/u06-hr/e1-equality-and-pay-transparency-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-20-equality-and-pay-transparency-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-20-equality-and-pay-transparency-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-20-equality-and-pay-transparency-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-20-equality-and-pay-transparency-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-20-equality-and-pay-transparency-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-20-equality-and-pay-transparency-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-20-equality-and-pay-transparency-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-20-equality-and-pay-transparency-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Indicators, gaps, measures | E-F9-20 | measures |

## Actions

| Action | Who | Result |
|---|---|---|
| Publish | HR, owner | Score published |
| Declare | HR | Sent |

## States

- Normal: compute the equality index and pay gaps, plan measures and publish.
- Empty: no payroll year yet: "The index needs a closed payroll year".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a published year.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F9-20 Equality index](../../data/e-f09-20-equality-index.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-20 Equality index | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F9-20); fields editable within the role | U06, U13 | `u06-hr/s-f09-20-equality-and-pay-transparency-e-f09-20-equality-index-draft-desktop-{light,dark}.png`, `u13-owner/s-f09-20-equality-and-pay-transparency-e-f09-20-equality-index-draft-{desktop,phone}-{light,dark}.png` |
| E-F9-20 Equality index | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U06, U13 | `u06-hr/s-f09-20-equality-and-pay-transparency-e-f09-20-equality-index-published-desktop-{light,dark}.png`, `u13-owner/s-f09-20-equality-and-pay-transparency-e-f09-20-equality-index-published-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-07 Fair pay and speaking up](../../flows/fl-f09-07-fair-pay-and-speaking-up.md)

## Open questions

None.

---

⬅️ [S-F9-19 Contract editor](../01-people/s-f09-19-contract-editor.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-21 Whistleblowing](s-f09-21-whistleblowing.md)
