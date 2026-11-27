🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-07 Passengers, removals, courier and freight](README.md) › 🖥️ S-SC07-21 Passenger transport

# 🖥️ S-SC07-21 Passenger transport

**Status:** 🔄 waiting for the owner

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md): the trips, their vehicles and the drivers who
  qualify.
- [U30 Driver](../../../../01-users/personas/u30-driver.md): their trip with the stops and the passenger list.

## Purpose

Plan a passenger trip with a vehicle that has the seats and a driver who holds the licence for its class.

## Entry points

Transport and logistics › Passenger trips; the planning board; the driver's phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Trip PT-2210  Sat 22 Nov  07:30  Lyon -> Annecy                  State: Planned  [Assign]        |
| Passengers 48   Class needed: coach 49-53 seats   Quote Q-1042   Price 960.00                    |
| Vehicle              Seats  Class   Free      Driver            Licence   Hours left             |
| Coach 41       52     D       yes       Moreau            D, card   6 h 20                       |
| Coach 12      49     D       yes       Petit             B only    not allowed                   |
| Minibus 7   19     D1      yes       Garcia            D1        9 h                             |
| Stops: 07:30 Lyon station, 09:10 Annecy lake              Reduced mobility: 2                    |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-07 step 1, U29 | desktop | ![FL-SC07-07 step 1, U29, light](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/1-passenger-transport-desktop-light.png) | ![FL-SC07-07 step 1, U29, dark](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/1-passenger-transport-desktop-dark.png) |
| FL-SC07-07 step 1, U29 | phone | ![FL-SC07-07 step 1, U29, light](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/1-passenger-transport-phone-light.png) | ![FL-SC07-07 step 1, U29, dark](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/1-passenger-transport-phone-dark.png) |
| Error E1, U29 | desktop | ![Error E1, U29, light](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/e1-the-licence-class-is-missing-desktop-light.png) | ![Error E1, U29, dark](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/e1-the-licence-class-is-missing-desktop-dark.png) |
| Error E1, U29 | phone | ![Error E1, U29, light](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/e1-the-licence-class-is-missing-phone-light.png) | ![Error E1, U29, dark](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/e1-the-licence-class-is-missing-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-21-passenger-transport-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-21-passenger-transport-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-21-passenger-transport-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-21-passenger-transport-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-21-passenger-transport-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-21-passenger-transport-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-21-passenger-transport-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-21-passenger-transport-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Date and time | E-SC07-18 start | date and time | yes while Planned | yes |
| From and to | E-SC07-18 pick-up, drop-off | places | yes while Planned | yes |
| Passengers | E-SC07-18 passengers | number | yes while Planned | yes |
| Vehicle | E-SC07-18 vehicle | link | yes while Planned | yes |
| Driver | E-SC07-18 driver | link | yes while Planned | yes |
| Quote | E-SC07-18 quote | link | yes while Planned | no |
| Passenger list | E-SC07-18 passenger list | names and needs | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Assign | row | dispatcher | the driver and the vehicle are checked and the trip is Dispatched |
| Split | trip | dispatcher | two trips share the passengers |
| Start | driver's phone | driver | the trip is Running with the list of stops |
| Complete | driver's phone | driver | the trip is Completed and ready to bill |

## States

- Normal: the trip with its vehicles, drivers, licence checks and passengers.
- Empty: No trip yet, with New trip.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a licence not
  covering the class, a rest time exceeded or too many passengers, with the way to correct it.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC07-18 Passenger trip](../../data/e-sc07-18-passenger-trip.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-18 Passenger trip | Planned | Badge "Planned"; a new record starts here; next: Dispatched or Cancelled (BR-SC07-16, UC-SC07-21); fields editable within the role | U29, U30 | `u29-dispatcher/s-sc07-21-passenger-transport-e-sc07-18-passenger-trip-planned-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-21-passenger-transport-e-sc07-18-passenger-trip-planned-phone-{light,dark}.png` |
| E-SC07-18 Passenger trip | Dispatched | Badge "Dispatched"; next: Running (UC-SC07-21); fields editable within the role | U29, U30 | `u29-dispatcher/s-sc07-21-passenger-transport-e-sc07-18-passenger-trip-dispatched-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-21-passenger-transport-e-sc07-18-passenger-trip-dispatched-phone-{light,dark}.png` |
| E-SC07-18 Passenger trip | Running | Badge "Running"; next: Completed (UC-SC07-21); fields editable within the role | U29, U30 | `u29-dispatcher/s-sc07-21-passenger-transport-e-sc07-18-passenger-trip-running-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-21-passenger-transport-e-sc07-18-passenger-trip-running-phone-{light,dark}.png` |
| E-SC07-18 Passenger trip | Completed | Badge "Completed"; final: read-only, no next state; the history shows how it got here | U29, U30 | `u29-dispatcher/s-sc07-21-passenger-transport-e-sc07-18-passenger-trip-completed-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-21-passenger-transport-e-sc07-18-passenger-trip-completed-phone-{light,dark}.png` |
| E-SC07-18 Passenger trip | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U29, U30 | `u29-dispatcher/s-sc07-21-passenger-transport-e-sc07-18-passenger-trip-cancelled-{desktop,phone}-{light,dark}.png`, `u30-driver/s-sc07-21-passenger-transport-e-sc07-18-passenger-trip-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the dispatcher. The driver's phone shows the next stop, the passenger count and the list in large type.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC07-07](../../flows/fl-sc07-07-passengers-removals-courier-and-freight.md)

## Open questions

None.

---

⬅️ [S-SC07-20 Fleet assistant](../01-orders-and-planning/s-sc07-20-fleet-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-22 Removals](s-sc07-22-removals.md)
