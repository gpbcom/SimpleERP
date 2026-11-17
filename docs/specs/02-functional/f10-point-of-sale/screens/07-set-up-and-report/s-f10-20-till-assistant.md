🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏪 [F10 Point of sale (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F10-07 Set up and report](README.md) › 🖥️ S-F10-20 Till assistant

# 🖥️ S-F10-20 Till assistant

**Status:** ✅ specified

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U18 Waiter](../../../../01-users/personas/u18-waiter.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Ask the AI assistant at the till.

## Entry points

Point of sale in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F10-07 step 3, U17 | desktop | ![FL-F10-07 step 3, U17, light](../../images/07-set-up-and-report/u17-cashier/3-assistant-desktop-light.png) | ![FL-F10-07 step 3, U17, dark](../../images/07-set-up-and-report/u17-cashier/3-assistant-desktop-dark.png) |
| FL-F10-07 step 3, U17 | phone | ![FL-F10-07 step 3, U17, light](../../images/07-set-up-and-report/u17-cashier/3-assistant-phone-light.png) | ![FL-F10-07 step 3, U17, dark](../../images/07-set-up-and-report/u17-cashier/3-assistant-phone-dark.png) |
| FL-F10-07 step 3, U17 | tablet | ![FL-F10-07 step 3, U17, light](../../images/07-set-up-and-report/u17-cashier/3-assistant-tablet-light.png) | ![FL-F10-07 step 3, U17, dark](../../images/07-set-up-and-report/u17-cashier/3-assistant-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f10-20-till-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f10-20-till-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f10-20-till-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f10-20-till-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f10-20-till-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f10-20-till-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f10-20-till-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f10-20-till-assistant-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Ask the AI assistant at the till, as the wireframe shows.
- Empty: No question yet, with Ask a question.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: closed sessions and recorded sales, which are inalterable (CR-FR-026).
- Offline: The AI assistant says it is offline; questions are queued and answered when the network is back, with a
  notification, and changes still need confirmation then
  ([D182](../../../../06-decisions/f03-assistant/d182-offline-assistant.md)).

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F10-07 Set up and report](../../flows/fl-f10-07-set-up-and-report.md)

## Open questions

None.

---

⬅️ [S-F10-19 Customer display](../05-self-order-and-kiosk/s-f10-19-customer-display.md) · ⬆️ [Up](README.md) ·
➡️ [S-F10-21 Age check prompt](../08-vouchers-and-age-checks/s-f10-21-age-check-prompt.md)
