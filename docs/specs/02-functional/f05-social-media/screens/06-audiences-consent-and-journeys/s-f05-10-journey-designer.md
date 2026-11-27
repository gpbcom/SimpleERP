🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-06 Audiences, consent and journeys](README.md) › 🖥️ S-F5-10 Journey designer

# 🖥️ S-F5-10 Journey designer

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)

## Purpose

Automate marketing journeys.

## Entry points

Social media and marketing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-06 step 4, U12 | desktop | ![FL-F5-06 step 4, U12, light](../../images/06-audiences-consent-and-journeys/u12-marketing/4-journey-designer-desktop-light.png) | ![FL-F5-06 step 4, U12, dark](../../images/06-audiences-consent-and-journeys/u12-marketing/4-journey-designer-desktop-dark.png) |
| FL-F5-06 step 4, U12 | phone | ![FL-F5-06 step 4, U12, light](../../images/06-audiences-consent-and-journeys/u12-marketing/4-journey-designer-phone-light.png) | ![FL-F5-06 step 4, U12, dark](../../images/06-audiences-consent-and-journeys/u12-marketing/4-journey-designer-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-10-journey-designer-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-10-journey-designer-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-10-journey-designer-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-10-journey-designer-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-10-journey-designer-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-10-journey-designer-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-10-journey-designer-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-10-journey-designer-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Automate marketing journeys, as the wireframe shows.
- Empty: No journey yet, with New journey.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users without the marketing right; published items.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F5-06 Journey](../../data/e-f05-06-journey.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-06 Journey | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U12 | `u12-marketing/s-f05-10-journey-designer-e-f05-06-journey-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F5-05 Benchmark additions](../../flows/fl-f05-05-benchmark-additions.md)
- [FL-F5-06 Audiences, consent and journeys](../../flows/fl-f05-06-audiences-consent-and-journeys.md)

## Open questions

None.

---

⬅️ [S-F5-09 SMS campaign](../05-benchmark-additions/s-f05-09-sms-campaign.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-11 Event](../07-events-and-ticketing/s-f05-11-event.md)
