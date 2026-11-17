🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-06 Cashless, cinemas, tours and photographers](README.md) ›
🖥️ S-SC16-23 Tour

# 🖥️ S-SC16-23 Tour

**Status:** 🔄 waiting for the owner

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md): the dates, the contracts, the declarations
  and the settlements, at the desk and on the road.

## Purpose

Plan the dates of a tour with their contract terms, declare the artists and settle each show on its figures.

## Entry points

Events and culture › Tour; a show's page; the tour manager's phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Tour: Lumen 2026-27                        Balance +21,400.00 EUR  [Add date] [Settle] [Declare] |
| Date        Venue            Terms                      Tickets  Net        Settlement  State    |
| 2026-11-12  Lyon, Salle 3    6,000 + 70 % over 2,000   640      8,000.00   6,000.00    Settled   |
| 2026-11-14  Dijon, Zenith    5,000 flat                 -        -          -          Confirmed |
| 2026-11-19  Geneva, Arena    4,000 + 60 %               -        -          -           Option   |
| Dates: 24   Played 9   Settled 8                          Foreign artists: withholding 3         |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-06 step 3, U43 | desktop | ![FL-SC16-06 step 3, U43, light](../../images/06-cashless-cinemas-tours-and-photos/u43-event-producer/3-touring-desktop-light.png) | ![FL-SC16-06 step 3, U43, dark](../../images/06-cashless-cinemas-tours-and-photos/u43-event-producer/3-touring-desktop-dark.png) |
| FL-SC16-06 step 3, U43 | phone | ![FL-SC16-06 step 3, U43, light](../../images/06-cashless-cinemas-tours-and-photos/u43-event-producer/3-touring-phone-light.png) | ![FL-SC16-06 step 3, U43, dark](../../images/06-cashless-cinemas-tours-and-photos/u43-event-producer/3-touring-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-23-touring-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-23-touring-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-23-touring-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-23-touring-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-23-touring-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-23-touring-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-23-touring-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-23-touring-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Date and venue | E-SC16-21 date, venue | date and link | yes while Option | yes |
| Terms | E-SC16-21 terms | guarantee, share, costs | yes while Option or Confirmed | yes |
| Tickets sold | E-SC16-21 tickets | number | yes while Played | yes to settle |
| Net receipts | E-SC16-21 net receipts | amount in EUR | yes while Played | yes to settle |
| Settlement | E-SC16-21 settlement | amount in EUR | no | no |
| Declared | E-SC16-21 declared | yes or no | no | yes to settle |
| Withholding | E-SC16-21 withholding | amount in EUR | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add date | header | event producer | a date in state Option |
| Confirm | date | event producer | the contract is signed and the date is Confirmed |
| Declare | date | event producer | the performers are declared for the date |
| Settle | date | event producer | the settlement is computed and the date is Settled |

## States

- Normal: the dates with venue, terms, tickets, net receipts, settlement and state.
- Empty: No date yet, with Add date.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a contract
  without terms, a missing figure, a performer not declared, with the date.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC16-21 Tour date](../../data/e-sc16-21-tour-date.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-21 Tour date | Option | Badge "Option"; a new record starts here; next: Confirmed or Cancelled (UC-SC16-23); fields editable within the role | U43 | `u43-event-producer/s-sc16-23-touring-e-sc16-21-tour-date-option-{desktop,phone}-{light,dark}.png` |
| E-SC16-21 Tour date | Confirmed | Badge "Confirmed"; next: Played or Cancelled (UC-SC16-23); fields editable within the role | U43 | `u43-event-producer/s-sc16-23-touring-e-sc16-21-tour-date-confirmed-{desktop,phone}-{light,dark}.png` |
| E-SC16-21 Tour date | Played | Badge "Played"; next: Settled (BR-SC16-18); fields editable within the role | U43 | `u43-event-producer/s-sc16-23-touring-e-sc16-21-tour-date-played-{desktop,phone}-{light,dark}.png` |
| E-SC16-21 Tour date | Settled | Badge "Settled"; final: read-only, no next state; the history shows how it got here | U43 | `u43-event-producer/s-sc16-23-touring-e-sc16-21-tour-date-settled-{desktop,phone}-{light,dark}.png` |
| E-SC16-21 Tour date | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U43 | `u43-event-producer/s-sc16-23-touring-e-sc16-21-tour-date-cancelled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The tour manager's phone enters the tickets sold and the receipts after the show.

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

⬅️ [S-SC16-22 Cinema](s-sc16-22-cinema.md) · ⬆️ [Up](README.md) · ➡️ [S-SC16-24 Photography](s-sc16-24-photography.md)
