🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-05 Council, civil registry, permits and assets](README.md) ›
🖥️ S-SC20-17 Council meetings

# 🖥️ S-SC20-17 Council meetings

**Status:** ✅ specified

## Personas

- [U55 Elected official](../../../../01-users/personas/u55-elected-official.md): the meeting, its agenda, quorum, votes
  and transmission.
- [U54 Public finance officer](../../../../01-users/personas/u54-public-finance-officer.md): the budget and finance
  items of the meeting.

## Purpose

Convene and hold the council, record each vote and transmit the deliberations.

## Entry points

Public bodies › Council meetings; the calendar of the body.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Council: 28 March 2027, 18:30, Town hall                    State: Convened   [Convene] [Record] |
| Members: 23 in office   Present: 16   Proxies: 2   Quorum: met (12)                              |
| Item  Subject                         Votes for/against/abst.   Result    Transmitted            |
| 1     Budget 2027                     16 / 2 / 0                Adopted   -                      |
| 2     Hall rates                      18 / 0 / 0                Adopted   -                      |
| Minutes: draft                                           [Transmit adopted] [Post minutes]       |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-05 step 1, U55 | desktop | ![FL-SC20-05 step 1, U55, light](../../images/05-council-registry-permits-and-assets/u55-elected-official/1-council-meetings-desktop-light.png) | ![FL-SC20-05 step 1, U55, dark](../../images/05-council-registry-permits-and-assets/u55-elected-official/1-council-meetings-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-17-council-meetings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-17-council-meetings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-17-council-meetings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-17-council-meetings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-17-council-meetings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-17-council-meetings-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-17-council-meetings-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-17-council-meetings-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Meeting | E-SC20-12 meeting | date, time and place | yes while Proposed | yes |
| Items | E-SC20-12 items | list of subject, note and documents | yes while Proposed | yes |
| Attendance | E-SC20-12 attendance | list of member, present, proxy | yes | yes |
| Votes | E-SC20-12 votes | for, against, abstentions | yes | yes |
| Transmitted on | E-SC20-12 transmitted | date | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Convene | header | elected official | the convocation is sent within the delay |
| Record vote | row | elected official | the result of the item is saved |
| Transmit adopted | header | elected official | the adopted deliberations go to the prefecture |

## States

- Normal: the meeting with its items, attendance, quorum, votes, result and transmission.
- Empty: No meeting yet, with Convene a meeting.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a convocation
  too late, a quorum not met, a transmission failed, with the item named.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC20-12 Deliberation](../../data/e-sc20-12-deliberation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC20-12 Deliberation | Proposed | Badge "Proposed"; a new record starts here; next: On agenda (BR-SC20-17); fields editable within the role | U55, U54 | `u55-elected-official/s-sc20-17-council-meetings-e-sc20-12-deliberation-proposed-desktop-{light,dark}.png`, `u54-public-finance-officer/s-sc20-17-council-meetings-e-sc20-12-deliberation-proposed-desktop-{light,dark}.png` |
| E-SC20-12 Deliberation | On agenda | Badge "On agenda"; next: Adopted or Rejected (UC-SC20-17); fields editable within the role | U55, U54 | `u55-elected-official/s-sc20-17-council-meetings-e-sc20-12-deliberation-on-agenda-desktop-{light,dark}.png`, `u54-public-finance-officer/s-sc20-17-council-meetings-e-sc20-12-deliberation-on-agenda-desktop-{light,dark}.png` |
| E-SC20-12 Deliberation | Adopted | Badge "Adopted"; next: Transmitted (BR-SC20-17); fields editable within the role | U55, U54 | `u55-elected-official/s-sc20-17-council-meetings-e-sc20-12-deliberation-adopted-desktop-{light,dark}.png`, `u54-public-finance-officer/s-sc20-17-council-meetings-e-sc20-12-deliberation-adopted-desktop-{light,dark}.png` |
| E-SC20-12 Deliberation | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U55, U54 | `u55-elected-official/s-sc20-17-council-meetings-e-sc20-12-deliberation-rejected-desktop-{light,dark}.png`, `u54-public-finance-officer/s-sc20-17-council-meetings-e-sc20-12-deliberation-rejected-desktop-{light,dark}.png` |
| E-SC20-12 Deliberation | Transmitted | Badge "Transmitted"; final: read-only, no next state; the history shows how it got here | U55, U54 | `u55-elected-official/s-sc20-17-council-meetings-e-sc20-12-deliberation-transmitted-desktop-{light,dark}.png`, `u54-public-finance-officer/s-sc20-17-council-meetings-e-sc20-12-deliberation-transmitted-desktop-{light,dark}.png` |

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

- [FL-SC20-05](../../flows/fl-sc20-05-council-registry-permits-and-assets.md)

## Open questions

None.

---

⬅️ [S-SC20-16 Budget assistant](../04-public-hr-and-pay/s-sc20-16-budget-assistant.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-18 Civil registry](s-sc20-18-civil-registry.md)
