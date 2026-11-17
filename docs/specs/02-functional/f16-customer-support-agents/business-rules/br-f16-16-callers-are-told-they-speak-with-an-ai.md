🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-16 Callers are told they speak with an AI

# 📏 BR-F16-16 Callers are told they speak with an AI

**Status:** 🔄 waiting for the owner

## Statement

Every call answered by the voice agent begins with a sentence that tells the caller they speak with an AI, before any
question or recording notice is skipped; the voice agent never claims to be a person and always transfers to a person on
request.

## Why

People must know when they speak with a machine, and a caller may refuse to
([CR-FR-056](../../../10-country-packs/france/ai-and-recording/cr-fr-056-people-know-they-deal-with-an-ai.md)). The
owner asked for a phone voice agent
([D535](../../../06-decisions/f16-customer-support-agents/d535-benchmark-gaps-f16-customer-support-agents.md)).
(Proposed) The France-pack rule on the wording is written later.

## Examples

| Case | Result |
|---|---|
| Any incoming call | the first sentence says it is an AI |
| A caller who asks 'are you a person' | the voice agent says it is an AI |
| A caller who asks for a person | the call is transferred |
| A call in an unhandled language | the announcement is in the languages known, then a transfer |
| A silent caller | the announcement still plays before anything else |

## Applies to

- [UC-F16-20](../use-cases/07-live-chat-voice-and-contracts/uc-f16-20-answer-phone-calls-with-the-voice-agent.md)
- [E-F16-01 Customer request](../data/e-f16-01-customer-request.md)

## Exceptions

None.

## Configurable

The wording and the languages of the announcement, by the owner; its presence cannot be switched off.

## Open questions

None.

---

⬅️ [BR-F16-15](br-f16-15-the-ai-hands-over-to-a-person-with-the-full-history.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F16-17 Outreach targets affected customers only](br-f16-17-outreach-targets-affected-customers-only.md)
