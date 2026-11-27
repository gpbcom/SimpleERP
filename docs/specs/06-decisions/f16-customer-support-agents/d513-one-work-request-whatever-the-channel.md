🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎧 [Decisions: F16 Customer support agents](README.md) ›
📜 D513 One work request whatever the channel

# 📜 D513 One work request whatever the channel

**Status:** ✅ decided

## Context

How customer requests reach scheduling ([D512](d512-every-customer-request-feeds-scheduling.md)).

## Options

- The interview record keeps the owner's answer, not every option the question offered.

## Choice

One schedulable work request, whatever the channel (portal, email, phone, chat, order, contract, care plan, API); the AI
drafts it from free text and a person confirms when the AI is unsure.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling (interview
record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository), VD-31).

## Consequences

-
  [BR-F16-13](../../02-functional/f16-customer-support-agents/business-rules/br-f16-13-every-request-becomes-a-work-request.md).
- [FL-F16-06 Take in every customer
  request](../../02-functional/f16-customer-support-agents/flows/fl-f16-06-take-in-every-request.md),
  [UC-F16-16](../../02-functional/f16-customer-support-agents/use-cases/06-take-in-every-request/uc-f16-16-turn-any-request-into-a-work-request.md),
  [S-F16-14 Work
  requests](../../02-functional/f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md).

## Related

- [E-F16-12 Work request](../../02-functional/f16-customer-support-agents/data/e-f16-12-work-request.md)
-
  [BR-F16-13](../../02-functional/f16-customer-support-agents/business-rules/br-f16-13-every-request-becomes-a-work-request.md)
- [FL-F16-06 Take in every customer
  request](../../02-functional/f16-customer-support-agents/flows/fl-f16-06-take-in-every-request.md)
- [D512 Every customer request feeds scheduling](d512-every-customer-request-feeds-scheduling.md)
- Interview record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)

---

⬅️ [D512 Every customer request feeds scheduling](d512-every-customer-request-feeds-scheduling.md) ·
⬆️ [Up](README.md) · ➡️ [D514 Scheduling objectives](../f09-hr-and-projects/d514-scheduling-objectives.md)
