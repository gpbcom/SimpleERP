🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-07 Benchmark additions](README.md) › 🖥️ S-F2-14 Signature requests

# 🖥️ S-F2-14 Signature requests

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U06 HR](../../../../01-users/personas/u06-hr.md)

## Purpose

Send documents for e-signature.

## Entry points

No-code configuration in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-07 step 3, U16 | desktop | ![FL-F2-07 step 3, U16, light](../../images/07-benchmark-additions/u16-office-worker/3-e-signature-desktop-light.png) | ![FL-F2-07 step 3, U16, dark](../../images/07-benchmark-additions/u16-office-worker/3-e-signature-desktop-dark.png) |
| FL-F2-07 step 3, U16 | phone | ![FL-F2-07 step 3, U16, light](../../images/07-benchmark-additions/u16-office-worker/3-e-signature-phone-light.png) | ![FL-F2-07 step 3, U16, dark](../../images/07-benchmark-additions/u16-office-worker/3-e-signature-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-14-signature-requests-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-14-signature-requests-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-14-signature-requests-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-14-signature-requests-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-14-signature-requests-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-14-signature-requests-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f02-14-signature-requests-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f02-14-signature-requests-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Send documents for e-signature, as the wireframe shows.
- Empty: No signature request yet, with Send for signature.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a signed or expired request and its proof.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F2-14 Signature request](../../data/e-f02-14-signature-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-14 Signature request | Sent | Badge "Sent"; a new record starts here; next: Signed or Refused (UC-F2-14); fields editable within the role | U03, U06, U16 | `u03-sales/s-f02-14-signature-requests-e-f02-14-signature-request-sent-{desktop,phone,tablet}-{light,dark}.png`, `u06-hr/s-f02-14-signature-requests-e-f02-14-signature-request-sent-desktop-{light,dark}.png`, `u16-office-worker/s-f02-14-signature-requests-e-f02-14-signature-request-sent-{desktop,phone}-{light,dark}.png` |
| E-F2-14 Signature request | Signed | Badge "Signed"; next: Expired (UC-F2-14); fields editable within the role | U03, U06, U16 | `u03-sales/s-f02-14-signature-requests-e-f02-14-signature-request-signed-{desktop,phone,tablet}-{light,dark}.png`, `u06-hr/s-f02-14-signature-requests-e-f02-14-signature-request-signed-desktop-{light,dark}.png`, `u16-office-worker/s-f02-14-signature-requests-e-f02-14-signature-request-signed-{desktop,phone}-{light,dark}.png` |
| E-F2-14 Signature request | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U03, U06, U16 | `u03-sales/s-f02-14-signature-requests-e-f02-14-signature-request-refused-{desktop,phone,tablet}-{light,dark}.png`, `u06-hr/s-f02-14-signature-requests-e-f02-14-signature-request-refused-desktop-{light,dark}.png`, `u16-office-worker/s-f02-14-signature-requests-e-f02-14-signature-request-refused-{desktop,phone}-{light,dark}.png` |
| E-F2-14 Signature request | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U03, U06, U16 | `u03-sales/s-f02-14-signature-requests-e-f02-14-signature-request-expired-{desktop,phone,tablet}-{light,dark}.png`, `u06-hr/s-f02-14-signature-requests-e-f02-14-signature-request-expired-desktop-{light,dark}.png`, `u16-office-worker/s-f02-14-signature-requests-e-f02-14-signature-request-expired-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F2-13 Documents workspace](s-f02-13-documents-workspace.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-15 Build assistant](s-f02-15-build-assistant.md)
