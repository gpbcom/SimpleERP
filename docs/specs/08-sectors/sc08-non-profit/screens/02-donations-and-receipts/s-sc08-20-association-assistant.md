🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-02 Donations and receipts](README.md) ›
🖥️ S-SC08-20 Association assistant

# 🖥️ S-SC08-20 Association assistant

**Status:** ✅ specified

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to ask the AI assistant about the association,
[UC-SC08-20](../../use-cases/02-donations-and-receipts/uc-sc08-20-ask-the-assistant-about-the-association.md).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-02 step 6, U31 | desktop | ![FL-SC08-02 step 6, U31, light](../../images/02-donations-and-receipts/u31-treasurer/6-assistant-desktop-light.png) | ![FL-SC08-02 step 6, U31, dark](../../images/02-donations-and-receipts/u31-treasurer/6-assistant-desktop-dark.png) |
| FL-SC08-02 step 6, U31 | phone | ![FL-SC08-02 step 6, U31, light](../../images/02-donations-and-receipts/u31-treasurer/6-assistant-phone-light.png) | ![FL-SC08-02 step 6, U31, dark](../../images/02-donations-and-receipts/u31-treasurer/6-assistant-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-20-association-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-20-association-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-20-association-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-20-association-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-20-association-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-20-association-assistant-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-20-association-assistant-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-20-association-assistant-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC08-04 Gift](../../data/e-sc08-04-gift.md),
[E-F8-18 Grant](../../../../02-functional/f08-accounting/data/e-f08-18-grant.md), shown as
the entity pages list them, with their examples.

## Actions

- Ask: [UC-SC08-20](../../use-cases/02-donations-and-receipts/uc-sc08-20-ask-the-assistant-about-the-association.md),
  step 1.
- Confirm a draft:
  [UC-SC08-20](../../use-cases/02-donations-and-receipts/uc-sc08-20-ask-the-assistant-about-the-association.md), step 4.

## States

- Normal: the conversation with answers, links and drafts.
- Empty: suggested questions.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an action beyond the user's rights: the AI assistant refuses and
  says which role can do it.
- Read-only: answers only for roles that cannot act.
- Offline: not available offline: the AI assistant needs the network; the last answers stay readable.

Shown entities (VD-15): [E-SC08-04 Gift](../../data/e-sc08-04-gift.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-04 Gift | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U31 | `u13-owner/s-sc08-20-association-assistant-e-sc08-04-gift-active-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-sc08-20-association-assistant-e-sc08-04-gift-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC08-02 Donations and receipts](../../flows/fl-sc08-02-donations-and-receipts.md)

## Open questions

None.

---

⬅️ [S-SC08-19 Association dashboard](../06-accounts-and-data/s-sc08-19-association-dashboard.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-21 Grant-making](../07-foundations-integration-and-federations/s-sc08-21-grant-making.md)
