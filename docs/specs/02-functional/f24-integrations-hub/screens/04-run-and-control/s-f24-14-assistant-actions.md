🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-04 Run and control](README.md) › 🖥️ S-F24-14 Assistant actions

# 🖥️ S-F24-14 Assistant actions

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Ask the AI assistant to act in a connected tool.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-04 step 1, U13 | desktop | ![FL-F24-04 step 1, U13, light](../../images/04-run-and-control/u13-owner/1-assistant-desktop-light.png) | ![FL-F24-04 step 1, U13, dark](../../images/04-run-and-control/u13-owner/1-assistant-desktop-dark.png) |
| FL-F24-04 step 1, U13 | phone | ![FL-F24-04 step 1, U13, light](../../images/04-run-and-control/u13-owner/1-assistant-phone-light.png) | ![FL-F24-04 step 1, U13, dark](../../images/04-run-and-control/u13-owner/1-assistant-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-14-assistant-actions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-14-assistant-actions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-14-assistant-actions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-14-assistant-actions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-14-assistant-actions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-14-assistant-actions-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f24-14-assistant-actions-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f24-14-assistant-actions-offline-phone-dark.png) |

## Fields and columns

As its entities.

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Icon | E-F24-12, or the category's icon (BR-F24-16) | tile sized by BR-F24-16, name as accessible name | no | yes |

## Actions

As its use case's main flow.

## States

- Normal: proposed actions with each tool's icon and the confirm button.
- Empty: example requests.
- Loading: the frame and titles show at once with placeholder rows for the actions; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: within rights.
- Offline: the AI assistant says it is offline; the request is queued and answered when the network is back, with a
  notification (D182).

Shown entities (VD-15): [E-F24-09 Connector action](../../data/e-f24-09-connector-action.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-09 Connector action | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U13 | `u03-sales/s-f24-14-assistant-actions-e-f24-09-connector-action-active-{desktop,phone,tablet}-{light,dark}.png`, `u13-owner/s-f24-14-assistant-actions-e-f24-09-connector-action-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F24-04 Run and control](../../flows/fl-f24-04-run-and-control.md)

## Open questions

None.

---

⬅️ [S-F24-13 History import](../03-crm-and-ats/s-f24-13-history-import.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-15 Health](s-f24-15-health.md)
