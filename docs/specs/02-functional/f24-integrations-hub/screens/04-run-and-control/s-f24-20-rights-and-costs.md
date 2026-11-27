🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-04 Run and control](README.md) › 🖥️ S-F24-20 Rights and costs

# 🖥️ S-F24-20 Rights and costs

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Control the rights and costs of connectors.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-04 step 5, U07 | desktop | ![FL-F24-04 step 5, U07, light](../../images/04-run-and-control/u07-administrator/5-rights-costs-desktop-light.png) | ![FL-F24-04 step 5, U07, dark](../../images/04-run-and-control/u07-administrator/5-rights-costs-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-20-rights-and-costs-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-20-rights-and-costs-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-20-rights-and-costs-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-20-rights-and-costs-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-20-rights-and-costs-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-20-rights-and-costs-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-20-rights-and-costs-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-20-rights-and-costs-offline-desktop-dark.png) |

## Fields and columns

As its entities.

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Icon | E-F24-12, or the category's icon (BR-F24-16) | tile sized by BR-F24-16, name as accessible name | no | yes |
| Review period and next review | the company's review period (UC-F24-20) | every quarter by default, or a shorter period the company sets; the next review date | no | yes |

## Actions

As its use case's main flow.

## States

- Normal: connectors with their icons, scopes, roles and costs, under the review period (every quarter by default,
  shorter when the company sets it, [D575](../../../../06-decisions/foundations/d575-answers-of-2026-11-27-on-the-last-open-points.md))
  and the next review date.
- Empty: "No connector".
- Loading: the frame and titles show at once with placeholder rows for the rights; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner reads.
- Offline: not available offline: set online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F24-09 Connector action](../../data/e-f24-09-connector-action.md),
[E-F24-02 Tool connection](../../data/e-f24-02-tool-connection.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-09 Connector action | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f24-20-rights-and-costs-e-f24-09-connector-action-active-desktop-{light,dark}.png`, `u13-owner/s-f24-20-rights-and-costs-e-f24-09-connector-action-active-{desktop,phone}-{light,dark}.png` |
| E-F24-02 Tool connection | Proposed | Badge "Proposed"; a new record starts here; next: Active (UC-F24-21); fields editable within the role | U07, U13 | `u07-administrator/s-f24-20-rights-and-costs-e-f24-02-tool-connection-proposed-desktop-{light,dark}.png`, `u13-owner/s-f24-20-rights-and-costs-e-f24-02-tool-connection-proposed-{desktop,phone}-{light,dark}.png` |
| E-F24-02 Tool connection | Active | Badge "Active"; next: Revoked (UC-F24-17); fields editable within the role | U07, U13 | `u07-administrator/s-f24-20-rights-and-costs-e-f24-02-tool-connection-active-desktop-{light,dark}.png`, `u13-owner/s-f24-20-rights-and-costs-e-f24-02-tool-connection-active-{desktop,phone}-{light,dark}.png` |
| E-F24-02 Tool connection | Revoked | Badge "Revoked"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f24-20-rights-and-costs-e-f24-02-tool-connection-revoked-desktop-{light,dark}.png`, `u13-owner/s-f24-20-rights-and-costs-e-f24-02-tool-connection-revoked-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F24-19 Requests](../05-keep-the-catalogue/s-f24-19-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-21 Automation](../06-business-tools/s-f24-21-automation.md)
