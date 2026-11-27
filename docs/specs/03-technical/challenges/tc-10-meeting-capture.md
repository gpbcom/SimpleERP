🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🎙️ TC-10 Capturing meetings on outside platforms

# 🎙️ TC-10 Capturing meetings on outside platforms

**Status:** ✅ listed for the technical interviews

## Challenge

Import transcripts from Meet, Teams and Zoom, and run a self-hosted bot that joins a meeting as a participant, with
consent, then turns it into records of the ERP.

## Raised by

- [F4 Meetings](../../02-functional/f04-meetings/README.md)
- [F16 Customer support agents](../../02-functional/f16-customer-support-agents/README.md)

## Why it is hard

- Each platform has its own API, rights and rules for bots, and they change.
- Speakers must be told apart without voice prints (country pack).
- Recordings are large and personal.

## Already decided

- [D23](../../06-decisions/foundations/d23-meeting-bot-consent.md) Meeting bot consent

## Options to weigh

- Headless browser bots, against the platforms' official meeting APIs, per platform.
- Where recordings are kept and for how long.

## Settled in

- 19a Architecture and scalability ([chapter](../../../technical/architecture/architecture.md))
- 19i AI operations ([chapter](../../../technical/operations/ai-operations.md))
- 19c Storage ([chapter](../../../technical/data/storage.md))
- Then the technical capabilities: [T7 AI providers and models](../t07-ai-providers-and-models/README.md),
  [T12 Connectors and scrapers](../t12-connectors-and-scrapers/README.md) (REQ-T12-18).

## Questions for the interview

- Which platforms must the bot join in the first version?
- Is the raw recording kept, or only the transcript?

---

⬅️ [TC-09 Local AI without a graphics card](tc-09-local-ai-without-a-graphics-card.md) · ⬆️ [Up](README.md) ·
➡️ [TC-11 Connectors, scrapers and the outside world](tc-11-connectors-and-generated-scrapers.md)
