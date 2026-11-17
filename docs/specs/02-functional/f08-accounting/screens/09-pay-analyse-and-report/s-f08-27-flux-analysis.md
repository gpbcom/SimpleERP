🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-09 Pay, analyse and report](README.md) › 🖥️ S-F8-27 Flux analysis

# 🖥️ S-F8-27 Flux analysis

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)

## Purpose

Show the month's variances with AI comments to review.

## Entry points

Accounting › Closing › Flux analysis.

## Wireframe

```text
+------------------------------------------------------------------+
| Flux November 2026 vs October   threshold 10 % and 5,000 EUR      |
| Account     Oct      Nov      Var.    Comment (draft)            |
| Rent        10,000   13,800   +38 %   New depot from October [ok]|
| Fuel        8,200    12,900   +57 %   Price and 2 new vans  [ok] |
|                                   [Send to the owner]             |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-09 step 2, U05 | desktop | ![FL-F8-09 step 2, U05, light](../../images/09-pay-analyse-and-report/u05-accounting/2-flux-analysis-desktop-light.png) | ![FL-F8-09 step 2, U05, dark](../../images/09-pay-analyse-and-report/u05-accounting/2-flux-analysis-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-27-flux-analysis-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-27-flux-analysis-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-27-flux-analysis-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-27-flux-analysis-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-27-flux-analysis-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-27-flux-analysis-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-27-flux-analysis-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-27-flux-analysis-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Accounts, variances, comments | E-F8-24 | comments |

## Actions

| Action | Who | Result |
|---|---|---|
| Confirm, edit | accounting | Comment confirmed |
| Send | accounting | Monthly report |

## States

- Normal: show the month's variances with AI comments to review.
- Empty: no variance above the threshold: "Nothing unusual this month".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a sent month.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F8-24 Variance comment](../../data/e-f08-24-variance-comment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-24 Variance comment | Draft | Badge "Draft"; a new record starts here; next: Confirmed (UC-F8-27); fields editable within the role | U05 | `u05-accounting/s-f08-27-flux-analysis-e-f08-24-variance-comment-draft-desktop-{light,dark}.png` |
| E-F8-24 Variance comment | Confirmed | Badge "Confirmed"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f08-27-flux-analysis-e-f08-24-variance-comment-confirmed-desktop-{light,dark}.png` |

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
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F8-09 Pay, analyse and report](../../flows/fl-f08-09-pay-analyse-and-report.md)

## Open questions

None.

---

⬅️ [S-F8-26 Doubtful debts](../08-year-end-duties/s-f08-26-doubtful-debts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-28 Sustainability report](s-f08-28-sustainability-report.md)
