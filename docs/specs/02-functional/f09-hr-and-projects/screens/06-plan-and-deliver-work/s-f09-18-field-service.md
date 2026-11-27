🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-06 Plan and deliver work](README.md) › 🖥️ S-F9-18 Field service

# 🖥️ S-F9-18 Field service

**Status:** ✅ specified

## Personas

- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Run field service.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-06 step 3, U14 | phone | ![FL-F9-06 step 3, U14, light](../../images/06-plan-and-deliver-work/u14-field-worker/3-field-service-phone-light.png) | ![FL-F9-06 step 3, U14, dark](../../images/06-plan-and-deliver-work/u14-field-worker/3-field-service-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f09-18-field-service-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f09-18-field-service-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f09-18-field-service-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f09-18-field-service-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f09-18-field-service-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f09-18-field-service-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-18-field-service-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-18-field-service-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Run field service, as the wireframe shows.
- Empty: No intervention today yet, with Nothing planned.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Works offline ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)): today's schedule, time and
  intervention records stay on the phone and their changes wait in a queue, sent when the network is back; everything
  else waits for the network.

Shown entities (VD-15): [E-F9-16 Shift](../../data/e-f09-16-shift.md),
[E-F9-18 Project and task](../../data/e-f09-18-project-and-task.md),
[E-F9-37 Field worksheet](../../data/e-f09-37-field-worksheet.md),
[E-F16-12 Work request](../../../f16-customer-support-agents/data/e-f16-12-work-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-16 Shift | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F9-15); fields editable within the role | U02, U14 | `u02-manager/s-f09-18-field-service-e-f09-16-shift-draft-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-18-field-service-e-f09-16-shift-draft-phone-{light,dark}.png` |
| E-F9-16 Shift | Published | Badge "Published"; final: read-only, no next state; the history shows how it got here | U02, U14 | `u02-manager/s-f09-18-field-service-e-f09-16-shift-published-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-18-field-service-e-f09-16-shift-published-phone-{light,dark}.png` |
| E-F9-18 Project and task | New | Badge "New"; a new record starts here; next: Planned (UC-F9-18); fields editable within the role | U02, U14 | `u02-manager/s-f09-18-field-service-e-f09-18-project-and-task-new-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-18-field-service-e-f09-18-project-and-task-new-phone-{light,dark}.png` |
| E-F9-18 Project and task | Planned | Badge "Planned"; next: Active (UC-F9-31); fields editable within the role | U02, U14 | `u02-manager/s-f09-18-field-service-e-f09-18-project-and-task-planned-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-18-field-service-e-f09-18-project-and-task-planned-phone-{light,dark}.png` |
| E-F9-18 Project and task | Active | Badge "Active"; next: Delivered (UC-F9-17); fields editable within the role | U02, U14 | `u02-manager/s-f09-18-field-service-e-f09-18-project-and-task-active-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-18-field-service-e-f09-18-project-and-task-active-phone-{light,dark}.png` |
| E-F9-18 Project and task | Delivered | Badge "Delivered"; next: Done (UC-F9-17); fields editable within the role | U02, U14 | `u02-manager/s-f09-18-field-service-e-f09-18-project-and-task-delivered-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-18-field-service-e-f09-18-project-and-task-delivered-phone-{light,dark}.png` |
| E-F9-18 Project and task | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U02, U14 | `u02-manager/s-f09-18-field-service-e-f09-18-project-and-task-done-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-18-field-service-e-f09-18-project-and-task-done-phone-{light,dark}.png` |
| E-F9-37 Field worksheet | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U14 | `u02-manager/s-f09-18-field-service-e-f09-37-field-worksheet-active-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-18-field-service-e-f09-37-field-worksheet-active-phone-{light,dark}.png` |
| E-F16-12 Work request | Blocked | Badge "Blocked"; next: Ready (UC-F9-35); fields editable within the role | U14 | `u14-field-worker/s-f09-18-field-service-e-f16-12-work-request-blocked-phone-{light,dark}.png` |
| E-F16-12 Work request | Scheduled | Badge "Scheduled"; next: In progress, Ready or Cancelled (BR-F9-06, UC-F9-35); fields editable within the role | U14 | `u14-field-worker/s-f09-18-field-service-e-f16-12-work-request-scheduled-phone-{light,dark}.png` |
| E-F16-12 Work request | In progress | Badge "In progress"; next: Done (BR-F9-06); fields editable within the role | U14 | `u14-field-worker/s-f09-18-field-service-e-f16-12-work-request-in-progress-phone-{light,dark}.png` |
| E-F16-12 Work request | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U14 | `u14-field-worker/s-f09-18-field-service-e-f16-12-work-request-done-phone-{light,dark}.png` |
| E-F16-12 Work request | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U14 | `u14-field-worker/s-f09-18-field-service-e-f16-12-work-request-cancelled-phone-{light,dark}.png` |

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
- [FL-F9-12 Schedule customer requests](../../flows/fl-f09-12-schedule-customer-requests.md)

## Open questions

None.

---

⬅️ [S-F9-17 Projects](s-f09-17-projects.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-19 Contract editor](../01-people/s-f09-19-contract-editor.md)
