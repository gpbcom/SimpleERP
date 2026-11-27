🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-01 Find and connect](README.md) › 🖥️ S-F24-01 Catalogue

# 🖥️ S-F24-01 Catalogue

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Browse the connector catalogue.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-01 step 1, U07 | desktop | ![FL-F24-01 step 1, U07, light](../../images/01-find-and-connect/u07-administrator/1-catalogue-desktop-light.png) | ![FL-F24-01 step 1, U07, dark](../../images/01-find-and-connect/u07-administrator/1-catalogue-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-01-catalogue-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-01-catalogue-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-01-catalogue-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-01-catalogue-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-01-catalogue-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-01-catalogue-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-01-catalogue-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-01-catalogue-offline-desktop-dark.png) |

## Fields and columns

As its entities.

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Icon | E-F24-12, or the category's icon (BR-F24-16) | tile sized by BR-F24-16, name as accessible name | no | yes |

## Actions

As its use case's main flow.

## States

- Normal: connectors by category, each with its icon, vendor country, cost and rights.
- Empty: "No connector matches": filters to clear and the request link.
- Loading: the frame and titles show at once with placeholder rows for the connectors; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: users other than administrators browse without connecting.
- Offline: not available offline: the catalogue is read online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F24-01 Connector](../../data/e-f24-01-connector.md),
[E-F24-02 Tool connection](../../data/e-f24-02-tool-connection.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-01 Connector | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f24-01-catalogue-e-f24-01-connector-active-desktop-{light,dark}.png` |
| E-F24-02 Tool connection | Proposed | Badge "Proposed"; a new record starts here; next: Active (UC-F24-21); fields editable within the role | U07 | `u07-administrator/s-f24-01-catalogue-e-f24-02-tool-connection-proposed-desktop-{light,dark}.png` |

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

⬆️ [Up](README.md) · ➡️ [S-F24-02 Connect](s-f24-02-connect.md)
