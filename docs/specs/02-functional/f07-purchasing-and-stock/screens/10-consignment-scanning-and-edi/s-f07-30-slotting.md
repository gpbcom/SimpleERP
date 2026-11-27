🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F7-30 Slotting

# 🖥️ S-F7-30 Slotting

**Status:** 🔄 waiting for the owner

## Personas

- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md): the proposals and the decisions.
- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md): the move tasks, on a phone.

## Purpose

See the proposed moves with their reason and gain, decide, and follow the moves.

## Entry points

Purchasing and stock › Slotting; the operator's task list on the phone.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Slotting analysis: last 3 months         24 proposals    Expected gain 18 percent distance  |
|---------------------------------------------------------------------------------------------|
| ITEM            FROM     TO       REASON                    GAIN    STATE                   |
| Oak plank 30mm  C-14-4   A-02-1   300 picks a month         9 m     Proposed                |
| Brass hinge     C-02-1   A-02-2   picked with oak plank     4 m     Approved               |
| [Approve] [Reject] [Change destination] [Run again]                                         |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-10 step 6, U04 | desktop | ![FL-F7-10 step 6, U04, light](../../images/10-consignment-scanning-and-edi/u04-purchasing/6-slotting-desktop-light.png) | ![FL-F7-10 step 6, U04, dark](../../images/10-consignment-scanning-and-edi/u04-purchasing/6-slotting-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-30-slotting-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-30-slotting-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-30-slotting-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-30-slotting-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-30-slotting-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-30-slotting-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-30-slotting-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-30-slotting-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Item | E-F7-27 item | name | no | yes |
| From and to | E-F7-27 locations | two codes | to: yes | yes |
| Reason | E-F7-27 reason | text | no | yes |
| Gain | E-F7-27 expected gain | metres per pick | no | yes |
| State | E-F7-27 state | badge | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Approve | row, bulk bar | purchasing, warehouse manager | the move task is created |
| Reject | row | purchasing, warehouse manager | the proposal is dropped for 3 months |
| Change destination | row | purchasing, warehouse manager | another location, checked for capacity |
| Run again | header | purchasing | a new analysis with the current parameters |

## States

- Normal: the proposals with their reason, gain and state, and the parameters of the run.
- Empty: No proposal, with Run the analysis.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); an analysis
  that could not run shows the missing data (item sizes, pick history).
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-27 Slotting proposal](../../data/e-f07-27-slotting-proposal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-27 Slotting proposal | Proposed | Badge "Proposed"; a new record starts here; next: Approved or Rejected (UC-F7-30); fields editable within the role | U04, U15 | `u04-purchasing/s-f07-30-slotting-e-f07-27-slotting-proposal-proposed-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-30-slotting-e-f07-27-slotting-proposal-proposed-{phone,tablet}-{light,dark}.png` |
| E-F7-27 Slotting proposal | Approved | Badge "Approved"; next: Postponed or Done (BR-F7-24, UC-F7-30); fields editable within the role | U04, U15 | `u04-purchasing/s-f07-30-slotting-e-f07-27-slotting-proposal-approved-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-30-slotting-e-f07-27-slotting-proposal-approved-{phone,tablet}-{light,dark}.png` |
| E-F7-27 Slotting proposal | Rejected | Badge "Rejected"; final: read-only, no next state; the history shows how it got here | U04, U15 | `u04-purchasing/s-f07-30-slotting-e-f07-27-slotting-proposal-rejected-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-30-slotting-e-f07-27-slotting-proposal-rejected-{phone,tablet}-{light,dark}.png` |
| E-F7-27 Slotting proposal | Postponed | Badge "Postponed"; next: Approved (BR-F7-24); fields editable within the role | U04, U15 | `u04-purchasing/s-f07-30-slotting-e-f07-27-slotting-proposal-postponed-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-30-slotting-e-f07-27-slotting-proposal-postponed-{phone,tablet}-{light,dark}.png` |
| E-F7-27 Slotting proposal | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U04, U15 | `u04-purchasing/s-f07-30-slotting-e-f07-27-slotting-proposal-done-desktop-{light,dark}.png`, `u15-warehouse-operator/s-f07-30-slotting-e-f07-27-slotting-proposal-done-{phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The operator sees the move tasks on a phone, after the picks, each with a scan check
([UC-F7-26](../../use-cases/10-consignment-scanning-and-edi/uc-f07-26-scan-in-the-warehouse-app.md)). The analysis and
the decisions are desktop only.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F7-10](../../flows/fl-f07-10-consignment-scanning-and-edi.md)

## Open questions

None.

---

⬅️ [S-F7-29 Supplier EDI](s-f07-29-supplier-edi.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-L01 Supplier records](../00-lists/s-f07-l01-supplier-records.md)
