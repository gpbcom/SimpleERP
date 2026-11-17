🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-07 Benchmark additions](README.md) › 🖥️ S-F2-13 Documents workspace

# 🖥️ S-F2-13 Documents workspace

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Manage documents in a workspace.

## Entry points

No-code configuration in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-07 step 2, U16 | desktop | ![FL-F2-07 step 2, U16, light](../../images/07-benchmark-additions/u16-office-worker/2-documents-desktop-light.png) | ![FL-F2-07 step 2, U16, dark](../../images/07-benchmark-additions/u16-office-worker/2-documents-desktop-dark.png) |
| FL-F2-07 step 2, U16 | phone | ![FL-F2-07 step 2, U16, light](../../images/07-benchmark-additions/u16-office-worker/2-documents-phone-light.png) | ![FL-F2-07 step 2, U16, dark](../../images/07-benchmark-additions/u16-office-worker/2-documents-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-13-documents-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-13-documents-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-13-documents-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-13-documents-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-13-documents-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-13-documents-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f02-13-documents-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f02-13-documents-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Manage documents in a workspace, as the wireframe shows.
- Empty: No document yet in this folder, with Upload and the scanner mail-in address.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: folders shared for reading; signed documents.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F2-13 Document](../../data/e-f02-13-document.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-13 Document | To sort | Badge "To sort"; a new record starts here; next: To validate (UC-F2-13); fields editable within the role | U05, U07, U16 | `u05-accounting/s-f02-13-documents-workspace-e-f02-13-document-to-sort-desktop-{light,dark}.png`, `u07-administrator/s-f02-13-documents-workspace-e-f02-13-document-to-sort-desktop-{light,dark}.png`, `u16-office-worker/s-f02-13-documents-workspace-e-f02-13-document-to-sort-{desktop,phone}-{light,dark}.png` |
| E-F2-13 Document | To validate | Badge "To validate"; next: Done (UC-F2-13); fields editable within the role | U05, U07, U16 | `u05-accounting/s-f02-13-documents-workspace-e-f02-13-document-to-validate-desktop-{light,dark}.png`, `u07-administrator/s-f02-13-documents-workspace-e-f02-13-document-to-validate-desktop-{light,dark}.png`, `u16-office-worker/s-f02-13-documents-workspace-e-f02-13-document-to-validate-{desktop,phone}-{light,dark}.png` |
| E-F2-13 Document | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U05, U07, U16 | `u05-accounting/s-f02-13-documents-workspace-e-f02-13-document-done-desktop-{light,dark}.png`, `u07-administrator/s-f02-13-documents-workspace-e-f02-13-document-done-desktop-{light,dark}.png`, `u16-office-worker/s-f02-13-documents-workspace-e-f02-13-document-done-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F2-07 Benchmark additions](../../flows/fl-f02-07-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F2-12 Spreadsheet](s-f02-12-spreadsheet.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-14 Signature requests](s-f02-14-signature-requests.md)
