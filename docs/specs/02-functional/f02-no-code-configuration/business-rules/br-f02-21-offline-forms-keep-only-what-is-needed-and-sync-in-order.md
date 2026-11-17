🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-21 Offline forms keep only what is needed and sync in order

# 📏 BR-F2-21 Offline forms keep only what is needed and sync in order

**Status:** ✅ specified

## Statement

An offline form keeps on the phone only the records chosen, encrypts them, sends its queue in the order the records were
made, and settles conflicts by the record type's rule (last change, merge, or ask).

## Why

Phones get lost; offline work must not lose or duplicate a visit or a delivery (TC-06).

## Examples

| Case | Result |
|---|---|
| Two offline changes to different fields | Merged |
| Same field changed twice, rule ask | Second user chooses |
| Phone lost | Its data is encrypted; the session is revoked |

## Applies to

- [UC-F2-21 Make a phone form work offline](../use-cases/09-portals-and-offline-forms/uc-f02-21-make-a-phone-form-work-offline.md)
- [UC-F2-22 Fill a form offline on the phone](../use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md)
- [UC-F6-21 Take orders offline on the road](../../f06-customers-and-sales/use-cases/09-sell-on-the-road-and-steer-sales/uc-f06-21-take-orders-offline-on-the-road.md)

## Exceptions

None.

## Configurable

Records kept, period, conflict rule.

## Open questions

None.

---

⬅️ [BR-F2-20](br-f02-20-a-portal-shows-only-the-chosen-fields-of-the-persons-own-records.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-22](br-f02-22-a-change-that-breaks-something-is-not-published-unread.md)
