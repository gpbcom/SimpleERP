🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🔧 [SC19 Trades and home services](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC19-01 Maintenance contracts](README.md) › 🖥️ S-SC19-02 Recurring visits

# 🖥️ S-SC19-02 Recurring visits

**Status:** ✅ specified

## Personas

- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md): the visits to generate, plan and move, with their
  legal due dates.

## Purpose

Generate the visits of the active contracts before their legal due dates and place them on the rounds.

## Entry points

Trades and home services › Planned visits; the monthly generation reminder; a contract's page.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Visits: March 2027                                [Generate] [Ask for proposals] [Confirm all]   |
| Contract  Customer         Equipment    Window          Legal due   Technician  State            |
| C-0412    Martin           Gas boiler   1-15 Apr        30 Apr      Leroy       Confirmed        |
| C-0398    Dubois           Heat pump    10-25 Mar       31 Mar      -           To plan          |
| C-0377    Perrin           Gas boiler   1-10 Mar        28 Feb      -           Overdue          |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC19-01 step 2, U29 | desktop | ![FL-SC19-01 step 2, U29, light](../../images/01-maintenance-contracts/u29-dispatcher/2-recurring-visits-desktop-light.png) | ![FL-SC19-01 step 2, U29, dark](../../images/01-maintenance-contracts/u29-dispatcher/2-recurring-visits-desktop-dark.png) |
| FL-SC19-01 step 2, U29 | phone | ![FL-SC19-01 step 2, U29, light](../../images/01-maintenance-contracts/u29-dispatcher/2-recurring-visits-phone-light.png) | ![FL-SC19-01 step 2, U29, dark](../../images/01-maintenance-contracts/u29-dispatcher/2-recurring-visits-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc19-02-recurring-visits-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc19-02-recurring-visits-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc19-02-recurring-visits-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc19-02-recurring-visits-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc19-02-recurring-visits-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc19-02-recurring-visits-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc19-02-recurring-visits-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc19-02-recurring-visits-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Contract | E-SC19-02 contract | link | no | yes |
| Equipment | E-SC19-02 equipment | text | no | yes |
| Window | E-SC19-02 window | two dates | yes while To plan | yes |
| Legal due date | E-SC19-02 legal due | date | no | yes |
| Technician | E-SC19-02 technician | link | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Generate | header | dispatcher | the month's visits are created from the contracts |
| Ask for proposals | header | dispatcher | a technician and a day are proposed for each visit |
| Confirm | row | dispatcher | the visit joins the round and the customer is told |

## States

- Normal: the visits with contract, customer, equipment, window, legal due date, technician and state.
- Empty: No visit to plan this month.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a legal due
  date before the window, a technician without the qualification, with the visit named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC19-02 Planned visit](../../data/e-sc19-02-planned-visit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC19-02 Planned visit | To plan | Badge "To plan"; a new record starts here; next: Proposed or Overdue (UC-F9-33, BR-SC19-02); fields editable within the role | U29 | `u29-dispatcher/s-sc19-02-recurring-visits-e-sc19-02-planned-visit-to-plan-{desktop,phone}-{light,dark}.png` |
| E-SC19-02 Planned visit | Proposed | Badge "Proposed"; next: Confirmed (BR-SC19-02); fields editable within the role | U29 | `u29-dispatcher/s-sc19-02-recurring-visits-e-sc19-02-planned-visit-proposed-{desktop,phone}-{light,dark}.png` |
| E-SC19-02 Planned visit | Confirmed | Badge "Confirmed"; next: Done or Overdue (UC-SC19-03, BR-SC19-02); fields editable within the role | U29 | `u29-dispatcher/s-sc19-02-recurring-visits-e-sc19-02-planned-visit-confirmed-{desktop,phone}-{light,dark}.png` |
| E-SC19-02 Planned visit | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U29 | `u29-dispatcher/s-sc19-02-recurring-visits-e-sc19-02-planned-visit-done-{desktop,phone}-{light,dark}.png` |
| E-SC19-02 Planned visit | Overdue | Badge "Overdue"; next: Confirmed (UC-SC19-02); fields editable within the role | U29 | `u29-dispatcher/s-sc19-02-recurring-visits-e-sc19-02-planned-visit-overdue-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC19-01 Maintenance contracts](../../flows/fl-sc19-01-maintenance-contracts.md)

## Open questions

None.

---

⬅️ [S-SC19-01 Maintenance contract](s-sc19-01-maintenance-contract.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC19-03 Legal check-ups](s-sc19-03-legal-check-ups.md)
