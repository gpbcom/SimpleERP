🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-01 Public accounting](README.md) › 🖥️ S-SC20-03 Orders and titles

# 🖥️ S-SC20-03 Orders and titles

**Status:** ✅ specified

## Personas

- [U54 Public finance officer](../../../../01-users/personas/u54-public-finance-officer.md): the payment orders and
  revenue titles to draft, sign and send.

## Purpose

Draft and sign the payment orders and revenue titles from the commitments and the supporting documents.

## Entry points

Public bodies › Orders and titles; a checked supplier invoice; a revenue due.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Orders and titles                                          [Draft] [Sign batch] [Send]           |
| Kind       Number    Third party      Amount     Commitment   Signed by    State                 |
| Mandate    M-1204    Mobilier Pro     18,000     2027-0411    -            Drafted               |
| Mandate    M-1203    Travaux Sud      60,000     2027-0398    Mayor        Signed                |
| Title      T-0388    Valmont Hall     240        -            Mayor        Sent                  |
| Rejected: M-1198 missing contract copy                       [Correct]                           |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-01 step 3, U54 | desktop | ![FL-SC20-01 step 3, U54, light](../../images/01-public-accounting/u54-public-finance-officer/3-orders-and-titles-desktop-light.png) | ![FL-SC20-01 step 3, U54, dark](../../images/01-public-accounting/u54-public-finance-officer/3-orders-and-titles-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-03-orders-and-titles-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-03-orders-and-titles-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-03-orders-and-titles-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-03-orders-and-titles-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-03-orders-and-titles-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-03-orders-and-titles-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-03-orders-and-titles-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-03-orders-and-titles-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Kind | E-SC20-03 kind | mandate or revenue title | yes while Drafted | yes |
| Third party | E-SC20-03 third party | link | yes while Drafted | yes |
| Amount | E-SC20-03 amount | amount | yes while Drafted | yes |
| Commitment | E-SC20-03 commitment | link | yes while Drafted | yes for a mandate |
| Supporting documents | E-SC20-03 documents | list | yes while Drafted | yes |
| Signed by | E-SC20-03 signed by | user with a delegation | no | yes to send |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Draft | header | public finance officer | an order is created from an invoice or a due |
| Sign batch | header | authorising officer or delegate | the orders are signed |
| Send | header | public finance officer | the signed batch goes to the public accountant |

## States

- Normal: the orders and titles with kind, third party, amount, commitment, signer and state.
- Empty: No order or title yet.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  document, a signer without delegation, a rejection, with the order named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-03 Payment order](../../data/e-sc20-03-payment-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-03 Payment order | Drafted | Badge "Drafted"; a new record starts here; next: Signed (BR-SC20-03); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-03-orders-and-titles-e-sc20-03-payment-order-drafted-desktop-{light,dark}.png` |
| E-SC20-03 Payment order | Signed | Badge "Signed"; next: Sent (UC-SC20-04); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-03-orders-and-titles-e-sc20-03-payment-order-signed-desktop-{light,dark}.png` |
| E-SC20-03 Payment order | Sent | Badge "Sent"; next: Paid or Rejected (UC-SC20-04); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-03-orders-and-titles-e-sc20-03-payment-order-sent-desktop-{light,dark}.png` |
| E-SC20-03 Payment order | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U54 | `u54-public-finance-officer/s-sc20-03-orders-and-titles-e-sc20-03-payment-order-paid-desktop-{light,dark}.png` |
| E-SC20-03 Payment order | Rejected | Badge "Rejected"; next: Drafted (UC-SC20-03); fields editable within the role | U54 | `u54-public-finance-officer/s-sc20-03-orders-and-titles-e-sc20-03-payment-order-rejected-desktop-{light,dark}.png` |

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

⬅️ [S-SC20-02 Commitments](s-sc20-02-commitments.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-04 Treasury exchange](s-sc20-04-treasury-exchange.md)
