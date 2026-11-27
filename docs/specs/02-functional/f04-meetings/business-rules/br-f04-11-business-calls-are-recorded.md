🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🎙️ [F4 Meetings](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F4-11 Business calls recorded only when switched on

# 📏 BR-F4-11 Business calls recorded only when switched on

**Status:** ✅ specified

## Statement

Call recording is off by default ([D449](../../../06-decisions/f04-meetings/d449-call-recording-off-by-default.md)). An
administrator switches it on per purpose (training, proof of an order, quality), for a team or the company, after the
staff committee is consulted and with people told, employees and callers; then each external call through the company
phone system is recorded, opened by the spoken message (BR-F4-01); the other party can ask to stop; internal
calls between colleagues are not recorded; a user can switch a call off during it.

## Why

Calls are business records like meetings. See
[D222](../../../06-decisions/f04-meetings/d222-business-calls-recorded.md).

Legal values from the France country pack:
[CR-FR-059 Recordings are announced](../../../10-country-packs/france/ai-and-recording/cr-fr-059-recordings-are-announced.md).

Legal values from the France country pack:
[CR-FR-206 Staff committee consulted before monitoring tools](../../../10-country-packs/france/labour/cr-fr-206-cse-consulted-on-monitoring.md),
[CR-FR-207 Call recording at work kept proportionate](../../../10-country-packs/france/data-protection/cr-fr-207-call-recording-proportionate.md).

## Examples

| Case | Result |
|---|---|
| A customer calls Léa, recording off (the default) | Not recorded |
| Recording switched on for proof of orders | Message, then recorded |
| Léa calls a colleague | Not recorded |
| The customer asks to stop | Stopped |

## Applies to

- [UC-F4-04](../use-cases/02-record-in-person-or-by-phone/uc-f04-04-record-a-phone-call.md)

## Exceptions

Calls to emergency numbers are never recorded.

## Configurable

Yes: per purpose, team or company, by an administrator, after the staff committee is consulted (D449).

## Open questions

None.

---

⬅️ [BR-F4-10 Offline recordings upload later](br-f04-10-offline-recordings-upload-later.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F4-12 Links are suggested, then confirmed](br-f04-12-links-are-suggested-then-confirmed.md)
