🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🧭 [F21 Onboarding and module activation](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F21-19 Differences are explained before the old tool stops

# 📏 BR-F21-19 Differences are explained before the old tool stops

**Status:** ✅ specified

## Statement

The old tool can be marked stopped only when every difference of the parallel run above the tolerance has an explanation
or an accepted note, and an error found in SimpleERP has been corrected and compared again.

## Why

A difference nobody understands is a mistake waiting for the first closing or the first pay run to show it. The owner
asked for a parallel run
([D540](../../../06-decisions/f21-onboarding-and-modules/d540-benchmark-gaps-f21-onboarding-and-modules.md)).

## Examples

| Case | Result |
|---|---|
| A gap of 0.50 EUR from rounding | explained as rounding |
| A gap of 170 EUR with no explanation | the old tool stays open |
| A gap caused by an error in SimpleERP | corrected, the measure compared again |
| A gap accepted with the accountant's approval | counts as explained |
| A gap below the tolerance | not listed |

## Applies to

- [UC-F21-28](../use-cases/06-experts-cutover-and-parallel-run/uc-f21-28-run-old-and-new-tools-in-parallel.md)
- [E-F21-21 Parallel run](../data/e-f21-21-parallel-run.md)
- [E-F21-14 Migration source](../data/e-f21-14-migration-source.md)
- [E-F21-15 Opening balance check](../data/e-f21-15-opening-balance-check.md)

## Exceptions

None.

## Configurable

The tolerance (0.50 EUR by default) by the administrator.

## Open questions

None.

---

⬅️ [BR-F21-18 Go-live waits for a complete checklist](br-f21-18-go-live-waits-for-a-complete-checklist.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F21-20](br-f21-20-settings-proposed-from-documents-are-confirmed-by-a-person.md)
