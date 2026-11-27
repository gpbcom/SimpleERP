🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-07 Passengers, removals, courier and freight](README.md) › 🖥️ S-SC07-22 Removals

# 🖥️ S-SC07-22 Removals

**Status:** 🔄 waiting for the owner

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md): the quotes, the dates and the crews of each
  removal.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their quote to sign, then the list and the invoice.

## Purpose

Quote a move from its volume, hold the customer to the signed quote, list the goods with their condition and record
damage on the day.

## Entry points

Transport and logistics › Removals; the planning board; the customer's page on the phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Removal RM-0713  Dupont  Lyon 3e -> Villeurbanne  12 Dec        State: Signed  [Plan the day]    |
| Volume 28 m3   Floors 4 -> 2   Lift: no   Crew 3   Truck 20 m3 + trailer   Time 7 h              |
| Item               Room       Condition at loading        Photo   At unloading                   |
| Wardrobe 3 doors   Bedroom    Good                        yes     Scratch on the side            |
| Sofa 3 seats       Living     Small mark on the arm       yes     Same                           |
| Quote 1,980.00  signed 2026-11-30 on the phone      Insurance value 12,000    [Invoice]          |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-07 step 2, U29 | desktop | ![FL-SC07-07 step 2, U29, light](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/2-removals-desktop-light.png) | ![FL-SC07-07 step 2, U29, dark](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/2-removals-desktop-dark.png) |
| FL-SC07-07 step 2, U29 | phone | ![FL-SC07-07 step 2, U29, light](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/2-removals-phone-light.png) | ![FL-SC07-07 step 2, U29, dark](../../images/07-passengers-removals-courier-and-freight/u29-dispatcher/2-removals-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-22-removals-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-22-removals-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-22-removals-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-22-removals-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-22-removals-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-22-removals-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc07-22-removals-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc07-22-removals-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Customer | E-SC07-19 customer | link | no | yes |
| From and to | E-SC07-19 from, to | addresses with floor | yes while Quoted | yes |
| Volume | E-SC07-19 volume | number in m3 | yes while Quoted | yes |
| Crew and truck | E-SC07-19 crew, truck | links | yes | yes |
| Quote | E-SC07-19 quote | link | no | yes |
| Insured value | E-SC07-19 declared value | amount in EUR | yes while Quoted | yes |
| Items | E-SC07-19 items | list with condition and photo | yes on the day | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send quote | header | dispatcher | the customer receives it on the phone |
| Sign | customer's page | customer | the quote binds and the removal is Signed |
| Record item | crew's phone | crew | an item with its condition and photos |
| Note damage | item | crew, customer | a damage note with a photo attached to the removal |

## States

- Normal: the move with its quote, its crew and the listed items with their condition.
- Empty: No removal yet, with New removal.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a quote changed
  after signature or a truck not free, with the date to change.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC07-19 Removal](../../data/e-sc07-19-removal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC07-19 Removal | Quoted | Badge "Quoted"; a new record starts here; next: Signed or Lost (BR-SC07-17, UC-SC07-22); fields editable within the role | U29, U09 | `u29-dispatcher/s-sc07-22-removals-e-sc07-19-removal-quoted-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc07-22-removals-e-sc07-19-removal-quoted-phone-{light,dark}.png` |
| E-SC07-19 Removal | Signed | Badge "Signed"; next: Moved (UC-SC07-22); fields editable within the role | U29, U09 | `u29-dispatcher/s-sc07-22-removals-e-sc07-19-removal-signed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc07-22-removals-e-sc07-19-removal-signed-phone-{light,dark}.png` |
| E-SC07-19 Removal | Moved | Badge "Moved"; next: Closed (UC-SC07-22); fields editable within the role | U29, U09 | `u29-dispatcher/s-sc07-22-removals-e-sc07-19-removal-moved-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc07-22-removals-e-sc07-19-removal-moved-phone-{light,dark}.png` |
| E-SC07-19 Removal | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U29, U09 | `u29-dispatcher/s-sc07-22-removals-e-sc07-19-removal-closed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc07-22-removals-e-sc07-19-removal-closed-phone-{light,dark}.png` |
| E-SC07-19 Removal | Lost | Badge "Lost"; final: read-only, no next state; the history shows how it got here | U29, U09 | `u29-dispatcher/s-sc07-22-removals-e-sc07-19-removal-lost-{desktop,phone}-{light,dark}.png`, `u09-customer/s-sc07-22-removals-e-sc07-19-removal-lost-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop for the dispatcher. The crew's phone lists the rooms and takes photos, and the customer's page has the quote to
read and sign with a finger.

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

⬅️ [S-SC07-21 Passenger transport](s-sc07-21-passenger-transport.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-23 Last mile](s-sc07-23-last-mile.md)
