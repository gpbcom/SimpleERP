🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏋️ [SC18 Sports and fitness](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC18-01 Memberships and access](README.md) › 🖥️ S-SC18-03 Door access

# 🖥️ S-SC18-03 Door access

**Status:** 🔄 waiting for the owner

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own entries and the reason of a denial.

## Purpose

Show the member the result of a door scan and let the staff see and override the entries.

## Entry points

The member's app at the door; Sports and fitness › Access events; the AI assistant.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Door: Main entrance                                                   08:14                      |
| Mia L.   Annual adult   Granted       Welcome back, Mia                                          |
| Jules P. Monthly        Denied        Dues overdue 39.00 EUR   [Open for the member]             |
| Today: 214 entries   3 denied   1 overridden                                                     |
| Reason for an override [ forgot the card                    ]                                    |
| [Open the door]  [Show the member's entries]                                                     |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC18-01 step 3, U09 | phone | ![FL-SC18-01 step 3, U09, light](../../images/01-memberships-and-access/u09-customer/3-door-access-phone-light.png) | ![FL-SC18-01 step 3, U09, dark](../../images/01-memberships-and-access/u09-customer/3-door-access-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc18-03-door-access-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc18-03-door-access-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc18-03-door-access-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc18-03-door-access-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc18-03-door-access-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc18-03-door-access-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc18-03-door-access-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc18-03-door-access-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Member | E-SC18-03 member | link | no | yes |
| Door | E-SC18-03 door | text | no | yes |
| Time | E-SC18-03 at | date and time | no | yes |
| Result | E-SC18-03 result | granted, denied, overridden | no | yes |
| Reason | E-SC18-03 reason | text | yes while Denied | no |
| Overridden by | E-SC18-03 overridden by | employee | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Open the door | header | staff | a denied entry becomes Overridden with a reason |
| Show the entries | member | owner, staff | the entries of one member for a stated need |

## States

- Normal: the entries of the day with their result and reason.
- Empty: No entry yet today.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a denial with
  its reason, shown to the member and the staff.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC18-03 Access event](../../data/e-sc18-03-access-event.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC18-03 Access event | Granted | Badge "Granted"; a new record starts here; no other state; fields editable within the role | U09 | `u09-customer/s-sc18-03-door-access-e-sc18-03-access-event-granted-phone-{light,dark}.png` |
| E-SC18-03 Access event | Denied | Badge "Denied"; a new record starts here; next: Overridden (UC-SC18-03); fields editable within the role | U09 | `u09-customer/s-sc18-03-door-access-e-sc18-03-access-event-denied-phone-{light,dark}.png` |
| E-SC18-03 Access event | Overridden | Badge "Overridden"; final: read-only, no next state; the history shows how it got here | U09 | `u09-customer/s-sc18-03-door-access-e-sc18-03-access-event-overridden-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The coach and the member use the phone, the owner and the treasurer a desktop, with the same actions in one column.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-SC18-01 Memberships and access](../../flows/fl-sc18-01-memberships-and-access.md)

## Open questions

None.

---

⬅️ [S-SC18-02 Dues collection](s-sc18-02-dues-collection.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC18-04 Membership changes](s-sc18-04-membership-changes.md)
