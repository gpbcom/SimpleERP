🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-13 Every customer request becomes one work request

# 📏 BR-F16-13 Every customer request becomes one work request

**Status:** 🔄 draft (GH-2 step S4b, from VD-30, VD-31 / D512, D513)

## Statement

Every customer request that asks for work, whatever its type (a service or an intervention, an order to fulfil and
deliver, a project or an engagement, a booking or an appointment) and whatever its channel (portal, email, phone, chat,
order, contract, care plan, API), becomes one work request; the AI drafts it, a person confirms it when the AI is unsure
of a field, and only work requests feed scheduling.

## Why

- The owner's decisions VD-30 and VD-31
  [D512](../../../06-decisions/f16-customer-support-agents/d512-every-customer-request-feeds-scheduling.md),
  [D513](../../../06-decisions/f16-customer-support-agents/d513-one-work-request-whatever-the-channel.md): scheduling
  has one input, the same for every capability and every channel, so the planner sees all the work in one place and the
  engine treats every kind of request alike.
- A draft the AI is unsure of is never scheduled as it stands: a person confirms or completes it first (VD-31).

## Examples

| Case | Result |
|---|---|
| A repair asked by email, every field clear | Work request of type "Intervention", drafted by the AI, then Ready |
| A repair asked by phone, the address unclear | Work request To confirm; a person completes the address, then Ready |
| An online order to deliver | Work request of type "Delivery", linked to the order |
| A care plan with a visit every Tuesday | One work request per visit, linked to the care plan's visit |
| A training session booked through the portal | Work request of type "Training session", linked to the booking |
| A customer asks the opening hours by chat | No work request: there is no work to schedule (D517) |
| The same repair asked by email, then by phone | (Proposed) The call is linked to the first work request; no second one |

## Applies to

- [UC-F16-16](../use-cases/06-take-in-every-request/uc-f16-16-turn-any-request-into-a-work-request.md)
- [UC-F16-01](../use-cases/01-resolve-a-request/uc-f16-01-resolve-a-customer-request-automatically.md)
- [UC-F9-33](../../f09-hr-and-projects/use-cases/12-schedule-customer-requests/uc-f09-33-schedule-a-work-request.md)
- [E-F16-01 Customer request](../data/e-f16-01-customer-request.md)
- [E-F16-12 Work request](../data/e-f16-12-work-request.md)
- [E-F2-25 Request type](../../f02-no-code-configuration/data/e-f02-25-request-type.md)

## Exceptions

A request that needs no field work, such as a question answered at once, is not turned into a work request (D517).
Requests that come from inside the company (an internal order, a maintenance request) are outside this rule: it
covers customer requests (Proposed).

## Configurable

Partly:
- the request types and their defaults (UC-F2-30), and the channels connected (F16, F24);
- (Proposed) the confidence under which the AI asks a person to confirm a draft, per request type;
- not whether a customer request that asks for work becomes a work request.

## Open questions

None.

---

⬅️ [BR-F16-12 Fraud signals stop automatic refunds](br-f16-12-fraud-signals-stop-automatic-refunds.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F16-14](br-f16-14-flagged-posts-are-moderated-before-publication.md)
