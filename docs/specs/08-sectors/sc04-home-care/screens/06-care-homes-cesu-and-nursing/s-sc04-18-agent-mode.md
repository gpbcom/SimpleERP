🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-06 Care homes, CESU, agent mode, childcare and nursing](README.md) ›
🖥️ S-SC04-18 Agent mode

# 🖥️ S-SC04-18 Agent mode

**Status:** 🔄 waiting for the owner

## Personas

- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md): every mandate and the payslip runs.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own mandate, hours and payslips.

## Purpose

Run mandates for family employers: contracts, hours, payslips and the provider's fee.

## Entry points

Home care › Mandates; the family's page; the customer portal for the family.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Mandate: Martin family, carer Aisha T.                               Active   [Save] [End]       |
| Scope  search, contract, payslips, declarations     Fee 38.00 EUR a month     Signed 2026-10-02  |
| Employer  Martin family (not the provider)   Contract signed 2026-10-05                          |
| Month     Hours   Approved   Payslip       Declaration                                           |
| 2026-10   62.00   yes        issued        sent                                                  |
| 2026-11   58.50   waiting    -             -          [Remind the family]                        |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-06 step 3, U25 | desktop | ![FL-SC04-06 step 3, U25, light](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/3-agent-mode-desktop-light.png) | ![FL-SC04-06 step 3, U25, dark](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/3-agent-mode-desktop-dark.png) |
| FL-SC04-06 step 3, U25 | phone | ![FL-SC04-06 step 3, U25, light](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/3-agent-mode-phone-light.png) | ![FL-SC04-06 step 3, U25, dark](../../images/06-care-homes-cesu-and-nursing/u25-care-coordinator/3-agent-mode-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-18-agent-mode-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-18-agent-mode-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-18-agent-mode-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-18-agent-mode-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-18-agent-mode-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-18-agent-mode-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-18-agent-mode-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-18-agent-mode-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Family | E-SC04-16 family | link | no | yes |
| Carer | E-SC04-16 carer | link | no | yes |
| Scope and fee | E-SC04-16 scope, fee | choice and amount | yes while Draft | yes |
| Signed on | E-SC04-16 signed on | date | no | yes |
| Months | E-SC04-16 months | hours, approval, payslip, declaration | no | no |
| Employer | E-SC04-16 employer | the family | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send for signature | header | coordinator | the family receives the mandate on the phone |
| Prepare the contract | mandate | coordinator | the contract in the family's name |
| Approve hours | month row | family | the month's hours are approved |
| End the mandate | mandate | coordinator, family | the mandate becomes Ended |

## States

- Normal: the mandate with its scope, fee, employer and monthly hours, approvals, payslips and declarations.
- Empty: No mandate yet, with New mandate.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a contract
  naming the provider as employer or hours not approved, with what to change.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC04-16 Mandate](../../data/e-sc04-16-mandate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-16 Mandate | Draft | Badge "Draft"; a new record starts here; next: Active or Cancelled (BR-SC04-18, UC-SC04-18); fields editable within the role | U25, U09 | `u25-care-coordinator/s-sc04-18-agent-mode-e-sc04-16-mandate-draft-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc04-18-agent-mode-e-sc04-16-mandate-draft-phone-{light,dark}.png` |
| E-SC04-16 Mandate | Active | Badge "Active"; next: Ended (UC-SC04-18); fields editable within the role | U25, U09 | `u25-care-coordinator/s-sc04-18-agent-mode-e-sc04-16-mandate-active-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc04-18-agent-mode-e-sc04-16-mandate-active-phone-{light,dark}.png` |
| E-SC04-16 Mandate | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U25, U09 | `u25-care-coordinator/s-sc04-18-agent-mode-e-sc04-16-mandate-ended-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc04-18-agent-mode-e-sc04-16-mandate-ended-phone-{light,dark}.png` |
| E-SC04-16 Mandate | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U25, U09 | `u25-care-coordinator/s-sc04-18-agent-mode-e-sc04-16-mandate-cancelled-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc04-18-agent-mode-e-sc04-16-mandate-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coordinator works on a desktop; the carer and the family use the phone, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC04-06](../../flows/fl-sc04-06-care-homes-cesu-and-nursing.md)

## Open questions

None.

---

⬅️ [S-SC04-17 CESU](s-sc04-17-cesu.md) · ⬆️ [Up](README.md) · ➡️ [S-SC04-19 Childcare](s-sc04-19-childcare.md)
