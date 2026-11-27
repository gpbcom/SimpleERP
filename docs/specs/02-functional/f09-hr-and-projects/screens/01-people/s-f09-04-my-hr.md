🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-01 People](README.md) ›
🖥️ S-F9-04 My HR

# 🖥️ S-F9-04 My HR

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U14 Field worker](../../../../01-users/personas/u14-field-worker.md)

## Purpose

Use employee self-service.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

My qualifications ([S-F9-35](../13-keep-qualifications/s-f09-35-employee-qualifications.md)) and, in teams with the
live-position option, My position history ([S-F9-34](../12-schedule-customer-requests/s-f09-34-my-position.md)).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-01 step 4, U01 | phone | ![FL-F9-01 step 4, U01, light](../../images/01-people/u01-employee/4-self-service-phone-light.png) | ![FL-F9-01 step 4, U01, dark](../../images/01-people/u01-employee/4-self-service-phone-dark.png) |
| FL-F9-01 step 4, U01 | desktop | ![FL-F9-01 step 4, U01, light](../../images/01-people/u01-employee/4-self-service-desktop-light.png) | ![FL-F9-01 step 4, U01, dark](../../images/01-people/u01-employee/4-self-service-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-04-my-hr-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-04-my-hr-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-04-my-hr-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-04-my-hr-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-04-my-hr-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-04-my-hr-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-04-my-hr-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-04-my-hr-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Use employee self-service, as the wireframe shows.
- Empty: No request yet, with Request time off.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F9-01 Employee record](../../data/e-f09-01-employee-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-01 Employee record | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U14 | `u01-employee/s-f09-04-my-hr-e-f09-01-employee-record-active-{desktop,phone}-{light,dark}.png`, `u14-field-worker/s-f09-04-my-hr-e-f09-01-employee-record-active-phone-{light,dark}.png` |

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

⬅️ [S-F9-03 HR duties](s-f09-03-hr-duties.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-05 Job position](../02-recruit/s-f09-05-job-position.md)
