🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-06 Accounts and data](README.md) › 🖥️ S-SC08-17 News

# 🖥️ S-SC08-17 News

**Status:** 🔄 waiting for the owner

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to communicate with members
([UC-SC08-17](../../use-cases/06-accounts-and-data/uc-sc08-17-communicate-with-members.md)).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-06 step 3, U12 | desktop | ![FL-SC08-06 step 3, U12, light](../../images/06-accounts-and-data/u12-marketing/3-news-desktop-light.png) | ![FL-SC08-06 step 3, U12, dark](../../images/06-accounts-and-data/u12-marketing/3-news-desktop-dark.png) |
| FL-SC08-06 step 3, U12 | phone | ![FL-SC08-06 step 3, U12, light](../../images/06-accounts-and-data/u12-marketing/3-news-phone-light.png) | ![FL-SC08-06 step 3, U12, dark](../../images/06-accounts-and-data/u12-marketing/3-news-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-17-news-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-17-news-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-17-news-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-17-news-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-17-news-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-17-news-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-17-news-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-17-news-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC08-01 Member](../../data/e-sc08-01-member.md), shown as the entity pages list them, with their
examples.

## Actions

- Write: [UC-SC08-17](../../use-cases/06-accounts-and-data/uc-sc08-17-communicate-with-members.md), step 1.
- Choose recipients: [UC-SC08-17](../../use-cases/06-accounts-and-data/uc-sc08-17-communicate-with-members.md), step 2.
- Approve: [UC-SC08-17](../../use-cases/06-accounts-and-data/uc-sc08-17-communicate-with-members.md), step 3.
- Send: [UC-SC08-17](../../use-cases/06-accounts-and-data/uc-sc08-17-communicate-with-members.md), step 4.

## States

- Normal: newsletters with recipients and sending state.
- Empty: "No newsletter".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no consent: the member is skipped.
- Read-only: a sent newsletter is read-only.
- Offline: not available offline: office work on members, gifts and accounts shared by the board. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC08-01 Member](../../data/e-sc08-01-member.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-01 Member | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U12, U13 | `u12-marketing/s-sc08-17-news-e-sc08-01-member-active-{desktop,phone}-{light,dark}.png`, `u13-owner/s-sc08-17-news-e-sc08-01-member-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

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

⬅️ [S-SC08-16 Bequests](../02-donations-and-receipts/s-sc08-16-bequests.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-18 Data rights](s-sc08-18-data-rights.md)
