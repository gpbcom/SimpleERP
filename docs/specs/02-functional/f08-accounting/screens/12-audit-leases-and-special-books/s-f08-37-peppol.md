🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F8-37 Peppol

# 🖥️ S-F8-37 Peppol

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the registration and the exchanges.

## Purpose

Register the company on Peppol, send and receive invoices abroad and read their statuses.

## Entry points

Accounting › Peppol; an invoice's Send by Peppol action; the AI assistant.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Peppol: Atelier Verdier                      Active   Access point: Hub partner             |
|---------------------------------------------------------------------------------------------|
| Identifier  0225:552081317        Capabilities  invoice, credit note                         |
| EXCHANGES   Sent 14   Delivered 13   Failed 1   Received 6                                   |
| WHEN        DIRECTION  COUNTERPARTY      DOCUMENT    STATUS      NOTE                        |
| 2026-11-12  Out        Brasserie Nova BE  INV-2310    Delivered   -                          |
| 2026-11-13  Out        Maison Roth DE     INV-2314    Failed      invalid tax code           |
| [Look up a company] [Resend] [Open the invoice]                                              |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-12 step 3, U05 | desktop | ![FL-F8-12 step 3, U05, light](../../images/12-audit-leases-and-special-books/u05-accounting/3-peppol-desktop-light.png) | ![FL-F8-12 step 3, U05, dark](../../images/12-audit-leases-and-special-books/u05-accounting/3-peppol-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-37-peppol-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-37-peppol-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-37-peppol-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-37-peppol-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-37-peppol-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-37-peppol-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-37-peppol-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-37-peppol-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Participant and identifier | E-F8-42 | text | yes while Pending | yes |
| Access point | E-F8-42 | text | yes while Pending | yes |
| Capabilities | E-F8-42 | list | yes | yes |
| Exchanges | E-F6-05, E-F7-05 | table | no | no |
| Status and note | E-F6-05 delivery status | badge and text | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Register | header | accounting | the registration is requested from the directory |
| Look up a company | header | accounting | whether a counterparty is reachable |
| Resend | row | accounting | a Failed invoice is sent again after correction |
| Deregister | header | accounting | the company leaves Peppol |

## States

- Normal: the registration, the counts of exchanges and the list with their statuses.
- Empty: Not registered, with Register on Peppol.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a rejected
  document shows the access point's validation errors in plain words.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-42 Peppol participant](../../data/e-f08-42-peppol-participant.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-42 Peppol participant | Pending | Badge "Pending"; a new record starts here; next: Active or Refused (UC-F8-38); fields editable within the role | U05 | `u05-accounting/s-f08-37-peppol-e-f08-42-peppol-participant-pending-desktop-{light,dark}.png` |
| E-F8-42 Peppol participant | Active | Badge "Active"; next: Suspended or Deregistered (UC-F8-38); fields editable within the role | U05 | `u05-accounting/s-f08-37-peppol-e-f08-42-peppol-participant-active-desktop-{light,dark}.png` |
| E-F8-42 Peppol participant | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f08-37-peppol-e-f08-42-peppol-participant-refused-desktop-{light,dark}.png` |
| E-F8-42 Peppol participant | Suspended | Badge "Suspended"; next: Active (UC-F8-38); fields editable within the role | U05 | `u05-accounting/s-f08-37-peppol-e-f08-42-peppol-participant-suspended-desktop-{light,dark}.png` |
| E-F8-42 Peppol participant | Deregistered | Badge "Deregistered"; final: read-only, no next state; the history shows how it got here | U05 | `u05-accounting/s-f08-37-peppol-e-f08-42-peppol-participant-deregistered-desktop-{light,dark}.png` |

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

- [FL-F8-12](../../flows/fl-f08-12-audit-leases-and-special-books.md)

## Open questions

None.

---

⬅️ [S-F8-36 Leases](s-f08-36-leases.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-38 Business travel](s-f08-38-business-travel.md)
