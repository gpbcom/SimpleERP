🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-01 Find and connect](README.md) › 🖥️ S-F24-02 Connect

# 🖥️ S-F24-02 Connect

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Connect a tool in the fewest steps.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-01 step 2, U07 | desktop | ![FL-F24-01 step 2, U07, light](../../images/01-find-and-connect/u07-administrator/2-connect-desktop-light.png) | ![FL-F24-01 step 2, U07, dark](../../images/01-find-and-connect/u07-administrator/2-connect-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/06-business-tools/u07-administrator/e1-connect-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/06-business-tools/u07-administrator/e1-connect-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-02-connect-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-02-connect-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-02-connect-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-02-connect-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-02-connect-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-02-connect-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-02-connect-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-02-connect-offline-desktop-dark.png) |

## Fields and columns

As its entities.

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Icon | E-F24-12, or the category's icon (BR-F24-16) | tile sized by BR-F24-16, name as accessible name | no | yes |

## Actions

As its use case's main flow.

## States

- Normal: the connector's icon, sign-in and proposed settings.
- Empty: never empty: opens from a connector.
- Loading: the frame and titles show at once with placeholder rows for the settings; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: other roles cannot connect.
- Offline: not available offline: sign-in needs the network. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F24-02 Tool connection](../../data/e-f24-02-tool-connection.md),
[E-F24-11 Connector category](../../data/e-f24-11-connector-category.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-02 Tool connection | Proposed | Badge "Proposed"; a new record starts here; next: Active (UC-F24-21); fields editable within the role | U07 | `u07-administrator/s-f24-02-connect-e-f24-02-tool-connection-proposed-desktop-{light,dark}.png` |
| E-F24-02 Tool connection | Active | Badge "Active"; next: Revoked (UC-F24-17); fields editable within the role | U07 | `u07-administrator/s-f24-02-connect-e-f24-02-tool-connection-active-desktop-{light,dark}.png` |
| E-F24-11 Connector category | Active | Badge "Active"; a new record starts here; next: Retired (UC-F24-01); fields editable within the role | U07, U13 | `u07-administrator/s-f24-02-connect-e-f24-11-connector-category-active-desktop-{light,dark}.png`, `u13-owner/s-f24-02-connect-e-f24-11-connector-category-active-{desktop,phone}-{light,dark}.png` |
| E-F24-11 Connector category | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U07, U13 | `u07-administrator/s-f24-02-connect-e-f24-11-connector-category-retired-desktop-{light,dark}.png`, `u13-owner/s-f24-02-connect-e-f24-11-connector-category-retired-{desktop,phone}-{light,dark}.png` |

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

- [FL-F24-01 Find and connect](../../flows/fl-f24-01-find-and-connect.md)

## Open questions

None.

---

⬅️ [S-F24-01 Catalogue](s-f24-01-catalogue.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-03 Suite sign-in](../02-office-suites/s-f24-03-suite-sign-in.md)
