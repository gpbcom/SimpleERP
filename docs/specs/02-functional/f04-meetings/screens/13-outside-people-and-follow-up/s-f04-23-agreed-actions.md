🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🎙️ [F4 Meetings](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F4-13 Outside people and follow-up](README.md) ›
🖥️ S-F4-23 Agreed actions

# 🖥️ S-F4-23 Agreed actions

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Show the customer the actions agreed in a meeting, to confirm or change.

## Entry points

The follow-up email's link; the customer portal.

## Wireframe

```text
+----------------------------------------+
| Meeting of 2026-11-28 with Acme        |
| Agreed actions                         |
| Acme: send the plans      12-05  [ok]  |
| Durand: sign the quote    12-08  [ok]  |
| Acme: site visit          12-12  [ok]  |
| [Confirm all]   [Ask a change]         |
+----------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F4-13 step 2, U09 | phone | ![FL-F4-13 step 2, U09, light](../../images/13-outside-people-and-follow-up/u09-customer/2-agreed-actions-phone-light.png) | ![FL-F4-13 step 2, U09, dark](../../images/13-outside-people-and-follow-up/u09-customer/2-agreed-actions-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f04-23-agreed-actions-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f04-23-agreed-actions-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f04-23-agreed-actions-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f04-23-agreed-actions-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f04-23-agreed-actions-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f04-23-agreed-actions-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f04-23-agreed-actions-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f04-23-agreed-actions-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Action, owner, date | E-F4-04 | change request with comment |

## Actions

| Action | Who | Result |
|---|---|---|
| Confirm all | customer | Organiser told |
| Ask a change | customer | Action reopened |

## States

- Normal: show the customer the actions agreed in a meeting, to confirm or change.
- Empty: never: sent only with actions.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: once confirmed: read only.
- Offline: Not available offline: a page served live to the customer
  ([D407](../../../../06-decisions/technical/d407-front-end.md)).

Shown entities (VD-15): [E-F4-01 Meeting](../../data/e-f04-01-meeting.md),
[E-F4-04 Action item](../../data/e-f04-04-action-item.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F4-01 Meeting | Planned | Badge "Planned"; a new record starts here; next: Live (UC-F4-01); fields editable within the role | U09 | `u09-customer/s-f04-23-agreed-actions-e-f04-01-meeting-planned-phone-{light,dark}.png` |
| E-F4-01 Meeting | Live | Badge "Live"; next: Ended (UC-F4-02); fields editable within the role | U09 | `u09-customer/s-f04-23-agreed-actions-e-f04-01-meeting-live-phone-{light,dark}.png` |
| E-F4-01 Meeting | Ended | Badge "Ended"; next: Waiting for review (UC-F4-01); fields editable within the role | U09 | `u09-customer/s-f04-23-agreed-actions-e-f04-01-meeting-ended-phone-{light,dark}.png` |
| E-F4-01 Meeting | Waiting for review | Badge "Waiting for review"; next: Checked (UC-F4-05); fields editable within the role | U09 | `u09-customer/s-f04-23-agreed-actions-e-f04-01-meeting-waiting-for-review-phone-{light,dark}.png` |
| E-F4-01 Meeting | Checked | Badge "Checked"; final: read-only, no next state; the history shows how it got here | U09 | `u09-customer/s-f04-23-agreed-actions-e-f04-01-meeting-checked-phone-{light,dark}.png` |
| E-F4-04 Action item | Open | Badge "Open"; a new record starts here; next: Done (UC-F4-27); fields editable within the role | U03, U09 | `u03-sales/s-f04-23-agreed-actions-e-f04-04-action-item-open-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f04-23-agreed-actions-e-f04-04-action-item-open-phone-{light,dark}.png` |
| E-F4-04 Action item | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U03, U09 | `u03-sales/s-f04-23-agreed-actions-e-f04-04-action-item-done-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-f04-23-agreed-actions-e-f04-04-action-item-done-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone first; desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F4-13 Outside people and follow-up](../../flows/fl-f04-13-outside-people-and-follow-up.md)

## Open questions

None.

---

⬅️ [S-F4-22 Speaker requests](s-f04-22-speaker-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F4-24 Employee calendar](../s-f04-24-employee-calendar.md)
