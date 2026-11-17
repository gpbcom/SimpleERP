🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F8-08 Year-end duties](README.md) ›
🖥️ S-F8-26 Doubtful debts

# 🖥️ S-F8-26 Doubtful debts

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)

## Purpose

Review overdue receivables and provision those at risk.

## Entry points

Accounting › Closing › Doubtful debts.

## Wireframe

```text
+------------------------------------------------------------------+
| Doubtful debts at 2026-12-31                                      |
| Customer         Invoice        Days  Excl. VAT  Proposed  Reason |
| Café Bellecour   INV-2026-0911  200   2,000      50 %      age    |
| SARL Dupuis      INV-2026-0402  310   4,800      100 %     liquid.|
|                                   [Confirm all] [Post]            |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-08 step 1, U05 | desktop | ![FL-F8-08 step 1, U05, light](../../images/08-year-end-duties/u05-accounting/1-doubtful-debts-desktop-light.png) | ![FL-F8-08 step 1, U05, dark](../../images/08-year-end-duties/u05-accounting/1-doubtful-debts-desktop-dark.png) |
| Error E1, U05 | desktop | ![Error E1, U05, light](../../images/08-year-end-duties/u05-accounting/e1-doubtful-debts-refused-desktop-light.png) | ![Error E1, U05, dark](../../images/08-year-end-duties/u05-accounting/e1-doubtful-debts-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-26-doubtful-debts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-26-doubtful-debts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-26-doubtful-debts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-26-doubtful-debts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-26-doubtful-debts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-26-doubtful-debts-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-26-doubtful-debts-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-26-doubtful-debts-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Invoices, age, proposed rate, reason | E-F8-23 | rate and reason |

## Actions

| Action | Who | Result |
|---|---|---|
| Post | accounting | Provisions posted |

## States

- Normal: review overdue receivables and provision those at risk.
- Empty: no overdue receivable: "Nothing to provision".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted provisions of a locked period.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F8-23 Doubtful debt provision](../../data/e-f08-23-doubtful-debt-provision.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-23 Doubtful debt provision | Set | Badge "Set"; a new record starts here; next: Reversed (UC-F8-26); fields editable within the role | U05 | `u05-accounting/s-f08-26-doubtful-debts-e-f08-23-doubtful-debt-provision-set-desktop-{light,dark}.png` |
| E-F8-23 Doubtful debt provision | Reversed | Badge "Reversed"; next: Written off (UC-F8-26); fields editable within the role | U05 | `u05-accounting/s-f08-26-doubtful-debts-e-f08-23-doubtful-debt-provision-reversed-desktop-{light,dark}.png` |
| E-F8-23 Doubtful debt provision | Written off | Badge "Written off"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f08-26-doubtful-debts-e-f08-23-doubtful-debt-provision-written-off-desktop-{light,dark}.png` |

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

- [FL-F8-08 Year-end duties](../../flows/fl-f08-08-year-end-duties.md)

## Open questions

None.

---

⬅️ [S-F8-25 Annual accounts](s-f08-25-annual-accounts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-27 Flux analysis](../09-pay-analyse-and-report/s-f08-27-flux-analysis.md)
