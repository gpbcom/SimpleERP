🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-06 Plan and deliver work](README.md) › 🖥️ S-F9-17 Projects

# 🖥️ S-F9-17 Projects

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U06 Human resources](../../../../01-users/personas/u06-hr.md): only the tasks assigned to them, such as a prepared
  LinkedIn message to send
  ([D570](../../../../06-decisions/f09-hr-and-projects/d570-linkedin-sending-prepared-by-default.md))

## Purpose

Manage projects and tasks.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34); for HR, the notification of a prepared LinkedIn message,
which opens their task list on its task (D570).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-06 step 2, U02 | desktop | ![FL-F9-06 step 2, U02, light](../../images/06-plan-and-deliver-work/u02-manager/2-projects-desktop-light.png) | ![FL-F9-06 step 2, U02, dark](../../images/06-plan-and-deliver-work/u02-manager/2-projects-desktop-dark.png) |
| FL-F9-06 step 2, U02 | phone | ![FL-F9-06 step 2, U02, light](../../images/06-plan-and-deliver-work/u02-manager/2-projects-phone-light.png) | ![FL-F9-06 step 2, U02, dark](../../images/06-plan-and-deliver-work/u02-manager/2-projects-phone-dark.png) |
| Prepared LinkedIn messages, U06 | desktop | ![Prepared LinkedIn messages, U06, light](../../images/06-plan-and-deliver-work/u06-hr/2-projects-desktop-light.png) | ![Prepared LinkedIn messages, U06, dark](../../images/06-plan-and-deliver-work/u06-hr/2-projects-desktop-dark.png) |
| Prepared LinkedIn messages, U06 | phone | ![Prepared LinkedIn messages, U06, light](../../images/06-plan-and-deliver-work/u06-hr/2-projects-phone-light.png) | ![Prepared LinkedIn messages, U06, dark](../../images/06-plan-and-deliver-work/u06-hr/2-projects-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-17-projects-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-17-projects-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-17-projects-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-17-projects-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-17-projects-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-17-projects-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-17-projects-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-17-projects-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow, and for a task an outreach sequence created:

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Send | task carrying a prepared outreach message | the HR user the task is assigned to | the message goes out through Unipile within the account's limits (BR-F9-41), and the task closes as Done, outcome sent (D570) |
| Open the thread | task carrying a prepared outreach message | the HR user the task is assigned to | [S-F9-39 Prospect conversations](../02-recruit/s-f09-39-prospect-conversations.md) on that message |

## States

- Normal: Manage projects and tasks, as the wireframe shows. A task carrying a prepared outreach message shows the
  prospect, the kind of message, its text, the date it expires and Send; once sent, expired or cancelled it closes with
  its outcome ([E-F9-18](../../data/e-f09-18-project-and-task.md)).
- Empty: No project yet, with New project.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F9-18 Project and task](../../data/e-f09-18-project-and-task.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-18 Project and task | New | Badge "New"; a new record starts here; next: Planned (UC-F9-18); fields editable within the role | U02, U03, U09 | `u02-manager/s-f09-17-projects-e-f09-18-project-and-task-new-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f09-17-projects-e-f09-18-project-and-task-new-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f09-17-projects-e-f09-18-project-and-task-new-phone-{light,dark}.png` |
| E-F9-18 Project and task | Planned | Badge "Planned"; next: Active (UC-F9-31); fields editable within the role | U02, U03, U09 | `u02-manager/s-f09-17-projects-e-f09-18-project-and-task-planned-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f09-17-projects-e-f09-18-project-and-task-planned-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f09-17-projects-e-f09-18-project-and-task-planned-phone-{light,dark}.png` |
| E-F9-18 Project and task | Active | Badge "Active"; next: Delivered (UC-F9-17); fields editable within the role | U02, U03, U09 | `u02-manager/s-f09-17-projects-e-f09-18-project-and-task-active-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f09-17-projects-e-f09-18-project-and-task-active-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f09-17-projects-e-f09-18-project-and-task-active-phone-{light,dark}.png` |
| E-F9-18 Project and task | Delivered | Badge "Delivered"; next: Done (UC-F9-17); fields editable within the role | U02, U03, U09 | `u02-manager/s-f09-17-projects-e-f09-18-project-and-task-delivered-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f09-17-projects-e-f09-18-project-and-task-delivered-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f09-17-projects-e-f09-18-project-and-task-delivered-phone-{light,dark}.png` |
| E-F9-18 Project and task | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U02, U03, U09 | `u02-manager/s-f09-17-projects-e-f09-18-project-and-task-done-{desktop,phone}-{light,dark}.png`, `u03-sales/s-f09-17-projects-e-f09-18-project-and-task-done-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f09-17-projects-e-f09-18-project-and-task-done-phone-{light,dark}.png` |

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

⬅️ [S-F9-16 Timesheets](../03-time/s-f09-16-timesheets.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-18 Field service](s-f09-18-field-service.md)
