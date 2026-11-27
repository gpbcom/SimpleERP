🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F7-01 Procure](README.md) ›
🖥️ S-F7-01 Purchase request

# 🖥️ S-F7-01 Purchase request

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Request and approve a purchase.

## Entry points

Purchasing or Stock in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-01 step 1, U01 | desktop | ![FL-F7-01 step 1, U01, light](../../images/01-procure/u01-employee/1-request-and-approve-desktop-light.png) | ![FL-F7-01 step 1, U01, dark](../../images/01-procure/u01-employee/1-request-and-approve-desktop-dark.png) |
| Error E1, U01 | desktop | ![Error E1, U01, light](../../images/01-procure/u01-employee/e1-budget-exceeded-desktop-light.png) | ![Error E1, U01, dark](../../images/01-procure/u01-employee/e1-budget-exceeded-desktop-dark.png) |
| Error E1, U01 | phone | ![Error E1, U01, light](../../images/01-procure/u01-employee/e1-budget-exceeded-phone-light.png) | ![Error E1, U01, dark](../../images/01-procure/u01-employee/e1-budget-exceeded-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-01-purchase-request-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-01-purchase-request-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-01-purchase-request-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-01-purchase-request-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-01-purchase-request-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-01-purchase-request-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f07-01-purchase-request-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f07-01-purchase-request-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Request and approve a purchase, as the wireframe shows.
- Empty: No purchase request yet, with New request.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F7-02 Purchase request](../../data/e-f07-02-purchase-request.md),
[E-F7-03 Purchase order](../../data/e-f07-03-purchase-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-02 Purchase request | Draft | Badge "Draft"; a new record starts here; next: To approve or Refused (UC-F7-20, UC-F7-01); fields editable within the role | U01, U02 | `u01-employee/s-f07-01-purchase-request-e-f07-02-purchase-request-draft-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f07-01-purchase-request-e-f07-02-purchase-request-draft-{desktop,phone}-{light,dark}.png` |
| E-F7-02 Purchase request | To approve | Badge "To approve"; next: Approved or Refused (UC-F7-01); fields editable within the role | U01, U02 | `u01-employee/s-f07-01-purchase-request-e-f07-02-purchase-request-to-approve-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f07-01-purchase-request-e-f07-02-purchase-request-to-approve-{desktop,phone}-{light,dark}.png` |
| E-F7-02 Purchase request | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U01, U02 | `u01-employee/s-f07-01-purchase-request-e-f07-02-purchase-request-refused-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f07-01-purchase-request-e-f07-02-purchase-request-refused-{desktop,phone}-{light,dark}.png` |
| E-F7-02 Purchase request | Approved | Badge "Approved"; next: Ordered or Refused (UC-F7-01); fields editable within the role | U01, U02 | `u01-employee/s-f07-01-purchase-request-e-f07-02-purchase-request-approved-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f07-01-purchase-request-e-f07-02-purchase-request-approved-{desktop,phone}-{light,dark}.png` |
| E-F7-02 Purchase request | Ordered | Badge "Ordered"; final: read-only, no next state; the history shows how it got here | U01, U02 | `u01-employee/s-f07-01-purchase-request-e-f07-02-purchase-request-ordered-{desktop,phone}-{light,dark}.png`, `u02-manager/s-f07-01-purchase-request-e-f07-02-purchase-request-ordered-{desktop,phone}-{light,dark}.png` |
| E-F7-03 Purchase order | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-F7-02); fields editable within the role | U01 | `u01-employee/s-f07-01-purchase-request-e-f07-03-purchase-order-draft-{desktop,phone}-{light,dark}.png` |
| E-F7-03 Purchase order | Sent | Badge "Sent"; next: Confirmed (UC-F7-02); fields editable within the role | U01 | `u01-employee/s-f07-01-purchase-request-e-f07-03-purchase-order-sent-{desktop,phone}-{light,dark}.png` |
| E-F7-03 Purchase order | Confirmed | Badge "Confirmed"; next: Received (UC-F7-04); fields editable within the role | U01 | `u01-employee/s-f07-01-purchase-request-e-f07-03-purchase-order-confirmed-{desktop,phone}-{light,dark}.png` |
| E-F7-03 Purchase order | Received | Badge "Received"; next: Billed (UC-F7-01); fields editable within the role | U01 | `u01-employee/s-f07-01-purchase-request-e-f07-03-purchase-order-received-{desktop,phone}-{light,dark}.png` |
| E-F7-03 Purchase order | Billed | Badge "Billed"; final: read-only, no next state; the history shows how it got here | U01 | `u01-employee/s-f07-01-purchase-request-e-f07-03-purchase-order-billed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; receipts, picking and counts on phones, offline.

## Accessibility

Labelled controls; quantities and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F7-01 Procure](../../flows/fl-f07-01-procure.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F7-02 Purchase order](s-f07-02-purchase-order.md)
