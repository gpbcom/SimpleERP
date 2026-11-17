🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F17-04 Alerts and sharing](README.md) › 🖥️ S-F17-15 Alerts

# 🖥️ S-F17-15 Alerts

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Get alerts on changes.

## Entry points

Competitive analysis in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F17-04 step 1, U12 | desktop | ![FL-F17-04 step 1, U12, light](../../images/04-alerts-and-sharing/u12-marketing/1-alerts-desktop-light.png) | ![FL-F17-04 step 1, U12, dark](../../images/04-alerts-and-sharing/u12-marketing/1-alerts-desktop-dark.png) |
| FL-F17-04 step 1, U12 | phone | ![FL-F17-04 step 1, U12, light](../../images/04-alerts-and-sharing/u12-marketing/1-alerts-phone-light.png) | ![FL-F17-04 step 1, U12, dark](../../images/04-alerts-and-sharing/u12-marketing/1-alerts-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f17-15-alerts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f17-15-alerts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f17-15-alerts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f17-15-alerts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f17-15-alerts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f17-15-alerts-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f17-15-alerts-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f17-15-alerts-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: alerts with thresholds and the changes that fired them.
- Empty: "No alert yet": thresholds to set.
- Loading: the frame and titles show at once with placeholder rows for the alerts; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: followers read alerts; thresholds are set by marketing.
- Offline: Alerts already received stay readable. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F17-13 Alert](../../data/e-f17-13-alert.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F17-13 Alert | Sent | Badge "Sent"; a new record starts here; next: Received (UC-F17-15); fields editable within the role | U03, U12 | `u03-sales/s-f17-15-alerts-e-f17-13-alert-sent-{desktop,phone,tablet}-{light,dark}.png`, `u12-marketing/s-f17-15-alerts-e-f17-13-alert-sent-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F17-14 Win and loss](../03-analyse-and-arm-sales/s-f17-14-win-and-loss.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-16 Digest](s-f17-16-digest.md)
