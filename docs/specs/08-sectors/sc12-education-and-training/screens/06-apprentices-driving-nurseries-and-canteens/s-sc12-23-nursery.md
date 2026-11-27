🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-06 Apprentices, driving schools, nurseries, canteens](README.md) ›
🖥️ S-SC12-23 Nursery

# 🖥️ S-SC12-23 Nursery

**Status:** ✅ specified

## Personas

- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md): the places, contracts, presence
  and reports.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their child's hours and invoices.

## Purpose

Book the nursery places by hour, compute the hourly rate from the fund's scale and report the hours done.

## Entry points

Education and training › Childcare places; the day's presence list; the parent's phone.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Place CP-2026-044: Lina, 3 days a week                                  Active   [Record presenc |
| Family Mrs Idrissi   Income reference 2,400.00 a month   Family size 2 children                  |
| Rate 0.0615 % -> 1.48 an hour (floor 0.50, ceiling 4.20)   Scale of 2026-01                      |
| Contract Mon, Tue, Thu 8:30 to 17:30   27 hours a week                                           |
| November   Contracted 118   Done 112   Deducted 6   Invoice 165.76                               |
| Report to the fund: prepared      [Send the report]                                              |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-06 step 3, U38 | desktop | ![FL-SC12-06 step 3, U38, light](../../images/06-apprentices-driving-nurseries-and-canteens/u38-training-coordinator/3-nursery-desktop-light.png) | ![FL-SC12-06 step 3, U38, dark](../../images/06-apprentices-driving-nurseries-and-canteens/u38-training-coordinator/3-nursery-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-23-nursery-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-23-nursery-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-23-nursery-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-23-nursery-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-23-nursery-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-23-nursery-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc12-23-nursery-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc12-23-nursery-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Child and family | E-SC12-22 child, family | text and link | yes while Waiting | yes |
| Days and hours | E-SC12-22 contract hours | days and times | yes while Waiting | yes |
| Income reference | E-SC12-22 income reference | amount a month | yes | yes |
| Hourly rate | E-SC12-22 hourly rate | amount | no | no |
| Hours done | E-SC12-22 hours done | number | no | no |
| Report state | E-SC12-22 report | choice | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Confirm the place | place | director | the place becomes Active with its rate |
| Record presence | day list | staff | arrival and departure times of the child |
| Send the report | header | director | the hours of the month go to the fund |
| End | place | director | the place becomes Ended |

## States

- Normal: the place, the family's rate with its scale, the hours contracted and done, and the report.
- Empty: No place yet, with New place.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing scale
  or income reference, with what to enter.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC12-22 Childcare place](../../data/e-sc12-22-childcare-place.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-22 Childcare place | Waiting | Badge "Waiting"; a new record starts here; next: Active or Cancelled (UC-SC12-23); fields editable within the role | U38, U09 | `u38-training-coordinator/s-sc12-23-nursery-e-sc12-22-childcare-place-waiting-desktop-{light,dark}.png`, `u09-customer/s-sc12-23-nursery-e-sc12-22-childcare-place-waiting-phone-{light,dark}.png` |
| E-SC12-22 Childcare place | Active | Badge "Active"; next: Ended (UC-SC12-23); fields editable within the role | U38, U09 | `u38-training-coordinator/s-sc12-23-nursery-e-sc12-22-childcare-place-active-desktop-{light,dark}.png`, `u09-customer/s-sc12-23-nursery-e-sc12-22-childcare-place-active-phone-{light,dark}.png` |
| E-SC12-22 Childcare place | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U38, U09 | `u38-training-coordinator/s-sc12-23-nursery-e-sc12-22-childcare-place-ended-desktop-{light,dark}.png`, `u09-customer/s-sc12-23-nursery-e-sc12-22-childcare-place-ended-phone-{light,dark}.png` |
| E-SC12-22 Childcare place | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U38, U09 | `u38-training-coordinator/s-sc12-23-nursery-e-sc12-22-childcare-place-cancelled-desktop-{light,dark}.png`, `u09-customer/s-sc12-23-nursery-e-sc12-22-childcare-place-cancelled-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coordinator works on a desktop; the apprentice, the instructor and the parents use the phone, with the same actions
in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC12-06](../../flows/fl-sc12-06-apprentices-driving-nurseries-and-canteens.md)

## Open questions

None.

---

⬅️ [S-SC12-22 Driving school](s-sc12-22-driving-school.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-24 Canteen and activities](s-sc12-24-canteen.md)
