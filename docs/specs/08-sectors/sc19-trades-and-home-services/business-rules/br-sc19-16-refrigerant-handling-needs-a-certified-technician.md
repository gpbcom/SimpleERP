🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-16 Refrigerant handling needs a certified technician

# 📏 BR-SC19-16 Refrigerant handling needs a certified technician

**Status:** 🔄 waiting for the owner

## Statement

A refrigerant handling is recorded only for a technician whose certificate for that work is valid at the date, and a
record is closed only with its quantities. A record is corrected by a new entry, never deleted.

## Why

Handling refrigerant without the certificate is an offence and an unrecorded quantity cannot be shown to an inspector
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)). (Proposed) The France-pack
rule is written later.

## Examples

| Case | Result |
|---|---|
| Valid certificate | the handling is recorded |
| Certificate expired | refused |
| Quantity missing | not closed |
| Recovered more than charged | flagged for a check |
| Wrong quantity entered | corrected by a new entry |

## Applies to

- [UC-SC19-16](../use-cases/04-installations-and-labels/uc-sc19-16-keep-refrigerant-and-grid-connection-records.md)
- [E-SC19-10 Regulated record](../data/e-sc19-10-regulated-record.md)
- [E-SC19-10 Regulated record](../data/e-sc19-10-regulated-record.md)
- [E-F9-12](../../../02-functional/f09-hr-and-projects/data/e-f09-12-certification.md)

## Exceptions

None.

## Configurable

The intervals of the leak checks and the sizes they apply to, from the country pack.

## Open questions

None.

---

⬅️ [BR-SC19-15 Label audits are planned before expiry](br-sc19-15-label-audits-are-planned-before-expiry.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC19-17](br-sc19-17-call-out-surcharges-are-shown-before-dispatch.md)
