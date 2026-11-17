🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-05 On-call, warranties, van stock and site quotes](README.md) › 🖥️ S-SC19-17 On-call

# 🖥️ S-SC19-17 On-call

**Status:** 🔄 waiting for the owner

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md): the rota of the month and the emergency calls with
  their surcharges.
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md): my on-call weeks and the emergency in progress,
  on the phone.

## Purpose

Plan the emergency rota, show the surcharge before dispatch and pass the allowances to payroll.

## Entry points

Trades and home services › On-call; the on-call phone's incoming call.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| On-call: March 2027                                  [Publish rota] [Swap] [Emergencies]         |
| Week   Plumbing        Heating         Electricity     Locksmith                                 |
| 10     Leroy / Petit   Noel / Petit    Bernard / -     Moreau / Noel                             |
| 11     Petit / Leroy   Noel / Leroy    Bernard / Noel  Moreau / -   (no backup)                  |
| Surcharges: night 90 EUR, Sunday 70 EUR, holiday 110 EUR          State: Draft                   |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-05 step 1, U29 | desktop | ![FL-SC19-05 step 1, U29, light](../../images/05-on-call-warranties-van-stock-and-site-quotes/u29-dispatcher/1-on-call-desktop-light.png) | ![FL-SC19-05 step 1, U29, dark](../../images/05-on-call-warranties-van-stock-and-site-quotes/u29-dispatcher/1-on-call-desktop-dark.png) |
| FL-SC19-05 step 1, U29 | phone | ![FL-SC19-05 step 1, U29, light](../../images/05-on-call-warranties-van-stock-and-site-quotes/u29-dispatcher/1-on-call-phone-light.png) | ![FL-SC19-05 step 1, U29, dark](../../images/05-on-call-warranties-van-stock-and-site-quotes/u29-dispatcher/1-on-call-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-17-on-call-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-17-on-call-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-17-on-call-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-17-on-call-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-17-on-call-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-17-on-call-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-17-on-call-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-17-on-call-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Week | E-SC19-11 week | date range | no | yes |
| Trade | E-SC19-11 trade | list of trades switched on | no | yes |
| On call | E-SC19-11 technician | link | yes while Draft | yes |
| Backup | E-SC19-11 backup | link | yes while Draft | yes |
| Surcharge | E-SC19-11 surcharge | amount per hour band | yes while Draft | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Publish rota | header | dispatcher | technicians and the on-call phone receive it |
| Swap | row | dispatcher | the week is swapped between two technicians |
| Open emergency | header | dispatcher | an intervention is created with the surcharge |

## States

- Normal: the weeks by trade with on-call technician, backup, surcharge and state.
- Empty: No rota yet, with Build the rota.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); no backup, a
  rest time broken, no surcharge for the hour, with the week named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-11 On-call rota](../../data/e-sc19-11-on-call-rota.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-11 On-call rota | Draft | Badge "Draft"; a new record starts here; next: Published (BR-SC19-17); fields editable within the role | U29, U14 | `u29-dispatcher/s-sc19-17-on-call-e-sc19-11-on-call-rota-draft-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-sc19-17-on-call-e-sc19-11-on-call-rota-draft-phone-{light,dark}.png` |
| E-SC19-11 On-call rota | Published | Badge "Published"; next: Draft or Closed (UC-SC19-17); fields editable within the role | U29, U14 | `u29-dispatcher/s-sc19-17-on-call-e-sc19-11-on-call-rota-published-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-sc19-17-on-call-e-sc19-11-on-call-rota-published-phone-{light,dark}.png` |
| E-SC19-11 On-call rota | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U29, U14 | `u29-dispatcher/s-sc19-17-on-call-e-sc19-11-on-call-rota-closed-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-sc19-17-on-call-e-sc19-11-on-call-rota-closed-phone-{light,dark}.png` |

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

- [FL-SC19-05](../../flows/fl-sc19-05-on-call-warranties-van-stock-and-site-quotes.md)

## Open questions

None.

---

⬅️ [S-SC19-16 Regulated records](../04-installations-and-labels/s-sc19-16-regulated-records.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-18 Builders' warranties](s-sc19-18-builders-warranties.md)
