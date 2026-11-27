🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-07 Forum, live chat, voice and support contracts](README.md) › 🖥️ S-F16-20 Support contracts

# 🖥️ S-F16-20 Support contracts

**Status:** ✅ specified

## Personas

- [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md): every contract, balance
  and renewal.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their balance and bookings, from a phone.

## Purpose

Sell a block of support hours, follow the balance and ask consent beyond it.

## Entry points

Customer support agents › Support contracts; the customer's record; the portal.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Support contracts                                    Active 12   Almost used 3     [+ New]  |
|---------------------------------------------------------------------------------------------|
| CUSTOMER         HOURS  USED  LEFT  VALID UNTIL   RATE    STATE                            |
| Atelier Verdier  20     1.5   18.5  2027-11-14     90 EUR  Active                           |
| Norte SL         10     9.5   0.5   2027-02-01     95 EUR  Active, almost used              |
| Garden Tools     10     10    0     2026-11-10     95 EUR  Used up, consent needed          |
| [Renew] [Book time] [Ask consent] [Open customer]                                           |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-07 step 5, U41 | desktop | ![FL-F16-07 step 5, U41, light](../../images/07-live-chat-voice-and-contracts/u41-customer-success-manager/5-support-contracts-desktop-light.png) | ![FL-F16-07 step 5, U41, dark](../../images/07-live-chat-voice-and-contracts/u41-customer-success-manager/5-support-contracts-desktop-dark.png) |
| FL-F16-07 step 5, U41 | phone | ![FL-F16-07 step 5, U41, light](../../images/07-live-chat-voice-and-contracts/u41-customer-success-manager/5-support-contracts-phone-light.png) | ![FL-F16-07 step 5, U41, dark](../../images/07-live-chat-voice-and-contracts/u41-customer-success-manager/5-support-contracts-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-20-support-contracts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-20-support-contracts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-20-support-contracts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-20-support-contracts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-20-support-contracts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-20-support-contracts-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-20-support-contracts-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-20-support-contracts-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-F16-16 customer | name | no | yes |
| Hours, used, left | E-F16-16 hours | three numbers | no | yes |
| Valid until | E-F16-16 end date | date | while Offered | yes |
| Rate | E-F16-16 rate | amount per hour | while Offered | yes |
| Bookings | E-F16-16 bookings | list of hours and requests | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New contract | header | success manager | quote and invoice a block of hours |
| Book time | request | office worker | reduces the balance |
| Ask consent | row | office worker, success manager | asks the customer to accept extra hours |
| Renew | row | success manager | a new block for the same customer |

## States

- Normal: the contracts with hours, balance, validity and state.
- Empty: No contract yet, with New contract.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  booking shows the balance and the validity.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F16-16 Support contract](../../data/e-f16-16-support-contract.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-16 Support contract | Offered | Badge "Offered"; a new record starts here; next: Active or Cancelled (UC-F16-22); fields editable within the role | U41, U09 | `u41-customer-success-manager/s-f16-20-support-contracts-e-f16-16-support-contract-offered-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-20-support-contracts-e-f16-16-support-contract-offered-phone-{light,dark}.png` |
| E-F16-16 Support contract | Active | Badge "Active"; next: Used up or Expired (BR-F16-18, UC-F16-22); fields editable within the role | U41, U09 | `u41-customer-success-manager/s-f16-20-support-contracts-e-f16-16-support-contract-active-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-20-support-contracts-e-f16-16-support-contract-active-phone-{light,dark}.png` |
| E-F16-16 Support contract | Used up | Badge "Used up"; next: Active or Expired (BR-F16-18, UC-F16-22); fields editable within the role | U41, U09 | `u41-customer-success-manager/s-f16-20-support-contracts-e-f16-16-support-contract-used-up-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-20-support-contracts-e-f16-16-support-contract-used-up-phone-{light,dark}.png` |
| E-F16-16 Support contract | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U41, U09 | `u41-customer-success-manager/s-f16-20-support-contracts-e-f16-16-support-contract-expired-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-20-support-contracts-e-f16-16-support-contract-expired-phone-{light,dark}.png` |
| E-F16-16 Support contract | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U41, U09 | `u41-customer-success-manager/s-f16-20-support-contracts-e-f16-16-support-contract-cancelled-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-20-support-contracts-e-f16-16-support-contract-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The manager's table is desktop only. The customer reads their balance, validity and bookings on a phone and answers a
consent question with one tap.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F16-07](../../flows/fl-f16-07-live-chat-voice-and-contracts.md)

## Open questions

None.

---

⬅️ [S-F16-19 Proactive outreach](s-f16-19-proactive-outreach.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-21 Canned replies](s-f16-21-canned-replies.md)
