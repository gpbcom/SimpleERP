🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F7-29 Supplier EDI

# 🖥️ S-F7-29 Supplier EDI

**Status:** 🔄 waiting for the owner

## Personas

- [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md): the messages of their suppliers.

## Purpose

See every EDI message per supplier and order, resend a failed one and read the responses.

## Entry points

Purchasing and stock › EDI messages; a purchase order's Messages tab.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Supplier EDI: Menuiserie Dupont          Sent 12   Acknowledged 11   Failed 1   Received 8  |
|---------------------------------------------------------------------------------------------|
| WHEN         DIRECTION  TYPE             REFERENCE  STATE          TRIES                    |
| 2026-11-14   Out        Order            PO-2310    Acknowledged   1                        |
| 2026-11-14   Out        Order            PO-2311    Failed         3                        |
| 2026-11-14   In         Despatch advice  PO-2310    Processed      -                        |
| [Resend] [Open the message] [Open the order]                                                |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-10 step 5, U04 | desktop | ![FL-F7-10 step 5, U04, light](../../images/10-consignment-scanning-and-edi/u04-purchasing/5-supplier-edi-desktop-light.png) | ![FL-F7-10 step 5, U04, dark](../../images/10-consignment-scanning-and-edi/u04-purchasing/5-supplier-edi-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f07-29-supplier-edi-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f07-29-supplier-edi-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f07-29-supplier-edi-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f07-29-supplier-edi-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f07-29-supplier-edi-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f07-29-supplier-edi-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f07-29-supplier-edi-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f07-29-supplier-edi-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| When and direction | E-F7-26 | date and in or out | no | yes |
| Type and reference | E-F7-26 | text | no | yes |
| State and tries | E-F7-26 | badge and number | no | yes |
| Order | E-F7-03 | link | no | no |
| Reason | E-F7-26 | text | no | for Failed or Rejected |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Resend | row | purchasing | a Failed or Rejected message is queued again |
| Open the message | row | purchasing | the content in a readable form |
| Accept the change | response | purchasing | the order takes the supplier's answer |

## States

- Normal: the messages of the supplier with their states and the orders they concern.
- Empty: No EDI message yet, with Set up EDI for a supplier.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a message that
  failed shows the reason and the number of tries.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-26 EDI message](../../data/e-f07-26-edi-message.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-26 EDI message | Queued | Badge "Queued"; a new record starts here; next: Sent (UC-F7-29); fields editable within the role | U04 | `u04-purchasing/s-f07-29-supplier-edi-e-f07-26-edi-message-queued-desktop-{light,dark}.png` |
| E-F7-26 EDI message | Sent | Badge "Sent"; next: Acknowledged, Retrying or Rejected (BR-F7-23, UC-F7-29); fields editable within the role | U04 | `u04-purchasing/s-f07-29-supplier-edi-e-f07-26-edi-message-sent-desktop-{light,dark}.png` |
| E-F7-26 EDI message | Acknowledged | Badge "Acknowledged"; final: read-only, no next state; the history shows how it got here | U04 | `u04-purchasing/s-f07-29-supplier-edi-e-f07-26-edi-message-acknowledged-desktop-{light,dark}.png` |
| E-F7-26 EDI message | Retrying | Badge "Retrying"; next: Sent or Failed (BR-F7-23); fields editable within the role | U04 | `u04-purchasing/s-f07-29-supplier-edi-e-f07-26-edi-message-retrying-desktop-{light,dark}.png` |
| E-F7-26 EDI message | Failed | Badge "Failed"; next: Queued (UC-F7-29); fields editable within the role | U04 | `u04-purchasing/s-f07-29-supplier-edi-e-f07-26-edi-message-failed-desktop-{light,dark}.png` |
| E-F7-26 EDI message | Rejected | Badge "Rejected"; next: Queued (UC-F7-29); fields editable within the role | U04 | `u04-purchasing/s-f07-29-supplier-edi-e-f07-26-edi-message-rejected-desktop-{light,dark}.png` |
| E-F7-26 EDI message | Received | Badge "Received"; a new record starts here; next: Processed or Rejected (UC-F7-29); fields editable within the role | U04 | `u04-purchasing/s-f07-29-supplier-edi-e-f07-26-edi-message-received-desktop-{light,dark}.png` |
| E-F7-26 EDI message | Processed | Badge "Processed"; final: read-only, no next state; the history shows how it got here | U04 | `u04-purchasing/s-f07-29-supplier-edi-e-f07-26-edi-message-processed-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

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

⬅️ [S-F7-28 Returnable packaging](s-f07-28-returnable-packaging.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-30 Slotting](s-f07-30-slotting.md)
