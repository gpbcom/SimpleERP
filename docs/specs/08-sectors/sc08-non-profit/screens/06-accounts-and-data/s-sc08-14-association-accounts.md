🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-06 Accounts and data](README.md) › 🖥️ S-SC08-14 Association accounts

# 🖥️ S-SC08-14 Association accounts

**Status:** ✅ specified

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)

## Purpose

Used to keep association accounts
([UC-SC08-14](../../use-cases/06-accounts-and-data/uc-sc08-14-keep-association-accounts.md)).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-06 step 1, U31 | desktop | ![FL-SC08-06 step 1, U31, light](../../images/06-accounts-and-data/u31-treasurer/1-accounts-desktop-light.png) | ![FL-SC08-06 step 1, U31, dark](../../images/06-accounts-and-data/u31-treasurer/1-accounts-desktop-dark.png) |
| FL-SC08-06 step 1, U31 | phone | ![FL-SC08-06 step 1, U31, light](../../images/06-accounts-and-data/u31-treasurer/1-accounts-phone-light.png) | ![FL-SC08-06 step 1, U31, dark](../../images/06-accounts-and-data/u31-treasurer/1-accounts-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-14-association-accounts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-14-association-accounts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-14-association-accounts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-14-association-accounts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-14-association-accounts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-14-association-accounts-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-14-association-accounts-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-14-association-accounts-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC08-09 Grant report](../../data/e-sc08-09-grant-report.md),
[E-F8-19 Dedicated fund](../../../../02-functional/f08-accounting/data/e-f08-19-dedicated-fund.md),
[E-F8-19 Dedicated fund](../../../../02-functional/f08-accounting/data/e-f08-19-dedicated-fund.md), shown as the entity
pages list them, with their examples.

## Actions

- Record: [UC-SC08-14](../../use-cases/06-accounts-and-data/uc-sc08-14-keep-association-accounts.md), step 1.
- Carry dedicated funds: [UC-SC08-14](../../use-cases/06-accounts-and-data/uc-sc08-14-keep-association-accounts.md),
  step 2.
- Close the year: [UC-SC08-14](../../use-cases/06-accounts-and-data/uc-sc08-14-keep-association-accounts.md), step 3.
- Present: [UC-SC08-14](../../use-cases/06-accounts-and-data/uc-sc08-14-keep-association-accounts.md), step 4.

## States

- Normal: entries, dedicated funds and contributions in kind.
- Empty: "No entry".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a dedicated fund overspent: the treasurer is alerted.
- Read-only: closed years are read-only.
- Offline: not available offline: office work on members, gifts and accounts shared by the board. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15):
[E-F8-19 Dedicated fund](../../../../02-functional/f08-accounting/data/e-f08-19-dedicated-fund.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-19 Dedicated fund | Open | Badge "Open"; a new record starts here; next: Closed (UC-SC08-14); fields editable within the role | U13, U31 | `u13-owner/s-sc08-14-association-accounts-e-f08-19-dedicated-fund-open-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-sc08-14-association-accounts-e-f08-19-dedicated-fund-open-{desktop,phone}-{light,dark}.png` |
| E-F8-19 Dedicated fund | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U13, U31 | `u13-owner/s-sc08-14-association-accounts-e-f08-19-dedicated-fund-closed-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-sc08-14-association-accounts-e-f08-19-dedicated-fund-closed-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC08-06 Accounts and data](../../flows/fl-sc08-06-accounts-and-data.md)

## Open questions

None.

---

⬅️ [S-SC08-13 Temporary bar](../05-events/s-sc08-13-temporary-bar.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-15 Publication](s-sc08-15-publication.md)
