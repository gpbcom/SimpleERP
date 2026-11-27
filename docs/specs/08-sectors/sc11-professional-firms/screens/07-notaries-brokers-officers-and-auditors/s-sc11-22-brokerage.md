🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-07 Notaries, brokers, judicial officers and audit firms](README.md) ›
🖥️ S-SC11-22 Brokerage

# 🖥️ S-SC11-22 Brokerage

**Status:** 🔄 waiting for the owner

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md): the offers, policies and renewals.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own policies.

## Purpose

Compare offers, place policies and keep the brokerage's registration current.

## Entry points

Professional firm › Policies; the registration banner; the client's portal.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Registration: 22001234    Valid until 2027-02-28   Liability insurance valid   Guarantee valid   |
| Policy P-2026-0881: Mr Faure, tenant's insurance                  Quoted   [Place]               |
| Offer         Insurer    Premium   Cover               Commission                                |
| A             Insurer 1  420.00    contents 20,000     12 %                                      |
| B             Insurer 2  480.00    contents 30,000     12 %    chosen                            |
| Renewals in 60 days: 14        [Compare for renewal]                                             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-07 step 2, U36 | desktop | ![FL-SC11-07 step 2, U36, light](../../images/07-notaries-brokers-officers-and-auditors/u36-professional/2-brokerage-desktop-light.png) | ![FL-SC11-07 step 2, U36, dark](../../images/07-notaries-brokers-officers-and-auditors/u36-professional/2-brokerage-desktop-dark.png) |
| FL-SC11-07 step 2, U36 | phone | ![FL-SC11-07 step 2, U36, light](../../images/07-notaries-brokers-officers-and-auditors/u36-professional/2-brokerage-phone-light.png) | ![FL-SC11-07 step 2, U36, dark](../../images/07-notaries-brokers-officers-and-auditors/u36-professional/2-brokerage-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-22-brokerage-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-22-brokerage-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-22-brokerage-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-22-brokerage-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-22-brokerage-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-22-brokerage-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-22-brokerage-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-22-brokerage-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Client | E-SC11-17 client | link | yes while Quoted | yes |
| Branch and cover | E-SC11-17 branch, cover | text | yes while Quoted | yes |
| Insurer and premium | E-SC11-17 insurer, premium | text and amount | yes while Quoted | yes |
| Commission | E-SC11-17 commission | percentage | yes while Quoted | no |
| Start and renewal date | E-SC11-17 start, renewal | dates | yes while Quoted | yes |
| Registration check | E-SC11-17 registration checked on | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Request quotes | policy | broker | offers asked from the insurers |
| Place | policy | broker | the policy becomes Active if the registration is current |
| Renew | policy | broker | a new term with its premium |
| Cancel | policy | broker | the policy becomes Cancelled with its date |

## States

- Normal: the registration banner, the offers, the policy with its commission and dates.
- Empty: No policy yet, with New policy.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a lapsed
  registration or a missing guarantee, with the date and what to renew.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC11-17 Policy](../../data/e-sc11-17-policy.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-17 Policy | Quoted | Badge "Quoted"; a new record starts here; next: Active (BR-SC11-17); fields editable within the role | U36, U09 | `u36-professional/s-sc11-22-brokerage-e-sc11-17-policy-quoted-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc11-22-brokerage-e-sc11-17-policy-quoted-phone-{light,dark}.png` |
| E-SC11-17 Policy | Active | Badge "Active"; next: Renewal due or Cancelled (UC-SC11-22); fields editable within the role | U36, U09 | `u36-professional/s-sc11-22-brokerage-e-sc11-17-policy-active-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc11-22-brokerage-e-sc11-17-policy-active-phone-{light,dark}.png` |
| E-SC11-17 Policy | Renewal due | Badge "Renewal due"; next: Active or Cancelled (UC-SC11-22); fields editable within the role | U36, U09 | `u36-professional/s-sc11-22-brokerage-e-sc11-17-policy-renewal-due-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc11-22-brokerage-e-sc11-17-policy-renewal-due-phone-{light,dark}.png` |
| E-SC11-17 Policy | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U36, U09 | `u36-professional/s-sc11-22-brokerage-e-sc11-17-policy-cancelled-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc11-22-brokerage-e-sc11-17-policy-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the broker; the client reads their policies and renewals on the phone.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC11-07](../../flows/fl-sc11-07-notaries-brokers-officers-and-auditors.md)

## Open questions

None.

---

⬅️ [S-SC11-21 Notary](s-sc11-21-notary.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-23 Judicial officer](s-sc11-23-judicial-officer.md)
