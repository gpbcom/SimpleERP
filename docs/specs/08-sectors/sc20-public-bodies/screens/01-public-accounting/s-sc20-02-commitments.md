🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-01 Public accounting](README.md) › 🖥️ S-SC20-02 Commitments

# 🖥️ S-SC20-02 Commitments

**Status:** ✅ specified

## Personas

- [U54 Public finance officer](../../../../01-users/personas/u54-public-finance-officer.md): the commitments by chapter,
  with the credit left.

## Purpose

Commit expenditure on a chapter before an order and keep the credit left up to date.

## Entry points

Public bodies › Commitments; a department's request; a purchase request.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Commitments: 2027                                          [New commitment] [Release]            |
| Number      Chapter           Supplier        Amount    Used     Credit left   State             |
| 2027-0411   Schools           Mobilier Pro    18,000    0        42,000        Open              |
| 2027-0398   Roads             Travaux Sud     120,000   60,000   300,000       Partly used       |
| 2027-0377   General services  Papeterie Lac   2,400     2,400    -             Closed            |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-01 step 2, U54 | desktop | ![FL-SC20-01 step 2, U54, light](../../images/01-public-accounting/u54-public-finance-officer/2-commitments-desktop-light.png) | ![FL-SC20-01 step 2, U54, dark](../../images/01-public-accounting/u54-public-finance-officer/2-commitments-desktop-dark.png) |
| Error E1, U54 | desktop | ![Error E1, U54, light](../../images/01-public-accounting/u54-public-finance-officer/e1-the-credit-is-exceeded-desktop-light.png) | ![Error E1, U54, dark](../../images/01-public-accounting/u54-public-finance-officer/e1-the-credit-is-exceeded-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-02-commitments-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-02-commitments-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-02-commitments-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-02-commitments-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-02-commitments-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-02-commitments-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-02-commitments-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-02-commitments-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Number | E-SC20-02 number | text | no | yes |
| Chapter | E-SC20-02 chapter | link to a budget chapter | yes while Open | yes |
| Supplier | E-SC20-02 supplier | link | yes while Open | yes |
| Amount | E-SC20-02 amount | amount | yes while Open | yes |
| Credit left | E-SC20-01 left | amount | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New commitment | header | public finance officer | a commitment is checked against the credit |
| Release | row | public finance officer | an unused amount is freed |
| Transfer | row | public finance officer | a transfer between chapters is requested |

## States

- Normal: the commitments with number, chapter, supplier, amount, use and state.
- Empty: No commitment yet, with New commitment.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a credit not
  enough, a chapter missing, with the chapter named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-02 Commitment](../../data/e-sc20-02-commitment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-02 Commitment | Open | Badge "Open"; a new record starts here; next: Partly used or Closed (UC-SC20-03, UC-SC20-02); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-02-commitments-e-sc20-02-commitment-open-desktop-{light,dark}.png` |
| E-SC20-02 Commitment | Partly used | Badge "Partly used"; next: Closed (UC-SC20-03); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-02-commitments-e-sc20-02-commitment-partly-used-desktop-{light,dark}.png` |
| E-SC20-02 Commitment | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U54 | `u54-public-finance-officer/s-sc20-02-commitments-e-sc20-02-commitment-closed-desktop-{light,dark}.png` |

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

⬅️ [S-SC20-01 Budget vote](s-sc20-01-budget-vote.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-03 Orders and titles](s-sc20-03-orders-and-titles.md)
