🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-08 Engineers, screen sharing, reports and languages](README.md) › 🖥️ S-F20-29 Engineer booking

# 🖥️ S-F20-29 Engineer booking

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the calls of their company and the slots they
  can book.
- [U48 Hosting engineer](../../../../01-users/personas/u48-hosting-engineer.md): the calls of the shift.

## Purpose

Book a call with a hosting engineer inside the plan's hours, and follow its state.

## Entry points

Hosted support assistant › Engineer calls; the AI assistant's offer of a call; the request's page.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Book an engineer     Plan: Business   Calls left this month: 1 of 2   Hours: Mon-Fri 8:00-19:00  |
|---------------------------------------------------------------------------------------------|
| Request [4127 Invoices do not post v]   Urgency [Urgent v]   Language [Francais v]  Way [Video v] |
| FIRST FREE SLOTS (within 1 hour): Today 14:00   14:30   15:00                                 |
| YOUR CALLS                                                                                   |
| 2026-11-14 14:30  Requested  Request 4127   Francais   Engineer: to be confirmed     [Move]  |
| [Book]                                                                                       |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-08 step 1, U07 | desktop | ![FL-F20-08 step 1, U07, light](../../images/08-engineers-sharing-and-reports/u07-administrator/1-engineer-booking-desktop-light.png) | ![FL-F20-08 step 1, U07, dark](../../images/08-engineers-sharing-and-reports/u07-administrator/1-engineer-booking-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-29-engineer-booking-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-29-engineer-booking-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-29-engineer-booking-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-29-engineer-booking-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-29-engineer-booking-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-29-engineer-booking-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f20-29-engineer-booking-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f20-29-engineer-booking-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Request or topic | E-F20-19 request, topic | request and text | yes while Requested | yes |
| Urgency | E-F20-19 urgency | urgent, normal | yes while Requested | yes |
| Language | E-F20-19 language | a supported language | yes while Requested | yes |
| Slot and way | E-F20-19 slot, way | date, time, video or phone | yes while Requested or Confirmed | yes |
| Engineer | E-F20-19 engineer | name | by the engineer team | no |
| Summary | E-F20-19 summary | text | by the engineer | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Book | header | administrator | saves the call as Requested and alerts the engineer |
| Move or cancel | call | administrator | changes the slot, with the notice the plan asks for |
| Confirm | call | hosting engineer | the call becomes Confirmed and the invitation is sent |
| Record the summary | call | hosting engineer | the summary goes on the request |

## States

- Normal: the plan's hours, the calls left, the free slots and the company's calls.
- Empty: No call yet, with Book.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  booking says whether the calls are used up or no slot is free in time.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F20-19 Engineer call](../../data/e-f20-19-engineer-call.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-19 Engineer call | Requested | Badge "Requested"; a new record starts here; next: Confirmed or Cancelled (BR-F20-20, UC-F20-29); fields editable within the role | U07, U48 | `u07-administrator/s-f20-29-engineer-booking-e-f20-19-engineer-call-requested-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f20-29-engineer-booking-e-f20-19-engineer-call-requested-{desktop,phone}-{light,dark}.png` |
| E-F20-19 Engineer call | Confirmed | Badge "Confirmed"; next: Held, Missed or Cancelled (UC-F20-29); fields editable within the role | U07, U48 | `u07-administrator/s-f20-29-engineer-booking-e-f20-19-engineer-call-confirmed-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f20-29-engineer-booking-e-f20-19-engineer-call-confirmed-{desktop,phone}-{light,dark}.png` |
| E-F20-19 Engineer call | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U07, U48 | `u07-administrator/s-f20-29-engineer-booking-e-f20-19-engineer-call-cancelled-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f20-29-engineer-booking-e-f20-19-engineer-call-cancelled-{desktop,phone}-{light,dark}.png` |
| E-F20-19 Engineer call | Held | Badge "Held"; final: read-only, no next state; the history shows how it got here | U07, U48 | `u07-administrator/s-f20-29-engineer-booking-e-f20-19-engineer-call-held-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f20-29-engineer-booking-e-f20-19-engineer-call-held-{desktop,phone}-{light,dark}.png` |
| E-F20-19 Engineer call | Missed | Badge "Missed"; final: read-only, no next state; the history shows how it got here | U07, U48 | `u07-administrator/s-f20-29-engineer-booking-e-f20-19-engineer-call-missed-desktop-{light,dark}.png`, `u48-hosting-engineer/s-f20-29-engineer-booking-e-f20-19-engineer-call-missed-{desktop,phone}-{light,dark}.png` |

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

- [FL-F20-08](../../flows/fl-f20-08-engineers-sharing-and-reports.md)

## Open questions

None.

---

⬅️ [S-F20-28 Incident handling](../03-incidents/s-f20-28-incident-handling.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-30 Consented access](s-f20-30-consented-access.md)
