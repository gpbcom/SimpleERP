🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-06 Portal and assistant](README.md) ›
🖥️ S-SC10-20 Portfolio assistant

# 🖥️ S-SC10-20 Portfolio assistant

**Status:** ✅ specified

## Personas

- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md)
- [U35 Real-estate agent](../../../../01-users/personas/u35-real-estate-agent.md)

## Purpose

Used to ask the AI assistant about the portfolio,
[UC-SC10-20](../../use-cases/06-portal-and-assistant/uc-sc10-20-ask-the-assistant-about-the-portfolio.md).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-06 step 2, U34 | desktop | ![FL-SC10-06 step 2, U34, light](../../images/06-portal-and-assistant/u34-property-manager/2-assistant-desktop-light.png) | ![FL-SC10-06 step 2, U34, dark](../../images/06-portal-and-assistant/u34-property-manager/2-assistant-desktop-dark.png) |
| FL-SC10-06 step 2, U34 | tablet | ![FL-SC10-06 step 2, U34, light](../../images/06-portal-and-assistant/u34-property-manager/2-assistant-tablet-light.png) | ![FL-SC10-06 step 2, U34, dark](../../images/06-portal-and-assistant/u34-property-manager/2-assistant-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-20-portfolio-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-20-portfolio-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-20-portfolio-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-20-portfolio-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-20-portfolio-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-20-portfolio-assistant-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc10-20-portfolio-assistant-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc10-20-portfolio-assistant-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC10-07 Lease](../../data/e-sc10-07-lease.md),
[E-SC10-13 Co-owners' assembly](../../data/e-sc10-13-co-owners-assembly.md), shown as the entity pages list them, with
their examples.

## Actions

- Ask: [UC-SC10-20](../../use-cases/06-portal-and-assistant/uc-sc10-20-ask-the-assistant-about-the-portfolio.md), step
  1.
- Confirm a draft:
  [UC-SC10-20](../../use-cases/06-portal-and-assistant/uc-sc10-20-ask-the-assistant-about-the-portfolio.md), step 4.

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

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC10-06 Portal and assistant](../../flows/fl-sc10-06-portal-and-assistant.md)

## Open questions

None.

---

⬅️ [S-SC10-19 Portal](s-sc10-19-portal.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-21 Short-term rentals](../07-short-stays-commercial-and-coworking/s-sc10-21-short-term-rentals.md)
