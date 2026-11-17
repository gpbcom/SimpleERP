🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-06 Audiences, consent and journeys](README.md) › 🖥️ S-F5-16 Deliverability

# 🖥️ S-F5-16 Deliverability

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Check the sending domain and follow bounces, complaints and suppressions.

## Entry points

Marketing › Deliverability.

## Wireframe

```text
+------------------------------------------------------------------+
| Sending domain acme-boutique.fr   SPF ok  DKIM missing  DMARC ok |
| Add: selector1._domainkey  TXT  "v=DKIM1; k=rsa; p=..."  [Check] |
| Campaign      Sent    Hard bounces  Complaints  Rate             |
| Autumn sale   9,800   12            2           0.02 %           |
| Suppressed: 214 addresses                     [See list]         |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-06 step 3, U12 | desktop | ![FL-F5-06 step 3, U12, light](../../images/06-audiences-consent-and-journeys/u12-marketing/3-deliverability-desktop-light.png) | ![FL-F5-06 step 3, U12, dark](../../images/06-audiences-consent-and-journeys/u12-marketing/3-deliverability-desktop-dark.png) |
| FL-F5-06 step 3, U12 | phone | ![FL-F5-06 step 3, U12, light](../../images/06-audiences-consent-and-journeys/u12-marketing/3-deliverability-phone-light.png) | ![FL-F5-06 step 3, U12, dark](../../images/06-audiences-consent-and-journeys/u12-marketing/3-deliverability-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-16-deliverability-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-16-deliverability-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-16-deliverability-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-16-deliverability-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-16-deliverability-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-16-deliverability-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-16-deliverability-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-16-deliverability-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Domain checks, rates, suppressions | E-F5-10, E-F5-05 | no |

## Actions

| Action | Who | Result |
|---|---|---|
| Check | marketing, administrator | Records checked again |

## States

- Normal: check the sending domain and follow bounces, complaints and suppressions.
- Empty: no campaign sent yet: only the domain checks.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users who are not marketing or administrators.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F5-10 Consent and suppression record](../../data/e-f05-10-consent-and-suppression-record.md),
[E-F5-05 Email or SMS campaign](../../data/e-f05-05-email-or-sms-campaign.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-10 Consent and suppression record | Given | Badge "Given"; a new record starts here; next: Withdrawn or Suppressed (UC-F5-15, UC-F5-14); fields editable within the role | U12 | `u12-marketing/s-f05-16-deliverability-e-f05-10-consent-and-suppression-record-given-{desktop,phone}-{light,dark}.png` |
| E-F5-10 Consent and suppression record | Withdrawn | Badge "Withdrawn"; next: Given (UC-F5-15); fields editable within the role | U12 | `u12-marketing/s-f05-16-deliverability-e-f05-10-consent-and-suppression-record-withdrawn-{desktop,phone}-{light,dark}.png` |
| E-F5-10 Consent and suppression record | Suppressed | Badge "Suppressed"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-16-deliverability-e-f05-10-consent-and-suppression-record-suppressed-{desktop,phone}-{light,dark}.png` |
| E-F5-05 Email or SMS campaign | Draft | Badge "Draft"; a new record starts here; next: Scheduled (UC-F5-08); fields editable within the role | U12 | `u12-marketing/s-f05-16-deliverability-e-f05-05-email-or-sms-campaign-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-05 Email or SMS campaign | Scheduled | Badge "Scheduled"; next: Sent (UC-F5-08); fields editable within the role | U12 | `u12-marketing/s-f05-16-deliverability-e-f05-05-email-or-sms-campaign-scheduled-{desktop,phone}-{light,dark}.png` |
| E-F5-05 Email or SMS campaign | Sent | Badge "Sent"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-16-deliverability-e-f05-05-email-or-sms-campaign-sent-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F5-06 Audiences, consent and journeys](../../flows/fl-f05-06-audiences-consent-and-journeys.md)

## Open questions

None.

---

⬅️ [S-F5-15 Consent register](s-f05-15-consent-register.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-17 Ticketing setup](../07-events-and-ticketing/s-f05-17-ticketing-setup.md)
