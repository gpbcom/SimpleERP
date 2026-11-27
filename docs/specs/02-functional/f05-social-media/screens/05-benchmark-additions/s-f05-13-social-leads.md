🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-05 Benchmark additions](README.md) › 🖥️ S-F5-13 Social leads

# 🖥️ S-F5-13 Social leads

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Turn social interactions into leads.

## Entry points

Social media and marketing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-05 step 3, U12 | desktop | ![FL-F5-05 step 3, U12, light](../../images/05-benchmark-additions/u12-marketing/3-journey-desktop-light.png) | ![FL-F5-05 step 3, U12, dark](../../images/05-benchmark-additions/u12-marketing/3-journey-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-13-social-leads-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-13-social-leads-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-13-social-leads-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-13-social-leads-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-13-social-leads-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-13-social-leads-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-13-social-leads-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-13-social-leads-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Turn social interactions into leads, as the wireframe shows.
- Empty: No social lead yet, with Connect an account.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users without the marketing right; published items.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-20 Lead](../../../f06-customers-and-sales/data/e-f06-20-lead.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-20 Lead | Active | Badge "Active"; a new record starts here; next: Qualified or Disqualified (UC-F6-01); fields editable within the role | U03 | `u03-sales/s-f05-13-social-leads-e-f06-20-lead-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-20 Lead | Qualified | Badge "Qualified"; next: Disqualified or Converted (UC-F6-01, UC-F6-02); fields editable within the role | U03 | `u03-sales/s-f05-13-social-leads-e-f06-20-lead-qualified-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-20 Lead | Disqualified | Badge "Disqualified"; final: read-only, no next state; the history shows how it got here | U03 | `u03-sales/s-f05-13-social-leads-e-f06-20-lead-disqualified-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-20 Lead | Converted | Badge "Converted"; final: read-only, no next state; the history shows how it got here | U03 | `u03-sales/s-f05-13-social-leads-e-f06-20-lead-converted-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-20 Lead | Qualified | Badge "Qualified"; next: Disqualified or Converted (UC-F6-01, UC-F6-02); fields editable within the role | U03 | `u03-sales/s-f05-13-social-leads-e-f06-20-lead-qualified-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-20 Lead | Disqualified | Badge "Disqualified"; final: read-only, no next state; the history shows how it got here | U03 | `u03-sales/s-f05-13-social-leads-e-f06-20-lead-disqualified-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-20 Lead | Converted | Badge "Converted"; final: read-only, no next state; the history shows how it got here | U03 | `u03-sales/s-f05-13-social-leads-e-f06-20-lead-converted-{desktop,phone,tablet}-{light,dark}.png` |

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

## Open questions

None.

---

⬅️ [S-F5-12 Survey](../08-pages-forms-surveys-and-whatsapp/s-f05-12-survey.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-14 Segments](../06-audiences-consent-and-journeys/s-f05-14-segments.md)
