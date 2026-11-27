🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🔧 [SC19 Trades and home services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC19-19 Each van is counted at every reload

# 📏 BR-SC19-19 Each van is counted at every reload

**Status:** ✅ specified

## Statement

A van is counted at every reload and the difference to the expected stock is explained or written off before the next
load. A reload never goes over the maximum of a part and a part under its minimum is proposed for reload.

## Why

A van stock that is never counted hides losses and leaves technicians without parts
([D563](../../../06-decisions/sectors/d563-benchmark-gaps-sc19-trades-and-home-services.md)).

## Examples

| Case | Result |
|---|---|
| Part under its minimum | reload proposed |
| Van not counted | reload refused |
| One part missing | explained or written off |
| Reload over the maximum | quantity cut |
| Part lent to another van | transfer between vans recorded |

## Applies to

- [UC-SC19-19](../use-cases/05-on-call-warranties-van-stock-and-site-quotes/uc-sc19-19-keep-stock-in-each-van.md)
- [E-SC19-13 Van stock](../data/e-sc19-13-van-stock.md)
- [E-SC19-13 Van stock](../data/e-sc19-13-van-stock.md)
- [E-F7-11](../../../02-functional/f07-purchasing-and-stock/data/e-f07-11-stock-count.md)

## Exceptions

None.

## Configurable

The write-off limit of a technician and the minimum and maximum of each part, set by purchasing.

## Open questions

None.

---

⬅️ [BR-SC19-18](br-sc19-18-works-start-only-with-a-valid-insurance-certificate.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC19-20](br-sc19-20-a-quote-signed-on-site-carries-the-withdrawal-notice.md)
