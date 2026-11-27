🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F8-30 Payment means

# 🖥️ S-F8-30 Payment means

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the cheques and the LCR.
- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md): the remittances to the bank.

## Purpose

Group cheques and LCR on remittance slips, remit them and follow them until the bank credits.

## Entry points

Accounting › Payment means; a customer payment's Remit action.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Remittance slip RS-2026-044 cheques            Remitted 2026-11-12       Bank account BNP-1  |
|---------------------------------------------------------------------------------------------|
| Items 12   Total 8,640 EUR   On transit 8,640 EUR   Credited 8,490 EUR   Unpaid 150 EUR     |
| NUMBER    DRAWER          BANK        AMOUNT   STATE                                         |
| 0004412   Bois et Fils    CIC         1,200    Credited                                      |
| 0087321   Marc T.         LCL         150      Unpaid                                        |
| [Add a cheque] [Remit the slip] [Match the bank credit] [Mark unpaid]                        |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-11 step 2, U05 | desktop | ![FL-F8-11 step 2, U05, light](../../images/11-treasury-and-payment-means/u05-accounting/2-payment-means-desktop-light.png) | ![FL-F8-11 step 2, U05, dark](../../images/11-treasury-and-payment-means/u05-accounting/2-payment-means-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-30-payment-means-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-30-payment-means-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-30-payment-means-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-30-payment-means-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-30-payment-means-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-30-payment-means-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-30-payment-means-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-30-payment-means-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Slip, type and bank account | E-F8-35 | text | yes while Draft | yes |
| Items | E-F8-35 lines | table of number, drawer, amount | yes while Draft | yes |
| Total, on transit, credited, unpaid | E-F8-35 | four amounts | no | yes |
| State of each item | E-F8-35 line state | badge | no | yes |
| Bank credit | E-F8-04 | link | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add a cheque | header | accounting | the cheque joins the slip |
| Remit the slip | header | accounting, treasurer | the slip becomes Remitted and the amounts go to transit |
| Match the bank credit | row | accounting | credited items move to the bank account |
| Mark unpaid | row | accounting | the invoice is reopened |

## States

- Normal: the slip's items with their states and the amounts on transit and credited.
- Empty: No remittance slip yet, with New slip.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a cheque with
  inconsistent amounts shows both and blocks the remittance.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-35 Remittance slip](../../data/e-f08-35-remittance-slip.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-35 Remittance slip | Draft | Badge "Draft"; a new record starts here; next: Remitted (UC-F8-31); fields editable within the role | U05, U31 | `u05-accounting/s-f08-30-payment-means-e-f08-35-remittance-slip-draft-desktop-{light,dark}.png`, `u31-treasurer/s-f08-30-payment-means-e-f08-35-remittance-slip-draft-{desktop,phone}-{light,dark}.png` |
| E-F8-35 Remittance slip | Remitted | Badge "Remitted"; next: Credited or Partly credited (BR-F8-23); fields editable within the role | U05, U31 | `u05-accounting/s-f08-30-payment-means-e-f08-35-remittance-slip-remitted-desktop-{light,dark}.png`, `u31-treasurer/s-f08-30-payment-means-e-f08-35-remittance-slip-remitted-{desktop,phone}-{light,dark}.png` |
| E-F8-35 Remittance slip | Credited | Badge "Credited"; next: Closed (UC-F8-31); fields editable within the role | U05, U31 | `u05-accounting/s-f08-30-payment-means-e-f08-35-remittance-slip-credited-desktop-{light,dark}.png`, `u31-treasurer/s-f08-30-payment-means-e-f08-35-remittance-slip-credited-{desktop,phone}-{light,dark}.png` |
| E-F8-35 Remittance slip | Partly credited | Badge "Partly credited"; next: Credited or Closed (BR-F8-23, UC-F8-31); fields editable within the role | U05, U31 | `u05-accounting/s-f08-30-payment-means-e-f08-35-remittance-slip-partly-credited-desktop-{light,dark}.png`, `u31-treasurer/s-f08-30-payment-means-e-f08-35-remittance-slip-partly-credited-{desktop,phone}-{light,dark}.png` |
| E-F8-35 Remittance slip | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U05, U31 | `u05-accounting/s-f08-30-payment-means-e-f08-35-remittance-slip-closed-desktop-{light,dark}.png`, `u31-treasurer/s-f08-30-payment-means-e-f08-35-remittance-slip-closed-{desktop,phone}-{light,dark}.png` |

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

- [FL-F8-11 Treasury and payment means](../../flows/fl-f08-11-treasury-and-payment-means.md)

## Open questions

None.

---

⬅️ [S-F8-29 Loans](s-f08-29-loans.md) · ⬆️ [Up](README.md) · ➡️ [S-F8-31 FX revaluation](s-f08-31-fx-revaluation.md)
