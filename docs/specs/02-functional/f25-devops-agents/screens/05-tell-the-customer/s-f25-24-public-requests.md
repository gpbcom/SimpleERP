🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-05 Tell the customer](README.md) › 🖥️ S-F25-24 Public requests

# 🖥️ S-F25-24 Public requests

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

List declined requests, anonymised, and collect votes.

## Entry points

Help, Public requests; a declined request's message.

## Wireframe

```text
Public requests                      Sort: [most votes v]
-------------------------------------------------------------------------------
Request                        Status             Reason            Votes
Export payslips to Silae       declined           custom need       26  [Voted]
Kanban for purchases           declined           not planned       9   [Vote]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-05 step 5, U13 | desktop | ![FL-F25-05 step 5, U13, light](../../images/05-tell-the-customer/u13-owner/5-public-requests-desktop-light.png) | ![FL-F25-05 step 5, U13, dark](../../images/05-tell-the-customer/u13-owner/5-public-requests-desktop-dark.png) |
| FL-F25-05 step 5, U13 | phone | ![FL-F25-05 step 5, U13, light](../../images/05-tell-the-customer/u13-owner/5-public-requests-phone-light.png) | ![FL-F25-05 step 5, U13, dark](../../images/05-tell-the-customer/u13-owner/5-public-requests-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-24-public-requests-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-24-public-requests-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-24-public-requests-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-24-public-requests-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-24-public-requests-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-24-public-requests-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-24-public-requests-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-24-public-requests-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Request | E-F25-03 | title | no | yes |
| Status, reason | E-F25-09 | text | no | yes |
| Votes | E-F25-14 | count | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Vote | row | owner, administrator | vote counted |
| Withdraw | row | owner, administrator | vote removed |

## States

- Normal: declined requests with reasons and votes.
- Empty: "No declined request".
- Loading: the frame and titles show at once with placeholder rows for the requests; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a second vote refused.
- Read-only: employees read only.
- Offline: The list last loaded stays visible; voting needs the network. Nothing else is queued: D38 keeps only today's
  schedule, time and intervention records offline; a banner says the connection is lost and the actions come back with
  it.

Shown entities (VD-15): [E-F25-09 Request status](../../data/e-f25-09-request-status.md),
[E-F25-14 Vote](../../data/e-f25-14-vote.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-09 Request status | Planned | Badge "Planned"; a new record starts here; next: Received or Declined (BR-F25-09, UC-F25-14); fields editable within the role | U07, U13 | `u07-administrator/s-f25-24-public-requests-e-f25-09-request-status-planned-desktop-{light,dark}.png`, `u13-owner/s-f25-24-public-requests-e-f25-09-request-status-planned-{desktop,phone}-{light,dark}.png` |
| E-F25-09 Request status | Received | Badge "Received"; next: Shipped or Declined (UC-F25-15, UC-F25-14); fields editable within the role | U07, U13 | `u07-administrator/s-f25-24-public-requests-e-f25-09-request-status-received-desktop-{light,dark}.png`, `u13-owner/s-f25-24-public-requests-e-f25-09-request-status-received-{desktop,phone}-{light,dark}.png` |
| E-F25-09 Request status | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f25-24-public-requests-e-f25-09-request-status-declined-desktop-{light,dark}.png`, `u13-owner/s-f25-24-public-requests-e-f25-09-request-status-declined-{desktop,phone}-{light,dark}.png` |
| E-F25-09 Request status | Shipped | Badge "Shipped"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f25-24-public-requests-e-f25-09-request-status-shipped-desktop-{light,dark}.png`, `u13-owner/s-f25-24-public-requests-e-f25-09-request-status-shipped-{desktop,phone}-{light,dark}.png` |
| E-F25-14 Vote | Counted | Badge "Counted"; a new record starts here; next: Withdrawn (UC-F25-12); fields editable within the role | U07, U13 | `u07-administrator/s-f25-24-public-requests-e-f25-14-vote-counted-desktop-{light,dark}.png`, `u13-owner/s-f25-24-public-requests-e-f25-14-vote-counted-{desktop,phone}-{light,dark}.png` |
| E-F25-14 Vote | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f25-24-public-requests-e-f25-14-vote-withdrawn-desktop-{light,dark}.png`, `u13-owner/s-f25-24-public-requests-e-f25-14-vote-withdrawn-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone and desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F25-05 Tell the customer](../../flows/fl-f25-05-tell-the-customer.md)

## Open questions

None.

---

⬅️ [S-F25-23 Spec checks](../02-feature-requests/s-f25-23-spec-checks.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-25 Public roadmap](../07-roadmap-beta-and-credits/s-f25-25-public-roadmap.md)
