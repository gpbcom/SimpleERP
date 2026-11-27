🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏋️ [SC18 Sports and fitness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC18-15 Health data stays with the member and coach

# 📏 BR-SC18-15 Health data stays with the member and coach

**Status:** ✅ specified

## Statement

A progress record is visible only to the member and their coach; it is never shown to the club's other staff, to the
owner or in a list, and it is exported or erased at the member's request.

## Why

Weight, times and notes on health are sensitive and their leak harms the member. The owner asked for personal training
([D562](../../../06-decisions/sectors/d562-benchmark-gaps-sc18-sports-and-fitness.md)). The health-data rules
come from the France pack, written later.

## Examples

| Case | Result |
|---|---|
| The coach opens the record | allowed |
| A receptionist opens the record | refused and logged |
| The owner opens the record | refused, only counts are shown |
| The member asks for an erasure | erased |
| A club-wide statistic | no names |

## Applies to

- [UC-SC18-15 Follow progress](../use-cases/04-personal-training/uc-sc18-15-follow-progress.md)
- [E-SC18-12 Progress record](../data/e-sc18-12-progress-record.md)
- [E-SC18-12 Progress record](../data/e-sc18-12-progress-record.md)

## Exceptions

None.

## Configurable

The measures kept and the retention after the member leaves, by the owner.

## Open questions

None.

---

⬅️ [BR-SC18-14 Programmes respect declared health limits](br-sc18-14-programmes-respect-declared-health-limits.md) ·
⬆️ [Up](README.md) · ➡️ [BR-SC18-16 Answers follow the asker's rights](br-sc18-16-answers-follow-the-askers-rights.md)
