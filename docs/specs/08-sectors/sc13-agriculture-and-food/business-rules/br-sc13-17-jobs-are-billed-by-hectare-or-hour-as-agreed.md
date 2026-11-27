🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🌾 [SC13 Agriculture and food](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC13-17 Jobs are billed by hectare or hour as agreed

# 📏 BR-SC13-17 Jobs are billed by hectare or hour as agreed

**Status:** 🔄 waiting for the owner

## Statement

A job is billed on the basis agreed with the farm, the hectare or the hour, and the invoice line uses the quantity the
driver confirmed in that basis. The basis cannot change once the job is Done, and a job without a confirmed quantity is
not invoiced.

## Why

A farm that agreed on hectares should not pay for hours, and a job without a quantity cannot be billed. The owner asked
for farm contractors ([D557](../../../06-decisions/sectors/d557-benchmark-gaps-sc13-agriculture-and-food.md)).
(Proposed) The France-pack rule is written later.

## Examples

| Case | Result |
|---|---|
| Per hectare, 13.8 ha at 42.00 EUR | 579.60 EUR |
| Per hour, 6.5 h at 95.00 EUR | 617.50 EUR |
| Per hectare, area differs from the field by more than the tolerance | the farmer chooses the agreed or the measured area |
| Job Done without a quantity | not invoiced, listed as missing |
| Basis changed after Done | refused |

## Applies to

- [UC-SC13-22](../use-cases/06-vineyards-contractors-and-cooperatives/uc-sc13-22-work-as-an-agricultural-contractor.md)
- [E-SC13-18 Field job](../data/e-sc13-18-field-job.md)
- [E-F6-05 Invoice](../../../02-functional/f06-customers-and-sales/data/e-f06-05-invoice.md)

## Exceptions

None.

## Configurable

The area tolerance and the machines' rates, by the farmer.

## Open questions

None.

---

⬅️ [BR-SC13-16](br-sc13-16-harvest-and-stock-declarations-are-filed-on-time.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC13-18 Rebates follow the members' deliveries](br-sc13-18-rebates-follow-the-members-deliveries.md)
