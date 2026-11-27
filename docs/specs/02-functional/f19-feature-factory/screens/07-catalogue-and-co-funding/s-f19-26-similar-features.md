🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-07 Similar features, catalogue, co-funding and maintenance](README.md) ›
🖥️ S-F19-26 Similar features

# 🖥️ S-F19-26 Similar features

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the features close to their need, before any quote.

## Purpose

Show what already exists before a feature is quoted, and record the owner's choice.

## Entry points

Feature factory › the request, after the chatbot's summary; the request's page.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Similar features for: "Remind me 3 days before a lease ends"          3 results              |
|---------------------------------------------------------------------------------------------|
| NAME                WHERE          CLOSE   WHAT IT COVERS                  PRICE      USED BY   |
| Lease reminders     Hosted store   82 %    reminders on any date field     included   140       |
| Date alerts         Plugin store   64 %    alerts on dates of records      9 EUR/mo   2,300     |
| Contract renewals   Hosted store   41 %    renewal dates of contracts      included   310       |
| [Open] [Install]                   [None fits, continue to the quote]   Why: __________       |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-07 step 1, U13 | desktop | ![FL-F19-07 step 1, U13, light](../../images/07-catalogue-and-co-funding/u13-owner/1-similar-features-desktop-light.png) | ![FL-F19-07 step 1, U13, dark](../../images/07-catalogue-and-co-funding/u13-owner/1-similar-features-desktop-dark.png) |
| FL-F19-07 step 1, U13 | phone | ![FL-F19-07 step 1, U13, light](../../images/07-catalogue-and-co-funding/u13-owner/1-similar-features-phone-light.png) | ![FL-F19-07 step 1, U13, dark](../../images/07-catalogue-and-co-funding/u13-owner/1-similar-features-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-26-similar-features-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-26-similar-features-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-26-similar-features-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-26-similar-features-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-26-similar-features-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-26-similar-features-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-26-similar-features-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-26-similar-features-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Need | request description | text | no | yes |
| Name and place | listing name, hosted or plugin store | text | no | yes |
| Closeness | computed match | percent | no | yes |
| What it covers | listing summary | text | no | yes |
| Price and use | listing price, installs | text and number | no | yes |
| Why none fits | owner's words | text | yes | when none fits |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Open | row | owner, administrator | the listing with its details |
| Install | row | owner, administrator | installs it with the usual steps and closes the request |
| None fits, continue | footer | owner, administrator | records the reason and prepares the quote |
| Show more | list | owner, administrator | adds the next closest results |

## States

- Normal: the closest features with their closeness, price and use, and the choice buttons.
- Empty: Nothing close exists, with Continue to the quote.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a store that
  cannot be read says so and offers to continue with the reason recorded.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F19-07](../../flows/fl-f19-07-catalogue-and-co-funding.md)

## Open questions

None.

---

⬅️ [S-F19-25 Factory accounting](../05-bill-and-credit/s-f19-25-factory-accounting.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-27 Fixed-price catalogue](s-f19-27-fixed-price-catalogue.md)
