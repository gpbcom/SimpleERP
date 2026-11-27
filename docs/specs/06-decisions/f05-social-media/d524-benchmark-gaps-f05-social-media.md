🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📣 [Decisions: F5 Social media](README.md) ›
📜 D524 Benchmark gaps of F5 Social media and marketing

# 📜 D524 Benchmark gaps of F5 Social media and marketing

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found five features
other ERPs and marketing suites offer that F5 had no use case for: marketing cards, customer referral, push
notifications, brand listening and postal mail campaigns.

## Options

- G09 Marketing cards: personalised cards made from the brand kit, or leave visuals to external tools.
- G43 Customer referral: a referral programme paid on paid sales, or none.
- G44 Push notifications: push to opted-in devices, or email and SMS only.
- G45 Brand listening: listening to public mentions, or the inbox only.
- G46 Postal mail campaigns: postal campaigns through a print partner, or electronic channels only.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F5 gets five use cases in one new flow, each with its screen, its rule, its entity and its list, at full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G09 | Marketing cards | UC-F5-24: personalised cards that use only consented personal data | "Marketing cards" |
| G43 | Customer referral | UC-F5-25: a referral programme whose rewards wait for the paid sale | "Customer referral" |
| G44 | Push notifications | UC-F5-26: push notifications only to devices that opted in | "Push notifications" |
| G45 | Brand listening | UC-F5-27: listening to public content only | "Brand listening" |
| G46 | Postal mail campaigns | UC-F5-28: postal campaigns that honour opt-outs | "Postal mail campaigns" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F5 Social media and
marketing").

## Consequences

- G09 Marketing cards:
  [UC-F5-24](../../02-functional/f05-social-media/use-cases/10-referrals-push-and-listening/uc-f05-24-create-marketing-cards.md),
  [S-F5-24](../../02-functional/f05-social-media/screens/10-referrals-push-and-listening/s-f05-24-marketing-cards.md)
  and
  [BR-F5-19](../../02-functional/f05-social-media/business-rules/br-f05-19-cards-use-only-consented-personal-data.md),
  with [E-F5-21](../../02-functional/f05-social-media/data/e-f05-21-marketing-card.md) Marketing card and its list
  [S-F5-L21](../../02-functional/f05-social-media/screens/00-lists/s-f05-l21-marketing-cards.md).
- G43 Customer referral:
  [UC-F5-25](../../02-functional/f05-social-media/use-cases/10-referrals-push-and-listening/uc-f05-25-run-a-customer-referral-programme.md),
  [S-F5-25](../../02-functional/f05-social-media/screens/10-referrals-push-and-listening/s-f05-25-referral-programme.md)
  and
  [BR-F5-20](../../02-functional/f05-social-media/business-rules/br-f05-20-referral-rewards-wait-until-the-referred-sale-is-paid.md),
  with [E-F5-22](../../02-functional/f05-social-media/data/e-f05-22-referral.md) Referral and its list
  [S-F5-L22](../../02-functional/f05-social-media/screens/00-lists/s-f05-l22-referrals.md).
- G44 Push notifications:
  [UC-F5-26](../../02-functional/f05-social-media/use-cases/10-referrals-push-and-listening/uc-f05-26-send-push-notifications.md),
  [S-F5-26](../../02-functional/f05-social-media/screens/10-referrals-push-and-listening/s-f05-26-push-campaign.md) and
  [BR-F5-21](../../02-functional/f05-social-media/business-rules/br-f05-21-push-needs-the-devices-opt-in.md), with
  [E-F5-23](../../02-functional/f05-social-media/data/e-f05-23-push-campaign.md) Push campaign and its list
  [S-F5-L23](../../02-functional/f05-social-media/screens/00-lists/s-f05-l23-push-campaigns.md).
- G45 Brand listening:
  [UC-F5-27](../../02-functional/f05-social-media/use-cases/10-referrals-push-and-listening/uc-f05-27-listen-to-brand-mentions.md),
  [S-F5-27](../../02-functional/f05-social-media/screens/10-referrals-push-and-listening/s-f05-27-brand-mentions.md) and
  [BR-F5-22](../../02-functional/f05-social-media/business-rules/br-f05-22-listening-collects-public-content-only.md),
  with [E-F5-24](../../02-functional/f05-social-media/data/e-f05-24-brand-mention.md) Brand mention and its list
  [S-F5-L24](../../02-functional/f05-social-media/screens/00-lists/s-f05-l24-brand-mentions.md).
- G46 Postal mail campaigns:
  [UC-F5-28](../../02-functional/f05-social-media/use-cases/10-referrals-push-and-listening/uc-f05-28-send-postal-mail-campaigns.md),
  [S-F5-28](../../02-functional/f05-social-media/screens/10-referrals-push-and-listening/s-f05-28-postal-campaign.md)
  and [BR-F5-23](../../02-functional/f05-social-media/business-rules/br-f05-23-postal-campaigns-honour-opt-outs.md),
  with [E-F5-25](../../02-functional/f05-social-media/data/e-f05-25-postal-campaign.md) Postal campaign and its list
  [S-F5-L25](../../02-functional/f05-social-media/screens/00-lists/s-f05-l25-postal-campaigns.md).
- Drawn in [FL-F5-10](../../02-functional/f05-social-media/flows/fl-f05-10-referrals-push-and-listening.md) Cards,
  referrals, push and listening.

## Related

- [FL-F5-10](../../02-functional/f05-social-media/flows/fl-f05-10-referrals-push-and-listening.md)
- [BR-F5-08](../../02-functional/f05-social-media/business-rules/br-f05-08-marketing-needs-consent.md)

---

⬅️ [D523 Benchmark gaps of F4 Meetings](../f04-meetings/d523-benchmark-gaps-f04-meetings.md) · ⬆️ [Up](README.md) ·
➡️ [D525](../f06-customers-and-sales/d525-benchmark-gaps-f06-customers-and-sales.md)
