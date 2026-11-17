🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📣 [Decisions: F5 Social media](README.md) ›
📜 D462 F5 Social media and marketing: gaps and improvements

# 📜 D462 F5 Social media and marketing: gaps and improvements

**Status:** ✅ decided

## Context

The gaps-and-improvements round of 2026-11-12 (D457), for F5 and the sectors that rely on it.

## Options

- **Contact, segment and consent entities.** Campaigns use segments, but there is no Segment or Consent entity and no
  proof of consent (BR-F5-08). Serves U12, SC08, SC16.
- **Deliverability.** Bounce, complaint and suppression handling are absent. SPF/DKIM is checked only in hosted F18, so
  self-hosted senders are uncovered.
- **Landing pages and forms.** Absent. Leads are traced only through links (BR-F5-06).
- **WhatsApp Business messaging.** About 4 mentions in all the specs. Serves SC02, SC06, SC16.
- **Campaign budget, cost per lead and ROI per channel.** "Budget" is absent from F5. Serves U13, U12.
- **One ticketing model.** UC-F5-11 sells tickets, while SC16 (seat maps, box office) and SC08 UC-12 re-specify
  ticketing.
- **Confirm the waiting proposals.** D246 automatic mode, BR-F5-02, D250 and all 8 entities and 7 screens.
- **Split the shared flow.** Email, SMS and journeys share one "benchmark additions" flow (fl-f05-05); fl-f05-04 has
  only 199 words.
- **Brand kit and asset library.** Absent; it could be shared with F18 identity and F3 writing style.
- **Extend A/B tests.** Variants exist only on email; add posts and SMS, with a winner rule.

## Choice

Confirmed by the owner on 2026-11-12:

- F5 Social media and marketing: gaps: All four: segments, consent and deliverability; landing pages and forms; WhatsApp
  Business; budget and ROI (ticketing goes to the shared model)
- F5 Social media and marketing: improvements: All three: split the shared flow; brand kit and assets; A/B tests
  everywhere
- F5 Social media and marketing: proposals: "Confirm all of F5"

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

- The chosen gaps and improvements become use cases, rules, entities, screens and flows of F5.
- F5's waiting proposals are confirmed (D457).

## Related

- [F5 Social media and marketing](../../02-functional/f05-social-media/README.md)

---

⬅️ [D461 F4 Meetings: gaps and improvements](../f04-meetings/d461-f04-gaps-and-improvements.md) · ⬆️ [Up](README.md) ·
➡️ [D463 F6 Customers and sales: gaps and improvements](../f06-customers-and-sales/d463-f06-gaps-and-improvements.md)
