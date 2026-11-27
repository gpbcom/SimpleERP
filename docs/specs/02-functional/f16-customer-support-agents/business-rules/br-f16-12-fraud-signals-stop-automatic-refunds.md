🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-12 Fraud signals stop automatic refunds

# 📏 BR-F16-12 Fraud signals stop automatic refunds

**Status:** ✅ specified

## Statement

A request whose customer or order shows a fraud signal (refunds above the usual rate, a new account with a high-value
claim, a delivery proof that contradicts the claim) is never refunded automatically: it goes to a person with the
signals.

## Why

Refund abuse grows when refunds are automatic (D473).

## Examples

| Case | Result |
|---|---|
| Customer with 4 refunds in 60 days (threshold 3) | to a person |
| Lost-parcel claim with a signed delivery proof | to a person |
| Ordinary first refund | automatic within its limit |

## Applies to

- [UC-F16-15 Detect refund abuse and fraud signals](../use-cases/03-review-and-monitor/uc-f16-15-detect-refund-abuse-and-fraud-signals.md)
- [UC-F16-01 Resolve a customer request automatically](../use-cases/01-resolve-a-request/uc-f16-01-resolve-a-customer-request-automatically.md)

## Exceptions

None.

## Configurable

The support lead sets the thresholds of each signal.

## Open questions

None.

---

⬅️ [BR-F16-11 Answers in the customer's language](br-f16-11-answers-in-the-customers-language.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F16-13 Every customer request becomes one work request](br-f16-13-every-request-becomes-a-work-request.md)
