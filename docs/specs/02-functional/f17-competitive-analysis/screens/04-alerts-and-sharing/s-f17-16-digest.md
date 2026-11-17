🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-04 Alerts and sharing](README.md) › 🖥️ S-F17-16 Digest

# 🖥️ S-F17-16 Digest

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Receive a periodic digest.

## Entry points

Competitive analysis in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-04 step 2, U13 | desktop | ![FL-F17-04 step 2, U13, light](../../images/04-alerts-and-sharing/u13-owner/2-digest-desktop-light.png) | ![FL-F17-04 step 2, U13, dark](../../images/04-alerts-and-sharing/u13-owner/2-digest-desktop-dark.png) |
| FL-F17-04 step 2, U13 | phone | ![FL-F17-04 step 2, U13, light](../../images/04-alerts-and-sharing/u13-owner/2-digest-phone-light.png) | ![FL-F17-04 step 2, U13, dark](../../images/04-alerts-and-sharing/u13-owner/2-digest-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-16-digest-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-16-digest-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-16-digest-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-16-digest-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-16-digest-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-16-digest-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-16-digest-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-16-digest-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the digest with its period and links to details.
- Empty: "No digest yet": the first one comes at the end of the period.
- Loading: the frame and titles show at once with placeholder rows for the digest; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: A digest already opened stays readable. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F17-13 Alert](../../data/e-f17-13-alert.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-13 Alert | Sent | Badge "Sent"; a new record starts here; next: Received (UC-F17-15); fields editable within the role | U13 | `u13-owner/s-f17-16-digest-e-f17-13-alert-sent-{desktop,phone}-{light,dark}.png` |
| E-F17-13 Alert | Received | Badge "Received"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f17-16-digest-e-f17-13-alert-received-{desktop,phone}-{light,dark}.png` |

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
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F17-04 Alerts and sharing](../../flows/fl-f17-04-alerts-and-sharing.md)

## Open questions

None.

---

⬅️ [S-F17-15 Alerts](s-f17-15-alerts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-17 Market shares](../03-analyse-and-arm-sales/s-f17-17-market-shares.md)
