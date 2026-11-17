🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F20-20 Calls follow the plan's times

# 📏 BR-F20-20 Calls follow the plan's times

**Status:** 🔄 waiting for the owner

## Statement

A call can be booked only inside the service hours of the company's support plan, no later than the plan's target for
its urgency, in a language listed as supported, and within the number of calls the plan includes; further calls are
offered at the plan's price.

## Why

The plan is a promise made to every customer: a call outside its hours would take an engineer from another customer's
urgent request. The owner asked for calls with an engineer
([D539](../../../06-decisions/f20-hosted-support-assistant/d539-benchmark-gaps-f20-hosted-support-assistant.md)).

## Examples

| Case | Result |
|---|---|
| An urgent call on a working day at 10:00 | a slot within the hour or an immediate call back |
| A call on a Sunday on a working-day plan | no slot offered |
| A third call on a plan with two | offered at the plan's price |
| A call booked in a language not supported | refused, English offered with a note |
| A call moved 30 minutes before | refused: the notice is one working hour |

## Applies to

- [UC-F20-29](../use-cases/08-engineers-sharing-and-reports/uc-f20-29-book-a-call-with-an-engineer.md)
- [E-F20-19 Engineer call](../data/e-f20-19-engineer-call.md)
- [E-F20-12 Support plan](../data/e-f20-12-support-plan.md)

## Exceptions

A security incident ([UC-F20-15](../use-cases/03-incidents/uc-f20-15-handle-a-security-incident-or-breach.md)) is
handled at once whatever the hours.

## Configurable

The hours, the calls per month and the notice, per plan, by the simple-ERP team.

## Open questions

None.

---

⬅️ [BR-F20-19 NIS2 facts on time](br-f20-19-nis2-facts-on-time.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F20-21 Access ends at its time limit and is audited](br-f20-21-access-ends-at-its-time-limit-and-is-audited.md)
