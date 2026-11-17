🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-09 Satisfaction asked once per resolved request

# 📏 BR-F16-09 Satisfaction asked once per resolved request

**Status:** ✅ specified

## Statement

A resolved request sends the customer one short survey (a score from 1 to 5 and an optional comment) on its own channel;
there is no reminder, and a score of 2 or less puts the request in the review queue.

## Why

Quality must also be judged by customers, not only by the AI judge and samples (D473).

## Examples

| Case | Result |
|---|---|
| Request resolved, survey answered with 5 | recorded |
| Survey answered with 2 and "still not refunded" | recorded, request in the review queue |
| Customer who opted out of surveys | no survey |

## Applies to

- [UC-F16-09 Rate the answer and measure satisfaction](../use-cases/05-customer-side/uc-f16-09-rate-the-answer-and-measure-satisfaction.md)
- [UC-F16-04 Review, correct and escalate](../use-cases/03-review-and-monitor/uc-f16-04-review-correct-and-escalate.md)
- [UC-F16-05 Monitor resolution and accuracy](../use-cases/03-review-and-monitor/uc-f16-05-monitor-resolution-and-accuracy.md)

## Exceptions

Customers who opted out get none.

## Configurable

The survey text per language; whether to ask for a comment.

## Open questions

None.

---

⬅️ [BR-F16-08 No duplicate action](br-f16-08-no-duplicate-action.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F16-10](br-f16-10-the-help-centre-shows-only-published-public-articles.md)
