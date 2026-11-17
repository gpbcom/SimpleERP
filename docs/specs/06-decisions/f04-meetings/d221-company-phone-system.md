🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎙️ [Decisions: F4 Meetings](README.md) › 📜 D221 Telephony

# 📜 D221 Telephony

**Status:** ✅ decided

## Context

Through which telephony calls are recorded.

## Options

- The company phone system.
- Mobile call recording.
- Both.

## Choice

The company's IP phone system (SIP: Asterisk, FreePBX, 3CX and others) or a cloud telephony service with an API,
connected by the administrator; mobiles through that system's app.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

No recording of mobile calls outside the phone system.

## Related

- [UC-F4-03](../../02-functional/f04-meetings/use-cases/02-record-in-person-or-by-phone/uc-f04-03-record-an-in-person-meeting.md)
- [UC-F4-04](../../02-functional/f04-meetings/use-cases/02-record-in-person-or-by-phone/uc-f04-04-record-a-phone-call.md)

---

⬅️ [D220 Offline recording](d220-offline-recording.md) · ⬆️ [Up](README.md) ·
➡️ [D222 Which calls are recorded](d222-business-calls-recorded.md)
