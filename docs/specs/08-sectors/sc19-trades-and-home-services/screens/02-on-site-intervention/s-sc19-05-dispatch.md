🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-02 On-site intervention](README.md) › 🖥️ S-SC19-05 Dispatch

# 🖥️ S-SC19-05 Dispatch

**Status:** 🔄 waiting for the owner

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md): the requests, the technicians on the map and the
  proposals.

## Purpose

Create interventions from calls, send the nearest qualified technician and announce the terms to the customer.

## Entry points

Trades and home services › Interventions › Dispatch; the incoming call route; the customer portal.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Dispatch                                              [New intervention] [Map] [Auto mode: off]  |
| Request  Customer      Trade      Problem        Proposed        Arrival   State                 |
| I-3305   Garcia        Plumbing   Leak (sink)    Leroy           25 min    Requested             |
| I-3304   Bernard       Heating    No hot water   Petit           40 min    Dispatched            |
| I-3303   Moreau        Electricity Power cut     -               -         Requested             |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-02 step 1, U29 | desktop | ![FL-SC19-02 step 1, U29, light](../../images/02-on-site-intervention/u29-dispatcher/1-dispatch-desktop-light.png) | ![FL-SC19-02 step 1, U29, dark](../../images/02-on-site-intervention/u29-dispatcher/1-dispatch-desktop-dark.png) |
| FL-SC19-02 step 1, U29 | phone | ![FL-SC19-02 step 1, U29, light](../../images/02-on-site-intervention/u29-dispatcher/1-dispatch-phone-light.png) | ![FL-SC19-02 step 1, U29, dark](../../images/02-on-site-intervention/u29-dispatcher/1-dispatch-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-05-dispatch-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-05-dispatch-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-05-dispatch-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-05-dispatch-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-05-dispatch-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-05-dispatch-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-05-dispatch-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-05-dispatch-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-SC19-04 customer | link | yes while Requested | yes |
| Address | E-SC19-04 address | address | yes while Requested | yes |
| Trade | E-SC19-04 trade | list of trades switched on | yes while Requested | yes |
| Problem | E-SC19-04 problem | text | yes while Requested | yes |
| Technician | E-SC19-04 technician | link | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New intervention | header | dispatcher | a request is created from the call |
| Propose | row | dispatcher | the nearest qualified technician is shown with his arrival |
| Dispatch | row | dispatcher | the technician receives the intervention |

## States

- Normal: the interventions with customer, trade, problem, proposed technician, arrival and state.
- Empty: No intervention open.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); no technician
  with the qualification, an address missing, with the request named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-04 Intervention](../../data/e-sc19-04-intervention.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-04 Intervention | Requested | Badge "Requested"; a new record starts here; next: Dispatched or Cancelled (BR-SC19-05, UC-SC19-05); fields editable within the role | U29 | `u29-dispatcher/s-sc19-05-dispatch-e-sc19-04-intervention-requested-{desktop,phone}-{light,dark}.png` |
| E-SC19-04 Intervention | Dispatched | Badge "Dispatched"; next: On site or Cancelled (UC-SC19-06, UC-SC19-05); fields editable within the role | U29 | `u29-dispatcher/s-sc19-05-dispatch-e-sc19-04-intervention-dispatched-{desktop,phone}-{light,dark}.png` |
| E-SC19-04 Intervention | On site | Badge "On site"; next: Reported (UC-SC19-06); fields editable within the role | U29 | `u29-dispatcher/s-sc19-05-dispatch-e-sc19-04-intervention-on-site-{desktop,phone}-{light,dark}.png` |
| E-SC19-04 Intervention | Reported | Badge "Reported"; next: Invoiced (BR-SC19-08); fields editable within the role | U29 | `u29-dispatcher/s-sc19-05-dispatch-e-sc19-04-intervention-reported-{desktop,phone}-{light,dark}.png` |
| E-SC19-04 Intervention | Invoiced | Badge "Invoiced"; final: read-only, no next state; the history shows how it got here | U29 | `u29-dispatcher/s-sc19-05-dispatch-e-sc19-04-intervention-invoiced-{desktop,phone}-{light,dark}.png` |
| E-SC19-04 Intervention | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U29 | `u29-dispatcher/s-sc19-05-dispatch-e-sc19-04-intervention-cancelled-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC19-02 On-site intervention](../../flows/fl-sc19-02-on-site-intervention.md)

## Open questions

None.

---

⬅️ [S-SC19-04 Contract renewal](../01-maintenance-contracts/s-sc19-04-contract-renewal.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-06 Site report](s-sc19-06-site-report.md)
