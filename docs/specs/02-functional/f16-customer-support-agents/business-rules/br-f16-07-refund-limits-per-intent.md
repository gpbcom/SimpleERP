🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F16-07 Refund limits per intent

# 📏 BR-F16-07 Refund limits per intent

**Status:** ✅ specified

## Statement

Each refund intent sets the highest amount an agent may refund per request and per customer per period; above it, the
refund is prepared and waits for a person's approval.

## Why

A block that moves money needs limits (D473).

## Examples

| Case | Result |
|---|---|
| Late-delivery refund 40.00 EUR, limit 50.00 EUR per request | refunded automatically |
| Duplicate-charge refund 180.00 EUR, limit 150.00 EUR | prepared, waits for approval |
| Third refund to the same customer in 30 days, limit 2 | waits for approval |

## Applies to

- [UC-F16-08 Support requests in the agent workspace](../use-cases/04-human-agent-workspace/uc-f16-08-work-requests-in-the-agent-workspace.md)
- [UC-F16-15 Detect refund abuse and fraud signals](../use-cases/03-review-and-monitor/uc-f16-15-detect-refund-abuse-and-fraud-signals.md)
- [UC-F16-01 Resolve a customer request automatically](../use-cases/01-resolve-a-request/uc-f16-01-resolve-a-customer-request-automatically.md)
- [UC-F16-02 Write and test a procedure for an intent](../use-cases/02-automate-an-intent/uc-f16-02-write-and-test-a-procedure.md)

## Exceptions

None: no setting lets an agent refund without limit.

## Configurable

The support lead sets the limits per intent; the owner approves limits above 500.00 EUR.

## Open questions

None.

---

⬅️ [BR-F16-06 One person on a request at a time](br-f16-06-one-person-on-a-request-at-a-time.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F16-08 No duplicate action](br-f16-08-no-duplicate-action.md)
