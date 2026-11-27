🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-05 Benchmark additions](README.md) › 🖥️ S-F5-09 SMS campaign

# 🖥️ S-F5-09 SMS campaign

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)

## Purpose

Send SMS campaigns within the sending window: by default 8:00 to 20:00, never on Sundays or public holidays, a
product default held in the country pack from the SMS operators' code of conduct (AF2M), which the company may narrow
([UC-F5-09](../../use-cases/05-benchmark-additions/uc-f05-09-send-sms-campaigns.md),
[D575](../../../../06-decisions/foundations/d575-answers-of-2026-11-27-on-the-last-open-points.md)).

## Entry points

Social media and marketing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-05 step 2, U12 | desktop | ![FL-F5-05 step 2, U12, light](../../images/05-benchmark-additions/u12-marketing/2-sms-desktop-light.png) | ![FL-F5-05 step 2, U12, dark](../../images/05-benchmark-additions/u12-marketing/2-sms-desktop-dark.png) |
| FL-F5-05 step 2, U12 | phone | ![FL-F5-05 step 2, U12, light](../../images/05-benchmark-additions/u12-marketing/2-sms-phone-light.png) | ![FL-F5-05 step 2, U12, dark](../../images/05-benchmark-additions/u12-marketing/2-sms-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-09-sms-campaign-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-09-sms-campaign-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-09-sms-campaign-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-09-sms-campaign-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-09-sms-campaign-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-09-sms-campaign-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-09-sms-campaign-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-09-sms-campaign-offline-phone-dark.png) |

## Fields and columns

As its entities, with:

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Send at | E-F5-05 send at | date and time, inside the sending window for an SMS | yes while Draft | yes, to be Scheduled |
| Sending window | the company's window, the country pack's by default | 8:00 to 20:00, no Sundays or public holidays, or narrower | no | yes |

## Actions

As its use case's main flow.

## States

- Normal: Send SMS campaigns, as the wireframe shows.
- Empty: No SMS campaign yet, with New campaign.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122); a send or a schedule outside the sending window is refused and the next
  time inside it is offered (UC-F5-09 4f): a Sunday at 10:00 offers Monday at 8:00.
- Read-only: for users without the marketing right; published items.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F5-05 Email or SMS campaign](../../data/e-f05-05-email-or-sms-campaign.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-05 Email or SMS campaign | Draft | Badge "Draft"; a new record starts here; next: Scheduled (UC-F5-08); fields editable within the role | U12 | `u12-marketing/s-f05-09-sms-campaign-e-f05-05-email-or-sms-campaign-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-05 Email or SMS campaign | Scheduled | Badge "Scheduled"; next: Sent (UC-F5-08); fields editable within the role | U12 | `u12-marketing/s-f05-09-sms-campaign-e-f05-05-email-or-sms-campaign-scheduled-{desktop,phone}-{light,dark}.png` |
| E-F5-05 Email or SMS campaign | Sent | Badge "Sent"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-09-sms-campaign-e-f05-05-email-or-sms-campaign-sent-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F5-08 Email campaign](s-f05-08-email-campaign.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-10 Journey designer](../06-audiences-consent-and-journeys/s-f05-10-journey-designer.md)
