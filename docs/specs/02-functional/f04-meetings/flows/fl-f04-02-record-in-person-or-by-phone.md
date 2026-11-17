🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
🔀 [Flows](README.md) › 🔀 FL-F4-02 Record in person or by phone

# 🔀 FL-F4-02 Record in person or by phone

**Status:** ✅ specified

## Summary

From a meeting in a room, on a site or on the phone to a transcript with suggested links.

## Personas

- [U03 Sales](../../../01-users/personas/u03-sales.md)
- [U14 Field worker](../../../01-users/personas/u14-field-worker.md)
- Any internal participant
- [U04 Purchasing](../../../01-users/personas/u04-purchasing.md)

## Flowchart

```mermaid
flowchart TD
  K{Kind} -- in person --> A[Confirm everyone was told]
  A --> R[Recording]
  R --> N{Network?}
  N -- no --> E[Kept encrypted, uploaded later]
  N -- yes --> T[Transcribed]
  E --> T
  K -- external call --> M[Spoken message]
  M --> R2[Call recorded]
  R2 --> T
  K -- internal call --> X[Not recorded]
  T --> L[Links suggested]
  L --> V[Review, UC-F4-05]
```

## Sequence diagram

See [UC-F4-03](../use-cases/02-record-in-person-or-by-phone/uc-f04-03-record-an-in-person-meeting.md#sequence-diagram)
and [UC-F4-04](../use-cases/02-record-in-person-or-by-phone/uc-f04-04-record-a-phone-call.md#sequence-diagram).

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U14, U03 | [S-F4-03](../screens/02-record-in-person-or-by-phone/s-f04-03-phone-recorder.md) | [UC-F4-03](../use-cases/02-record-in-person-or-by-phone/uc-f04-03-record-an-in-person-meeting.md) | Confirm everyone was told, record |
| 2 | U14 | [S-F4-03](../screens/02-record-in-person-or-by-phone/s-f04-03-phone-recorder.md) | [UC-F4-03](../use-cases/02-record-in-person-or-by-phone/uc-f04-03-record-an-in-person-meeting.md) | Offline, waiting to upload |
| 3 | U03, U04 | [S-F4-04](../screens/02-record-in-person-or-by-phone/s-f04-04-call.md) | [UC-F4-04](../use-cases/02-record-in-person-or-by-phone/uc-f04-04-record-a-phone-call.md) | A call recorded, contact suggested |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F4-18 Recording notice](../data/e-f04-18-recording-notice.md) | Active | 3 [S-F4-04](../screens/02-record-in-person-or-by-phone/s-f04-04-call.md) | Recording notices |
| [E-F4-01 Meeting](../data/e-f04-01-meeting.md) | Planned, Live, Ended, Waiting for review, Checked | 1, 2 [S-F4-03](../screens/02-record-in-person-or-by-phone/s-f04-03-phone-recorder.md); 3 [S-F4-04](../screens/02-record-in-person-or-by-phone/s-f04-04-call.md) | Meetings |

## Errors

Microphone refused; upload failing; phone system unreachable.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U14 | phone | [light](../images/02-record-in-person-or-by-phone/u14-field-worker/1-confirm-and-record-phone-light.png) | [dark](../images/02-record-in-person-or-by-phone/u14-field-worker/1-confirm-and-record-phone-dark.png) |
| 1 | U03 | desktop | [light](../images/02-record-in-person-or-by-phone/u03-sales/1-confirm-and-record-desktop-light.png) | [dark](../images/02-record-in-person-or-by-phone/u03-sales/1-confirm-and-record-desktop-dark.png) |
| 1 | U03 | phone | [light](../images/02-record-in-person-or-by-phone/u03-sales/1-confirm-and-record-phone-light.png) | [dark](../images/02-record-in-person-or-by-phone/u03-sales/1-confirm-and-record-phone-dark.png) |
| 1 | U03 | tablet | [light](../images/02-record-in-person-or-by-phone/u03-sales/1-confirm-and-record-tablet-light.png) | [dark](../images/02-record-in-person-or-by-phone/u03-sales/1-confirm-and-record-tablet-dark.png) |
| 2 | U14 | phone | [light](../images/02-record-in-person-or-by-phone/u14-field-worker/2-offline-recording-phone-light.png) | [dark](../images/02-record-in-person-or-by-phone/u14-field-worker/2-offline-recording-phone-dark.png) |
| 3 | U03 | desktop | [light](../images/02-record-in-person-or-by-phone/u03-sales/3-call-recorded-desktop-light.png) | [dark](../images/02-record-in-person-or-by-phone/u03-sales/3-call-recorded-desktop-dark.png) |
| 3 | U03 | phone | [light](../images/02-record-in-person-or-by-phone/u03-sales/3-call-recorded-phone-light.png) | [dark](../images/02-record-in-person-or-by-phone/u03-sales/3-call-recorded-phone-dark.png) |
| 3 | U03 | tablet | [light](../images/02-record-in-person-or-by-phone/u03-sales/3-call-recorded-tablet-light.png) | [dark](../images/02-record-in-person-or-by-phone/u03-sales/3-call-recorded-tablet-dark.png) |
| 3 | U04 | desktop | [light](../images/02-record-in-person-or-by-phone/u04-purchasing/3-call-recorded-desktop-light.png) | [dark](../images/02-record-in-person-or-by-phone/u04-purchasing/3-call-recorded-desktop-dark.png) |
| E1 | U14 | phone | [light](../images/02-record-in-person-or-by-phone/u14-field-worker/e1-microphone-refused-phone-light.png) | [dark](../images/02-record-in-person-or-by-phone/u14-field-worker/e1-microphone-refused-phone-dark.png) |
| E2 | U14 | phone | [light](../images/02-record-in-person-or-by-phone/u14-field-worker/e2-upload-failing-phone-light.png) | [dark](../images/02-record-in-person-or-by-phone/u14-field-worker/e2-upload-failing-phone-dark.png) |
| E3 | U03 | desktop | [light](../images/02-record-in-person-or-by-phone/u03-sales/e3-phone-system-down-desktop-light.png) | [dark](../images/02-record-in-person-or-by-phone/u03-sales/e3-phone-system-down-desktop-dark.png) |
| E3 | U03 | phone | [light](../images/02-record-in-person-or-by-phone/u03-sales/e3-phone-system-down-phone-light.png) | [dark](../images/02-record-in-person-or-by-phone/u03-sales/e3-phone-system-down-phone-dark.png) |
| E3 | U03 | tablet | [light](../images/02-record-in-person-or-by-phone/u03-sales/e3-phone-system-down-tablet-light.png) | [dark](../images/02-record-in-person-or-by-phone/u03-sales/e3-phone-system-down-tablet-dark.png) |

## Open questions

None.

---

⬅️ [FL-F4-01 Record an online meeting](fl-f04-01-record-an-online-meeting.md) · ⬆️ [Up](README.md) ·
➡️ [FL-F4-03 Review a meeting](fl-f04-03-review-a-meeting.md)
