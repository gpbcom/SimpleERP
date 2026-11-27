🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-18 Work beyond the prepaid balance needs consent

# 📏 BR-F16-18 Work beyond the prepaid balance needs consent

**Status:** 🔄 waiting for the owner

## Statement

Support work is booked against the prepaid balance only while it lasts; when the balance reaches zero, no further hour
is booked, worked or invoiced until the customer has consented to a stated number of extra hours at a stated rate.

## Why

A customer who finds extra hours on the next invoice feels cheated and may dispute it. The owner asked for prepaid
support hours
([D535](../../../06-decisions/f16-customer-support-agents/d535-benchmark-gaps-f16-customer-support-agents.md)); usage is
billed from metered data
([BR-F6-10](../../f06-customers-and-sales/business-rules/br-f06-10-usage-is-billed-from-metered-data.md)).

## Examples

| Case | Result |
|---|---|
| Balance 0.5 hour and a job of 1.5 hours | 0.5 hour booked, then consent asked for 1 hour |
| Balance zero | no hour booked until the customer accepts |
| A customer who accepts 2 hours at 95 EUR | 2 hours are invoiced separately |
| A contract past its validity | no booking, renewal offered |
| A customer who cannot be reached | work stops, the request waits |

## Applies to

- [UC-F16-22](../use-cases/07-live-chat-voice-and-contracts/uc-f16-22-sell-prepaid-support-hours.md)
- [E-F16-16 Support contract](../data/e-f16-16-support-contract.md)
- [E-F9-17 Timesheet line](../../f09-hr-and-projects/data/e-f09-17-timesheet-line.md)

## Exceptions

Work the customer's plan already includes is not booked on the block.

## Configurable

The alert level (20 percent by default), by the success manager.

## Open questions

None.

---

⬅️ [BR-F16-17 Outreach targets affected customers only](br-f16-17-outreach-targets-affected-customers-only.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F16-19](br-f16-19-variables-come-from-the-request-never-guessed.md)
