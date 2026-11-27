🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F8-38 Business travel

# 🖥️ S-F8-38 Business travel

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md): their own trips, from their phone.
- [U02 Manager](../../../../01-users/personas/u02-manager.md): the trips of their team waiting for approval.

## Purpose

Book a trip within the policy, ask for an exception and approve a team's trips.

## Entry points

The home screen on a phone › Travel; Accounting › Trips; the AI assistant.

## Wireframe

```text
+---------------------------------------------+
| New trip                       Draft        |
|---------------------------------------------|
| Purpose  Client visit, Lille                |
| Tue 2027-01-12  Lyon > Lille   train 2nd    |
|                 policy: within       62 EUR |
| Hotel  Lille 1 night   142 EUR              |
|                 policy: above cap 120 EUR   |
| Total  204 EUR      Needs approval          |
| [Add a leg] [Ask for an exception] [Send]   |
+---------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-12 step 4, U01 | phone | ![FL-F8-12 step 4, U01, light](../../images/12-audit-leases-and-special-books/u01-employee/4-business-travel-phone-light.png) | ![FL-F8-12 step 4, U01, dark](../../images/12-audit-leases-and-special-books/u01-employee/4-business-travel-phone-dark.png) |
| FL-F8-12 step 4, U01 | desktop | ![FL-F8-12 step 4, U01, light](../../images/12-audit-leases-and-special-books/u01-employee/4-business-travel-desktop-light.png) | ![FL-F8-12 step 4, U01, dark](../../images/12-audit-leases-and-special-books/u01-employee/4-business-travel-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-38-business-travel-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-38-business-travel-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-38-business-travel-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-38-business-travel-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-38-business-travel-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-38-business-travel-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f08-38-business-travel-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f08-38-business-travel-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Purpose and dates | E-F8-43 | text and dates | yes while Draft | yes |
| Legs | E-F8-43 legs | list of transport, hotel, car | yes while Draft | yes |
| Policy check per leg | E-F8-43 | badge and reason | no | yes |
| Total cost | E-F8-43 | amount with currency | no | yes |
| Approval | E-F8-43 | name and reason | manager | when outside the policy |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send | header | employee | a trip within the policy is booked, otherwise sent to the manager |
| Ask for an exception | leg | employee | a reason is added for the manager |
| Approve or reject | manager's list | manager | the trip is booked or returned with the reason |
| Cancel | trip | employee, manager | the bookings are cancelled as the provider allows |

## States

- Normal: the trip's legs with their policy checks, the total and the approval state.
- Empty: No trip yet, with New trip.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a provider that
  cannot book shows the leg and the provider's reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-43 Trip](../../data/e-f08-43-trip.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-43 Trip | Draft | Badge "Draft"; a new record starts here; next: Booked or Awaiting approval (UC-F8-39, BR-F8-31); fields editable within the role | U01, U02 | `u01-employee/s-f08-38-business-travel-e-f08-43-trip-draft-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f08-38-business-travel-e-f08-43-trip-draft-{desktop,phone}-{light,dark}.png` |
| E-F8-43 Trip | Booked | Badge "Booked"; next: Completed or Cancelled (UC-F8-39); fields editable within the role | U01, U02 | `u01-employee/s-f08-38-business-travel-e-f08-43-trip-booked-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f08-38-business-travel-e-f08-43-trip-booked-{desktop,phone}-{light,dark}.png` |
| E-F8-43 Trip | Awaiting approval | Badge "Awaiting approval"; next: Approved or Rejected (BR-F8-31); fields editable within the role | U01, U02 | `u01-employee/s-f08-38-business-travel-e-f08-43-trip-awaiting-approval-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f08-38-business-travel-e-f08-43-trip-awaiting-approval-{desktop,phone}-{light,dark}.png` |
| E-F8-43 Trip | Approved | Badge "Approved"; next: Booked or Cancelled (UC-F8-39); fields editable within the role | U01, U02 | `u01-employee/s-f08-38-business-travel-e-f08-43-trip-approved-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f08-38-business-travel-e-f08-43-trip-approved-{desktop,phone}-{light,dark}.png` |
| E-F8-43 Trip | Rejected | Badge "Rejected"; next: Draft (UC-F8-39); fields editable within the role | U01, U02 | `u01-employee/s-f08-38-business-travel-e-f08-43-trip-rejected-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f08-38-business-travel-e-f08-43-trip-rejected-{desktop,phone}-{light,dark}.png` |
| E-F8-43 Trip | Completed | Badge "Completed"; final: read-only, no next state; the history shows how it got here | U01, U02 | `u01-employee/s-f08-38-business-travel-e-f08-43-trip-completed-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f08-38-business-travel-e-f08-43-trip-completed-{desktop,phone}-{light,dark}.png` |
| E-F8-43 Trip | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U01, U02 | `u01-employee/s-f08-38-business-travel-e-f08-43-trip-cancelled-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f08-38-business-travel-e-f08-43-trip-cancelled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Built for a phone first: one leg per card with its policy badge, the total pinned at the bottom. The manager's approval
list also works on a phone; accounting's table is desktop.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F8-12](../../flows/fl-f08-12-audit-leases-and-special-books.md)

## Open questions

None.

---

⬅️ [S-F8-37 Peppol](s-f08-37-peppol.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-39 Cash-basis books](s-f08-39-cash-basis-books.md)
