🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) ›
🧗 [Technical challenges from the functional side](README.md) › 🧠 TC-09 Local AI without a graphics card

# 🧠 TC-09 Local AI without a graphics card

**Status:** ✅ listed for the technical interviews

## Challenge

Run the AI assistant, embeddings, meeting transcription and summaries on the company's own servers by default, with no
graphics card, and keep the ERP fully usable with the AI turned off.

## Raised by

- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [F4 Meetings](../../02-functional/f04-meetings/README.md)
- [F5 Social media and marketing](../../02-functional/f05-social-media/README.md)
- [F15 Legal assistant](../../02-functional/f15-legal-assistant/README.md)
- [T7 AI providers and models](../t07-ai-providers-and-models/README.md)

## Why it is hard

- Transcribing an hour of meeting and answering with a language model on CPU is slow.
- Server sizing must stay affordable for a small company.
- Quality must be measured per feature and per model.

## Already decided

- [D5](../../06-decisions/foundations/d05-where-the-ai-runs.md) Where the AI runs
- [D22](../../06-decisions/foundations/d22-no-graphics-card-needed.md) No graphics card needed

## Options to weigh

- Small local models per task, queued work, and an external provider per feature by the administrator's choice.
- Batch transcription after the meeting, against live.
- An evaluation set per AI feature.

## Settled in

- 19b Performance and capacity ([chapter](../../../technical/infrastructure/performance-and-capacity.md))
- 19i AI operations ([chapter](../../../technical/operations/ai-operations.md))
- Then the technical capabilities: [T7 AI providers and models](../t07-ai-providers-and-models/README.md).

## Questions for the interview

- What is the reference server for a 25-person company?
- Which AI features are acceptable only as overnight work on CPU?

---

⬅️ [TC-08 Search and RAG that respect rights and erasure](tc-08-permission-aware-search.md) · ⬆️ [Up](README.md) ·
➡️ [TC-10 Capturing meetings on outside platforms](tc-10-meeting-capture.md)
