🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-01 People](README.md) ›
🖥️ S-F9-02 Activity plan

# 🖥️ S-F9-02 Activity plan

**Status:** ✅ specified

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Onboard and offboard.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-01 step 2, U06 | desktop | ![FL-F9-01 step 2, U06, light](../../images/01-people/u06-hr/2-onboarding-desktop-light.png) | ![FL-F9-01 step 2, U06, dark](../../images/01-people/u06-hr/2-onboarding-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-02-activity-plan-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-02-activity-plan-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-02-activity-plan-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-02-activity-plan-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-02-activity-plan-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-02-activity-plan-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-02-activity-plan-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-02-activity-plan-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Onboard and offboard, as the wireframe shows.
- Empty: No activity plan yet, with New plan.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F9-04 Activity plan](../../data/e-f09-04-activity-plan.md),
[E-F9-01 Employee record](../../data/e-f09-01-employee-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-04 Activity plan | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U06 | `u02-manager/s-f09-02-activity-plan-e-f09-04-activity-plan-active-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-02-activity-plan-e-f09-04-activity-plan-active-desktop-{light,dark}.png` |
| E-F9-01 Employee record | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U02, U06 | `u02-manager/s-f09-02-activity-plan-e-f09-01-employee-record-active-{desktop,phone}-{light,dark}.png`, `u06-hr/s-f09-02-activity-plan-e-f09-01-employee-record-active-desktop-{light,dark}.png` |

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

- [FL-F9-01 People](../../flows/fl-f09-01-people.md)

## Open questions

None.

---

⬅️ [S-F9-01 Employee](s-f09-01-employee.md) · ⬆️ [Up](README.md) · ➡️ [S-F9-03 HR duties](s-f09-03-hr-duties.md)
