🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏋️ [SC18 Sports and fitness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC18-08 Coaches hold the diploma for the activity

# 📏 BR-SC18-08 Coaches hold the diploma for the activity

**Status:** ✅ specified

## Statement

A class is assigned only to a coach who holds the diploma, and where the law asks for it the professional card, for that
activity, valid on the day of the class; the planner cannot override this check.

## Why

An unqualified coach exposes members and the club and may be illegal. The owner asked for planning of coaches
([D562](../../../06-decisions/sectors/d562-benchmark-gaps-sc18-sports-and-fitness.md)). The diplomas and
cards required come from the France pack, written later
([CR-FR-210](../../../10-country-packs/france/labour/cr-fr-210-qualifications-tied-to-tasks.md)).

## Examples

| Case | Result |
|---|---|
| Boxing class, coach with the boxing diploma | allowed |
| Boxing class, coach with only a yoga diploma | refused |
| Diploma expired yesterday | refused |
| Diploma ending in 40 days | allowed and flagged |
| Volunteer coach in an association | the same check |

## Applies to

- [UC-SC18-08 Plan coaches](../use-cases/02-classes-and-waiting-lists/uc-sc18-08-plan-coaches.md)
- [E-F9-12](../../../02-functional/f09-hr-and-projects/data/e-f09-12-certification.md)

## Exceptions

None: the check is a legal duty and cannot be relaxed by the planner.

## Configurable

The diplomas each activity needs and the days before the end at which a diploma is flagged.

## Open questions

None.

---

⬅️ [BR-SC18-07 Freed places go to the first on the list](br-sc18-07-freed-places-go-to-the-first-on-the-list.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC18-09 A licence is issued once a year per member](br-sc18-09-a-licence-is-issued-once-a-year-per-member.md)
