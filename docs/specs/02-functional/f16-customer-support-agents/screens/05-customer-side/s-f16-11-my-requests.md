🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-05 Customer side](README.md) › 🖥️ S-F16-11 My requests

# 🖥️ S-F16-11 My requests

**Status:** 🔄 waiting for the owner

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Show the customer their requests with status, expected time and messages, and let them reply or ask for a person.

## Entry points

Customer portal (F6), My requests; the link in the acknowledgement email.

## Wireframe

```text
My requests
-------------------------------------------------------------------------------
5512  Refund for late delivery   in progress   AI agent   answer by 14:00
5401  Invoice copy               resolved      AI agent   rated 5
-------------------------------------------------------------------------------
5512: messages ...                [Reply] [Add a file] [Talk to a person]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-05 step 2, U09 | phone | ![FL-F16-05 step 2, U09, light](../../images/05-customer-side/u09-customer/2-my-requests-phone-light.png) | ![FL-F16-05 step 2, U09, dark](../../images/05-customer-side/u09-customer/2-my-requests-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f16-11-my-requests-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f16-11-my-requests-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f16-11-my-requests-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f16-11-my-requests-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f16-11-my-requests-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f16-11-my-requests-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-11-my-requests-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-11-my-requests-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Request | E-F16-01 | number and subject | no | yes |
| Status | E-F16-01 status | text | no | yes |
| Handled by | E-F16-01 | AI agent or person | no | yes |
| Expected | E-F16-05 | time | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Reply | request | customer | message added, clock resumes |
| Add a file | request | customer | file attached |
| Talk to a person | request | customer | request routed to a person |

## States

- Normal: the customer's requests with status, handler and expected time; the messages of the one opened.
- Empty: "No request yet": a link to the help centre and the request form.
- Loading: the frame and titles show at once with placeholder rows for the requests; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an expired link, with the sign-in.
- Read-only: resolved requests are read-only, with "Reopen" for (Proposed) 7 days.
- Offline: Requests last loaded stay readable; replies are sent only online. Nothing else is queued: D38 keeps only
  today's schedule, time and intervention records offline; a banner says the connection is lost and the actions come
  back with it.

Shown entities (VD-15): [E-F16-01 Customer request](../../data/e-f16-01-customer-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-01 Customer request | New | Badge "New"; a new record starts here; next: In progress (UC-F16-12); fields editable within the role | U09, U16 | `u09-customer/s-f16-11-my-requests-e-f16-01-customer-request-new-phone-{light,dark}.png`, `u16-office-worker/s-f16-11-my-requests-e-f16-01-customer-request-new-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | In progress | Badge "In progress"; next: Resolved or Waiting (UC-F16-01, UC-F16-07); fields editable within the role | U09, U16 | `u09-customer/s-f16-11-my-requests-e-f16-01-customer-request-in-progress-phone-{light,dark}.png`, `u16-office-worker/s-f16-11-my-requests-e-f16-01-customer-request-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | Resolved | Badge "Resolved"; next: Escalated (UC-F16-04); fields editable within the role | U09, U16 | `u09-customer/s-f16-11-my-requests-e-f16-01-customer-request-resolved-phone-{light,dark}.png`, `u16-office-worker/s-f16-11-my-requests-e-f16-01-customer-request-resolved-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | Waiting | Badge "Waiting"; next: Resolved (UC-F16-01); fields editable within the role | U09, U16 | `u09-customer/s-f16-11-my-requests-e-f16-01-customer-request-waiting-phone-{light,dark}.png`, `u16-office-worker/s-f16-11-my-requests-e-f16-01-customer-request-waiting-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | Escalated | Badge "Escalated"; next: Resolved (UC-F16-01); fields editable within the role | U09, U16 | `u09-customer/s-f16-11-my-requests-e-f16-01-customer-request-escalated-phone-{light,dark}.png`, `u16-office-worker/s-f16-11-my-requests-e-f16-01-customer-request-escalated-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone first (D34); desktop in two columns.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F16-05 Customer side](../../flows/fl-f16-05-customer-side.md)
- [FL-F16-06 Take in every request](../../flows/fl-f16-06-take-in-every-request.md)

## Open questions

None.

---

⬅️ [S-F16-10 Help centre](s-f16-10-help-centre.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-12 Intent discovery](../02-automate-an-intent/s-f16-12-intent-discovery.md)
