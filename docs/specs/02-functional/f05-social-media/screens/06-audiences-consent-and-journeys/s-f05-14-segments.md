🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-06 Audiences, consent and journeys](README.md) › 🖥️ S-F5-14 Segments

# 🖥️ S-F5-14 Segments

**Status:** ✅ specified

## Personas

- [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Build segments of contacts and see who can be reached per channel.

## Entry points

Marketing › Segments.

## Wireframe

```text
+------------------------------------------------------------------+
| Segment: Lyon buyers 2026          (o) Dynamic ( ) Static         |
| [City = Lyon] AND [Bought in 2026]                 [+ Condition] |
| 1,240 contacts  email 980  SMS 410  WhatsApp 120  postal 1,150   |
| Preview: Lea Roux, Paul Morel, ...                    [Save]     |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-06 step 1, U12 | desktop | ![FL-F5-06 step 1, U12, light](../../images/06-audiences-consent-and-journeys/u12-marketing/1-segments-desktop-light.png) | ![FL-F5-06 step 1, U12, dark](../../images/06-audiences-consent-and-journeys/u12-marketing/1-segments-desktop-dark.png) |
| FL-F5-06 step 1, U12 | phone | ![FL-F5-06 step 1, U12, light](../../images/06-audiences-consent-and-journeys/u12-marketing/1-segments-phone-light.png) | ![FL-F5-06 step 1, U12, dark](../../images/06-audiences-consent-and-journeys/u12-marketing/1-segments-phone-dark.png) |
| Error E1, U12 | desktop | ![Error E1, U12, light](../../images/06-audiences-consent-and-journeys/u12-marketing/e1-segments-refused-desktop-light.png) | ![Error E1, U12, dark](../../images/06-audiences-consent-and-journeys/u12-marketing/e1-segments-refused-desktop-dark.png) |
| Error E1, U12 | phone | ![Error E1, U12, light](../../images/06-audiences-consent-and-journeys/u12-marketing/e1-segments-refused-phone-light.png) | ![Error E1, U12, dark](../../images/06-audiences-consent-and-journeys/u12-marketing/e1-segments-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-14-segments-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-14-segments-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-14-segments-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-14-segments-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-14-segments-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-14-segments-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-14-segments-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-14-segments-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Conditions, kind, counts | E-F5-09 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Save | marketing | Segment usable |
| Preview | marketing | 20 contacts shown |

## States

- Normal: build segments of contacts and see who can be reached per channel.
- Empty: no segment yet: Build a segment, or describe one to the AI assistant.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: segments in use by a running journey: copied to change.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F5-09 Contact segment](../../data/e-f05-09-contact-segment.md),
[E-F5-18 Contact](../../data/e-f05-18-contact.md),
[E-F5-10 Consent and suppression record](../../data/e-f05-10-consent-and-suppression-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-09 Contact segment | Active | Badge "Active"; a new record starts here; next: Archived (UC-F5-14); fields editable within the role | U12 | `u12-marketing/s-f05-14-segments-e-f05-09-contact-segment-active-{desktop,phone}-{light,dark}.png` |
| E-F5-09 Contact segment | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-14-segments-e-f05-09-contact-segment-archived-{desktop,phone}-{light,dark}.png` |
| E-F5-18 Contact | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U12 | `u12-marketing/s-f05-14-segments-e-f05-18-contact-active-{desktop,phone}-{light,dark}.png` |
| E-F5-10 Consent and suppression record | Given | Badge "Given"; a new record starts here; next: Withdrawn or Suppressed (UC-F5-15, UC-F5-14); fields editable within the role | U12 | `u12-marketing/s-f05-14-segments-e-f05-10-consent-and-suppression-record-given-{desktop,phone}-{light,dark}.png` |
| E-F5-10 Consent and suppression record | Withdrawn | Badge "Withdrawn"; next: Given (UC-F5-15); fields editable within the role | U12 | `u12-marketing/s-f05-14-segments-e-f05-10-consent-and-suppression-record-withdrawn-{desktop,phone}-{light,dark}.png` |
| E-F5-10 Consent and suppression record | Suppressed | Badge "Suppressed"; final: read-only, no next state; the history shows how it got here | U12 | `u12-marketing/s-f05-14-segments-e-f05-10-consent-and-suppression-record-suppressed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F5-06 Audiences, consent and journeys](../../flows/fl-f05-06-audiences-consent-and-journeys.md)

## Open questions

None.

---

⬅️ [S-F5-13 Social leads](../05-benchmark-additions/s-f05-13-social-leads.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-15 Consent register](s-f05-15-consent-register.md)
