🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-06 Plan and deliver work](README.md) › 🖥️ S-F9-15 Planning

# 🖥️ S-F9-15 Planning

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)

## Purpose

Plan shifts.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-06 step 1, U02 | desktop | ![FL-F9-06 step 1, U02, light](../../images/06-plan-and-deliver-work/u02-manager/1-shifts-desktop-light.png) | ![FL-F9-06 step 1, U02, dark](../../images/06-plan-and-deliver-work/u02-manager/1-shifts-desktop-dark.png) |
| FL-F9-06 step 1, U02 | phone | ![FL-F9-06 step 1, U02, light](../../images/06-plan-and-deliver-work/u02-manager/1-shifts-phone-light.png) | ![FL-F9-06 step 1, U02, dark](../../images/06-plan-and-deliver-work/u02-manager/1-shifts-phone-dark.png) |
| Error E1, U02 | desktop | ![Error E1, U02, light](../../images/06-plan-and-deliver-work/u02-manager/e1-shift-conflict-desktop-light.png) | ![Error E1, U02, dark](../../images/06-plan-and-deliver-work/u02-manager/e1-shift-conflict-desktop-dark.png) |
| Error E1, U02 | phone | ![Error E1, U02, light](../../images/06-plan-and-deliver-work/u02-manager/e1-shift-conflict-phone-light.png) | ![Error E1, U02, dark](../../images/06-plan-and-deliver-work/u02-manager/e1-shift-conflict-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-15-planning-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-15-planning-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-15-planning-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-15-planning-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-15-planning-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-15-planning-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-15-planning-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-15-planning-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Plan shifts, as the wireframe shows.
- Empty: No shift planned yet, with Plan shifts.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Works offline ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)): today's schedule, time and
  intervention records stay on the phone and their changes wait in a queue, sent when the network is back; everything
  else waits for the network.

Shown entities (VD-15): [E-F9-16 Shift](../../data/e-f09-16-shift.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-16 Shift | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F9-15); fields editable within the role | U02, U14 | `u02-manager/s-f09-15-planning-e-f09-16-shift-draft-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-15-planning-e-f09-16-shift-draft-phone-{light,dark}.png` |
| E-F9-16 Shift | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U02, U14 | `u02-manager/s-f09-15-planning-e-f09-16-shift-published-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-15-planning-e-f09-16-shift-published-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F9-06 Plan and deliver work](../../flows/fl-f09-06-plan-and-deliver-work.md)

## Open questions

None.

---

⬅️ [S-F9-14 Visitors](../05-workplace-services/s-f09-14-visitors.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-16 Timesheets](../03-time/s-f09-16-timesheets.md)
