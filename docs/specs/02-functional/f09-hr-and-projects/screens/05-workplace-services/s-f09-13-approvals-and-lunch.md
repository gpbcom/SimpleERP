🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-05 Workplace services](README.md) › 🖥️ S-F9-13 Approvals and lunch

# 🖥️ S-F9-13 Approvals and lunch

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Request approvals and order lunch.

## Entry points

HR and projects in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-05 step 2, U01 | phone | ![FL-F9-05 step 2, U01, light](../../images/05-workplace-services/u01-employee/2-approvals-and-lunch-phone-light.png) | ![FL-F9-05 step 2, U01, dark](../../images/05-workplace-services/u01-employee/2-approvals-and-lunch-phone-dark.png) |
| FL-F9-05 step 2, U01 | desktop | ![FL-F9-05 step 2, U01, light](../../images/05-workplace-services/u01-employee/2-approvals-and-lunch-desktop-light.png) | ![FL-F9-05 step 2, U01, dark](../../images/05-workplace-services/u01-employee/2-approvals-and-lunch-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-13-approvals-and-lunch-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-13-approvals-and-lunch-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-13-approvals-and-lunch-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-13-approvals-and-lunch-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-13-approvals-and-lunch-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-13-approvals-and-lunch-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-13-approvals-and-lunch-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-13-approvals-and-lunch-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Request approvals and order lunch, as the wireframe shows.
- Empty: No approval request yet, with New request.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: validated or signed records; other employees' records outside the user's record rules.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F9-14 Approval request](../../data/e-f09-14-approval-request.md),
[E-F9-39 Lunch order](../../data/e-f09-39-lunch-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F9-14 Approval request | To approve | Badge "To approve"; a new record starts here; next: Approved or Refused (UC-F9-13); fields editable within the role | U01, U02 | `u01-employee/s-f09-13-approvals-and-lunch-e-f09-14-approval-request-to-approve-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-13-approvals-and-lunch-e-f09-14-approval-request-to-approve-{desktop,phone}-{light,dark}.png` |
| E-F9-14 Approval request | Approved | Badge "Approved"; final: read-only, no next state; the history shows how it got here | U01, U02 | `u01-employee/s-f09-13-approvals-and-lunch-e-f09-14-approval-request-approved-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-13-approvals-and-lunch-e-f09-14-approval-request-approved-{desktop,phone}-{light,dark}.png` |
| E-F9-14 Approval request | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U01, U02 | `u01-employee/s-f09-13-approvals-and-lunch-e-f09-14-approval-request-refused-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-13-approvals-and-lunch-e-f09-14-approval-request-refused-{desktop,phone}-{light,dark}.png` |
| E-F9-39 Lunch order | Active | Badge "Active"; a new record starts here; next: Sent (UC-F9-13); fields editable within the role | U01, U02 | `u01-employee/s-f09-13-approvals-and-lunch-e-f09-39-lunch-order-active-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-13-approvals-and-lunch-e-f09-39-lunch-order-active-{desktop,phone}-{light,dark}.png` |
| E-F9-39 Lunch order | Sent | Badge "Sent"; next: Confirmed or Not confirmed (UC-F9-13); fields editable within the role | U01, U02 | `u01-employee/s-f09-13-approvals-and-lunch-e-f09-39-lunch-order-sent-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-13-approvals-and-lunch-e-f09-39-lunch-order-sent-{desktop,phone}-{light,dark}.png` |
| E-F9-39 Lunch order | Confirmed | Badge "Confirmed"; next: Delivered (UC-F9-13); fields editable within the role | U01, U02 | `u01-employee/s-f09-13-approvals-and-lunch-e-f09-39-lunch-order-confirmed-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-13-approvals-and-lunch-e-f09-39-lunch-order-confirmed-{desktop,phone}-{light,dark}.png` |
| E-F9-39 Lunch order | Not confirmed | Badge "Not confirmed"; final: read-only, no next state; the history shows how it got here | U01, U02 | `u01-employee/s-f09-13-approvals-and-lunch-e-f09-39-lunch-order-not-confirmed-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-13-approvals-and-lunch-e-f09-39-lunch-order-not-confirmed-{desktop,phone}-{light,dark}.png` |
| E-F9-39 Lunch order | Delivered | Badge "Delivered"; final: read-only, no next state; the history shows how it got here | U01, U02 | `u01-employee/s-f09-13-approvals-and-lunch-e-f09-39-lunch-order-delivered-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f09-13-approvals-and-lunch-e-f09-39-lunch-order-delivered-{desktop,phone}-{light,dark}.png` |

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

- [FL-F9-05 Workplace services](../../flows/fl-f09-05-workplace-services.md)

## Open questions

None.

---

⬅️ [S-F9-12 Fleet](s-f09-12-fleet.md) · ⬆️ [Up](README.md) · ➡️ [S-F9-14 Visitors](s-f09-14-visitors.md)
