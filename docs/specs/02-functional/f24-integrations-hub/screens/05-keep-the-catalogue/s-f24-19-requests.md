🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-05 Keep the catalogue](README.md) › 🖥️ S-F24-19 Requests

# 🖥️ S-F24-19 Requests

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Request a missing connector.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-05 step 2, U13 | desktop | ![FL-F24-05 step 2, U13, light](../../images/05-keep-the-catalogue/u13-owner/2-request-desktop-light.png) | ![FL-F24-05 step 2, U13, dark](../../images/05-keep-the-catalogue/u13-owner/2-request-desktop-dark.png) |
| FL-F24-05 step 2, U13 | phone | ![FL-F24-05 step 2, U13, light](../../images/05-keep-the-catalogue/u13-owner/2-request-phone-light.png) | ![FL-F24-05 step 2, U13, dark](../../images/05-keep-the-catalogue/u13-owner/2-request-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/05-keep-the-catalogue/u13-owner/e1-not-possible-desktop-light.png) | ![Error E1, U13, dark](../../images/05-keep-the-catalogue/u13-owner/e1-not-possible-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/05-keep-the-catalogue/u13-owner/e1-not-possible-phone-light.png) | ![Error E1, U13, dark](../../images/05-keep-the-catalogue/u13-owner/e1-not-possible-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-19-requests-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-19-requests-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-19-requests-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-19-requests-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-19-requests-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-19-requests-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f24-19-requests-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f24-19-requests-offline-phone-dark.png) |

## Fields and columns

As its entities.

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Icon | E-F24-12, or the category's icon (BR-F24-16) | tile sized by BR-F24-16, name as accessible name | no | yes |

## Actions

As its use case's main flow.

## States

- Normal: requests with their state.
- Empty: "No request".
- Loading: the frame and titles show at once with placeholder rows for the requests; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: requesters read their own.
- Offline: not available offline: requests are sent online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F24-01 Connector](../../data/e-f24-01-connector.md),
[E-F24-16 Connector request](../../data/e-f24-16-connector-request.md),
[E-F24-12 Integration icon](../../data/e-f24-12-integration-icon.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-01 Connector | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f24-19-requests-e-f24-01-connector-active-{desktop,phone}-{light,dark}.png` |
| E-F24-16 Connector request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f24-19-requests-e-f24-16-connector-request-active-{desktop,phone}-{light,dark}.png` |
| E-F24-12 Integration icon | Proposed | Badge "Proposed"; a new record starts here; next: Approved (UC-F24-21); fields editable within the role | U13 | `u13-owner/s-f24-19-requests-e-f24-12-integration-icon-proposed-{desktop,phone}-{light,dark}.png` |
| E-F24-12 Integration icon | Approved | Badge "Approved"; next: Replaced or Withdrawn (UC-F24-01, UC-F24-27); fields editable within the role | U13 | `u13-owner/s-f24-19-requests-e-f24-12-integration-icon-approved-{desktop,phone}-{light,dark}.png` |
| E-F24-12 Integration icon | Replaced | Badge "Replaced"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f24-19-requests-e-f24-12-integration-icon-replaced-{desktop,phone}-{light,dark}.png` |
| E-F24-12 Integration icon | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f24-19-requests-e-f24-12-integration-icon-withdrawn-{desktop,phone}-{light,dark}.png` |

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

- [FL-F24-05 Keep the catalogue](../../flows/fl-f24-05-keep-the-catalogue.md)

## Open questions

None.

---

⬅️ [S-F24-18 Yearly review](s-f24-18-yearly-review.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-20 Rights and costs](../04-run-and-control/s-f24-20-rights-and-costs.md)
