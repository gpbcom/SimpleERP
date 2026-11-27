🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-02 Public procurement](README.md) › 🖥️ S-SC20-08 Public contract

# 🖥️ S-SC20-08 Public contract

**Status:** ✅ specified

## Personas

- [U54 Public finance officer](../../../../01-users/personas/u54-public-finance-officer.md): the contracts, their
  invoices, deadlines and amendments.

## Purpose

Follow a public contract and pay its invoices within the legal term.

## Entry points

Public bodies › Public contracts; an invoice from the national platform.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Contract MP-2027-009: School catering, Cantine Plus      State: In progress   [Amend]            |
| Amount 182,000   Start 1 Sep 2027   End 31 Aug 2028   Term: 30 days                              |
| Invoice   Received    Deadline     Paid        Late days   Interest                              |
| F-4401    1 Oct        31 Oct       24 Oct      0           0.00                                 |
| F-4455    1 Nov        1 Dec        -           -           -                                    |
| Amendments: 0 of 2 allowed                                     [Close]                           |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-02 step 4, U54 | desktop | ![FL-SC20-02 step 4, U54, light](../../images/02-public-procurement/u54-public-finance-officer/4-public-contract-desktop-light.png) | ![FL-SC20-02 step 4, U54, dark](../../images/02-public-procurement/u54-public-finance-officer/4-public-contract-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-08-public-contract-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-08-public-contract-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-08-public-contract-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-08-public-contract-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-08-public-contract-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-08-public-contract-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-08-public-contract-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-08-public-contract-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Tender file | E-SC20-07 tender file | link | no | yes |
| Amount | E-SC20-07 amount | amount | yes by amendment | yes |
| Payment term | E-SC20-07 term | number of days | no | yes |
| Invoices | E-SC20-07 invoices | list of invoice, receipt, deadline and payment | no | no |
| Amendments | E-SC20-07 amendments | list with approval | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Link invoice | row | public finance officer | an invoice is matched to the contract |
| Amend | header | public finance officer | an amendment is recorded with its approval |
| Close | header | public finance officer | the contract is accepted and closed |

## States

- Normal: the contract with amount, term, invoices with deadlines, amendments and state.
- Empty: No contract in progress.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an invoice not
  matched, an amendment without approval, with the invoice named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-07 Public contract](../../data/e-sc20-07-public-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-07 Public contract | Signed | Badge "Signed"; a new record starts here; next: In progress (UC-SC20-08); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-08-public-contract-e-sc20-07-public-contract-signed-desktop-{light,dark}.png` |
| E-SC20-07 Public contract | In progress | Badge "In progress"; next: Accepted or Terminated (UC-SC20-08); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-08-public-contract-e-sc20-07-public-contract-in-progress-desktop-{light,dark}.png` |
| E-SC20-07 Public contract | Accepted | Badge "Accepted"; next: Closed (BR-SC20-08); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-08-public-contract-e-sc20-07-public-contract-accepted-desktop-{light,dark}.png` |
| E-SC20-07 Public contract | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U54 | `u54-public-finance-officer/s-sc20-08-public-contract-e-sc20-07-public-contract-closed-desktop-{light,dark}.png` |
| E-SC20-07 Public contract | Terminated | Badge "Terminated"; final: read-only, no next state; the history shows how it got here | U54 | `u54-public-finance-officer/s-sc20-08-public-contract-e-sc20-07-public-contract-terminated-desktop-{light,dark}.png` |

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

- [FL-SC20-02 Public procurement](../../flows/fl-sc20-02-public-procurement.md)

## Open questions

None.

---

⬅️ [S-SC20-07 Bid analysis](s-sc20-07-bid-analysis.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-09 Citizen request](../03-citizen-services/s-sc20-09-citizen-request.md)
