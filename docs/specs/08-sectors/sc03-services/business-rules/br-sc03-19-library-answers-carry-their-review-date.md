🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💼 [SC03 Services](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC03-19 Library answers carry their review date

# 📏 BR-SC03-19 Library answers carry their review date

**Status:** 🔄 waiting for the owner

## Statement

Every library answer carries its owner and its review date, and an answer past its review date is shown as Stale and is
not added to a tender until its owner has reviewed it. An answer left unreviewed for two review periods is Retired.

## Why

An out-of-date answer in a tender is a commitment the firm may no longer keep; the review date is the guard. The owner
asked for the tender answer library ([D547](../../../06-decisions/sectors/d547-benchmark-gaps-sc03-services.md)).

## Examples

| Case | Result |
|---|---|
| Reviewed 2026-03-01, every 12 months | Stale from 2027-03-02 |
| Stale answer added to a tender | refused |
| Stale answer reviewed | Approved, new review date |
| Two missed reviews | Retired |

## Applies to

- [UC-SC03-19](../use-cases/06-staffing-agencies-and-certification/uc-sc03-19-answer-a-tender-from-the-answer-library.md)
- [E-SC03-20 Answer](../data/e-sc03-20-answer.md)
- [E-SC03-02 Statement of work](../data/e-sc03-02-statement-of-work.md)

## Exceptions

None.

## Configurable

The review period (12 months by default), per answer, by its owner.

## Open questions

None.

---

⬅️ [BR-SC03-18](br-sc03-18-certificates-lapse-without-their-surveillance-audit.md) · ⬆️ [Up](README.md)
