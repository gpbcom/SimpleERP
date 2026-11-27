🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F5-20 Referral rewards wait until the referred sale is paid

# 📏 BR-F5-20 Referral rewards wait until the referred sale is paid

**Status:** ✅ specified

## Statement

A referral reward is granted only when the referred customer's invoice is paid, in proportion to what is paid above the
programme's minimum order; until then the referral stays Pending, and a refund of the referred order reverses the
reward.

## Why

Paying a reward on an order that is cancelled, refunded or never paid costs the company twice. The owner asked for
customer referral ([D524](../../../06-decisions/f05-social-media/d524-benchmark-gaps-f05-social-media.md));
[BR-F5-18 Return counts only traced revenue](br-f05-18-return-counts-only-traced-revenue.md) applies the same idea to
campaign return.

## Examples

| Case | Result |
|---|---|
| Referred invoice of 200 EUR paid in full, minimum order 50 EUR | the reward is granted |
| Referred invoice sent, not paid | the referral stays Pending |
| Reward granted, referred order refunded 10 days later | the reward is withdrawn, the referral is Reversed |
| Friend pays an instalment plan [UC-F6-23](../../f06-customers-and-sales/use-cases/08-collect-and-settle/uc-f06-23-agree-an-instalment-plan.md) | the reward waits until the minimum order is paid |
| Referrer and friend with the same delivery address | held for marketing, no reward until accepted |

## Applies to

- [UC-F5-25](../use-cases/10-referrals-push-and-listening/uc-f05-25-run-a-customer-referral-programme.md)
- [E-F5-22 Referral](../data/e-f05-22-referral.md)
- [E-F6-05 Invoice](../../f06-customers-and-sales/data/e-f06-05-invoice.md)
- [E-F6-06 Customer payment](../../f06-customers-and-sales/data/e-f06-06-customer-payment.md)

## Exceptions

None.

## Configurable

Yes: the reward, the minimum order and the dates, by marketing; never a reward before payment.

## Open questions

None.

---

⬅️ [BR-F5-19 Cards use only consented personal data](br-f05-19-cards-use-only-consented-personal-data.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F5-21 Push needs the device's opt-in](br-f05-21-push-needs-the-devices-opt-in.md)
