🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-01 See and set up](README.md) › 🖥️ S-F22-20 Cost assistant

# 🖥️ S-F22-20 Cost assistant

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Ask the AI assistant about costs.

## Entry points

Unified platform cost management in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-01 step 5, U13 | desktop | ![FL-F22-01 step 5, U13, light](../../images/01-see-and-set-up/u13-owner/5-assistant-desktop-light.png) | ![FL-F22-01 step 5, U13, dark](../../images/01-see-and-set-up/u13-owner/5-assistant-desktop-dark.png) |
| FL-F22-01 step 5, U13 | phone | ![FL-F22-01 step 5, U13, light](../../images/01-see-and-set-up/u13-owner/5-assistant-phone-light.png) | ![FL-F22-01 step 5, U13, dark](../../images/01-see-and-set-up/u13-owner/5-assistant-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-20-cost-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-20-cost-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-20-cost-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-20-cost-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-20-cost-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-20-cost-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f22-20-cost-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f22-20-cost-assistant-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the conversation with figures.
- Empty: example questions.
- Loading: the frame and titles show at once with placeholder rows for the conversation; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: figures within the user's rights.
- Offline: the AI assistant says it is offline; the question is queued and answered when the network is back, with a
  notification (D182).

Shown entities (VD-15): [E-F22-02 Metered call record](../../data/e-f22-02-metered-call-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-02 Metered call record | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U02, U13 | `u02-manager/s-f22-20-cost-assistant-e-f22-02-metered-call-record-recorded-{desktop,phone}-{light,dark}.png`, `u13-owner/s-f22-20-cost-assistant-e-f22-02-metered-call-record-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-F22-01 See and set up](../../flows/fl-f22-01-see-and-set-up.md)

## Open questions

None.

---

⬅️ [S-F22-19 Cost reports](../04-accounting/s-f22-19-cost-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-21 Currencies](s-f22-21-currencies.md)
