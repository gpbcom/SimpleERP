🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-06 Cashless, cinemas, tours and photographers](README.md) ›
🖥️ S-SC16-21 Cashless payments

# 🖥️ S-SC16-21 Cashless payments

**Status:** 🔄 waiting for the owner

## Personas

- [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md): the gate: linking wristbands and
  loading accounts on the phone.
- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md): the money loaded, spent, held and refunded.

## Purpose

Link wristbands to accounts, load and debit them at the stands, and refund the unused balances after the event.

## Entry points

Events and culture › Cashless; the gate's phone; a stand's till.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Cashless: Jazz Night 2026                     Held 18,420.00 EUR  [Close accounts] [Pay refunds] |
| Wristband   Visitor        Loaded    Spent     Balance   State       Refund                      |
| 0412        Marie L.       20.00     12.50     7.50      Active      -                           |
| 0413        Karim D.       50.00     50.00     0.00      Closed      -                           |
| 0414        Julie R.       30.00     8.00      22.00     Refunded    22.00 on 2026-07-20         |
| Accounts: 3,204    Active 2,980   Refund requests waiting 41                                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-06 step 1, U44 | phone | ![FL-SC16-06 step 1, U44, light](../../images/06-cashless-cinemas-tours-and-photos/u44-box-office-agent/1-cashless-phone-light.png) | ![FL-SC16-06 step 1, U44, dark](../../images/06-cashless-cinemas-tours-and-photos/u44-box-office-agent/1-cashless-phone-dark.png) |
| FL-SC16-06 step 1, U44 | desktop | ![FL-SC16-06 step 1, U44, light](../../images/06-cashless-cinemas-tours-and-photos/u44-box-office-agent/1-cashless-desktop-light.png) | ![FL-SC16-06 step 1, U44, dark](../../images/06-cashless-cinemas-tours-and-photos/u44-box-office-agent/1-cashless-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-21-cashless-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-21-cashless-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-21-cashless-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-21-cashless-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-21-cashless-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-21-cashless-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-21-cashless-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-21-cashless-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Wristband | E-SC16-19 wristband | text | no | yes |
| Visitor | E-SC16-19 visitor | link or anonymous | yes while Active | no |
| Loaded | E-SC16-19 loaded | amount in EUR | no | no |
| Spent | E-SC16-19 spent | amount in EUR | no | no |
| Balance | E-SC16-19 balance | amount in EUR | no | no |
| Bank account | E-SC16-19 refund account | text | yes while Closed | yes to refund |
| Refunded on | E-SC16-19 refunded on | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Link wristband | phone | box office agent | an account in state Active |
| Load | account | box office agent | the balance grows by the amount |
| Close accounts | header | event producer | every account is Closed and refundable |
| Pay refunds | header | event producer | the refunds requested are paid and the accounts are Refunded |

## States

- Normal: the accounts with wristband, visitor, loaded, spent, balance and state.
- Empty: No account yet, with Link wristband.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a purchase
  above the balance, a missing bank account, a second refund, with the account.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC16-19 Cashless account](../../data/e-sc16-19-cashless-account.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-19 Cashless account | Active | Badge "Active"; a new record starts here; next: Closed (UC-SC16-21); fields editable within the role | U44, U43 | `u44-box-office-agent/s-sc16-21-cashless-e-sc16-19-cashless-account-active-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-sc16-21-cashless-e-sc16-19-cashless-account-active-{desktop,phone}-{light,dark}.png` |
| E-SC16-19 Cashless account | Closed | Badge "Closed"; next: Refunded or Expired (BR-SC16-16); fields editable within the role | U44, U43 | `u44-box-office-agent/s-sc16-21-cashless-e-sc16-19-cashless-account-closed-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-sc16-21-cashless-e-sc16-19-cashless-account-closed-{desktop,phone}-{light,dark}.png` |
| E-SC16-19 Cashless account | Refunded | Badge "Refunded"; final: read-only, no next state; the history shows how it got here | U44, U43 | `u44-box-office-agent/s-sc16-21-cashless-e-sc16-19-cashless-account-refunded-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-sc16-21-cashless-e-sc16-19-cashless-account-refunded-{desktop,phone}-{light,dark}.png` |
| E-SC16-19 Cashless account | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U44, U43 | `u44-box-office-agent/s-sc16-21-cashless-e-sc16-19-cashless-account-expired-{desktop,phone}-{light,dark}.png`, `u43-event-producer/s-sc16-21-cashless-e-sc16-19-cashless-account-expired-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The gate's phone scans a wristband and shows its balance with Load as the main button.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC16-06](../../flows/fl-sc16-06-cashless-cinemas-tours-and-photos.md)

## Open questions

None.

---

⬅️ [S-SC16-20 Events assistant](../05-declarations-and-reports/s-sc16-20-events-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-22 Cinema](s-sc16-22-cinema.md)
