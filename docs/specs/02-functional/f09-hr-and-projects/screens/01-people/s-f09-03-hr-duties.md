🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F9-01 People](README.md) ›
🖥️ S-F9-03 HR duties

# 🖥️ S-F9-03 HR duties

**Status:** ✅ specified

## Personas

- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Comply with French HR duties.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-01 step 3, U06 | desktop | ![FL-F9-01 step 3, U06, light](../../images/01-people/u06-hr/3-french-duties-desktop-light.png) | ![FL-F9-01 step 3, U06, dark](../../images/01-people/u06-hr/3-french-duties-desktop-dark.png) |
| Error E1, U06 | desktop | ![Error E1, U06, light](../../images/08-hr-duties/u06-hr/e1-hr-duties-refused-desktop-light.png) | ![Error E1, U06, dark](../../images/08-hr-duties/u06-hr/e1-hr-duties-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-03-hr-duties-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-03-hr-duties-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-03-hr-duties-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-03-hr-duties-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-03-hr-duties-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-03-hr-duties-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f09-03-hr-duties-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f09-03-hr-duties-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Comply with French HR duties, as the wireframe shows.
- Empty: No duty due yet, with Nothing due.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F9-41 Pre-hiring declaration (DPAE)](../../data/e-f09-41-pre-hiring-declaration-dpae.md),
[E-F9-01 Employee record](../../data/e-f09-01-employee-record.md), [E-F9-05 HR duty](../../data/e-f09-05-hr-duty.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-41 Pre-hiring declaration (DPAE) | To send | Badge "To send"; a new record starts here; next: Sent (BR-F9-03); fields editable within the role | U06, U45 | `u06-hr/s-f09-03-hr-duties-e-f09-41-pre-hiring-declaration-dpae-to-send-desktop-{light,dark}.png`, `u45-payroll-officer/s-f09-03-hr-duties-e-f09-41-pre-hiring-declaration-dpae-to-send-desktop-{light,dark}.png` |
| E-F9-41 Pre-hiring declaration (DPAE) | Sent | Badge "Sent"; next: Acknowledged or Refused (UC-F9-03); fields editable within the role | U06, U45 | `u06-hr/s-f09-03-hr-duties-e-f09-41-pre-hiring-declaration-dpae-sent-desktop-{light,dark}.png`, `u45-payroll-officer/s-f09-03-hr-duties-e-f09-41-pre-hiring-declaration-dpae-sent-desktop-{light,dark}.png` |
| E-F9-41 Pre-hiring declaration (DPAE) | Acknowledged | Badge "Acknowledged"; final: read-only, no next state; the history shows how it got here | U06, U45 | `u06-hr/s-f09-03-hr-duties-e-f09-41-pre-hiring-declaration-dpae-acknowledged-desktop-{light,dark}.png`, `u45-payroll-officer/s-f09-03-hr-duties-e-f09-41-pre-hiring-declaration-dpae-acknowledged-desktop-{light,dark}.png` |
| E-F9-41 Pre-hiring declaration (DPAE) | Refused | Badge "Refused"; next: Sent; fields editable within the role | U06, U45 | `u06-hr/s-f09-03-hr-duties-e-f09-41-pre-hiring-declaration-dpae-refused-desktop-{light,dark}.png`, `u45-payroll-officer/s-f09-03-hr-duties-e-f09-41-pre-hiring-declaration-dpae-refused-desktop-{light,dark}.png` |
| E-F9-01 Employee record | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U06 | `u06-hr/s-f09-03-hr-duties-e-f09-01-employee-record-active-desktop-{light,dark}.png` |
| E-F9-05 HR duty | Due | Badge "Due"; a new record starts here; next: Done (UC-F9-03); fields editable within the role | U06, U45 | `u06-hr/s-f09-03-hr-duties-e-f09-05-hr-duty-due-desktop-{light,dark}.png`, `u45-payroll-officer/s-f09-03-hr-duties-e-f09-05-hr-duty-due-desktop-{light,dark}.png` |
| E-F9-05 HR duty | Done | Badge "Done"; next: Late (UC-F9-03); fields editable within the role | U06, U45 | `u06-hr/s-f09-03-hr-duties-e-f09-05-hr-duty-done-desktop-{light,dark}.png`, `u45-payroll-officer/s-f09-03-hr-duties-e-f09-05-hr-duty-done-desktop-{light,dark}.png` |
| E-F9-05 HR duty | Late | Badge "Late"; next: Done (UC-F9-03); fields editable within the role | U06, U45 | `u06-hr/s-f09-03-hr-duties-e-f09-05-hr-duty-late-desktop-{light,dark}.png`, `u45-payroll-officer/s-f09-03-hr-duties-e-f09-05-hr-duty-late-desktop-{light,dark}.png` |

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
- [FL-F9-08 HR duties](../../flows/fl-f09-08-hr-duties.md)

## Open questions

None.

---

⬅️ [S-F9-02 Activity plan](s-f09-02-activity-plan.md) · ⬆️ [Up](README.md) · ➡️ [S-F9-04 My HR](s-f09-04-my-hr.md)
