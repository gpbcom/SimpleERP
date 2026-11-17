🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎧 [Decisions: F16 Customer support agents](README.md) ›
📜 D535 Benchmark gaps of F16 Customer support agents

# 📜 D535 Benchmark gaps of F16 Customer support agents

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found six support
features that F16 did not cover: a community forum, live chat with people, a phone voice agent, proactive outreach,
prepaid support hours and canned replies. F16 already has channels, the voice of F4's telephony and an agent workspace;
these complete the public, voice and contract sides.

## Options

- G06 Forum / community Q&A: a moderated forum, or no community space.
- G07 Live chat with people: live chat that starts with the AI agent and hands over to a person, or a chat with people
  only.
- G87 Phone voice agent: a voice agent that says it is an AI, or phone calls for people only.
- G88 Proactive outreach: outreach to affected customers only, or announcements to every customer.
- G89 Prepaid support hours: prepaid hours with consent beyond the balance, or hours billed afterwards.
- G90 Canned replies: canned replies with variables from the records, or free macros.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F16 gets six use cases in one new flow, FL-F16-07, each with its screen and its rule, and five entities with their
lists; the voice agent has no entity of its own, since the call is logged as a customer request. All at full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G06 | Forum / community Q&A | UC-F16-18: a forum whose flagged posts are moderated before publication | "Forum / community Q&A" |
| G07 | Live chat with people | UC-F16-19: live chat whose handover carries the full history | "Live chat with people" |
| G87 | Phone voice agent | UC-F16-20: a voice agent that tells callers they speak with an AI | "Phone voice agent" |
| G88 | Proactive outreach | UC-F16-21: outreach that targets affected customers only | "Proactive outreach" |
| G89 | Prepaid support hours | UC-F16-22: prepaid hours with consent beyond the balance | "Prepaid support hours" |
| G90 | Canned replies | UC-F16-23: canned replies whose variables come from the request | "Canned replies" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F16 Customer support
agents").

## Consequences

- G06 Forum / community Q&A:
  [UC-F16-18](../../02-functional/f16-customer-support-agents/use-cases/07-live-chat-voice-and-contracts/uc-f16-18-run-the-community-forum.md),
  [S-F16-16](../../02-functional/f16-customer-support-agents/screens/07-live-chat-voice-and-contracts/s-f16-16-forum.md)
  and
  [BR-F16-14](../../02-functional/f16-customer-support-agents/business-rules/br-f16-14-flagged-posts-are-moderated-before-publication.md),
  with [E-F16-13](../../02-functional/f16-customer-support-agents/data/e-f16-13-forum-post.md) Forum post and its list
  [S-F16-L13](../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l13-forum-posts.md).
- G07 Live chat with people:
  [UC-F16-19](../../02-functional/f16-customer-support-agents/use-cases/07-live-chat-voice-and-contracts/uc-f16-19-answer-website-visitors-in-live-chat.md),
  [S-F16-17](../../02-functional/f16-customer-support-agents/screens/07-live-chat-voice-and-contracts/s-f16-17-live-chat.md)
  and
  [BR-F16-15](../../02-functional/f16-customer-support-agents/business-rules/br-f16-15-the-ai-hands-over-to-a-person-with-the-full-history.md),
  with [E-F16-14](../../02-functional/f16-customer-support-agents/data/e-f16-14-chat-session.md) Chat session and its
  list [S-F16-L14](../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l14-chat-sessions.md).
- G87 Phone voice agent:
  [UC-F16-20](../../02-functional/f16-customer-support-agents/use-cases/07-live-chat-voice-and-contracts/uc-f16-20-answer-phone-calls-with-the-voice-agent.md),
  [S-F16-18](../../02-functional/f16-customer-support-agents/screens/07-live-chat-voice-and-contracts/s-f16-18-voice-agent.md)
  and
  [BR-F16-16](../../02-functional/f16-customer-support-agents/business-rules/br-f16-16-callers-are-told-they-speak-with-an-ai.md).
- G88 Proactive outreach:
  [UC-F16-21](../../02-functional/f16-customer-support-agents/use-cases/07-live-chat-voice-and-contracts/uc-f16-21-warn-customers-before-they-ask.md),
  [S-F16-19](../../02-functional/f16-customer-support-agents/screens/07-live-chat-voice-and-contracts/s-f16-19-proactive-outreach.md)
  and
  [BR-F16-17](../../02-functional/f16-customer-support-agents/business-rules/br-f16-17-outreach-targets-affected-customers-only.md),
  with [E-F16-15](../../02-functional/f16-customer-support-agents/data/e-f16-15-outreach.md) Outreach and its list
  [S-F16-L15](../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l15-outreaches.md).
- G89 Prepaid support hours:
  [UC-F16-22](../../02-functional/f16-customer-support-agents/use-cases/07-live-chat-voice-and-contracts/uc-f16-22-sell-prepaid-support-hours.md),
  [S-F16-20](../../02-functional/f16-customer-support-agents/screens/07-live-chat-voice-and-contracts/s-f16-20-support-contracts.md)
  and
  [BR-F16-18](../../02-functional/f16-customer-support-agents/business-rules/br-f16-18-work-beyond-the-prepaid-balance-needs-consent.md),
  with [E-F16-16](../../02-functional/f16-customer-support-agents/data/e-f16-16-support-contract.md) Support contract
  and its list
  [S-F16-L16](../../02-functional/f16-customer-support-agents/screens/00-lists/s-f16-l16-support-contracts.md).
- G90 Canned replies:
  [UC-F16-23](../../02-functional/f16-customer-support-agents/use-cases/07-live-chat-voice-and-contracts/uc-f16-23-use-canned-replies.md),
  [S-F16-21](../../02-functional/f16-customer-support-agents/screens/07-live-chat-voice-and-contracts/s-f16-21-canned-replies.md)
  and
  [BR-F16-19](../../02-functional/f16-customer-support-agents/business-rules/br-f16-19-variables-come-from-the-request-never-guessed.md),
  with the canned reply as a section of
  [E-F16-07](../../02-functional/f16-customer-support-agents/data/e-f16-07-macro.md) Macro
  ([D566](../foundations/d566-answers-of-2026-11-15-after-the-benchmark-gap-round.md), F16: E-F16-17 is merged into it,
  and its list S-F16-L17 is gone).
- Drawn in [FL-F16-07](../../02-functional/f16-customer-support-agents/flows/fl-f16-07-live-chat-voice-and-contracts.md)
  Forum, live chat, voice and support contracts.

## Related

- [FL-F16-07](../../02-functional/f16-customer-support-agents/flows/fl-f16-07-live-chat-voice-and-contracts.md)
- [D473 F16 Customer support agents: gaps and improvements](d473-f16-gaps-and-improvements.md)
- [D237 Customer support agents](d237-customer-support-agents.md)
- [BR-F16-04](../../02-functional/f16-customer-support-agents/business-rules/br-f16-04-customers-know-and-can-reach-a-person.md)

---

⬅️ [D534 Benchmark gaps of F15 Legal assistant](../f15-legal-assistant/d534-benchmark-gaps-f15-legal-assistant.md) ·
⬆️ [Up](README.md) · ➡️ [D536](../f17-competitive-analysis/d536-benchmark-gaps-f17-competitive-analysis.md)
