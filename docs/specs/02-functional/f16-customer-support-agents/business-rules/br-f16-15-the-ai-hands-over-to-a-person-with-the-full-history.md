🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-15 The AI hands over to a person with the full history

# 📏 BR-F16-15 The AI hands over to a person with the full history

**Status:** 🔄 waiting for the owner

## Statement

When the AI agent hands a chat to a person, the person receives the whole conversation, the identified customer's record
and what the AI agent tried, in the chat itself; the customer is never asked to repeat what they said, and the handover
is never refused while a person is on duty.

## Why

A customer who must start over loses patience and trust, and
[BR-F16-04](br-f16-04-customers-know-and-can-reach-a-person.md) says customers can always reach a person. The owner
asked for live chat with people
([D535](../../../06-decisions/f16-customer-support-agents/d535-benchmark-gaps-f16-customer-support-agents.md)).

## Examples

| Case | Result |
|---|---|
| A visitor asks for a person | the chat moves to Waiting at once |
| The AI agent cannot answer | hands over with the transcript |
| An agent transfers a chat | the history goes with it |
| No agent on duty | the chat becomes a request, never a dead end |
| A signed-in customer | their record is shown to the agent |

## Applies to

- [UC-F16-19](../use-cases/07-live-chat-voice-and-contracts/uc-f16-19-answer-website-visitors-in-live-chat.md)
- [E-F16-14 Chat session](../data/e-f16-14-chat-session.md)
- [E-F16-14 Chat session](../data/e-f16-14-chat-session.md)

## Exceptions

None.

## Configurable

The wait before a call back is offered, by the owner.

## Open questions

None.

---

⬅️ [BR-F16-14](br-f16-14-flagged-posts-are-moderated-before-publication.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F16-16 Callers are told they speak with an AI](br-f16-16-callers-are-told-they-speak-with-an-ai.md)
