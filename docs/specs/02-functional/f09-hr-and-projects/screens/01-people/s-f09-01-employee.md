🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-01 People](README.md) ›
🖥️ S-F9-01 Employee

# 🖥️ S-F9-01 Employee

**Status:** ✅ specified

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Manage employee records and contracts.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-01 step 1, U06 | desktop | ![FL-F9-01 step 1, U06, light](../../images/01-people/u06-hr/1-employee-record-desktop-light.png) | ![FL-F9-01 step 1, U06, dark](../../images/01-people/u06-hr/1-employee-record-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-01-employee-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-01-employee-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-01-employee-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-01-employee-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-01-employee-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-01-employee-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-01-employee-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-01-employee-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Manage employee records and contracts, as the wireframe shows.
- Empty: No employee yet, with New employee.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F9-01 Employee record](../../data/e-f09-01-employee-record.md),
[E-F9-02 Contract](../../data/e-f09-02-contract.md),
[E-F9-40 Personnel register](../../data/e-f09-40-personnel-register.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-01 Employee record | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06 | `u06-hr/s-f09-01-employee-e-f09-01-employee-record-active-desktop-{light,dark}.png` |
| E-F9-02 Contract | Draft | Badge "Draft"; a new record starts here; next: Running (UC-F9-01); fields editable within the role | U06 | `u06-hr/s-f09-01-employee-e-f09-02-contract-draft-desktop-{light,dark}.png` |
| E-F9-02 Contract | Running | Badge "Running"; next: Expired (UC-F9-01); fields editable within the role | U06 | `u06-hr/s-f09-01-employee-e-f09-02-contract-running-desktop-{light,dark}.png` |
| E-F9-02 Contract | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U06 | `u06-hr/s-f09-01-employee-e-f09-02-contract-expired-desktop-{light,dark}.png` |
| E-F9-40 Personnel register | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06 | `u06-hr/s-f09-01-employee-e-f09-40-personnel-register-active-desktop-{light,dark}.png` |

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

⬆️ [Up](README.md) · ➡️ [S-F9-02 Activity plan](s-f09-02-activity-plan.md)
