🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🧭 [F21 Onboarding and module activation](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F21-17 Paid sessions are quoted before booking

# 📏 BR-F21-17 Paid sessions are quoted before booking

**Status:** ✅ specified

## Statement

A session that is paid is quoted before it is booked: the quote shows its scope, its length, its price excluding VAT and
its validity, and no slot is held and nothing is billed until the owner accepts it; a session that the plan includes
shows that it is included.

## Why

Help is only help if the cost is known first; a surprise bill at the end of a set-up spoils the trust the first run is
meant to build. The owner asked for expert sessions
([D540](../../../06-decisions/f21-onboarding-and-modules/d540-benchmark-gaps-f21-onboarding-and-modules.md)).

## Examples

| Case | Result |
|---|---|
| A session of 90 minutes at 240 EUR | quote first, booked after acceptance |
| A session included in the plan | booked without a quote, shown as included |
| A quote 15 days old | expired, a new quote is offered |
| A session that takes longer than quoted | billed at the quoted price |
| A second session needed | a new quote |

## Applies to

- [UC-F21-26](../use-cases/06-experts-cutover-and-parallel-run/uc-f21-26-book-an-implementation-expert.md)
- [E-F21-19 Expert session](../data/e-f21-19-expert-session.md)
- [E-F21-01 Onboarding progress](../data/e-f21-01-onboarding-progress.md)

## Exceptions

None.

## Configurable

The experts, their topics, prices and the included sessions, by the SimpleERP team and the partners.

## Open questions

None.

---

⬅️ [BR-F21-16 Employees onboard on the phone](br-f21-16-employees-onboard-on-the-phone.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F21-18 Go-live waits for a complete checklist](br-f21-18-go-live-waits-for-a-complete-checklist.md)
