🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-06 Business tools](README.md) › 🖥️ S-F24-21 Automation

# 🖥️ S-F24-21 Automation

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Connect automation tools with webhooks and a service account token.

## Entry points

Catalogue, Automation category.

## Wireframe

```text
Automation  [n8n icon] n8n                             [Add webhook] [New token]
-------------------------------------------------------------------------------
Event            Endpoint                              State     Failures
invoice paid     https://n8n.example/webhook/41        active    0
order created    https://n8n.example/webhook/42        paused    10
-------------------------------------------------------------------------------
Service account: automation-sales (rights: sales, read)
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-06 step 2, U07 | desktop | ![FL-F24-06 step 2, U07, light](../../images/06-business-tools/u07-administrator/2-automation-desktop-light.png) | ![FL-F24-06 step 2, U07, dark](../../images/06-business-tools/u07-administrator/2-automation-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-21-automation-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-21-automation-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-21-automation-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-21-automation-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-21-automation-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-21-automation-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-21-automation-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-21-automation-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Icon | E-F24-12 or category fallback | tile sized by BR-F24-16, name as accessible name | no | yes |
| Event | E-F24-13 events | list | yes | yes |
| Endpoint | E-F24-13 endpoint | URL | yes | yes |
| State | E-F24-13 state | list | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Add webhook | header | administrator | secret created |
| New token | header | administrator | service account token |
| Resume | row | administrator | active again |

## States

- Normal: webhooks and the service account.
- Empty: "No automation yet".
- Loading: the frame and titles show at once with placeholder rows for the webhooks; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a paused endpoint with its failures.
- Read-only: the owner reads.
- Offline: not available offline: set online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F24-13 Webhook subscription](../../data/e-f24-13-webhook-subscription.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-13 Webhook subscription | Active | Badge "Active"; a new record starts here; next: Paused or Deleted (UC-F24-22, UC-F24-20); fields editable within the role | U07 | `u07-administrator/s-f24-21-automation-e-f24-13-webhook-subscription-active-desktop-{light,dark}.png` |
| E-F24-13 Webhook subscription | Paused | Badge "Paused"; next: Active (UC-F24-22); fields editable within the role | U07 | `u07-administrator/s-f24-21-automation-e-f24-13-webhook-subscription-paused-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F24-06 Business tools](../../flows/fl-f24-06-business-tools.md)

## Open questions

None.

---

⬅️ [S-F24-20 Rights and costs](../04-run-and-control/s-f24-20-rights-and-costs.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-22 E-invoicing platform](s-f24-22-e-invoicing-platform.md)
