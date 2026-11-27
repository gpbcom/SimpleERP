🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-02 Ticketing](README.md) › 🖥️ S-SC16-06 Access control

# 🖥️ S-SC16-06 Access control

**Status:** ✅ specified

## Personas

- [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md)

## Purpose

Used to control access by scanning
([UC-SC16-06](../../use-cases/02-ticketing/uc-sc16-06-control-access-by-scanning.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-02 step 3, U44 | phone | ![FL-SC16-02 step 3, U44, light](../../images/02-ticketing/u44-box-office-agent/3-scan-phone-light.png) | ![FL-SC16-02 step 3, U44, dark](../../images/02-ticketing/u44-box-office-agent/3-scan-phone-dark.png) |
| FL-SC16-02 step 3, U44 | desktop | ![FL-SC16-02 step 3, U44, light](../../images/02-ticketing/u44-box-office-agent/3-scan-desktop-light.png) | ![FL-SC16-02 step 3, U44, dark](../../images/02-ticketing/u44-box-office-agent/3-scan-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-06-access-control-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-06-access-control-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-06-access-control-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-06-access-control-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-06-access-control-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-06-access-control-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-06-access-control-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-06-access-control-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-08 Admission ticket](../../data/e-sc16-08-admission-ticket.md), shown as the entity pages list
them, with their examples.

## Actions

- Scan: [UC-SC16-06](../../use-cases/02-ticketing/uc-sc16-06-control-access-by-scanning.md), step 1.
- Admit: [UC-SC16-06](../../use-cases/02-ticketing/uc-sc16-06-control-access-by-scanning.md), step 2.
- Count: [UC-SC16-06](../../use-cases/02-ticketing/uc-sc16-06-control-access-by-scanning.md), step 3.
- Close the doors: [UC-SC16-06](../../use-cases/02-ticketing/uc-sc16-06-control-access-by-scanning.md), step 4.

## States

- Normal: scans per gate with admits, refusals and counts.
- Empty: "Doors not open".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a second scan: it is refused with the first scan's time and gate.
- Read-only: past scans are read-only.
- Offline: scanners keep the ticket list and refuse a second scan on the same device; scans sync when the network is
  back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC16-02 Ticketing](../../flows/fl-sc16-02-ticketing.md)

## Open questions

None.

---

⬅️ [S-SC16-05 Ticketing](s-sc16-05-ticketing.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-07 Box office](s-sc16-07-box-office.md)
