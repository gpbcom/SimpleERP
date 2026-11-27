🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-05 Events](README.md) › 🖥️ S-SC08-13 Temporary bar

# 🖥️ S-SC08-13 Temporary bar

**Status:** ✅ specified

## Personas

- [U32 Volunteer](../../../../01-users/personas/u32-volunteer.md)
- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)

## Purpose

Used to run a temporary bar at events
([UC-SC08-13](../../use-cases/05-events/uc-sc08-13-run-a-temporary-bar-at-events.md)).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-05 step 2, U32 | phone | ![FL-SC08-05 step 2, U32, light](../../images/05-events/u32-volunteer/2-bar-phone-light.png) | ![FL-SC08-05 step 2, U32, dark](../../images/05-events/u32-volunteer/2-bar-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc08-13-temporary-bar-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc08-13-temporary-bar-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc08-13-temporary-bar-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc08-13-temporary-bar-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc08-13-temporary-bar-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc08-13-temporary-bar-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-13-temporary-bar-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-13-temporary-bar-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC08-13 Temporary bar](../../data/e-sc08-13-temporary-bar.md), shown as the entity pages list them,
with their examples.

## Actions

- Ask the authorisation: [UC-SC08-13](../../use-cases/05-events/uc-sc08-13-run-a-temporary-bar-at-events.md), step 1.
- Sell: [UC-SC08-13](../../use-cases/05-events/uc-sc08-13-run-a-temporary-bar-at-events.md), step 2.
- Close takings: [UC-SC08-13](../../use-cases/05-events/uc-sc08-13-run-a-temporary-bar-at-events.md), step 3.
- Post: [UC-SC08-13](../../use-cases/05-events/uc-sc08-13-run-a-temporary-bar-at-events.md), step 4.

## States

- Normal: bars with authorisation, drink groups and takings.
- Empty: "No bar".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, over the yearly number: the bar is refused
  ([BR-SC08-11](../../business-rules/br-sc08-11-bars-within-the-yearly-limit.md)).
- Read-only: closed takings are read-only.
- Offline: the till keeps selling offline,
  [UC-F10-14](../../../../02-functional/f10-point-of-sale/use-cases/06-mobile-and-delivery/uc-f10-14-sell-on-the-move-and-offline.md).

Shown entities (VD-15): [E-SC08-13 Temporary bar](../../data/e-sc08-13-temporary-bar.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-13 Temporary bar | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U31, U32 | `u31-treasurer/s-sc08-13-temporary-bar-e-sc08-13-temporary-bar-active-{desktop,phone}-{light,dark}.png`, `u32-volunteer/s-sc08-13-temporary-bar-e-sc08-13-temporary-bar-active-phone-{light,dark}.png` |

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

## Shown in

- [FL-SC08-05 Events](../../flows/fl-sc08-05-events.md)

## Open questions

None.

---

⬅️ [S-SC08-12 Events](s-sc08-12-events.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-14 Association accounts](../06-accounts-and-data/s-sc08-14-association-accounts.md)
