🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-01 Memberships and access](README.md) › 🖥️ S-SC18-01 Membership sale

# 🖥️ S-SC18-01 Membership sale

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): every plan, contract and sale.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own contract and its terms.

## Purpose

Offer a plan, show the terms, take the signature and start the membership.

## Entry points

Sports and fitness › Club memberships; the member's page; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Membership sale: Mia L.                                                  Offered                 |
| Plan   Annual adult   39.00 EUR a month   Commitment 12 months   Notice 1 month                  |
| Renewal  after 12 months, month by month   Cancel from the app, notice 1 month                   |
| Terms shown on 2026-11-21 10:05    Signed on the phone 2026-11-21 10:07                          |
| Payment  Direct debit (mandate to sign)   First due 2026-12-01                                   |
| [Sign]  [Start the membership]  [Send a copy]                                                    |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-01 step 1, U13 | desktop | ![FL-SC18-01 step 1, U13, light](../../images/01-memberships-and-access/u13-owner/1-membership-sale-desktop-light.png) | ![FL-SC18-01 step 1, U13, dark](../../images/01-memberships-and-access/u13-owner/1-membership-sale-desktop-dark.png) |
| FL-SC18-01 step 1, U13 | phone | ![FL-SC18-01 step 1, U13, light](../../images/01-memberships-and-access/u13-owner/1-membership-sale-phone-light.png) | ![FL-SC18-01 step 1, U13, dark](../../images/01-memberships-and-access/u13-owner/1-membership-sale-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc18-01-membership-sale-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc18-01-membership-sale-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc18-01-membership-sale-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc18-01-membership-sale-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc18-01-membership-sale-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc18-01-membership-sale-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-01-membership-sale-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-01-membership-sale-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Member | E-SC18-01 member | link | no | yes |
| Plan | E-SC18-01 plan | choice | yes while Offered | yes |
| Commitment and notice | E-SC18-01 commitment, notice | months | yes while Offered | yes |
| Cancellation terms | E-SC18-01 cancellation terms | text | no | yes |
| Signed on | E-SC18-01 signed on | date and time | no | yes |
| Payment method | E-SC18-02 mandate | link | yes while Offered | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Offer a plan | header | owner | a membership is created Offered |
| Sign | footer | member | the terms are signed |
| Start | footer | owner | the membership becomes Active and the access opens |
| Send a copy | footer | owner | the contract is sent to the member |

## States

- Normal: the plan, the terms shown, the signature and the payment method.
- Empty: No member chosen yet, with Find or create a member.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  signature or terms, or a failed payment, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-01 Club membership](../../data/e-sc18-01-club-membership.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-01 Club membership | Offered | Badge "Offered"; a new record starts here; next: Active or Withdrawn (BR-SC18-01, UC-SC18-01); fields editable within the role | U13, U09 | `u13-owner/s-sc18-01-membership-sale-e-sc18-01-club-membership-offered-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-01-membership-sale-e-sc18-01-club-membership-offered-phone-{light,dark}.png` |
| E-SC18-01 Club membership | Active | Badge "Active"; next: Frozen or Notice given (UC-SC18-04, BR-SC18-04); fields editable within the role | U13, U09 | `u13-owner/s-sc18-01-membership-sale-e-sc18-01-club-membership-active-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-01-membership-sale-e-sc18-01-club-membership-active-phone-{light,dark}.png` |
| E-SC18-01 Club membership | Frozen | Badge "Frozen"; next: Active (UC-SC18-04); fields editable within the role | U13, U09 | `u13-owner/s-sc18-01-membership-sale-e-sc18-01-club-membership-frozen-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-01-membership-sale-e-sc18-01-club-membership-frozen-phone-{light,dark}.png` |
| E-SC18-01 Club membership | Notice given | Badge "Notice given"; next: Ended (BR-SC18-04); fields editable within the role | U13, U09 | `u13-owner/s-sc18-01-membership-sale-e-sc18-01-club-membership-notice-given-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-01-membership-sale-e-sc18-01-club-membership-notice-given-phone-{light,dark}.png` |
| E-SC18-01 Club membership | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U13, U09 | `u13-owner/s-sc18-01-membership-sale-e-sc18-01-club-membership-ended-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-01-membership-sale-e-sc18-01-club-membership-ended-phone-{light,dark}.png` |
| E-SC18-01 Club membership | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U13, U09 | `u13-owner/s-sc18-01-membership-sale-e-sc18-01-club-membership-withdrawn-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc18-01-membership-sale-e-sc18-01-club-membership-withdrawn-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coach and the member use the phone, the owner and the treasurer a desktop, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-01 Memberships and access](../../flows/fl-sc18-01-memberships-and-access.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC18-02 Dues collection](s-sc18-02-dues-collection.md)
